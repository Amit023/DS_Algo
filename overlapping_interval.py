'''
    WAF that takes in a non-empty array of arbitary intervals, merges any overlapping intervals,
    and returns the new interval in no particular order

    interval = [starting_index, ending_index]
    Intervals are considered overlapping if the values considered in the interval is overlapping

    Sample Input: [[1, 2] [3, 5] [4, 7] [6, 8] [9, 10]]
    Sample Output: [[1,2] [3, 8] [9, 10]]
'''


# Time Complexity: O(N * log N)| Space Complexity: O(1)
def overlapping_intervals(intervals):
    merged_intervals = []

    sorted_intervals = sorted(intervals, key = lambda x: x[0])
    current_interval = sorted_intervals[0]
    merged_intervals.append(current_interval)

    for next_interval in sorted_intervals:
        _, current_interval_end = current_interval
        next_interval_start, next_interval_end = next_interval

        if current_interval_end >= next_interval_start:
            current_interval[1] = max(current_interval_end, next_interval_end)
        else:
            merged_intervals.append(next_interval)
            current_interval = next_interval
    
    return merged_intervals


print(overlapping_intervals( [[1, 2], [3, 5], [4, 7], [6, 8], [9, 10]]) )

print(overlapping_intervals( [[1, 8], [3, 5], [4, 7], [6, 8], [9, 10]]) )

