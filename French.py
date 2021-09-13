def french2eng(sentence):
    sentence=sentence.lower()
    sent_list=sentence.split()
    new_list=[]
    for word in sent_list:
        try:
            new_list.append(french_dict[word])
        except KeyError:
            new_list.append(word)
    #print(new_list)
    new_list=" ".join(new_list)
    return new_list
