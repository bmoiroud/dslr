import numpy as np
import pandas as pd

from logreg_train import h, pre_process
from sys import argv

if __name__ == "__main__":
	houses = ["Ravenclaw", "Slytherin", "Gryffindor", "Hufflepuff"]
	y_pred = []
	w = None

	try:
		if (".csv" not in argv[1]):
			raise Exception
		data = pd.read_csv(argv[1])
	except:
		print("usage: python3 logreg_train.py <dataset.csv>")
		exit(-1)
	try:
		w = np.load("./weights.npy")
	except:
		exit(-1)

	data, _ = pre_process(data)
	p = np.zeros((len(data), 4))

	for i in range(len(data)):
		for j in range(4):
			p[i][j] = np.mean(h(data[i] * w[j]))

	y_pred = [houses[int(np.where(p[i] == max(p[i]))[0])] for i in range(len(data))]
	with open("./houses.csv", "w") as file:
		file.write("Index,Hogwarts House\n")
		for i in range(len(y_pred)):
			file.write("{0},{1}\n".format(i, y_pred[i]))