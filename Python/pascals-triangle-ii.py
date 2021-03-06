''''
Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.

Note that the row index starts from 0.


In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 3
Output: [1,3,3,1]
Follow up:

Could you optimize your algorithm to use only O(k) extra space?
'''




class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        # method one
        # row = [1]
        # for i in range(1,rowIndex+1):
        #     row = list(map( lambda x,y : x+y , row + [0] , [0] + row ))
        # return row



        # method two    老土的方法，但有效，不用借助高等函数map()
        res = [1]
        for i in range(1, rowIndex+1):
            res = [1] + [res[i] + res[i + 1] for i in range(len(res) - 1)] + [1]
        return res
