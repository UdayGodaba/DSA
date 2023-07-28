def subseq(i, e, nums, d):
    
    if i == len(nums):
        if e in d:
            return
        d.append(e.copy())
        return
    e.append(nums[i])
    subseq(i+1, e, nums, d)
    e.pop()
    subseq(i+1, e, nums, d)

d = []
nums =  [1,2,2]
subseq(0, [], nums, d)
    
print(d)
