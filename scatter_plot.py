from sys import argv
from pandas import read_csv

import matplotlib.pyplot as plt

def		get_house_grades(data, house, k):
	x = []

	for i in range(data.shape[0]):
		if (data.iloc[i, 1] == house):
			x.append(data.iloc[i, k])
	return (x)

if __name__ == "__main__":
	try:
		if (".csv" not in argv[1]):
			raise Exception
		data = read_csv(argv[1])
	except:
		print("usage: python3 scatter_plot.py <dataset.csv>")
		exit(-1)

	plt.scatter(get_house_grades(data, "Hufflepuff", 7), get_house_grades(data, "Hufflepuff", 9), alpha=0.3, color='y', label="Hufflepuff")
	plt.scatter(get_house_grades(data, "Ravenclaw", 7), get_house_grades(data, "Ravenclaw", 9), alpha=0.3, color='b', label="Ravenclaw")
	plt.scatter(get_house_grades(data, "Gryffindor", 7), get_house_grades(data, "Gryffindor", 9), alpha=0.3, color='r', label="Gryffindor")
	plt.scatter(get_house_grades(data, "Slytherin", 7), get_house_grades(data, "Slytherin", 9), alpha=0.3, color='g', label="Slytherin")
	plt.ylabel(data.iloc[:, 9].name)
	plt.xlabel(data.iloc[:, 7].name)
	plt.legend()
	plt.show()