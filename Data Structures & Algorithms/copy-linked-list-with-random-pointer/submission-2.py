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
        dick={}
        if not head:
            return None
        cur=head
        while cur:
            dick[cur]=Node(cur.val)
            cur=cur.next
        cur=head
        while cur:
            dick[cur].next=dick.get(cur.next)
            dick[cur].random=dick.get(cur.random)
            cur=cur.next
        return dick[head]