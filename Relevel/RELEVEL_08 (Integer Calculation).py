for _ in range(int(input())):
	N = int(input())
	Z = input()
	P = int(input())
	count = 0
	for i in range(1,N):
		v1 = Z[:i]
		v2 = Z[i:]
		if v1[0] == '0' or v2[0] == '0':
			continue
		if int(v1)%P==0 and int(v2)%P==0:
			count += 1
	print(count)

"""
Problem Statement :

You are given an integer Z with N digits and an integer p.

A and B are two integers where A = Z/(10^k) and B = Z%(10^k).

For all possible values of k from 1 to N-1, find out the number of possible values k such that both A and B are divisible by p and both A and B should not have leading zeros.

 

Input Format :

 

First line contains a single integer T, the number of test cases.
First line of each test case contains a single integer N.
The following line contains a N digit integer Z.
The following line contains an integer p.
 

 

Output Format :

 

For each of the T test cases :
Print a line containing an integer, Number of possible values of k.
 

 

Constraints :

 

1 <= T <= 10^3
1 <= N <= 10^5
10^N-1 <= Z <= 10^N - 1
1 <= p <= 10^9
Note:- Sum of N over all test cases does not exceed 10^7 
 

 

Sample Input :

 

2
5
10001
1
9
125483640
2

 

 

Sample Output :

 

1
4

 

 

 

Explanation :

 

In the 1st test case, the only possible value of k is 1 such that A = 1000 and B = 1.

In the 2nd test case,  the possible values of A and B are {12, 5483640},  {1254, 83640}, {12548, 3640}, {1254836, 40}.

 
"""