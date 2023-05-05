def is_nan(x):
    return (x != x)

def NULL_not_found(object: any):
    if object is None:
        print("Nothing: ", object, " ", end="")
        print(type(object))
    elif is_nan(object):
        print("Cheese: ", object, " ", end="")
        print(type(object))
    elif object is 0:
        print("Zero: ", object, " ", end="")
        print(type(object))
    elif object is "":
        print("Empty: ", object, " ", end="")
        print(type(object))
    elif object is False:
        print("Fake: ", object, " ", end="")
        print(type(object))
    else:
        print("Type not Found")
    return 1