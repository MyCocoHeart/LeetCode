#encoding = utf-8
"""
@version:??
@author: xq
@contact:xiaoq_xiaoq@163.com
@file: maxConsecutiveOnes.py
@time: 2017/11/7 21:13
"""
class Solution(object):
    '''
    Given a binary array, find the maximum number of consecutive 1s in this array.

    Example 1:
    Input: [1,1,0,1,1,1]
    Output: 3
    Explanation: The first two digits or the last three digits are consecutive 1s.
        The maximum number of consecutive 1s is 3.
    Note:

    The input array will only contain 0 and 1.
    The length of input array is a positive integer and will not exceed 10,000

    '''

    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        oneConsecut = 0
        result =[]
        length =len(nums)
        for i in range(length):
            if nums[i]==1:
                oneConsecut += 1
                if((i != length-1) and (nums[i+1]==1)):
                    continue
                else:
                    result.append(oneConsecut)
                    oneConsecut = 0
        if result ==[]:
            return 0
        else:
            return max(result)