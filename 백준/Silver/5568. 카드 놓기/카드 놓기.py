# μΉ΄λ λκΈ°
import sys
import itertools

n = int(sys.stdin.readline())
r = int(sys.stdin.readline())
nums =[sys.stdin.readline().strip() for _ in range(n)]

output = set()

## π¨ μμ΄μ κ³μ°ν΄μ£Όλ ν¨μ
for i in list(itertools.permutations(nums, r)):
    output.add("".join(i))

print(len(output))