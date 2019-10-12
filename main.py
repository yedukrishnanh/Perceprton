import csv
import perceptron
import csvconv

#inputs 
lr=float(input("Input Learning Rate:"))
Epochs=int(input("Input Number Of Epochs:"))
#training
floatdata=csvconv.tofloat('train.csv')
weights=perceptron.train(floatdata,lr,Epochs)
print("Weights\n ",weights)
#testing
floattest=csvconv.tofloat('test.csv')
acc=perceptron.test(floattest,weights)
print("Accuracy=",acc)