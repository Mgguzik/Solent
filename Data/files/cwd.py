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

# with open("trail.txt") as file:
#     text = file.readlines()
#     print(text)
#
#     for each_item in text:
#         item = each_item.strip()
#         print(item)

with open("trail.txt") as file:
    text = file.readline()
    print(text)
    text = file.readline()
    print(text)
    text = file.readline()
    print(text)


    # print(text.split("\n"))

# def search(file_path):
#     print("Searching...", end="")




