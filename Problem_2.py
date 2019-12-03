# Space complexity:  O(1)
# Runtime complexity:  O(n)
# number of comparisions will decrease by 2 as grouping of elements is done.



def get(arr):
    if len(arr)%2==0:
        minimum = 100000000000
        maximum = -100000000000
    else:
        minimum = arr[-1]
        maximum = arr[-1]
        del arr[-1]
    for i in range(0,len(arr),2):
        if arr[i]<arr[i+1]:
            minimum = min(minimum,arr[i])
            maximum = max(maximum,arr[i+1])
        else:
            minimum = min(minimum,arr[i+1])
            maximum = max(maximum,arr[i])
    print(minimum,maximum)
    
arr = [4,-2,6,5,45,7,90]
get(arr)