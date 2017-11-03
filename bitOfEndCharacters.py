#encoding = utf-8
"""
@version:??
@author: xq
@contact:xiaoq_xiaoq@163.com
@file: bitOfEndCharacters.py
@time: 2017/11/3 9:18
"""


class Solution:
    '''
    We have two special characters. The first character can be represented by one bit 0. The second character can be represented by two bits (10 or 11).

    Now given a string represented by several bits. Return whether the last character must be a one-bit character or not. The given string will always end with a zero.

    Example 1:
    Input:
    bits = [1, 0, 0]
    Output: True
    Explanation:
    The only way to decode it is two-bit character and one-bit character. So the last character is one-bit character.
    Example 2:
    Input:
    bits = [1, 1, 1, 0]
    Output: False
    Explanation:
    The only way to decode it is two-bit character and two-bit character. So the last character is NOT one-bit character.
    '''

    def isOneBitCharacter(self, bits):
        i = 0
        while i < len(bits) - 1:
            i += bits[i] + 1
        return i == len(bits) - 1

    def mySolution(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        zeroNum = 0
        oneNum = 0
        twoOneNum = 0
        #因为已经知道最后一位肯定为0，所以如果长度为1则返回True
        bitsLength = len(bits)
        if (bitsLength == 1):
            return True
        # 如果数组长度大于1则,遇到0遍历的索引值加1，否则加2，然后判断是不是最后一位
        else:
            i = 0
            while i < (bitsLength - 1):
                if (bits[i] == 0):
                    i += 1
                else:
                    i +=2
            return i==bitsLength-1
