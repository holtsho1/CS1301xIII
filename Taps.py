def stars(movies,tvshows):
    new_dict={}
    input_list=[movies,tvshows]
    for programs in input_list:
        for title,actor_list in programs.items():
            for actor in actor_list:
                try:
                    new_dict[actor].append(title)
                except KeyError:
                    new_dict[actor]=[]
                    new_dict[actor].append(title)
                new_dict[actor].sort()
    return new_dict
