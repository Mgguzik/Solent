pop_dict = {"The Matrix":["Keanu Reeves", "Carrie- Anne Moss", "Hugo Weaving"],
            "Jack Ryan": ["John Krasinski", "Wendell Pierce", "Abbie Cornish"],
            "Harry Potter" : ["Daniel Radcliffe", "Emma Watson", "Ruper Grint"],
            "Friends": ["Jennifer Aniston", "Courtney Cox","Lisa Kudrow"],
            "The office" : ["Steve Carell", "Rain Wilson", "John Krasinski"]}
def get_cast(title):
    if title in pop_dict:
        return pop_dict[title]
    else:
        return []
# test#
# print(get_cast("Friends"))

def add_title(title, cast_list):
    pop_dict[title]= cast_list

add_title("Breaking Bad", ["Bryan Cranston", "Aaron Paul", "Anna Gunn"])
print(pop_dict)

def count_actors():
    actors = dict()
    for cast_list in pop_dict.values():
        for actor in cast_list:
            if actor in actors:
                actors[actor] +=1
            else:
                actors[actor] =1
    return actors
print(count_actors())