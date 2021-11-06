# Given an array of intervals where intervals[i] = [start_i, end_i], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

# Examples:

# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

# Input: intervals = [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.

"""
Are the intervals sorted?
No

Input : intervals = [[4,5],[1,4]]
output : [1,5]

Approach:
1. Sort the intervals
2. Have a result array
3. Store the first interval in it,
4. For the next set of intervals,
    Everytime fetch the interval in the result list
    Check if they are overlapping, 
      in which case club the intervals and update the result list
    else:
      add them to the result

Approach: 2
"""

def mergeSortedArray(intervals):
    intervals.sort()
    idx = 0
    while idx < len(intervals)-1:
      if intervals[idx][1] >= intervals[idx+1][0]:
        intervals[idx+1][0] = intervals[idx][0]
        if intervals[idx][1] > intervals[idx+1][1]:
          intervals[idx+1][1] = intervals[idx][1]
        intervals.pop(idx)
      else: idx += 1
    return intervals

print(mergeSortedArray([[1,3],[2,6],[8,10],[15,18]]))
print(mergeSortedArray([[4,5],[1,4]]))

# def mergeSortedArray(intervals):
#   if len(intervals) < 1:
#     return intervals

#   intervals.sort()
#   result = list()
#   result.append(intervals[0])
#   for idx in range(1,len(intervals)):
#     prev_interval = result[-1]
#     if prev_interval[1] <= intervals[idx][0]:
#       merged_intr = [prev_interval[0], intervals[idx][1]]
