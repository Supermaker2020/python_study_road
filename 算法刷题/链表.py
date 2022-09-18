'''
双指针秒杀链表
'''


# 快慢指针
# 1、删除排序链表中的重复元素
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode):
        if head == None:
            return None
        slow = head
        fast = head
        while fast != None:
            if fast.val != slow.val:
                slow.next = fast
                slow = slow.next
            fast = fast.next
        slow.next = None
        return head
