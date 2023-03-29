# import os
# path = os.getcwd()
# print(path)
#
# print(os.listdir(path))

import os

def cwd():
    path = os.getcwd()
    print(f"The current working directory is {path}")
    print("The directory contains the following: ")
    contents = os.listdir(path)
    for order, each_content in enumerate(contents):
        print(f"{order+1} : {each_content}")


def run():
    print("Processing")
    cwd()

# run()

with open("trail.txt") as file:
    text = file.read()
    print(text)
    print(text.split("\n"))

def search(file_path):
    print("Searching...", end="")




