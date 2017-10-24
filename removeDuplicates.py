#encoding = utf-8
"""
@version:??
@author: xq
@contact:xiaoq_xiaoq@163.com
@file: removeDuplicates.py
@time: 2017/10/24 20:57
"""


class Solution(object):
    '''
    Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.
Do not allocate extra space for another array, you must do this in place with constant memory.
For example,
Given input array nums = [1,1,2],
Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively. It doesn't matter what you leave beyond the new length.
    '''
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        k = len(nums)#get the length of nums
        if (k == 0):
            return 0
        elif (k == 1):
            return 1
        else:
            i = 0
            while i < k:
                j = i + 1
                if (j == k):
                    break
                if (nums[i] == nums[j]):
                    del nums[j]
                    k = len(nums)
                else:
                    i = j

            return k
