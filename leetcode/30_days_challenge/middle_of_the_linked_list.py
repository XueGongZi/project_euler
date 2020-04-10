# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        a, b, c = 1, 1, [head]
        while c[-1].next is not None:
            if a % 2 == 0:
                b += 1
            a += 1
            c.append(c[-1].next)
        if len(c) % 2 == 0:
            arr = c[b]
        else:
            arr = c[b - 1]
        return arr

a = [1, 2, 3, 4, 5]
b = [ListNode(a[0])]
for i in a[1:]:
    b[-1].next = ListNode(i)
    b.append(b[-1].next)
head = b[0]
print(Solution().middleNode(head).val)
        
