def miniMaxSum(arr):
    small = arr.index(min(arr))
    big = arr.index(max(arr))
    
    if small == big:
        print(4 * arr[small], 4 * arr[big])
        return
    
    min_sum = max_sum = 0
    
    for i in range(len(arr)):
        if i != small:
            max_sum += arr[i]
        if i != big:
            min_sum += arr[i]
    
    print(min_sum, max_sum)

miniMaxSum([1,2,3,4,5,6])




# way 2


def minMaxSum(arr):
    small = arr.index(min(arr))
    big = arr.index(max(arr))

    min_sum = sum(arr) - arr[big]
    max_sum = sum(arr) - arr[small]

    print(min_sum, max_sum)
 
 
minMaxSum([1,2,3,4,5,6])