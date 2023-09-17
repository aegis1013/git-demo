"""
猜數字遊戲
1.要可以任意產生亂數(1~50)
2.使用者可以猜數字
3.偵測是否正確
4.可以多次猜測
5.
"""
import random

low, high = 1, 50

x = random.randint(low, high)
print(x)
count = 0
# while True: #測試邏輯
#    x = random.randint(low, high)
#    print(x)
#    if x == 50:
#        break
for i in range(5):
    y = eval(input(f"目前猜測第{count+1}次請輸入一個數字{low}~{high}:"))
    if low < y < high:
        if y == x:
            print("恭喜猜對!")
            break
        else:
            if y > x:
                print("猜低一點")
                if y < high:
                    high = y - 1
            else:
                print("猜高一點")
                if y > low:
                    low = y + 1
        count += 1
    else:
        print("請重新輸入")

if y != x:
    print(f"答案為:{x}")
