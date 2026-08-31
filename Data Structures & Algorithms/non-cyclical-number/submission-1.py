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
        fast=n
        while True:
            slow=self.next_nums(slow)
            fast=self.next_nums(self.next_nums(fast))
            if slow==fast:
                break
        return slow==1
