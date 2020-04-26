""" All tasks come from www.codewars.com """

"""
TASK: Get Planet Name By ID

The function is not returning the correct values. Can you figure out why?

get_planet_name(3) # should return 'Earth'
"""


def get_planet_name(id):

    dict_id = {
        1 : "Mercury",
        2 : "Venus",
        3 : "Earth",
        4 : "Mars",
        5 : "Jupiter",
        6 : "Saturn",
        7 : "Uranus",
        8 : "Neptune"}
    return [value for key, value in dict_id.items()][id-1]


# def get_planet_name(id):
#     return {
#         1: "Mercury",
#         2: "Venus",
#         3: "Earth",
#         4: "Mars",
#         5: "Jupiter",
#         6: "Saturn",
#         7: "Uranus",
#         8: "Neptune",
#     }.get(id, None)