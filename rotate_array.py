def rotate_array(arr, k):
    n = len(arr)
    print("n=",n)
    k = k % n # if k is more than length then also it calculates k to rotate.
    return arr[-k:] + arr[:-k]

print(rotate_array([1,2,3,4,5], 2))

