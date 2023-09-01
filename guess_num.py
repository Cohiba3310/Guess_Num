import random

r = random.randint(1,100)
count = 0
while True:
	count = count + 1
	num = input('請從1~100隨機挑選一個數字！')
	num = int(num)
	if num == r:
		print('恭喜您！您猜中了！')
		print('你只花了', count, '次就猜中了！')
		break
	elif num > r:
		print('數字再小一點~')
	elif num < r:
		print('數字再大一點~')
	print('你已經猜', count, '次了喔~')