# takes a list and modifies it, remove the first and last elements, and returns None
def chop(list):
    del list[0]
    del list[-1]

# takes a list and returns a new list that contains all but the first and last elements

def middle(list):
    new = list
    return new[1:-1]

my_list = [1, 2, 2, 3, 4]
my_list2 = [1, 2, 2, 3, 4]

chop_list = chop(my_list)
print(my_list)
print(chop_list)

middle_list = middle(my_list2)
print(my_list2)
print(middle_list)