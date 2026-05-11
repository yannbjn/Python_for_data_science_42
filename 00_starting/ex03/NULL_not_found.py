def NULL_not_found(object: any) -> int:
    obj_type = type(object)

    if object is None:
        print(f"Nothing: {object} {obj_type}")
    elif obj_type == float and object != object: #this is to catch NaN
        print(f"Cheese: nan {obj_type}")
    elif obj_type == int and object == 0 and not isinstance(object, bool):
        print(f"Zero: {object} {obj_type}")
    elif obj_type == str and object == '':
        print(f"Empty: {object}")
    elif obj_type == bool and object is False:
        print(f"Fake: {object} {obj_type}")
    else:
        print("Type not Found")
        return 1
    
    return 0
