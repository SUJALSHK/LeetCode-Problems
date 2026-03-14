# Intuition
# I choose the straight approach without thinking anything:
# we are give two array:
# -combine two array
# -sort them
# -find the median
##########################################################################

# Approach
# you can see the code below
#############################################################################

# Complexity
# Time complexity: 0ms
# Space complexity: 12.67 MB



class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        combined = nums1 + nums2 #combine two list
        combined.sort() #using the sort() which is inbuilt function in python
        n = len(combined) #find the length of the list

        if n%2 ==1: #if odd return the median
            median = combined[n//2]
        else: # if even
            median = (combined[n//2-1] + combined[n//2]) /2.0
        return median


if __name__ == '__main__':
    solution = Solution()
    nums1 = [1, 2]
    nums2 = [3,4]
    solution.findMedianSortedArrays(nums1, nums2)
    print(nums1)
    print(nums2)
    print(solution.findMedianSortedArrays(nums1, nums2))