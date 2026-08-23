nums1=[1,2,3]
nums2=[4,6,5]
num=nums1+nums2
arr=sorted(num)
if len(arr)%2==0:
    mid=len(arr)//2
    print((arr[mid]+arr[mid-1])/2)
else:
    mid=len(arr)//2
    print(mid)