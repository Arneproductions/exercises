n = int(input())
arr = []

for _ in range(n):
    num = int(input())
    arr.append(num) 

def merge(arr, min, mid, max):
    n = max - min
    if n == 1:
        if arr[min] > arr[max]:
            temp = arr[min]
            arr[min] = arr[max]
            arr[max] = temp

            return 1

        return 0

    leftcount = mid - min + 1
    rightcount = max - mid
    
    L = arr[min:mid+1]
    R = arr[mid+1:max+1]

    i = 0     # Initial index of first subarray
    j = 0     # Initial index of second subarray
    k = min     # Initial index of merged subarray

    swapcount = 0
 
    while i < leftcount and j < rightcount:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
            swapcount += leftcount - i
            
        k += 1
    
    while i < leftcount:
        arr[k] = L[i]
        i += 1
        k += 1
        
    while j < rightcount:
        arr[k] = R[j]
        j += 1
        k += 1
    
    return swapcount
    
def merge_sort(arr, min, max):
    if (min < max):
        mid = min+(max-min)//2
        
        ls = merge_sort(arr, min, mid)
        rs = merge_sort(arr, mid+1, max)
        ms = merge(arr, min, mid, max)

        return ls+rs+ms
    
    return 0

res = merge_sort(arr, 0, (len(arr)-1))
print(res)