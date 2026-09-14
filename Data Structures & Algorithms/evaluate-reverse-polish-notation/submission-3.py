class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for i in tokens:
            if i=="+":
                a = stack.pop()
                b = stack.pop()
                stack.append(a + b)
            elif i=="*":
                c=stack.pop()
                d=stack.pop()
                stack.append(c*d)
            elif i=="-":
                c=stack.pop()
                d=stack.pop()
                stack.append(d-c)
            elif i=="/":
                c=stack.pop()
                d=stack.pop()
                stack.append(int(d/c))
            else:
                stack.append(int(i))
        return stack[0]
            
                