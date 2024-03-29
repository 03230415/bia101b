class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        list = [1,2,3,1]
        nums2 = set(int(nums))
        for i in nums:
            if nums != nums2:
                return True
            else:
                return False