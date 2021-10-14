import numpy as np

from sys import argv
from math import log
from pandas import read_csv

def		h(z):
	return (1 / (1 + np.exp(-z)))

def		cost(x, y):
	return (sum(y * np.log(x) + (1 - y) * np.log(1 - x)) / -y.shape[0])

def		d_cost(x, x2, y):
	return (np.dot(x2 - y, x) / y.shape[0])

def		train(x, y, theta):
	alpha = 0.1
	delta = 0.00001
	loss = 1
	new_loss = 0
	while (1):
		x2 = h(np.dot(x, theta))
		theta -= alpha * d_cost(x, x2, y)
		new_loss = cost(x2, y)
		if (loss - new_loss < delta):
			return (theta)
		loss = new_loss

def		feature_scaling(x):
	return ((x - np.mean(x)) / np.std(x))

def		normalize(x):
	for i in range(x.shape[1]):
		x[i] = (x[i] - min(x[i])) / (max(x[i]) - min(x[i]))
	return (x)
	
def		pre_process(data):
	data.fillna(method='ffill', inplace=True)
	y = data["Hogwarts House"]
	data.drop(["Index", "Hogwarts House", "First Name", "Last Name", "Birthday", "Arithmancy", "Defense Against the Dark Arts", "Care of Magical Creatures"], axis=1, inplace=True)
	data["Best Hand"] = [1 if hand == "Right" else 0 for hand in data["Best Hand"]]
	data = feature_scaling(data)
	return (data.to_numpy(), y.to_numpy())

if __name__ == "__main__":
	try:
		if (".csv" not in argv[1]):
			raise Exception
		data = read_csv(argv[1])
	except:
		print("usage: python3 logreg_train.py <dataset.csv>")
		exit(-1)

	houses = ["Ravenclaw", "Slytherin", "Gryffindor", "Hufflepuff"]
	data, res = pre_process(data)
	w = []
	for i in range(4):
		y = [1 if h == houses[i] else 0 for h in res]
		w.append(train(data, np.asarray(y), np.zeros(data.shape[1])))
	np.save("./weights.npy", w)