

def merge_sort(collection):
    print("START MERGE SORT",collection)
    def merge(left, right):
        print("MERGE LEFT",left,"AND RIGHT",right)
        result = []
        while left and right:
            result.append((left if left[0] <= right[0] else right).pop(0))
        return result + left + right 
    
    if len(collection) <= 1:
        return collection
    
    mid = len(collection) // 2 
    print("DIVIDE LEFT",collection[:mid],"AND RIGHT",collection[mid:])
    return merge(merge_sort(collection[:mid]),merge_sort(collection[mid:]))

print( merge_sort([0, 5, 3, 2, 2]))