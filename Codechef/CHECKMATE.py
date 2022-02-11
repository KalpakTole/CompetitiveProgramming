import sys
input = sys.stdin.readline

def main():
	for _ in range(int(input())):
		xk, yk = list(map(int, input().split()))
		x1, y1 = list(map(int, input().split()))
		x2, y2 = list(map(int, input().split()))
		ans = 'NO'
		if xk not in [1,8] and yk not in [1,8]:
			ans = 'NO'
			continue
		if xk == 1:
			if yk == 1 or yk == 8:
				if x1 == 2:
					if y1 == yk-1 or y1 == yk+1 or y2 == yk-1 or y2 == yk+1 or y2 == y1:
						ans = 'NO'
					else:
						ans = 'YES'
				elif x2 == 2:
					if y2 == yk-1 or y2 == yk+1 or y1 == yk-1 or y1 == yk+1 or y1 == y2:
						ans = 'NO'
					else:
						ans = 'YES'
				elif y1 == 2:
					if x1 == xk-1 or x1 == yk+1 or x2 == yk-1 or x2 == yk+1 or x2 == x1:
						ans = 'NO'
					else:
						ans = 'YES'
				elif y2 == 2:
					if x1 == xk-1 or x1 == yk+1 or x2 == yk-1 or x2 == yk+1 or x2 == x1:
						ans = 'NO'
					else:
						ans = 'YES'
			else:



						
			if yk not in [1,8]:
				if x1 != 2 and x2 != 2:
					ans = 'NO'
				elif x1 == 2:
					if y1 == yk-1 or y1 == yk+1 or y2 == yk-1 or y2 == yk+1 or y2 == y1:
						ans = 'NO'
					else:
						ans = 'YES'
				elif x2 == 2:
					if x2 == yk-1 or x2 == yk+1 or x1 == yk-1 or x1 == yk+1 or y1 == y2:
						ans = 'NO'
					else:
						ans = 'YES'
			else:

					


		

if __name__ == '__main__':
	main()