
# [(1, 3), (5, 8), (4, 10), (20, 25)]
# RETURN # [(1, 3), (4, 10), (20, 25)]

# 1. BF 방식


def solve(intervals):
    sorted_intervals = sorted(intervals, key=lambda a: a[0])
    merged_intervals = []

    for interval in sorted_intervals:
        if merged_intervals and interval[0] <= merged_intervals[-1][1]:
            merged_intervals[-1] = (merged_intervals[-1][0], max(merged_intervals[-1][1], interval[1]))
        else: 
            merged_intervals.append(interval)
    return merged_intervals

print(solve([(1, 3), (2,6), (5, 8), (4, 10), (20, 25)]))