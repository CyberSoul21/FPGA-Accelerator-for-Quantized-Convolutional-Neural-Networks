#pragma once

#ifdef __cplusplus
extern "C" {
#endif
 
void print_cpp(void);

// gemmlowp-master/fixedpoint/fixedpoint.h :51
struct FixedPointRawTypeTraits{
  typedef std::int32_t ScalarRawType;
  static constexpr int kLanes = 1; };

// gemmlowp-master/fixedpoint/fixedpoint.h :64
std::int32_t Dup(typename FixedPointRawTypeTraits::ScalarRawType x);

// gemmlowp-master/fixedpoint/fixedpoint.h :70
std::int32_t BitAnd(std::int32_t a, std::int32_t b);

// gemmlowp-master/fixedpoint/fixedpoint.h :88
std::int32_t BitNot(std::int32_t a);

// gemmlowp-master/fixedpoint/fixedpoint.h :94
std::int32_t Add(std::int32_t a, std::int32_t b);

// gemmlowp-master/fixedpoint/fixedpoint.h :141
std::int32_t ShiftRight(std::int32_t a, std::int8_t offset);

// gemmlowp-master/fixedpoint/fixedpoint.h :157
std::int32_t MaskIfNonZero(std::int32_t a);

// gemmlowp-master/fixedpoint/fixedpoint.h :186
std::int32_t MaskIfGreaterThan(std::int32_t a, std::int32_t b);

// gemmlowp-master/fixedpoint/fixedpoint.h :200
std::int32_t MaskIfLessThan(std::int32_t a, std::int32_t b);

// gemmlowp-master/fixedpoint/fixedpoint.h :340
std::int32_t SaturatingRoundingDoublingHighMul(std::int32_t a, std::int32_t b);

// gemmlowp-master/fixedpoint/fixedpoint.h :368
std::int32_t RoundingDivideByPOT(std::int32_t x, std::int8_t exponent);

// tensorflow-master/tensorflow/lite/kernels/internal/common.h :168
std::int32_t MultiplyByQuantizedMultiplier(std::int32_t x, std::int32_t quantized_multiplier, int shift);  

// tensorflow-master/tensorflow/lite/kernels/internal/quantization_util.cc :53
void    QuantizeMultiplier(double double_multiplier, std::int32_t* quantized_multiplier, int* shift);

#ifdef __cplusplus
}
#endif
