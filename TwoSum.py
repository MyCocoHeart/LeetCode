#encoding = utf-8
"""
@version:??
@author: xq
@contact:xiaoq_xiaoq@163.com
@file: TwoSum.py.py
@time: 2017/10/23 22:06
"""

class Solution:
    '''
    Given an array of integers, return indices of the two numbers such that they add up to a specific target.
    You may assume that each input would have exactly one solution, and you may not use the same element twice.
    Example:
    Given nums = [2, 7, 11, 15], target = 9,
    Because nums[0] + nums[1] = 2 + 7 = 9,
    return [0, 1].
    '''
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        result = []#the result which need to return
        k = 0 #the total number of removed
        data = nums[:]#copy nums
        for i in range(0, len(nums)):
            x = target - nums[i]
            data.remove(nums[i])
            k += 1
            if (x in data):
                result.append(i)
                if (x == nums[i]):
                    j = data.index(x)
                    result.append(j + k)
                    break
                else:
                    j = nums.index(x)
                    result.append(j)
                    break
            else:
                continue

        return result