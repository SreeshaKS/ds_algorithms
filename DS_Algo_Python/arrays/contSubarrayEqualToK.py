def subarraySum( nums, k):
        i = 0
        j = 0
        sANum = 0
        n = len(nums)
        
        while i < n:
            j = 0
            while j + i < n:
                x = nums[ i : i+j ]
                s = sum(x)
                if s == k:
                    sANum += 1
                j += 1
            if nums[i] == k:
                sANum += 1
            i += 1

        return sANum
print(subarraySum([1,2,1,2,1],3))