def population_density(dict_list):
    total_pop=0
    total_area=0
    density=0
    for country in dict_list:
        total_pop=country["population"]+total_pop
        total_area=country["area"]+total_area
    density=total_pop/total_area
    return density
