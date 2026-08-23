intervals=[[0,10],[11,20],[21,40]]
intervals.sort()
for i in range(1,len(intervals)):
    if intervals[i][0]<intervals[i-1][1]:
        print(False)
        break
else:
    print(True)
