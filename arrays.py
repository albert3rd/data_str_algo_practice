# Two Sum 

nums = [2,7,11,15]
target = 9

# Arrays


# Arrays

# CONTAINS DUPLICATE
nums1 = [1,2,3,1]

    # Contains duplicate: set up hashmap or hash set; Iterate over the values and add to list if it is not present. 

def contains_duplicate(nums):
    hash_map = {} #or hashset set()
    for i in nums:
        if i in hash_map:
            return True
        else:
            hash_map[i] = i # hashset.add(n)
    return False


# TWO SUM

def twoSum(nums, target):
    """
    Process
        The first step is to create a space in memory with a hash table.
        Then iterate over it and if the target - array value is not in the table
        then add the diff into the table.
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    hashed = {}
    for i in range(len(nums)):
        diff = target - nums[i]
        if diff in hashed:
            return [i, hashed[diff]]
        hashed[nums[i]] = i
    return -1

print(twoSum(nums,target))


# SECOND Median of Two Sorted Arrays










Time: O(n)
Space: O(n) 
def twoSum(nums, target):
    """
    Process
        The first step is to create a space in memory with a hash table.
        Then iterate over it and if the target - array value is not in the table
        then add the diff into the table.
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    hashed = {}
    for i in range(len(nums)):
        diff = target - nums[i]
        if diff in hashed:
            return [i, hashed[diff]]
        hashed[nums[i]] = i
    return -1

print(twoSum(nums,target))
