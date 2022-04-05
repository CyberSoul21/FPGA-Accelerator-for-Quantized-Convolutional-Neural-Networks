# Makefile pour créer une bibliothèque partagée
# 2020/09/12
# (c) Dorfell Parra  <dlparrap@unal.edu.co>

C++     = /usr/bin/g++
C++FLAGS= -lstd++ -Wall -Wextra -pedantic -c -fPIC
SRC     = src/monbib.cpp
OBJ     = monbib.o
LIB     = monbib.so

help:
	@echo "Créer bibliothèque partagée    " 	
	@echo "  make bib_par                 "
	@echo "                               " 

${OBJ}: ${SRC}
	@echo "Création de l'objet ...        " 
	${C++} ${C++FLAGS} -c ${SRC} -o ${OBJ}
	@echo "                               " 	

bib_par: ${OBJ}
	@echo "Création de la bibliothèque ..."
	${C++} -shared ${OBJ} -o ${LIB} 	  #g++ -o test test.cpp -lm
	@echo "                               " 	

clean: 
	rm -rf *.o *.so   
