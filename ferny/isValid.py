class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for ch in s:
            if ch in "{[(":
                stack.append(ch)
            else:
                if stack:
                    p = stack.pop()
                    if not (p == "{" and ch == "}" or p == "[" and ch == "]" or p == "(" and ch == ")"):
                        return False
                else:
                    return False

        print(stack)
        return not stack

print(Solution().isValid("(){}}{"))