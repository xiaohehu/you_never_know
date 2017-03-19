# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        start = 0
        end = n
        mid = start + (end - start) / 2
        while (start + 1) < end:
            if isBadVersion(mid):
                end = mid
                mid = start + (end - start) / 2
            else:
                start = mid
                mid = start + (end - start) / 2
        if isBadVersion(start):
            return start
        if isBadVersion(end):
            return end
