class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        biggestVolume = self.volume(left, height[left], right, height[right]) # starts as just volume using left and right
        while left < right:
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
            if biggestVolume < self.volume(left, height[left], right, height[right]): biggestVolume = self.volume(left, height[left], right, height[right])
        return biggestVolume

    def volume(self, index1, height1, index2, height2) -> int:
        low = height1 if height1 < height2 else height2
        high = height1 if height1 > height2 else height2
        return abs(low * (index2 - index1))