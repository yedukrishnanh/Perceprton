#training
def train(floatdata,lr,Epochs):
    weights = [0.0 for i in range(len(floatdata[0]))]
    correct= False
   ## while(correct==False):
    for i in range(Epochs):
        correct=True
        print(weights[0])
        for instance in floatdata:
            ye=weights[0]
            for attribute in range(len(weights)-1):
                ye +=weights[attribute+1]*instance[attribute]
            if ye>=0:
                ye=1.0
            else:
                ye=-1.0
            if ye!=instance[-1]:
                correct=False
                weights[0] += lr * (instance[-1] - ye)
                for k in range(len(weights)-1):
                    weights[k+1] += instance[k] * lr * (instance[-1] - ye)
        if correct:
            break
    print('Epochs Done=',i+1)
    return weights
#testing
def test(floattest,weights):
    r=0
    for instance in floattest:
        ye=weights[0]
        for attribute in range(len(weights)-1):
            ye +=weights[attribute+1]*instance[attribute]
        if ye>=0:
            ye=1.0
        else:
            ye=-1.0
        if ye!=instance[-1]:
            r-=1
        else:
            r+=1
    acc=(r/len(floattest))*100
    return acc
