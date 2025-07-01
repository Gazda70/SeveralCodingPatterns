class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def get_interval(self):
        print(str(self.start) + ", " + str(self.end))


def merge(intervals):
    if len(intervals) < 2:
        return intervals

    intervals.sort(key=lambda x: x.start)

    merged_intervals = []

    start = intervals[0].start
    end = intervals[0].end

    for i in range(1, len(intervals)):
        interval = intervals[i]

        if interval.start <= end:
            end = max(interval.end, end)
        else:
            merged_intervals.append(Interval(start, end))
            start = interval.start
            end = interval.end

    merged_intervals.append(Interval(start, end))

    return merged_intervals

merged = merge([Interval(6, 7), Interval(2, 4), Interval(5, 9)])

for m in merged:
    m.get_interval()

def merge(arr):
    if len(arr) < 2:
        return arr

    arr.sort(key=lambda x:x.start)
    merged_intervals = []
    start = arr[0].start
    end = arr[0].end

    for i in range(1, len(arr)):
        interval = arr[i]

        if interval.start < end:
            end = max(interval.end, end)
        else:
            merged_intervals.append(Interval(start, end))
            start = interval.start
            end = interval.end
    merged_intervals.append(Interval(start, end))

    return merged_intervals


def merge(arr):
    if len(arr) < 2:
        return arr

    arr.sort(key=lambda x:x.start)
    merged_intervals = []
    start = arr[0].start
    end = arr[0].end

    for i in range(1, len(arr)):
        interval = arr[i]

        if interval.start < end:
            end = max(interval.end, end)
        else:
            merged_intervals.append(Interval(start, end))
            start = interval.start
            end = interval.end
    merged_intervals.append(Interval(start, end))

    return merged_intervals
