import os
from os import path
import shutil
import re


def rename(name):
    pathed = fr'C:\Users\Serafim\Desktop\{name}'
    if not os.path.isdir(pathed):
        os.mkdir(pathed)
    return pathed


def replace_file(source_path, pathed, name_for_file):
    if path.exists(source_path):
        destination_path = f"{pathed}/{name_for_file}"
        shutil.move(source_path, destination_path)
    else:
        print("Invalid file path")


def find_the_file():
    path_to_file = ''
    pathed = r"C:\Users\Serafim\Downloads"
    list_dir = os.listdir(pathed)
    for i in list_dir:
        if re.search("audio-joiner", i) and not re.search(".dowload", i):
            path_to_file = (pathed + r'\\' + i)
            break
    return path_to_file
