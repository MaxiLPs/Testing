 #!/usr/bin/python

import unittest
import Xmen
from Xmen import codigo, status_code

"""
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
"""

A = [
	['A','A','A','A']
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

D = [
	['A'],
	['B'],
	['A'],
	['A']
	]

E =	[
	['B','A','F','W'],
	['A','R','Q','E'],
	['F','T','L','K'],
	['C','H','M','L'],
	]

F = [
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

G = [
	['B','A','F','W'],
	['A','R','Q'],
	['F','T','L','K'],
	['C','H','M','L'],
	]

H = []

class TestMutantService(unittest.TestCase):
	
	def test_ismutant(self):
		#Tests Verdaderos
		self.assertTrue(Xmen.MutantService.isMutant(A))
		self.assertTrue(Xmen.MutantService.isMutant(B))
		self.assertTrue(Xmen.MutantService.isMutant(F))
		#Test Falsos
		self.assertFalse(Xmen.MutantService.isMutant(C))
		self.assertFalse(Xmen.MutantService.isMutant(D))
		self.assertFalse(Xmen.MutantService.isMutant(E))


class TestValidateService(unittest.TestCase):

	def test_paramValidator(self):
		
		self.assertEqual(Xmen.ValidateService.paramValidator(A), (codigo["OK"],status_code["OK"]))
		#cuando es una matriz, pero es de distinto tamano algun vector
		self.assertEqual(Xmen.ValidateService.paramValidator(G), (codigo["OK"], status_code["P_Error"]))
		#cuando la matriz es vacia
		self.assertEqual(Xmen.ValidateService.paramValidator(H), (codigo["OK"], status_code["P_Error"]))
		#cuando no es una matriz
		self.assertEqual(Xmen.ValidateService.paramValidator(2), (codigo["Error"], status_code["T_Error"]))


if __name__ == "__main__":
	unittest.main()

