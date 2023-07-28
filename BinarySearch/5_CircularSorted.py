a = [11,12,15,18,2,5,6,8]
a = [15,18,2,5,6,8,11,12]
a = [12,15,18,2,5,6,8,11]
# a = [5,6,8,11,12,15,18,2]
# we need to find how many times it need to be rotated so that it is sorted
# if we find min val index it is done as it is sorted array just rotated
def BSCR(start, end, a):
    n = len(a)-1
    while start <= end:
        mid = int(start + (end - start)/2)
        if a[mid + n - 1]%n >= a[mid] and a[mid] <= a[mid + 1]%n:
            return mid
        elif a[mid + n - 1]%n  <= a[mid] <= a[mid + 1]%n:
            end = mid - 1
        else:
            start = mid + 1

print(BSCR(0, len(a)-1, a))