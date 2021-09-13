def total_stats(dict_list):
    stats_dict={}
    for pokemon in dict_list:
        summ=0
        for (key,value) in pokemon.items():
            #stats_dict[pokemon["name"]]=0   unnecessary line
            if type(value)==int:
                summ=summ+value
            stats_dict[pokemon["name"]]=summ
    return stats_dict
