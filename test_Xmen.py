 #!/usr/bin/python

import unittest
import Xmen


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
	['B','A','F','W'],
	['A','R','Q','E'],
	['F','T','L','K'],
	['C','H','M','L'],
	]


class TestXMen(unittest.TestCase):
    
    def test_ismutant(self):
        #self.assertTrue(Xmen.isMutant(B))
        self.assertFalse(Xmen.isMutant(B))
        
if __name__ == "__main__":
    unittest.main()

