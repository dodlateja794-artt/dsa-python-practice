import heapq    #it is inbuilt 
class medianfinder:   #take one class as medium finder
    def __init__(self):   #it calls itself as small and large when required
        self.small=[]
        self.large=[] 
    def addnum(self,num):   #this recieves one new number
        if not self.small or num<= -self.small[0]:    #If the smaller half is empty, or this number is smaller than/equal to the largest number currently in the smaller half, put it into small.
            heapq.heappush(self.small,-num)
        else:
            heapq.heappush(self.large,num)
        if len(self.small)>len(self.large)+1:
            value=-heapq.heappop(self.small)    #So move the largest value from small to large
            heapq.heappush(self.large,value)
        elif len(self.large)>len(self.small):
            value=heapq.heappop(self.large)    #So move the smallest value from large to small
            heapq.heappush(self.small,-value)
    def findmedian(self):
        if len(self.small)==len(self.large):
            return (-self.small[0]+self.large[0])/2
        return -self.small[0]
obj=medianfinder()

obj.addnum(5)
print(obj.findmedian())

obj.addnum(2)
print(obj.findmedian())

obj.addnum(10)
print(obj.findmedian())

obj.addnum(4)
print(obj.findmedian())