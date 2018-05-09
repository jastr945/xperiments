# just a reminder about sorting an array
my_array = ["1", "0", "x", "a", "c"]
my_array.sort()
print(my_array)


# removing duplicates from a list
def remove_dupes(my_list):
    """Iterating over a given list and returning a new list without duplicates"""
    new_list = []
    for i in my_list:
        if i not in new_list:
            new_list.append(i)
    return new_list

print(remove_dupes(['9', '3', '9', '0', '0', '1']))
