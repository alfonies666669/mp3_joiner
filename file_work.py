import os

path = r'C:\Users\Serafim\Downloads\man_who_laughs'


def list_books(pathfinding):
    not_empty_list = []
    for i in os.listdir(pathfinding):
        not_empty_list.append(pathfinding + r'\\' + i)
    return not_empty_list
