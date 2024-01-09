class Solution:

    def calculate_sum(self, fac):
        total = 0
        for idx,ch in enumerate(fac):
            total = total + pow(10,idx)*(ord(ch)-48)
        return total


    def decodeString(self, s: str) -> str:
        stack = ""
        for ch in s:
            if ch != "]":
                stack += ch
            else:
                n = len(stack)
                j = n - 1
                fac = ""
                while j >= 0:
                    if stack[j] == "[":
                        k = j - 1
                        while k >= 0:
                            if 48 <= ord(stack[k]) <= 57:
                                fac += stack[k]
                                k = k - 1
                            else:
                                break
                        fac = self.calculate_sum(fac)
                        # print(fac)
                        break
                    else:
                        j -= 1
                tmp = stack[j+1:n]
                # print(tmp)
                # print(k)
                stack = stack[:k+1]+fac*tmp
        return stack

# print(Solution().decodeString("abc3[cd]xyz"))





print(Solution().decodeString("3[a2[c]]"))