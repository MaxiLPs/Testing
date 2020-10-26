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
			return codigo["Error"], status_code["P_Error"]