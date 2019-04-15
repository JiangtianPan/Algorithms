# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head:
            return True
        else:
            nums = []
            while head:
                nums.append(head.val)
                head = head.next
            length = len(nums)
            if length == 1:
                return True
            for i in range(int(length/2)):
                print(i)
                if nums[i] == nums[length -1 -i]:
                    continue
                else:
                    return False
            return True