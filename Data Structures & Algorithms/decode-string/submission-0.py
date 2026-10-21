class Solution:
    def decodeString(self, s: str) -> str:
        num_stack=[]
        char_stack=[]
        num = 0
        current=""
        for i in s:
            if i.isdigit():
                num = num * 10 + int(i)
            elif i=="[":
                char_stack.append(current)
                num_stack.append(num)
                current=""
                num=0
            elif i=="]":
                prev=char_stack.pop()
                count=num_stack.pop()
                current=prev+current*count
            else:
                current+=i
        return current

