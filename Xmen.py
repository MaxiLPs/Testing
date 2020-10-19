#!/usr/bin/python
# Probando el gen mutante
from __future__ import print_function
from termcolor import colored
import json
import sys
import logging


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
	['A'],
	['A']
	]
C = [
	['A','B','A','A']
	]

G = []

dna = ["AABBAA","CAGGGC","TTATGT","AGAAGG","CCCCTA","TCACTG"]



class ValidateService(object):
	
	repeticion = 4	

	@staticmethod
	def paramValidator(lista):
		try:
			if not type(lista) is list:
				raise TypeError ('Se espera una lista')

			control_range = len(lista[0])
			for i in range(0, len(lista)):
				if len(lista[i]) < ValidateService.repeticion and len(lista) < ValidateService.repeticion:
					raise IndexError('Longitud menor a la cantidad de repeticion')
				if control_range != len(lista[i]):
					raise IndexError('Diferentes rangos en las filas de la matriz')
			
			return codigo["OK"], status_code["OK"]
			
		except TypeError:
			#cuando se espera una lista
			#print ('Error de tipo')
			return codigo["Error"], status_code["T_Error"]
		except IndexError:
			#cuando la matriz tiene distintos tamanos de filas
			#cuando las filas son menor a la cantidad deseada de busqueda
			#print ('Fuera de rango')
			return codigo["OK"], status_code["P_Error"]

class MutantService(object):
	
	genmutante = ['A', 'C', 'T', 'G']
	coorden_mutantes = []
	repeticion = 4

	@staticmethod
	def printMatrizMutante(matriz):
		for i in range(len(matriz)):
			for j in range(len(matriz[i])):
				x = matriz[i][j]
				
				if  [i,j] in MutantService.coorden_mutantes:
					if matriz[i][j] == MutantService.genmutante[0]:
						print (colored(matriz[i][j], 'green'), end=' ')
					elif matriz[i][j] == MutantService.genmutante[1]:
						print (colored(matriz[i][j], 'red'), end=' ')
					elif matriz[i][j] == MutantService.genmutante[2]:
						print (colored(matriz[i][j], 'blue'), end=' ')
					else:
						print (colored(matriz[i][j], 'cyan'), end=' ')
				else:
					print(matriz[i][j], end=' ')

	@staticmethod
	def isMutant(dna):
		matriz = [list(sub) for sub in dna]
		is_mutant = False
		filas = len(matriz)
		columnas = len(matriz[0])
		MutantService.coorden_mutantes=[]

		#print ('filas:', filas, 'columnas:', columnas)

		for i in range(0,filas):
			for j in range(0, columnas):
				#BUSCA HORIZONTAL
				if j < columnas-(MutantService.repeticion-1):
					if ( matriz[i][j] == matriz[i][j+1] and matriz[i][j] == matriz[i][j+2] and matriz[i][j] == matriz[i][j+3]):
						return True
						"""
						
						#codigo por si hay que imprimir la matriz

						is_mutant = True
						MutantService.coorden_mutantes.append([i,j+0])
						MutantService.coorden_mutantes.append([i,j+1])
						MutantService.coorden_mutantes.append([i,j+2])
						MutantService.coorden_mutantes.append([i,j+3])
						"""
				#BUSCA VERTICAL
				if i < filas-(MutantService.repeticion-1):
					if ( matriz[i][j] == matriz[i+1][j] and matriz[i][j] == matriz[i+2][j] and matriz[i][j] == matriz[i+3][j]):
						return True
						"""
						
						#codigo por si hay que imprimir la matriz

						is_mutant = True
						MutantService.coorden_mutantes.append([i+0,j])
						MutantService.coorden_mutantes.append([i+1,j])
						MutantService.coorden_mutantes.append([i+2,j])
						MutantService.coorden_mutantes.append([i+3,j])
						"""
				#BUSCA DIAGONAL DESCENDIENTE
				if i < filas-(MutantService.repeticion-1) and j < columnas-(MutantService.repeticion-1):
					if ( matriz[i][j] == matriz[i+1][j+1] and matriz[i][j] == matriz[i+2][j+2] and matriz[i][j] == matriz[i+3][j+3]):
						return True
						"""
						
						#codigo por si hay que imprimir la matriz

						is_mutant = True
						MutantService.coorden_mutantes.append([i+0,j+0])
						MutantService.coorden_mutantes.append([i+1,j+1])
						MutantService.coorden_mutantes.append([i+2,j+2])
						MutantService.coorden_mutantes.append([i+3,j+3])
						"""
				#BUSCA DIAGONAL DESCENDIENTE
				if j >= columnas-(MutantService.repeticion) and i <= filas-(MutantService.repeticion) and columnas > MutantService.repeticion:
					if ( matriz[i][j] == matriz[i+1][j-1] and matriz[i][j] == matriz[i+2][j-2] and matriz[i][j] == matriz[i+3][j-3]):
						return True
						"""
						
						#codigo por si hay que imprimir la matriz

						is_mutant = True
						MutantService.coorden_mutantes.append([i+0,j-0])
						MutantService.coorden_mutantes.append([i+1,j-1])
						MutantService.coorden_mutantes.append([i+2,j-2])
						MutantService.coorden_mutantes.append([i+3,j-3])
						"""		
		#MutantService.printMatrizMutante(matriz)	
		return False

responseJSON = {
				"code": status_code["OK"],
  				"is_mutant": False,
				"status": status_code["OK"]
				}


a_buscar=G

responseJSON["code"], responseJSON["status"] = ValidateService.paramValidator(a_buscar)


if responseJSON["status"] == status_code["OK"]:
	responseJSON["is_mutant"] = MutantService.isMutant(a_buscar)
	print('Es Mutante') if responseJSON["is_mutant"] else print('No es mutante')
else:
	print('UPS! Algo salio mal')

print(json.dumps(responseJSON))