def most_oscars(dictionary):
    max_awards=max(dictionary.values())
    for name, awards in dictionary.items():
        if awards == max_awards:
            max_name=name
    max_tuple=(max_name,max_awards)
    return max_tuple
