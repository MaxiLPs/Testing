#!/usr/bin/python
# Probando el gen mutante
from __future__ import print_function
from termcolor import colored
import json
import sys
import logging

genmutante = ['A', 'C', 'T', 'G']
repeticion = 4
coorden_mutantes = []
resultado = False

codigo = {
		"NoCode": 0,
		"OK": 200,
		"Created": 201,
		"Error": 400
		}

status_code =	{
				"NoCode": "NoCode",
				"OK": "OK",
				"P_Error": "Param Error",
				"T_Error": "Type Error"
				}

responseJSON =	{
				"code": None ,
  				"is_mutant": None,
				"status": None
				}




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
B = [
	['A'],
	['A'],
	['B'],
	['A']
	]
C = [
	['A','B','A','A']
	]

dna = ["AABBAA","CAGTGC","TTATGT","AGAAGG","CCCCTA","TCACTG"]





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
	#coorden_mutantes = ['']

def paramValidator(C):

	if isinstance(C, list): 
		control_range= len(C[0])
		#print(control_range)

		for i in range(0, len(C)):
			if len(C[i]) >= repeticion:
				if control_range != len(C[i]):
					responseJSON["status"] = status_code["P_Error"]
					print('Los valores ingresados deben tener la misma cantidad de caracteres')
					return False
			else:
				responseJSON["status"] = status_code["P_Error"]
				print ('En el indice:', i, 'cuenta con:', len(C[i]), 'caracteres. Se espera', repeticion, ' caracteres como minimo, para la busqueda del gen mutante')
				#print ('La cantidad minima esperada para la busqueda es:', repeticion)
				return False
		print ('Exito')
		responseJSON["status"] = status_code["OK"]
		return True
	else: 
	    
		responseJSON["status"] = status_code["T_Error"]
		responseJSON["code"] = codigo["Error"]
		
		print (json.dumps(responseJSON,sort_keys=True))
		return False
		#return json.dumps(responseJSON)
	    #print('Error: Se espera una lista')
	    


def isMutant(dna):

	#if not paramValidator(dna):
	#	return False

	matriz = [list(sub) for sub in dna]
	is_mutant = False
	filas = len(matriz)
	columnas = len(matriz[0])
	global coorden_mutantes
	coorden_mutantes=[]

	print ('filas:', filas, 'columnas:', columnas)
	print ('')
	#CONTROLES AQUI #
	for i in range(0,filas):
		for j in range(0, columnas):
			#BUSCA HORIZONTAL
			if j < columnas-(repeticion-1): # and columnas > repeticion-1:
				#print('i:', i, 'j:', j)
				#print('i:', i, 'j+0:', j+0, ' ->', matriz[i][j+0])
				#print('i:', i, 'j+1:', j+1, ' ->', matriz[i][j+1])
				#print('i:', i, 'j+2:', j+2, ' ->', matriz[i][j+2])
				#print('i:', i, 'j+3:', j+3, ' ->', matriz[i][j+3])
				if ( matriz[i][j] == matriz[i][j+1] and matriz[i][j] == matriz[i][j+2] and matriz[i][j] == matriz[i][j+3]):
					is_mutant = True
					coorden_mutantes.append([i,j+0])
					coorden_mutantes.append([i,j+1])
					coorden_mutantes.append([i,j+2])
					coorden_mutantes.append([i,j+3])
			#BUSCA VERTICAL
			if i < filas-(repeticion-1): # and filas > repeticion-1:
				#print('i+0:', i+0, 'j:', j, ' ->', matriz[i+0][j])
				#print('i+1:', i+1, 'j:', j, ' ->', matriz[i+1][j])
				#print('i+2:', i+2, 'j:', j, ' ->', matriz[i+2][j])
				#print('i+3:', i+3, 'j:', j, ' ->', matriz[i+3][j])
				if ( matriz[i][j] == matriz[i+1][j] and matriz[i][j] == matriz[i+2][j] and matriz[i][j] == matriz[i+3][j]):
					is_mutant = True
					coorden_mutantes.append([i+0,j])
					coorden_mutantes.append([i+1,j])
					coorden_mutantes.append([i+2,j])
					coorden_mutantes.append([i+3,j])
			#BUSCA DIAGONAL DESCENDIENTE
			if i < filas-(repeticion-1) and j < columnas-(repeticion-1): # and filas > repeticion and columnas > repeticion:
				#print('i+0:', i+0, 'j+0:', j+0, ' ->', matriz[i+0][j+0])
				#print('i+1:', i+1, 'j+1:', j+1, ' ->', matriz[i+1][j+1])
				#print('i+2:', i+2, 'j+2:', j+2, ' ->', matriz[i+2][j+2])
				#print('i+3:', i+3, 'j+3:', j+3, ' ->', matriz[i+3][j+3])
				if ( matriz[i][j] == matriz[i+1][j+1] and matriz[i][j] == matriz[i+2][j+2] and matriz[i][j] == matriz[i+3][j+3]):
					is_mutant = True
					coorden_mutantes.append([i+0,j+0])
					coorden_mutantes.append([i+1,j+1])
					coorden_mutantes.append([i+2,j+2])
					coorden_mutantes.append([i+3,j+3])
			#BUSCA DIAGONAL DESCENDIENTE
			if j >= columnas-(repeticion) and i <= filas-(repeticion):# and filas > repeticion and columnas > repeticion:
				#print('i+0:', i+0, 'j-0:', j-0, ' ->', matriz[i+0][j-0])
				#print('i+1:', i+1, 'j-1:', j-1, ' ->', matriz[i+1][j-1])
				#print('i+2:', i+2, 'j-2:', j-2, ' ->', matriz[i+2][j-2])
				#print('i+3:', i+3, 'j-3:', j-3, ' ->', matriz[i+3][j-3])
				if ( matriz[i][j] == matriz[i+1][j-1] and matriz[i][j] == matriz[i+2][j-2] and matriz[i][j] == matriz[i+3][j-3]):
					is_mutant = True
					coorden_mutantes.append([i+0,j-0])
					coorden_mutantes.append([i+1,j-1])
					coorden_mutantes.append([i+2,j-2])
					coorden_mutantes.append([i+3,j-3])
	
	printMatrizMutante(matriz)
	print (json.dumps(responseJSON))
	responseJSON["is_mutant"]= is_mutant
	print (json.dumps(responseJSON))
	return is_mutant
'''	
	if is_mutant:
		print('Es mutante')
		return is_mutant
	else:
		#print('No es mutante')
		return is_mutant
'''





resultado = paramValidator(2)#dna)

log = logging.getLogger("my-logger")
log.info("Hello, world")

if resultado:
	resultado = isMutant(dna)
	print('Es Mutante') if resultado else print('No es mutante')
else:
	print('verifique los errores mencionados anteriormetne')


#isMutant(sys.argv[1])

#printMatrizMutante(B)

#print('------------')
#print('el resultado es:', isMutant(C))
#print('------------')
#print('el resultado es:', isMutant(A))
#print('------------')
#print('el resultado es:', isMutant(C))
#print('------------')