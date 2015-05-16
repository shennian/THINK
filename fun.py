
targets = [[] for i in range(9)]
nums = '123456789'

for i in range(1, 10):
	j = 0
	while i+j <= len(nums):
		targets[i-1].append(nums[j : j+i])
		j += 1

num = 0
def match(result, s, targetNum, index, op):
	global num
	if len(result) == index:

		if s == targetNum:
			num += 1
			for i in range(len(result)-1):
				print result[i],op[i],
			print result[-1],
			print  '=', s
		return
	_op = []
	for i in op:
		_op.append(i)
	_op.append('+')
	match(result, s+result[index], 
					targetNum, index+1, _op)
	_op.pop()
	_op.append('-')
	match(result, s-result[index], 
					targetNum, index+1, _op)

def search(x, y, targets, result, targetNum):
	if x + y > 8:	
		return
	num = targets[y][x]
	r = []
	for i in result:
		r.append(i)
	r.append(int(num))	
	_x = int(num[-1])
	if _x == 9:
		op = []
		match(r, r[0], targetNum, 1, op)		
		return 
	for i in range(0, 9-x):
		search(_x, i, targets, r, targetNum)


for i in range(9):
	r = []
	t = 0
	search(0, i, targets, r, t)
print num
