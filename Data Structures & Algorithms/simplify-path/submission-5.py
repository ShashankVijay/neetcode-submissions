class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = ['/']
        for ch in path:
            if not stack:
                stack = ['/']
            if ch == '/':
                if stack[-1] == '/':
                    stack.pop()
                stack.append(ch)
                continue
            stack[-1] = stack[-1] + ch
        
        stack2 = []

        for i, subPath in enumerate(stack):
            if subPath == "/.":
                continue
            elif subPath == "/..":
                if stack2:
                    stack2.pop()
            else:
                stack2.append(subPath)

        if not stack2:
            stack2.append('/')
            
        if len(stack2) > 1 and stack2[-1] == '/':
            stack2.pop()
        return "".join(stack2)
        

