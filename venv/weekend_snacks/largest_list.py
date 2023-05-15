def largest_element_list(list1):
    lar_element = list1[0]
    for l in list1:
        if l > lar_element:
            lar_element = l
            return lar_element


li = [20, 45, 67, 88, 65, 90]
print(largest_element_list(list1))
