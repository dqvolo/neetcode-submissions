"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        dic={}
        i=Node(0)
        temp=i
        cur=head
        while cur:
            t=Node(cur.val)
            dic[cur]=t
            if temp:temp.next=t
            temp=temp.next
            cur=cur.next
        cur=head
        while cur:
            if cur.random:
                dic[cur].random=dic[cur.random]
            else:
                dic[cur].random=None
            cur=cur.next
        return i.next