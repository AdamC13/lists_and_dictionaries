import shutil
def line_break():
    terminal_width = shutil.get_terminal_size().columns
    line = '=' * terminal_width
    print(line)



# Task 1
def sq_nums(n):
    new_list = [num**2 for num in range(1,n) ]       #time complexity is linear as this is looping through a tuple --> range(1,n)
    return new_list                                  #space complexity is linear because the size of the list grows as the input grows
print(sq_nums(5))
line_break()



# Task 2
def reverse_within_list(array, i, j):
    if i > 0:
        arr_f = array[0:i]
    else:
        arr_f = []

    rev_arr = []
    for element in array[i:j+1]:
        rev_arr = [element] + rev_arr

    if (len(array) - 1) > j:
        arr_b = array[j+1:]
    else:
        arr_b = []

    return(arr_f + rev_arr + arr_b)

# the time complexity is linear and the space complexity is also linear

print(reverse_within_list([0,1,2,3,4,5], 2, 4))
line_break()



# Task 3
def merge_arrays(arr_l, arr_r):
    l = 0
    r = 0
    arr_m = []
    while l < len(arr_l) and r < len(arr_r):
        if arr_l[l] < arr_r[r]:
            arr_m.append(arr_l[l])
            l += 1
        else:
            arr_m.append(arr_r[r])
            r += 1
    
    while l < len(arr_l):
        arr_m.append(arr_l[l])
        l += 1
    while r < len(arr_r):
        arr_m.append(arr_r[r])
        r += 1

    return(arr_m)

# The time complexity is linear anf the space complexity is also linear

a = [0, 3, 45, 86, 1100]
b = [-1, 13, 25, 650, 651]
print(merge_arrays(a,b))
line_break()



# Task 1
def merge_dict(dict_a, dict_b):
    dict_c = dict_a.copy()
    for key in dict_b.keys():
        try:
            dict_c[key]
            dict_c[key] = [dict_c[key], dict_b[key]]
        except KeyError:
            dict_c[key] = dict_b[key]

    return dict_c

# the time complexity is linear and the space complexity is also linear

a = {
    "a" : "Hello",
    "b" : 35,
    "c" : [14, "bye"]
}
b = {
    "b" : "Adam",
    7 : 13,
    "15" : [75, "Cifelli"]
}

print(merge_dict(a, b))
line_break()



# Task 2
def dict_intersect(dict_a, dict_b):
    for key in dict_a:
        try:
            print(f'A common key is {key}. The values are {dict_a[key]} and {dict_b[key]}')
        except KeyError:
            continue

# the time complexity is linear and the space complexity is constant because I'm not storing anything

dict_intersect(a,b)
line_break()



# Task 3
def count(words):
    new_dict = {}
    for word in words:
        new_dict[word] = new_dict.setdefault(word, 0) + 1
    return new_dict

# The time complexity is linear and the space complexity is also linear

print(count(["Adam", "Cifelli", "Hello", "Bye", "Adam", "Bye", "Hi", "Adam"]))
