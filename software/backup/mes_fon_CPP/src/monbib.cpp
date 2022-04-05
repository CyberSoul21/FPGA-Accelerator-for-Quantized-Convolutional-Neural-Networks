#include <cassert>
#include <cmath>
#include <iostream>
#include <limits>
#include <stdio.h>
#include "../include/monbib.h"
 
void print_cpp(void) {  
  std::cout << "¡Salut dès CPP!" << std::endl;  }

std::int32_t Dup(typename FixedPointRawTypeTraits::ScalarRawType x) {
  return x; }

std::int32_t BitAnd(std::int32_t a, std::int32_t b) {
  std::int32_t c;
  c = a & b;
  std::cout << "c = "      << c << std::endl;
  return a & b; }

std::int32_t BitNot(std::int32_t a) {
  //std::cout << " a = " <<  a << std::endl; 
  //std::cout << "~a = " << ~a << std::endl; 
  return ~a; }

std::int32_t Add(std::int32_t a, std::int32_t b) {
  return a + b; }

std::int32_t ShiftRight(std::int32_t a, std::int8_t offset) {
  return a >> offset; }

std::int32_t MaskIfNonZero(std::int32_t a) {
  static constexpr std::int32_t zero = 0;
  return a ? BitNot(zero) : zero;  }

std::int32_t MaskIfGreaterThan(std::int32_t a, std::int32_t b) {
  return MaskIfNonZero(a > b);  }

std::int32_t MaskIfLessThan(std::int32_t a, std::int32_t b) {
  return MaskIfNonZero(a < b); }
 
// Returns the integer that represents the product of two fixed-point
// numbers, interpreting all integers as fixed-point values in the
// interval [-1, 1), rounding to the nearest value, and saturating
// -1 * -1 to the maximum value (since 1 is not in the half-open
// interval [-1, 1)).
//
// [The explanation below specializes to std::int32_t for example purpose.]
//
// The mapping between IntegerType and the interval [-1, 1) is unique and
// implied by IntegerType, which is assumed to be signed. For example,
// for IntegerType==std::int32_t, the mapping is
//   real_value = integer_value / 2^31.
// So in this case, and leaving aside rounding and saturating, this
// function computes ((a / 2^31) * (b / 2^31)) * 2^31, which simplifies to
//   (a * b) / 2^31.
//
// The 'doubling' part in the name of this function comes from the fact that
// this operation is very close to a "multiply-high" operation, keeping only
// the top half bits, except that that would be effectively computing
//   (a * b) / 2^32,
// so here we are computing 2x that, since
//   1/2^31 = 2 * 1/2^32.
// The idea is to use all of the available 32 bits in the destination int32
// value.
//
// [End of the explanation specializing to int32.]
std::int32_t SaturatingRoundingDoublingHighMul(std::int32_t a, std::int32_t b) {
  bool overflow = a == b && a == std::numeric_limits<std::int32_t>::min();
  std::int64_t a_64(a);  std::int64_t b_64(b);
  std::int64_t ab_64 = a_64 * b_64;
  std::int32_t nudge = ab_64 >= 0 ? (1 << 30) : (1 - (1 << 30));
  std::int32_t ab_x2_high32 =  static_cast<std::int32_t>((ab_64 + nudge) / (1ll << 31));
  std::cout << "overflow = " << overflow  << std::endl;
  std::cout << "a_64(a)= "   << a_64  << std::endl;
  std::cout << "b_64(b)= "   << b_64  << std::endl;
  std::cout << "ab_64 = "    << ab_64 << std::endl;
  std::cout << "nudge = "    << nudge << std::endl;
  std::cout << "ab_x2_high32 = " << ab_x2_high32 << std::endl; 
  return overflow ? std::numeric_limits<std::int32_t>::max() : ab_x2_high32;
}

std::int32_t RoundingDivideByPOT(std::int32_t x, std::int8_t exponent) {
  assert(exponent >= 0);
  assert(exponent <= 31);
  const std::int32_t mask = Dup((1ll << exponent) - 1);
  const std::int32_t zero = Dup(0);
  const std::int32_t one  = Dup(1);
  const std::int32_t remainder = BitAnd(x, mask);
  const std::int32_t threshold = Add(ShiftRight(mask, 1), BitAnd(MaskIfLessThan(x, zero), one));
  std::cout << "x = "      << x << std::endl;
  std::cout << "exponent = "      << exponent << std::endl;  
  std::cout << "Mask = "      << mask << std::endl;
  std::cout << "zero = "      << zero << std::endl;
  std::cout << "one  = "      << one  << std::endl;
  std::cout << "Remainder = " << remainder << std::endl;
  std::cout << "Threshold = " << threshold << std::endl;
  std::cout << "ShiftRigh = " << ShiftRight(x, exponent) << std::endl;
  std::cout << "MaskIfGre = " << MaskIfGreaterThan(remainder, threshold) << std::endl;
  std::cout << "Add int32_t= " <<  Add(ShiftRight(x, exponent), 
             BitAnd( MaskIfGreaterThan(remainder, threshold), one ) ) << std::endl;
  return Add( ShiftRight(x, exponent), 
              BitAnd( MaskIfGreaterThan(remainder, threshold), one ) ); 
}

std::int32_t MultiplyByQuantizedMultiplier(std::int32_t x, std::int32_t quantized_multiplier, int shift){
  std::int8_t left_shift  = shift > 0 ? shift :      0;
  std::int8_t right_shift = shift > 0 ? 0     : -shift;
  std::cout << "x = "                    << x                    << std::endl; 
  std::cout << "quantized_multiplier = " << quantized_multiplier  << std::endl; 
  std::cout << "shift = "                << shift                 << std::endl;
  std::cout << "left_shift = "                << left_shift                 << std::endl;
  std::cout << "right_shift = "                << right_shift                 << std::endl; 
  std::cout << "x * (1 << left_shift)= " << x * (1 << left_shift) << std::endl; 
  return RoundingDivideByPOT(SaturatingRoundingDoublingHighMul(x * (1 << left_shift), quantized_multiplier), right_shift); 
}

void QuantizeMultiplier(double double_multiplier, std::int32_t* quantized_multiplier, int* shift){
  if (double_multiplier == 0.) 
  {
    *quantized_multiplier = 0; 
    *shift = 0; 
    return; 
  } 

  const double q       = std::frexp(double_multiplier, shift);
        double q_fixed = static_cast<std::int64_t>(std::round(q*(1ll << 31)));

  if (q_fixed == (1ll << 31)) {
    q_fixed /= 2; ++*shift; }

  if (*shift < -31) {
    *shift = 0; q_fixed = 0;  }

  *quantized_multiplier = static_cast<std::int32_t>(q_fixed);

  std::cout << "--- Résultats en CPP ---" << std::endl;
  std::cout << "double multiplier = "     << double_multiplier     << std::endl; 
  std::cout << "q = "                     << q                     << std::endl; 
  std::cout << "q_fixed = "               << q_fixed               << std::endl; 
  std::cout << "*shift  = "               << *shift                << std::endl; 
  std::cout << "quantized_multiplier = "  << *quantized_multiplier << std::endl; 
}
