class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        combinedArray = nums1 + nums2
        combinedArray.sort()
        indx = len(combinedArray)/2
        print(combinedArray, indx)
        if len(combinedArray) == 2:
            return (combinedArray[0] + combinedArray[1])/2.0
        if len(combinedArray)%2 == 0:
            return (combinedArray[indx-1] + combinedArray[indx])/2.0
        else:
            return combinedArray[indx]
        
    
        
