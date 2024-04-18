def quick_power(n, k):
    MOD = int(1e9+7)

    if k == 1:
        return n

    half = quick_power(n, k // 2)
    if k % 2 == 0:
        return (half*half) % MOD
    return (half*half*n) % MOD

ans = quick_power(2,1e6)
print(ans)