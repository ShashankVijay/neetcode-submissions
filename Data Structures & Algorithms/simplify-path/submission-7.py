class Solution:
    def simplifyPath(self, path: str) -> str:
        arr = ['/']
        for ch in path:
            if ch == '/':
                if arr[-1] == '/':
                    arr.pop()
                arr.append(ch)
                continue
            arr[-1] = arr[-1] + ch
        
        stack2 = []

        for i, subPath in enumerate(arr):
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
        

