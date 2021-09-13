def phonebook(names,numbers):   
    dic = {}
    count=0
    for item in names:
        dic[item]=numbers[count]
        count+=1

    return dic