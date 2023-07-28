nums = [1,2,8,10,11,12,19]

start = 0
end = len(nums) - 1
target = int(input("Enter a number to find ceil : "))

index = -1
while start <= end:
    mid = (start + end) // 2
    if nums[mid] >= target:
        index = nums[mid]
        end = mid - 1
    else:
        start = mid + 1

print(index)