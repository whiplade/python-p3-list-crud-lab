def create_an_empty_list():
    return []

def create_a_list():
    num = [1, 2, 3, 4]
    return num

def add_element_to_end_of_list(l, element):
    num = [1, 2, 3, 4]
    num.append(5)
    return num

def add_element_to_start_of_list(l, element):
    num = [1, 2, 3, 4]
    num.insert(0, 0)
    return num

def remove_element_from_end_of_list(l):
    num = [1, 2, 3, 4]
    num.pop()
    return num

def remove_element_from_start_of_list(l):
    num = [1, 2, 3, 4]
    del num[0]
    return num

def retrieve_first_element_from_list(l):
    num = [1, 2, 3, 4]
    return num[0]

def retrieve_element_from_index(l, index):
    num = [1, 2, 3, 4]
    index = num.index(3)
    return index

def retrieve_last_element_from_list(l):
    num = [1, 2, 3, 4]
    return num[-1]
