#{ 
#Driver Code Starts
#Initial Template for Python 3

class A:
	__B=None
	__R=None
	__C=None
	def __init__(self, R, C,B):
		self.__R=R
		self.__B=B
		self.__C=C
	def __getP(self,i,j):
		assert 0<=i and i<self.__R and 0<=j and j<self.__C
		if(self.__B[i]>=j+1):
			return 0
		return 1
	def get(self,i,j):
		return self.__getP(i,j)
		

 # } Driver Code Ends
#User function Template for python3

class Solution:
	# do not edit this function
	# use it to get the value of A[i][j]
	def get(self, i, j):
	  return a.get(i,j)
	  
	def solve(self, R, C):
		li = []
		for i in range(R):
			tot = 0
			for j in range(C):
				tot += Solution.get(self,i,j)
			li.append(tot)
		return li.index(max(li))
				
		# code here

#{ 
#Driver Code Starts.

if __name__ == "__main__":
	t = int (input ())
	for tc in range (t):
		__R,__C = map(int,input().split())
		__B=[int(i) for i in input().split()]
		a=A(__R,__C,__B)
		ob = Solution()
		print(ob.solve(__R,__C))
#} Driver Code Ends