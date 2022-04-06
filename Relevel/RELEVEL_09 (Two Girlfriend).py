N = int(input())
S = list(map(int, input().split()))
max_len = 0
for i in range(1,N):
	v1 = S[:i]
	v2 = S[i:]
	if sorted(v1) == list(range(1,i+1)) and sorted(v2) == list(range(1,N-i+1)):
		max_len = max(max_len, i, N-i)
if max_len == 0:
	print(-1)
else:
	print(max_len)

"""
Problem Statement :


Antonio is the stud boy of his college and has two girlfriends. Both of his girlfriends are mathematicians and love permutations.
To buy gifts for them Antonio went to the Arrays(name of the shop) gift shop. The shop had several arrays. As Antonio did not have much money he was able to buy only one array.


But as he has to gift both of his girlfriends he decided to break the array into two non-empty parts and gift one to each of them. Now both of his girlfriends will be happy if they receive a permutations array and their happiness level will be the length of the array they receive.


Antonio loves his first girlfriend more than the second, so wants to gift her the maximum length permutations array. 
Given the array, you have to find this maximum length such that both his girlfriends receive a non-empty permutations array. If there is no way to do so, print -1.

 


Input Format :

 

First-line contains a single integer N, the length of the array.
Second-line contains N space-separated integers denoting the array elements.
 

 

Output Format :

 

Print the maximum length of the array Anotonio can gift to his first girlfriend. If there is no way to do so, print -1.
 

 

Constraints :

 

2<=N<=2*105
1<=A[i]<=N-1
 

 

Sample Input 1:


5
1 2 3 2 1

 


Sample Output 1 :


3

 


Explanation of Sample 1 :

 

Say we break array as (here A[i..j] represents subarray of array A starting at i and ending at j):

A[1..1], A[2..5] = [1], [2,3,2,1] (2nd array not a permutation)
A[1..2], A[3..5] = [1,2], [3,2,1] (both arrays are a permutation), so Antonio can gift the second array to his first girlfriend which has length 3.

Note: Antonio can also break the arrays as A[1..3], A[4..5] = [1,2,3], [2,1]. Here also both arrays are a permutation and first array has length 3.

 

 

Sample Input 2 :


5
1 2 2 3 2

 


Sample Output 2 :


-1

 


Explanation of Sample 2 :

 

There is no way to break the given array such that both of Antonio’s girlfriends receive a non-empty permutations array.

 
"""