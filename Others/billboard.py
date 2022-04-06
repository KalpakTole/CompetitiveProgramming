def maxRevenue(m, x, revenue, n, t) :
	 
	# Array to store maximum revenue
	# at each miles.
	maxRev = [0] * (m + 1)
 
	# actual minimum distance between
	# 2 billboards.
	nxtbb = 0;
	for i in range(1, m + 1) :
		 
		# check if all billboards are
		# already placed.
		if (nxtbb < n) :
			 
			# check if we have billboard for
			# that particular mile. If not,
			# copy the previous maximum revenue.
			if (x[nxtbb] != i) :
				maxRev[i] = maxRev[i - 1]
 
			# we do have billboard for this mile.
			else :
			 
				# We have 2 options, we either take
				# current or we ignore current billboard.
 
				# If current position is less than or
				# equal to t, then we can have only
				# one billboard.
				if (i <= t) :
					maxRev[i] = max(maxRev[i - 1],
									revenue[nxtbb])
 
				# Else we may have to remove
				# previously placed billboard
				else :
					maxRev[i] = max(maxRev[i - t - 1] +
									revenue[nxtbb],
									maxRev[i - 1]);
 
				nxtbb += 1
	 
		else :
			 
			maxRev[i] = maxRev[i - 1]
	 
	return maxRev[m]
	 
# Driver Code
if __name__ == "__main__" :
	 
	m = 50000
	x = [0, 3, 4, 9, 11, 15, 20, 23, 28, 33]
	revenue = [8429, 9142, 2732, 5217, 1587, 9613, 7510, 3414, 9006, 4584]
	n = len(x)
	t = 5
	print(maxRevenue(m, x, revenue, n, t))