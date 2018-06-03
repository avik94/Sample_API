def catchEmptyString(blank_string_checking, msg):
    for pos,value in enumerate(blank_string_checking):
        print(pos,value)
        if not value:
            return {"message":msg[pos]+" Cannot Be Blank"}
