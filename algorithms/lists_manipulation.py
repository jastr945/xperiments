# example input [1, 2, 3, 5], output: 4
def find_missing(my_list):
    """Returns a missing integer in a given list"""
    for index, elem in enumerate(my_list):
        ref = my_list[0]
        diff = elem - index
        results = []
        if ref!=diff:
            results.append(my_list[index] - 1)
            result = results[0]
            return result

print(find_missing([3, 4, 5, 7])) #6
print(find_missing([0, 1, 3, 4])) #2
print(find_missing([0, 1, 2, 3, 4, 6])) #5
print(find_missing([3, 4, 5, 6, 7, 9])) #8
print(find_missing([0, 2, 3, 4, 5, 6])) #1
