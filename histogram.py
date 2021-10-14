from sys import argv
from math import isnan
from pandas import read_csv

import matplotlib.pyplot as plt

def		get_house_grades(data, house):
	x = []

	for i in range(data.shape[0]):
		if (data.iloc[i, 1] == house and not isnan(data.iloc[i, 16])):
			x.append(data.iloc[i, 16])
	return (x)

if __name__ == "__main__":
	try:
		if (".csv" not in argv[1]):
			raise Exception
		data = read_csv(argv[1])
	except:
		print("usage: python3 histogram.py <dataset.csv>")
		exit(-1)
	
	plt.hist(get_house_grades(data, "Hufflepuff"), color="y", alpha=0.3, label="Hufflepuff")
	plt.hist(get_house_grades(data, "Ravenclaw"), color="b", alpha=0.3, label="Ravenclaw")
	plt.hist(get_house_grades(data, "Gryffindor"), color="r", alpha=0.3, label="Gryffindor")
	plt.hist(get_house_grades(data, "Slytherin"), color="g", alpha=0.3, label="Slytherin")
	plt.title(data.iloc[:, 16].name)
	plt.legend()
	plt.show()
