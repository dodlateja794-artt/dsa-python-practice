nums1=[1,2]
nums2=[4,6]
num=nums1+nums2
arr=sorted(num)
if len(arr)%2!=0:
    mid=len(arr)//2
    print(arr[mid])
else:
    mid=len(arr)//2
    print((arr[mid]+arr[mid-1])/2)

