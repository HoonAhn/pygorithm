# function that returns the number pair that adds up to target number. 
# Time Complexity: O(n)
def solve(nums:list, target:int):
    sum_hash = {}
    for i in range(len(nums)):
        sum_hash[nums[i]] = i

    for i in range(len(nums)):
        print(i,nums[i])
        other_pair = target-nums[i]
        if other_pair in sum_hash:
            return [i,sum_hash[other_pair]]
    return -1

print(solve([3,4,5,6,7,8,9,2,10],19))


