d = {}
nums = [1,3,1,1,2]
for i in range(len(nums)):
    if nums[i] not in d:
        d[nums[i]] = [i]
    else:
        d[nums[i]].append(i)

print(d)