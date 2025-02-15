from typing import List

class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

def interval_clash(intervals: List[Interval]) -> bool:
    time_set = set()
    if len(intervals) <= 1:
        return True

    else:
        for i in range(len(intervals)):
            if intervals[i][0] in time_set:
                return False
            else:
                j=intervals[i][0]
                k=intervals[i][1]
                for num in range(j,k):
                    time_set.add(num)
                    print(time_set)
        return True

some = interval_clash([(100,200),(200,300),(300,400),(400,500),(500,600),(600,700),(700,800),(800,900),(900,1000)])
print(some)