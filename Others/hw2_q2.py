def compute_percentile(S, percent):
	n = len(S)
	index = percent/100 * n
	if percent==100:
		return S[-1]
	if index == int(index):
		index = int(index)
		percentile = (S[index-1]+S[index])/2
		return percentile
	if not int(index) % 2 and str(index)[-2:]=='.5':
		index = round(index) + 1
	index = round(index)
	return S[index-1]

def kth_percentile(S,d):
	percent = input('Please enter the percentile to compute (1 to 100): ')
	suffix = d.get(percent[-1], 'th')
	print(f'The {percent}{suffix} percentile is: {compute_percentile(S, int(percent))}')

def main():
	d = {'1': 'st', '2': 'nd', '3': 'rd'}
	S = list(map(int, input('Please enter a list of numbers: ').split()))
	S.sort()
	print(f'The sorted list elements are: {S}')
	kth_percentile(S, d)
	while True:
		c = input('Would you like to compute another percentile? (yes/no): ')
		if c == 'yes' or c == 'y':
			kth_percentile(S,d)
		elif c == 'no' or c == 'n':
			break

main()
