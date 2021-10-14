from sys import argv
from pandas import read_csv

import seaborn as sns
import matplotlib.pyplot as plt


if __name__ == "__main__":
	try:
		if (".csv" not in argv[1]):
			raise Exception
		data = read_csv(argv[1])
	except:
		print("usage: python3 scatter_plot.py <dataset.csv>")
		exit(-1)

	data.dropna(inplace=True)
	g = sns.pairplot(data, vars={\
			"Arithmancy", "Astronomy", "Herbology", "Defense Against the Dark Arts", \
			"Divination", "Muggle Studies", "Ancient Runes", "History of Magic", \
			"Transfiguration", "Potions", "Care of Magical Creatures", "Charms", "Flying"
		}, \
		diag_kind="hist", \
		hue="Hogwarts House", \
		palette={ \
			"Hufflepuff":"#eee117", \
			"Ravenclaw":"#000a90", \
			"Gryffindor":"#7f0909", \
			"Slytherin":"#0d6217"
		}, \
		plot_kws={'alpha': 0.5}, \
		diag_kws={'alpha': 0.5})
	plt.show()
