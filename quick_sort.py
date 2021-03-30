def quick_sort(sorted_list):
    if len(sorted_list) <= 1:
        return sorted_list
    left = 0
    right = len(sorted_list)
    chosen = sorted_list[0]
    while left != right:
        while sorted_list[left] < chosen:
            left += 1
        while right > 0 and sorted_list[right-1] >= chosen:
            right -= 1
        if right == left == 0:
            right = left = 1
        if right != left:
            sorted_list[left], sorted_list[right-1] = sorted_list[right-1], sorted_list[left]
    return quick_sort(sorted_list[0:left:]) + quick_sort(sorted_list[right::])
