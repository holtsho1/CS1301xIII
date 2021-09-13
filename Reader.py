def reader(filename):
    file=open(filename,"r")

def reader(filename):
    file=open(filename,"r")
    file_dict={}
    for line in file:
        split_line=line.split()
        try:
            split_line[0]=int(split_line[0]) #number
            split_line[2]=int(split_line[2]) #grade
            split_line[3]=int(split_line[3]) #total
            split_line[4]=float(split_line[4]) #weight
        except:
            print("Type Error in file")
        #tuple_line=tuple(split_line)  old code
        #file_list.append(tuple_line)  old code
        file_dict[split_line[1]]={"number":split_line[0],"grade":split_line[2],"total":split_line[3],"weight":split_line[4]}
    file.close()
    return file_dict
