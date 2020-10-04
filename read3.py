data=[]
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 10000 == 0:
			print(len(data))
print('總共有', len(data), '則留言')

sum_len = 0
for d in data:
	sum_len = sum_len + len(d)
print('留言平均是', sum_len/len(data), '個字母')

new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('總共有', len(new), '則留言長度小於100個字母')