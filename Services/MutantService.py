from __future__ import print_function
from termcolor import colored

class MutantService(object):
	
	genmutante = ['A', 'C', 'T', 'G']
	coorden_mutantes = []
	repeticion = 4

	@staticmethod
	def printMatrizMutante(matriz):
		print ('fila', len(matriz))
		print ('columna', len(matriz[0]))
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
			print ('')

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