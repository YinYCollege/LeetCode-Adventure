class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # basic merge sorting
        combinedArr, i, j = [], 0, 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                combinedArr.append(nums1[i])
                i += 1
            else:
                combinedArr.append(nums2[j])
                j += 1
        while i < len(nums1):
            combinedArr.append(nums1[i])
            i += 1
        while j < len(nums2):
            combinedArr.append(nums2[j])
            j += 1
        if len(combinedArr) % 2 == 0:
            return (combinedArr[(len(combinedArr) // 2) - 1] + combinedArr[(len(combinedArr) // 2)]) / 2
        return combinedArr[len(combinedArr) // 2]