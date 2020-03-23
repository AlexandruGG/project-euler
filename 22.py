# Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.
# For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.
# What is the total of all the name scores in the file?

from string import ascii_uppercase
from typing import List


def read_names_file(filename: str) -> List[str]:
    with open(filename, 'r') as file:
        names_List: List[str] = file.read().replace('"', '').split(',')

    names_List.sort()
    return names_List


def get_name_score(name: str) -> int:
    return sum(ascii_uppercase.index(c) + 1 for c in name)


def calculate_total_score(filename: str) -> int:
    names_list: List[str] = read_names_file(filename)

    return sum(index * get_name_score(name) for index, name in enumerate(names_list, start=1))


print(f"Score Total: {calculate_total_score('22-names.txt')}")
