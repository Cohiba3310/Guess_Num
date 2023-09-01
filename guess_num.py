import random

r = random.randint(1,100)
while True:
	num = input('請從1~100隨機挑選一個數字！')
	num = int(num)
	if num == r:
		print('恭喜您！您猜中了！')
		break
	elif num > r:
		print('數字再小一點~')
	elif num < r:
		print('數字再大一點~')