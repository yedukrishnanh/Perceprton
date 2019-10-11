import csv

#inputs 
lr=float(input("Input Learning Rate:"))
th=float(input("Input threashold:"))
Epochs=int(input("Input Number Of Epochs:"))

#convert csv to float list
def reader(csvfile):
    floatdata=list()
    with open(csvfile) as datasetfile:
        dataset = csv.reader(datasetfile, delimiter=',')
        for row in dataset:
            cr=list(map(lambda x: float(x),row))
            floatdata.append(cr)
    return floatdata

floatdata=reader('file.csv')

#initialising Weights
weights = [1.0 for i in range(len(floatdata[0]))]

#train
for i in range(Epochs):
    for instance in floatdata:
            r = weights[0]
            for attribute in range(len(weights)-1):
                r += weights[attribute+1] * instance[attribute]
            if(r>=th):
                calculated=1.0
            else:
                calculated=0.0
            if calculated != instance[-1]:
                error = instance[-1] - calculated
                weights[0] += lr * error
                for i in range(len(weights)-1):
                    weights[i+1] += instance[i] * lr * error

print("Weights\n ",weights)