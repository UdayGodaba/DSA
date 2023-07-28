# You are given a 0-indexed integer array nums.

# We say that an integer x is expressible from nums if there exist some integers 0 <= index1 < index2 < ... < indexk < nums.length for which nums[index1] | nums[index2] | ... | nums[indexk] = x. In other words, an integer is expressible if it can be written as the bitwise OR of some subsequence of nums.

# Return the minimum positive non-zero integer that is not expressible from nums.

 

# Example 1:

# Input: nums = [2,1]
# Output: 4
# Explanation: 1 and 2 are already present in the array. We know that 3 is expressible, since nums[0] | nums[1] = 2 | 1 = 3. Since 4 is not expressible, we return 4.
# Example 2:

# Input: nums = [5,3,2]
# Output: 1
# Explanation: We can show that 1 is the smallest number that is not expressible.
 

# Constraints:

# 1 <= nums.length <= 105
# 1 <= nums[i] <= 109
# --------------------------------------------------------------------------------------------------------------------------------------------------------

# Intution :
            # if list is like [2**0, 2**1, 2**2, 2**3, 2**4,................,2**n] then it is possible to form every number in [1, 2**(n+1) - 1]
            # The 2**i which is missing is the least positive number that cannot be formed.
# -------------------------------------------------------------------------------------------------------------------------------------------------------

nums = [8,2048,32768,1,1024,512,4,467,65536,256,16384,205,262144,64,128,2,1200,131072,8192,16,524288,4096,32]
nums = [2,1]
nums = [5,3,2]

for i in range(33):
    if 1 << i not in nums:
        print("The least not possible positive number is :", 1 << i)
        break