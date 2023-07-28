a = [1,2,3,4,5,6,7,8,9,10]
start = 0
end = len(a) - 1
def BS(a, start, end, target):
    while start <= end:
        # mid = (start + end)//2
        mid = int(start + (end - start)/2)
        if a[mid] == target:
            return mid
        elif a[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return -1

print(BS(a, start, end, 1))