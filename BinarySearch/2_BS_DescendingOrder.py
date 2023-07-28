a = [10,9,8,7,6,5,4,3,2,1]
start = 0
end = len(a) - 1
def BS(a, start, end, target):
    while start <= end:
        # mid = (start + end)//2
        mid = int(start + (end - start)/2)
        if a[mid] == target:
            return mid
        elif a[mid] > target:
            start = mid + 1
        else:
            end = mid - 1
    return -1

print(BS(a, start, end, 10))