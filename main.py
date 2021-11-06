# Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

#     [4,5,6,7,0,1,2] if it was rotated 4 times.
#     [0,1,2,4,5,6,7] if it was rotated 7 times.


# Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

# Given the sorted rotated array nums of unique elements, return the minimum element of this array.

# You must write an algorithm that runs in O(log n) time.

# Examples:

# Input: nums = [3,4,5,1,2,3]
# Output: 1
# Explanation: The original array was [1,2,3,4,5] rotated 3 times.

# Input: nums = [4,5,6,7,0,1,2]
# Output: 0
# Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.

"""
Approach:

Edge Case: 
  if the first element is smaller than the last element, the array is already sorted after 'x' rotations.
    return the first element
  If there is just one element or None, return the array as such.

Go with the binary search Approach
  Get the middle element and left and right extreme numbers.
  Check if middle is less than both of them.
    if true:
      return the middle element as the smallest
    else:
      call the binary search in the direction of the smallest among the three
      If left extreme is smaller, move in the left direction
      else move in the right direction
      

"""

def rotated_min(nums):
  start, end = 0, len(nums) - 1
  if nums[0] < nums[-1]:
    return nums[0]
  if not nums:
    return None
  if len(nums) == 1:
    return nums[0]
  while start < end:
    print(start, end)
    if start == end:
      return nums[start]
    mid = (end - start) // 2
    if nums[mid] <= nums[end] and nums[mid] <= nums[start]:
      return nums[mid]
    elif nums[start] > nums[end]:
      start = mid + 1
    elif nums[start] < nums[end]:
      end = mid - 1
    else:
      return nums[mid]

print(rotated_min([3,4,5,1,2]))
# assert rotated_min([3,4,5,1,2]) == 1
# assert rotated_min([4,5,6,7,0,1,2]) == 0

    