# Problem-8
# Write a function insert that accepts a sorted list L of numbers and a number x as input. The function should return a sorted list with the element x inserted in the input list at the right place. The original list should not be disturbed in the process.

def insert(L, x):
    new_list = []  # new list to store the result
    inserted = False  # to track if x has been inserted

    for item in L:
        if not inserted and x <= item:
            new_list.append(x)  # insert x before the current item
            inserted = True
        new_list.append(item)  # add the current item

    if not inserted:
        new_list.append(x)  # if x is greater than all, add at the end

    return new_list


# Example
L = [1, 3, 5, 7]
print(insert(L, 4))  # Output: [1, 3, 4, 5, 7]
print(insert(L, 8))  # Output: [1, 3, 5, 7, 8]
print(insert(L, 0))  # Output: [0, 1, 3, 5, 7]