def word_lengths(string):
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
        string_dict[strings]=count
    return string_dict

