nums = [1,1,2]
#nums = [0,0,1,1,1,2,2,3,3,4]

def removeDuplicates(nums: list[int]) -> int:
    k=0
    print(f"Input nums is { nums }")
    
    for n in nums:
        if n == nums[k]:
            continue
        nums[k] = n
        k += 1

    print(f"Nums is now { nums }")
    return k

count = removeDuplicates(nums)
print(f"The count is { count }")
