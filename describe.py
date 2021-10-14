from sys import argv
from math import sqrt, isnan
from pandas import read_csv

def		Mean(data):
	n = Count(data)
	res = 0.0
	for i in range(len(data)):
		if (not isinstance(data[i], str) and not isnan(data[i])):
			res += float(data[i])
	if (n > 0):
		return (res / n)
	return (float('NaN'))

def		Std(data):
	m = Mean(data)
	var = 0.0
	j = 0

	if (not isinstance(data, str) and not isnan(m)):
		dev = data - m
	else:
		return (float('NaN'))
	n = Count(dev)
	for i in range(int(n)):
		if (not isnan(dev[i])):
			var += (dev[i] * dev[i])
		else:
			j += 1
	return (sqrt(var / (Count(dev) - 1)))

def		Min(data):
	n = len(data)
	res = data[0]

	if (isinstance(res, str)):
		return (float('NaN'))
	for i in range(1, n):
		if (data[i] < res):
			res = data[i]
	return (res)

def		Max(data):
	n = len(data)
	res = data[0]

	if (isinstance(res, str)):
		return (float('NaN'))
	for i in range(1, n):
		if (data[i] > res):
			res = data[i]
	return (res)

def		Percentile(data, p):
	if (isinstance(data[0], str)):
		return (float('NaN'))
	data = data.tolist()
	data = [x for x in data if not isnan(x)]
	data.sort()
	i = (Count(data) - 1) * p / 100
	try:
		data[int(i)]
	except:
		return(float('NaN'))
	return (data[int(i)] + ((data[int(i) + 1] - data[int(i)]) * (i - int(i))))

def		Count(data):
	j = 0.0
	for i in range(len(data)):
		if (not isinstance(data[i], str) and not isnan(data[i])):
			j += 1
	return (j)

if __name__ == "__main__":
	try:
		if (".csv" not in argv[1]):
			raise Exception
		data = read_csv(argv[1])
	except:
		print("usage: python3 describe.py <dataset.csv>")
		exit(-1)

	data2 = [["{0:<6}".format(" "), "{0:<6}".format("Count"), "{0:<6}".format("Mean"), \
				"{0:<6}".format("Std"), "{0:<6}".format("Min"), "{0:<6}".format("25%"), \
				"{0:<6}".format("50%"), "{0:<6}".format("75%"), "{0:<6}".format("Max")]]
	j = 1
	for i in range(data.shape[1]):
		if (not isinstance(data.iloc[:, i][0], str)):
			data2.append([])
			data2[j].append(data.iloc[:, i].name)
			data2[j].append(Count(data.iloc[:, i]))
			data2[j].append(Mean(data.iloc[:, i]))
			data2[j].append(Std(data.iloc[:, i]))
			data2[j].append(Min(data.iloc[:, i]))
			data2[j].append(Percentile(data.iloc[:, i], 25))
			data2[j].append(Percentile(data.iloc[:, i], 50))
			data2[j].append(Percentile(data.iloc[:, i], 75))
			data2[j].append(Max(data.iloc[:, i]))
			j += 1

	for i in range(len(data2[0])):
		print("{0}".format(data2[0][i]), end='')
		for j in range(1, len(data2)):
			if (not isinstance(data2[j][i], str)):
				s = "{0:>" + str(Max([len(data2[j][0]), len("{0:.6f}".format(Max(data2[j][1:]))), len("{0:.6f}".format(Min(data2[j][1:])))]) + 3) + ".6f}"
			else:
				s = "{0:>" + str(Max([len(data2[j][0]), len("{0:.6f}".format(Max(data2[j][1:]))), len("{0:.6f}".format(Min(data2[j][1:])))]) + 3) + "}"
			print(s.format(data2[j][i]), end='')
		print('')
