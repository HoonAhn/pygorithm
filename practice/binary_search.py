def binary_search(sorted_collcection, target):
    left = 0
    right = len(sorted_collcection) - 1

    while left <= right:
        mid = left + (right-left)//2
        cursor = sorted_collcection[mid]
        if cursor == target:
            return mid
        elif cursor > target:
            right = mid - 1
        else:
            left = mid + 1
    return None


def binary_search_recursion(sorted_collcection, target, left, right):
    if right < left:
        return None
    
    mid = left + (right - left) // 2

    if sorted_collcection[mid] == target:
        return mid
    elif sorted_collcection[mid] > target:
        return binary_search_recursion(sorted_collcection, target, left, mid-1)
    else:
        return binary_search_recursion(sorted_collcection, target, mid+1, right)

sorted_collcection = [0, 5, 7, 10, 15] 
target = 5
print(binary_search(sorted_collcection, target))
print(binary_search_recursion(sorted_collcection, target,0, len(sorted_collcection)-1))