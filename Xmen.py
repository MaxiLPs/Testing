#!/usr/bin/python
# Probando el gen mutante
from __future__ import print_function
from termcolor import colored


A = [
	['A','T','G','C','G','A'],
	['C','A','G','T','G','C'],
	['T','T','A','T','G','T'],
	['A','G','A','A','G','G'],
	['C','C','C','C','M','T'],
	['A','A','G','A','M','T'],
	['T','C','A','G','G','T'],
	['T','A','A','C','G','T'],
	['A','C','A','A','G','G']
    ]

genmutante = ['A', 'C', 'T', 'G']
repeticion = 4

filas = len(A)
columnas = len(A[0])


coorden_mutantes = []


def printMatrizMutante(matriz):
	for i in range(len(matriz)):
	    for j in range(len(matriz[i])):
	        x = matriz[i][j]
	        
	        if  [i,j] in coorden_mutantes:
	        	if matriz[i][j] == genmutante[0]:
	         		print (colored(matriz[i][j], 'green'), end=' ')
	         	elif matriz[i][j] == genmutante[1]:
	         		print (colored(matriz[i][j], 'red'), end=' ')
	         	elif matriz[i][j] == genmutante[2]:
	         		print (colored(matriz[i][j], 'blue'), end=' ')
	         	else:
	         		print (colored(matriz[i][j], 'cyan'), end=' ')
	        else:
	       		print(matriz[i][j], end=' ')
	    print(' ')


def isMutant(matriz):
	
	#CONTROLES AQUI #
	
	for i in range(0,filas):
		for j in range(0, columnas):
			#BUSCA HORIZONTAL
			if j < columnas-(repeticion-1):
				#print('i:', i, 'j:', j)
				#print('i:', i, 'j+0:', j+0, ' ->', matriz[i][j+0])
				#print('i:', i, 'j+1:', j+1, ' ->', matriz[i][j+1])
				#print('i:', i, 'j+2:', j+2, ' ->', matriz[i][j+2])
				#print('i:', i, 'j+3:', j+3, ' ->', matriz[i][j+3])
				if ( matriz[i][j] == matriz[i][j+1] and matriz[i][j] == matriz[i][j+2] and matriz[i][j] == matriz[i][j+3]):
					coorden_mutantes.append([i,j+0])
					coorden_mutantes.append([i,j+1])
					coorden_mutantes.append([i,j+2])
					coorden_mutantes.append([i,j+3])
			#BUSCA VERTICAL
			if i < filas-(repeticion-1):
				#print('i+0:', i+0, 'j:', j, ' ->', matriz[i+0][j])
				#print('i+1:', i+1, 'j:', j, ' ->', matriz[i+1][j])
				#print('i+2:', i+2, 'j:', j, ' ->', matriz[i+2][j])
				#print('i+3:', i+3, 'j:', j, ' ->', matriz[i+3][j])
				if ( matriz[i][j] == matriz[i+1][j] and matriz[i][j] == matriz[i+2][j] and matriz[i][j] == matriz[i+3][j]):
					coorden_mutantes.append([i+0,j])
					coorden_mutantes.append([i+1,j])
					coorden_mutantes.append([i+2,j])
					coorden_mutantes.append([i+3,j])
			#BUSCA DIAGONAL DESCENDIENTE
			if i < filas-(repeticion-1) and j < columnas-(repeticion-1):
				#print('i+0:', i+0, 'j+0:', j+0, ' ->', matriz[i+0][j+0])
				#print('i+1:', i+1, 'j+1:', j+1, ' ->', matriz[i+1][j+1])
				#print('i+2:', i+2, 'j+2:', j+2, ' ->', matriz[i+2][j+2])
				#print('i+3:', i+3, 'j+3:', j+3, ' ->', matriz[i+3][j+3])
				if ( matriz[i][j] == matriz[i+1][j+1] and matriz[i][j] == matriz[i+2][j+2] and matriz[i][j] == matriz[i+3][j+3]):
					coorden_mutantes.append([i+0,j+0])
					coorden_mutantes.append([i+1,j+1])
					coorden_mutantes.append([i+2,j+2])
					coorden_mutantes.append([i+3,j+3])
			#BUSCA DIAGONAL DESCENDIENTE
			if j >= columnas-(repeticion) and i <= filas-(repeticion):
				#print('i+0:', i+0, 'j-0:', j-0, ' ->', matriz[i+0][j-0])
				#print('i+1:', i+1, 'j-1:', j-1, ' ->', matriz[i+1][j-1])
				#print('i+2:', i+2, 'j-2:', j-2, ' ->', matriz[i+2][j-2])
				#print('i+3:', i+3, 'j-3:', j-3, ' ->', matriz[i+3][j-3])
				if ( matriz[i][j] == matriz[i+1][j-1] and matriz[i][j] == matriz[i+2][j-2] and matriz[i][j] == matriz[i+3][j-3]):
					coorden_mutantes.append([i+0,j-0])
					coorden_mutantes.append([i+1,j-1])
					coorden_mutantes.append([i+2,j-2])
					coorden_mutantes.append([i+3,j-3])

print ('filas:', filas, 'columnas:', columnas)

printMatrizMutante(A)

print('------------')
isMutant(A)
print('------------')
printMatrizMutante(A)
