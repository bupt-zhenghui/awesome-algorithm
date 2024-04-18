def ishuiwen(s):
    n = len(s)
    if n == 1:
        return True
    res = ""
    for ch in s:
        if ord('A') <= ord(ch) <= ord('Z'):
            res = res + chr(ord(ch)+32)
        elif ord('a') <= ord(ch) <= ord('z'):
            res = res + ch
        elif ord('0') <= ord(ch) <= ord('9'):
            res = res + ch
        else:
            continue
    m = len(res)
    l, r = 0, m - 1
    while l <= r:
        if not res[l] == res[r]:
            return False
        l = l + 1
        r = r - 1
    return True


s = ","
print(ishuiwen(s))