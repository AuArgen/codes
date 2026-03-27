from math import isqrt
from math import ceil
#
K, N = map(int, input().split())
# X = 2^K (Биттик жылышуу менен эсептөө эң тез иштейт)
X = 1 << K
# print(X)
# Тамырдын ичиндеги сан: Y = 4^K + 2^K * N
# 4^K деген бул (2^K)^2, б.а. 2^(2*K)
Y = (1 << (2 * K)) + X * N

# Y санынан бүтүн тамыр алуу (эч кандай float колдонбойбуз)
s = isqrt(Y)

# Тамырды ашыгы менен тегеректөө (Ceiling)
# Эгерде тамырдан так чыкса, өзүн алабыз, болбосо 1ди кошобуз
if s * s == Y:
    ceil_sqrt = s
else:
    ceil_sqrt = s + 1

# Жыйынтык: F = K - 2^K + ceil_sqrt
ans = K - X + ceil_sqrt

print(ans)