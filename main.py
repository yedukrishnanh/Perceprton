import sys
import csv
import perceptron
import csvconv

#inputs 
lr=float(input("Input Learning Rate:"))
Epochs=int(input("Input Number Of Epochs:"))

floatdata=csvconv.tofloat(sys.argv[1])
weights=perceptron.train(floatdata,Epochs,lr)

print("Weights\n ",weights)