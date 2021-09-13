def calculate_score(answers,key):
    grade_count=0
    if not len(answers)==len(key):
        return -1
    for i in range(len(answers)):
        if answers[i+1]==key[i+1]:
            grade_count+=1
    return grade_count
  