def taps(file):
    tapcount={}
    total=0
    for transaction in file:
        transaction=transaction.split(",")
        try:
            tapcount[transaction[3]]+=1
        except KeyError:
            tapcount[transaction[3]]=0
    for value in tapcount.values():
        total=total+value
    length=len(tapcount.values())
    average=total/length
    result=[average,tapcount]
    return result

def station_close_avg(file):
    result=taps(file)
    average=result[0]
    tapcount=result[1]
    diffcount={}
    #for station,value in tapcount.items():
        #diffcount
    given_value=average
    absolute_difference_function = lambda list_value : abs(list_value - given_value)
    closest_value = min(tapcount.values(), key=absolute_difference_function)
    #print(closest_value)
    stat_close_avg=list(tapcount.keys())[list(tapcount.values()).index(closest_value)]
    return stat_close_avg

def least_traffic(file):
    result=taps(file)
    average=result[0]
    tapcount=result[1]
    least_value=min(tapcount.values())
    least_stat=list(tapcount.keys())[list(tapcount.values()).index(least_value)]
    return least_stat