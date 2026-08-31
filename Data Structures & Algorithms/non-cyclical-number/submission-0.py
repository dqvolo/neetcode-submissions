class Solution:
    def next_nums(self, num):
        total = 0
        n = num

        while n:
            digit = n % 10
            total += digit ** 2
            n = n // 10

        return total
    def isHappy(self, n: int) -> bool:
        slow=n
        fast=self.next_nums(n)
        while slow!=fast:
            slow=self.next_nums(slow)
            fast=self.next_nums(self.next_nums(fast))
        return slow==1
