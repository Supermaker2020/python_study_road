'''
￥￥￥￥￥￥￥￥￥￥￥￥￥￥1、双指针秒杀数组题￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥
'''

'#########快慢指针#######'


# 1、 删除有序数组中的重复项
def removeDuplicates(nums: list):
    if len(nums) == 0:
        return 0
    slow = 0
    fast = 0
    while fast < len(nums):
        if nums[fast] != nums[slow]:
            slow += 1
            nums[slow] = nums[fast]
        fast += 1
    return slow + 1


numbers = [1, 2, 3, 4, 5, 5, 6, 7, 7]
res = removeDuplicates(numbers)
print(res)


# 2. 移除元素

def removeElement(nums: list[int], val: int):
    if not nums:
        return None
    slow = 0
    fast = 0
    while fast < len(nums):
        if nums[fast] != val:
            nums[slow] = nums[fast]
            slow += 1
        fast += 1
    return slow


# 3、 移动零到末尾
def moveZeroes(nums: list[int]):
    p = removeElement(nums, 0)
    for i in range(p, len(nums)):
        nums[i] = 0


'######左右指针*************'


# 1、二分查找
def binarySearch(nums: list[int], target: int):
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = int((right + left) / 2)
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
    return -1


# 2、两数之和
def twoSum(nums: list[int], target: int):
    left = 0
    right = len(nums) - 1
    while left < right:
        sum = nums[left] + nums[right]
        if sum == target:
            return [left + 1, right + 1]
        elif sum < target:
            left += 1
        elif sum > target:
            right -= 1
    return [-1, -1]


# 3、反转数组
def reverseString(s):
    left = 0
    right = len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1


# 4、回文字符串判断
def isPalindrome(s):
    left = 0
    right = len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True


# 5、最长回文子串
class Solution:
    def expandAroundCenter(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return left + 1, right - 1

    def longestPalindrome(self, s: str) -> str:
        start, end = 0, 0
        for i in range(len(s)):
            left1, right1 = self.expandAroundCenter(s, i, i)
            left2, right2 = self.expandAroundCenter(s, i, i + 1)
            if right1 - left1 > end - start:
                start, end = left1, right1
            if right2 - left2 > end - start:
                start, end = left2, right2
        return s[start: end + 1]


'''
################2、前缀和##################
'''


def sumRange(nums, left, right):
    res = 0
    for i in range(left, right + 1):
        res += nums[i]
    return res
