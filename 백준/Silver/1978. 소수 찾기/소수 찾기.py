# ์์ ์ฐพ๊ธฐ
import sys

n = int(sys.stdin.readline())
line = sys.stdin.readline().split()

count = 0

for i in range(n):
    # ๐จ ๋ณ์ ์ด๊ธฐํ ์์น ์กฐ์ฌํ๊ธฐ
    e = 0
    if int(line[i]) != 1:
        for j in range(2, int(line[i])):
            if int(line[i]) % j == 0:
                e += 1
        if e == 0:
            count += 1
                
print(count)