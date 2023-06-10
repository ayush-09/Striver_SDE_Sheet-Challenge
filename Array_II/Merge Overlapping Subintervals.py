"""
Spyder Editor

This is a temporary script file.
"""

def merge(intervals):
    res=[]
    if len(intervals)==0:
        return res
    intervals.sort()
    t=intervals[0][0]
    e=intervals[0][1]
    for i in intervals:
        if i[0]<=e:
            e=max(e,i[1])
        else:
            res.append([t,e])
            t=i[0]
            e=i[1]
    res.append([t,e])
    return res

if __name__=="__main__":
    intervals = [[1,3],[2,6],[8,10],[15,18]]
    print(merge(intervals))