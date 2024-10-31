import math
def NULL_not_found(object: any) -> int:
	if (object == None):
		print(f"Nothing: {type(object).__name__} {type(object)}")
	elif (isinstance(object, float) and math.isnan(object) == True):
		print(f"Cheese: nan {type(object)}")
	elif (isinstance(object, bool) and object == False):
		print(f"Fake: False {type(object)}")
	elif (isinstance(object, int) and object == 0):
		print(f"Zero: 0 {type(object)}")
	elif (isinstance(object, str) and object == ""):
		print(f"Empty: {type(object)}")
	else:
		print("Type not found")
	return(1)