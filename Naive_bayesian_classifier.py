import numpy as np
from math import exp
from math import pi
from math import sqrt
from random import seed

import numpy as np

class Human:
    name : str
    x : list
    sex : int # 1 man, 0 woman

    def __init__(self, name, x, sex=0):
        self.name = name
        self.x = x
        self.sex = sex

    def __repr__(self):
        return f"{self.name}\n Features: {self.x}\n Sex: {self.sex} \n\n"


A = Human('Antonio',[175,70],1)
B = Human('Andrea',[180,80],1)
C = Human('Giovanni',[190,85],1)
D = Human('Debora',[165, 54],0)
E = Human('Euclidea',[160, 50],0)
F = Human('Franca',[159, 48],0)

humans = [A, B, C, D, E, F]

new_human = Human('Riccardo',[180,80], 1)

# Calculate the Gaussian probability distribution function for x
def calculate_probability(x, mean, stdev):
    exponent = exp(-((x-mean)**2 / (2 * stdev**2 )))
    return round((1 / (sqrt(2 * pi) * stdev)) * exponent,3)

'''
Probabilities are calculated separately for each class.
This means that we first calculate the probability that a new piece of data belongs to the first class,
then calculate probabilities that it belongs to the second class, and so on for all the classes.


The probability that a piece of data belongs to a class is calculated as follows:

P(class|data) = P(X|class) * P(class)

You may note that this is different from the Bayes Theorem described above.
The division has been removed to simplify the calculation.
'''

# Split the dataset by class values, returns a dictionary
def separate_by_class(dataset):
	separated = dict()
	for i in range(len(dataset)):
		vector = dataset[i].x
		class_value = dataset[i].sex
		if (class_value not in separated):
			separated[class_value] = list()
		separated[class_value].append(vector)
	return separated

# Calculate the mean, stdev and count for each column in a dataset
def summarize_dataset(dataset):
    summaries = [(round(np.mean(column),3), round(np.var(column),3), len(column)) for column in zip(*dataset)]
    del(summaries[-1])
    return summaries

# Split dataset by class then calculate statistics for each row
def summarize_by_class(dataset):
    separated = separate_by_class(dataset)
    summaries = dict()
    for class_value, rows in separated.items():
        summaries[class_value] = summarize_dataset(rows)
    return summaries

# Calculate the probabilities of predicting each class for a given row
def calculate_class_probabilities(summaries, row):
    total_rows = sum([summaries[label][0][2] for label in summaries])
    probabilities = dict()
    for class_value, class_summaries in summaries.items():
        probabilities[class_value] = summaries[class_value][0][2]/float(total_rows)
        for i in range(len(class_summaries)):
            mean = class_summaries[i][0]
            stdev = class_summaries[i][1]
            probabilities[class_value] *= calculate_probability(row[i], mean, stdev)
    return probabilities

# Predict the class for a given row
def predict(summaries, row):
    probabilities = calculate_class_probabilities(summaries, row)
    best_label, best_prob = None, -1
    for class_value, probability in probabilities.items():
        if best_label is None or probability > best_prob:
            best_prob = probability
            best_label = class_value
    return best_label

# Naive Bayes Algorithm
def naive_bayes(train, test):
    summarize = summarize_by_class(train)
    predictions = list()
    
    output = predict(summarize, test.x)
    predictions.append(output)
    return(predictions)

predictions = naive_bayes(humans, new_human)
print(predictions)