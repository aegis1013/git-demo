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

# while True: #測試邏輯
#    x = random.randint(low, high)
#    print(x)
#    if x == 50:
#        break

y = eval(input(f"請輸入一個數字{low}~{high}"))

if y == x:
    print("恭喜猜對!")
else:
    print("猜錯了")
