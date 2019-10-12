import csv
import perceptron
import csvconv
import sys

#inputs 
lr=float(input("Input Learning Rate:"))
Epochs=int(input("Input Number Of Epochs:"))
#training
floatdata=csvconv.tofloat(sys.argv[1])
weights=perceptron.train(floatdata,lr,Epochs)
print("Weights\n ",weights)
#testing
floattest=csvconv.tofloat(sys.argv[2])
acc=perceptron.test(floattest,weights)
print("Accuracy=",acc)