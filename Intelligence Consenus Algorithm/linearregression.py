
class LinearRegression:

	def __init__(self, meanx, meany, sqmean, n):
		self.meanx = meanx
		self.meany = meany
		self.sqmean = sqmean
		self.meansq = self.meanSquare(meanx)
		self.n = n

	def get_input(self):
		print("Enter the number of tuples in dataset:")
		n = int(input())
		dataset_x = [n]
		dataset_y = [n]
		for i in range(0, n):
			print("Enter the value of x:")
		x = int(input())
		dataset_x.append(x)
		print("Enter the value of y")
		y = int(input())
		dataset_y.append(y)
		return dataset_x, dataset_y, n

	def mean(self, dataset, n):
		sum = 0
		for i in range(0, n):
			sum += dataset[i]
		return sum / n

	def newMean(self, mean, n, new, c):
		newmean = (mean*n + new)/n+1
		if c == "x":
			self.meanx = newmean
		else:
			self.meany = newmean

	def meanSquare(self, mean):
		meansq = mean**2
		return meansq

	def meansumofproducts(self, dataset_x, dataset_y, n):
		products = []
		for i in range(0, n):
			product = dataset_x[i] * dataset_y[i]
			products.append(product)
		return self.mean(products, n)

	def compute_coefficient(self, dataset_x, dataset_y, n):
		mean_sum_of_products = self.meansumofproducts(dataset_x, dataset_y, n)
		mean_x = self.mean(dataset_x, n)
		mean_y = self.mean(dataset_y, n)
		mean_x_sq = self.meansumofproducts(dataset_x, dataset_x, n)
		sq_mean = (mean_x) ** 2
		b = (mean_sum_of_products - (mean_x * mean_y)) / (mean_x_sq - sq_mean)
		return b

	def regression(self, dataset_x, dataset_y, n):
		mean_x = self.mean(dataset_x, n)
		mean_y = self.mean(dataset_y, n)
		b = self.compute_coefficient(dataset_x, dataset_y, n)
		print("Y -", mean_y, "=", b, "(X -", mean_x, ")")


