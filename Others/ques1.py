class Movie:
	def __init__(self, movie_id, movie_name, ticket_cost, category='Default'):
		self.movie_id = movie_id
		self.movie_name = movie_name
		self.ticket_cost = ticket_cost
		self.category = category
	
	def assign_Price_Category(self):
		if 0 < self.ticket_cost < 150:
			self.category = 'General'
		elif 150 <= self.ticket_cost < 250:
			self.category = 'Silver'
		elif 250 <= self.ticket_cost < 350:
			self.category = 'Gold'
		elif self.ticket_cost >= 350:
			self.category = 'Platinum'
		

class Movie_Ticket:
	def __init__(self, customer_name, movie_name, viewerCount, totalTicketCost):
		self.customer_name = customer_name
		self.movie_name = movie_name
		self.viewerCount = viewerCount
		self.totalTicketCost = totalTicketCost

def getCategoryWiseCount(movies):
	d = {}
	for movie in movies:
		d[movie.category] = d.get(movie.category, 0) + 1
	return d

def bookMovieTicket(movies, customer_name, movie_name, count_of_viewers):
	z = None
	for movie in movies:
		if movie.movie_name.lower() == movie_name.lower():
			z = movie
			break
	if z == None:
		return z
	totalTicketCost = z.ticket_cost * count_of_viewers
	mt = Movie_Ticket(customer_name, movie_name, count_of_viewers, totalTicketCost)
	return mt

def main():
	N = int(input())
	movies = []
	for i in range(N):
		movie_id = int(input())
		movie_name = input()
		ticket_cost = int(input())
		m = Movie(movie_id, movie_name, ticket_cost)
		m.assign_Price_Category()
		movies.append(m)
	customer_name = input()
	movie_name = input()
	count_of_viewers = int(input())
	a1 = getCategoryWiseCount(movies)
	print('Category wise ticket count:')
	for k,v in a1.items():
		print(k,':',v)
	a2 = bookMovieTicket(movies, customer_name, movie_name, count_of_viewers)
	if a2==None:
		print('Movie not Available')
	else:
		print(a2.customer_name,a2.totalTicketCost)

main()