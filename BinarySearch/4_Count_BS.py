a = [5,7,7,8,8,10,10,10,10,11,11,12,12]
# a = [4,4,4,4]
# a = [1]
start = 0
end = len(a) - 1
def BS(a, start, end, target):
    while start <= end:
        # mid = (start + end)//2
        mid = int(start + (end - start)/2)
        if a[mid] == target:
            first = last = mid
            while a[first - 1] == target and first-1 >= 0:
                    first -= 1
            while last + 1 < len(a) and a[last + 1] == target:
                    last += 1
            return last - first + 1
        elif a[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return 0
target = int(input("Enter a Target : "))
print("Count :",BS(a, start, end, target))