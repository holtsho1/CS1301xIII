def course_info(tup_list):
    course_dict={}
    course_dict["students"]=[]
    average=0
    for tup in tup_list:
        course_dict["students"].append(tup[0])
        average=average+tup[1]
    average=average/len(tup_list)
    course_dict["avg_age"]=average
    return course_dict
  