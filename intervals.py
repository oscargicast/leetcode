from typing import List, Union


def get_intervals(start: int, end: int, width: int) -> List[Union[int, int]]:
    intervals = []
    n_intervals = (end - start) // width
    start_interval = end_interval = start
    for i in range(n_intervals):
        start_interval += width * (i > 0) 
        end_interval = start_interval + width
        intervals.append([start_interval, end_interval])
    if end - end_interval > 0:
        intervals.append([end_interval, end])
    print(len(intervals))
    return intervals


if __name__ == "__main__":
    assert(get_intervals(0, 100, 30) == [[0, 30], [30, 60], [60, 90], [90, 100]])
    assert(get_intervals(1, 10, 4) == [[1, 5], [5, 9], [9, 10]])
    assert(get_intervals(1, 11, 4) == [[1, 5], [5, 9], [9, 11]])
    assert(get_intervals(1665238380, 1665319580, 86400) == [[1665238380, 1665319580]])
    assert(get_intervals(1665238380, 1665903254, 86400) == [[1665238380, 1665324780], [1665324780, 1665411180], [1665411180, 1665497580], [1665497580, 1665583980], [1665583980, 1665670380], [1665670380, 1665756780], [1665756780, 1665843180], [1665843180, 1665903254]]) 
