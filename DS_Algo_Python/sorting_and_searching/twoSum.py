class Solution:
    
    def binSearch(self,nums,low,high,key):
        if len(nums) == 0:
            return -1
        if high >= low:

            mid = (low + high) // 2

            if nums[mid] == key:
                # print(nums[mid],"key")
                return mid
            elif nums[mid] > key:
                return self.binSearch(nums,low,mid-1,key)
            else:
                return self.binSearch(nums,mid + 1,high,key)
            
        else:  
            return -1
        
    def twoSum(self, nums, target: int):
        
        if len(nums) == 2:
            if nums[0] + nums[1] == target:
                return [0,1]
            return []
        
        m = {}
        for i,num in enumerate(nums):
            m[num] = i 
               
        n = len(nums)
        
        p1 = 0
        p2 = 1
        while p1 < n - 1 or p2 < n-1:
            
            key = target - nums[p1]

            temp = nums[p1+1:]
            temp.sort()

            # print(key,target,p1,nums[p1],nums)
            index = self.binSearch( temp, 0, len(temp)-1 ,key )

            if index != -1:
                # print(key,[p1,p1+index])
                return [p1,m[key]]
            
            
            if nums[p1] + nums[p2] == target:
                return [p1,p2]
            
            p1 += 1
            p2 += 1
        return []
    
s = Solution()
print(s.twoSum([5,75,25],100))