class Solution:
    def swapPairs(self, head: 'ListNode') -> 'ListNode':
        if head and head.next:
            tmp = head.next
            head.next = self.swapPairs(tmp.next)
            tmp.next = head
            return tmp
        return head

//  (https://leetcode.com/explore/featured/card/recursion-i/250/principle-of-recursion/1681)[https://leetcode.com/explore/featured/card/recursion-i/250/principle-of-recursion/1681]
