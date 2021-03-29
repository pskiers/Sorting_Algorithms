def bubble_sort(sorted_list):
    disorder = True
    while disorder:
        disorder = False
        for i in range(1, len(sorted_list), 1):
            if sorted_list[i-1] > sorted_list[i]:
                disorder = True
                sorted_list[i-1], sorted_list[i] = sorted_list[i], sorted_list[i-1]
    return sorted_list
