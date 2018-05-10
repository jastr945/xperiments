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


# Traversing a linked list
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def traverse(self):
        node = self
        while node != None:
            print(node.val)
            node = node.next

if __name__ == "__main__":
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(1)
    node1.next = node2
    node2.next = node3
    node3.next = node4

    node1.traverse()


# list1=[1, 2, 3], list2=[4, 5, 6,5,10] How to sum these lists having different lengths?
def sum_lists(my_list1, my_list2):
    """Creating a sum of two lists"""
    sum1 = sum(my_list1)
    sum2 = sum(my_list2)
    return sum1 + sum2

print(sum_lists([1, 2, 3],[4, 5, 6,5,10]))
