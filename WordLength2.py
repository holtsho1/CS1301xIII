def length_words(string):
    string_dict={}
    string=string.lower()
    string=string.replace(".","")
    string=string.replace(",","")
    string=string.replace("?","")
    string=string.replace("!","")
    string=string.replace("'","")
    string_list=string.split()
    for strings in string_list:
        count=0
        for letters in strings:
            count+=1
        try:
            string_dict[count].append(strings)
        except KeyError:
            string_dict[count]=[]
            string_dict[count].append(strings)
        
        
    return string_dict
