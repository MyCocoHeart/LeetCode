#encoding = utf-8
"""
@version:??
@author: xq
@contact:xiaoq_xiaoq@163.com
@file: removeDuplicatesII.py
@time: 2017/10/30 20:36
"""


class Solution(object):
    '''
    Follow up for "Remove Duplicates":
    What if duplicates are allowed at most twice?
    For example,
    Given sorted array nums = [1,1,1,2,2,3],
    Your function should return length = 5, with the first five elements of nums being 1, 1, 2, 2 and 3. It doesn't matter what you leave beyond the new length.
    '''
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        k = len(nums)
        if (k == 0):
            return 0
        elif (k == 1):
            return 1
        else:
            i = 0
            num = 1
            while (i < k):
                j = i + 1
                if (j == k):
                    break
                if (nums[i] == nums[j]):
                    num += 1
                else:
                    num = 1
                if num <= 2:
                    i += 1
                else:
                    del nums[j]
                    k = len(nums)
            return k

    class Solution(object):
        def removeDuplicates(self, nums):
            """
            :type nums: List[int]
            :rtype: int
            """
            if nums is None or len(nums) == 0:
                return 0
            if len(nums) <= 2:
                return len(nums)
            i = 1
            for j in range(2, len(nums)):
                if nums[j] == nums[i] and nums[j] == nums[i - 1]:
                    j = j + 1
                else:
                    i = i + 1
                    nums[i] = nums[j]
                    j = j + 1
            return i + 1
    def removeDuplicates2(self, nums):
        """
        方法二
        :type nums: List[int]
        :rtype: int
        """
        if nums is None or len(nums)==0:
            return 0
        if len(nums)<=2:
            return len(nums)
        i=1
        for j in range(2,len(nums)):
            if nums[j]==nums[i] and nums[j]==nums[i-1]:
                j=j+1
            else:
                i=i+1
                nums[i]=nums[j]
                j=j+1
        return i+1
