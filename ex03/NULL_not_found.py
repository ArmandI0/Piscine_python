def NULL_not_found(object: any) -> int:
    if (isinstance(object, None)):
        print("Nothing: None <class 'NoneType'>")
    elif (isinstance(object, float) and object == NULL):
        print("Cheese: nan <class 'float'>")        
    return(1)