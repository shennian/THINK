nums = [
	[5, 3, 0, 0, 7, 0, 0, 0, 0],
	[6, 0, 0, 1, 9, 5, 0, 0, 0],
	[0, 9, 8, 0, 0, 0, 0, 6, 0],
	[8, 0, 0, 0, 6, 0, 0, 0, 3],
	[4, 0, 0, 8, 0, 3, 0, 0, 1],
	[7, 0, 0, 0, 2, 0, 0, 0, 6],
	[0, 6, 0, 0, 0, 0, 2, 8, 0],
	[0, 0, 0, 4, 1, 9, 0, 0, 5],
	[0, 0, 0, 0, 8, 0, 0, 7, 9],
]

flags = [[0 for i in range(9)] for j in range(9)]
for i in range(9):
	for j in range(9):
		if nums[i][j] != 0:
			flags[i][j] = 1

for i in nums:
	print i
def search(nums, flags, x, y):
	_nums= [[0 for i in range(9)] for j in range(9)]
	for i in range(9):
		for j in range(9):
			_nums[i][j] = nums[i][j]
	if y == 9:
		print "**"
		for i in nums:
			print i
		return
	if flags[y][x] == 1:
		if x == 8:
			search(_nums, flags, 0, y+1)
		else:
			search(_nums, flags, x+1, y)
		return
	targetNums = []
	for i in range(0, 9):
		if nums[i][x] != 0:
			targetNums.append(nums[i][x])
		if nums[y][i] != 0:
			targetNums.append(nums[y][i])
	_x = x / 3 * 3
	_y = y / 3 * 3
	for i in range(_y, _y + 3):
		for j in range(_x, _x + 3):
			targetNums.append(nums[i][j])
	targetNums.sort()
	searchNums = []
	for i in range(1, 10):
		if targetNums.count(i) == 0:
			searchNums.append(i)
	for i in searchNums:
		_nums[y][x] = i
		if x == 8:
			search(_nums, flags, 0, y+1)
		else:
			search(_nums, flags, x+1, y)
	return	
k = [[0 for i in range(9)] for j in range(9)]
search(nums, flags, 0, 0)	

# suan kong pan
#search(k, k, 0, 0)	
			


	