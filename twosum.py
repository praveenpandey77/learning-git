nums= [2,7, 8,15]
target= 9
def twoSum(nums,target):
    
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            sum = nums[i] + nums[j]
            if sum == target:
                return [i,j]



