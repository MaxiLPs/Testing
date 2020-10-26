
import sys
import logging
from flask import Flask, json, request, jsonify

sys.path.append('../Services')
from MutantService import MutantService
from ValidateService import ValidateService

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

api = Flask(__name__)

@api.route('/companies', methods=['POST'])
def get_companies():
	#adn = json.loads(request.data)
	#adn = json.dumps(adn["dna"])
	#adn = json.loads(adn)
	adn = json.loads(json.dumps(json.loads(request.data)["dna"]))

	#print ('data: ', adn)
	
	MutantService.printMatrizMutante(adn)
	#MutantService.isMutant(adn)

	responseJSON = {
				"code": status_code["OK"],
  				"is_mutant": False,
				"status": status_code["OK"]
				}
	MutantService.printMatrizMutante(adn)


	responseJSON["code"], responseJSON["status"] = ValidateService.paramValidator(adn)


	if responseJSON["status"] == status_code["OK"]:
		responseJSON["is_mutant"] = MutantService.isMutant(adn)

	return responseJSON

#MutantService.isMutant(y)


if __name__ == '__main__':
    api.run() 
