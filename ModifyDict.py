def modify_dict(dictionary):
    del_keys=[]
    for key in dictionary.keys():
        if not key[0].isupper():
            del_keys.append(key)
    for key in del_keys:
        del dictionary[key]
    return dictionary
