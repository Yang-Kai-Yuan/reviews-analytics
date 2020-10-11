data=[]
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 10000 == 0:
			print(len(data))
print('總共有', len(data), '則留言')

wc = {}
for d in data:
	words = d.split()
	for word in words:
		if word in wc:
			wc[word] += 1
		else:
			wc[word] = 1
for word in wc:
	if wc[word] > 10000:
		print(word, wc[word])

sum_len = 0
for d in data:
	sum_len = sum_len + len(d)
print('留言平均是', sum_len/len(data), '個字母')

new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('總共有', len(new), '則留言長度小於100個字母')

good = []
for d in data:
	if 'good' in d:
		good.append(d)
print('總共有', len(d), '則留言含good')
print(good[0])

bad = [d for d in data if 'bad' in d]
print('總共有', len(bad), '則留言含bad')