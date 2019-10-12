def train(floatdata,Epochs,lr):
    weights = [0.0 for i in range(len(floatdata[0]))]
    for i in range(Epochs):
        for instance in floatdata:
                r = weights[0]
                for attribute in range(len(weights)-1):
                    r += weights[attribute+1] * instance[attribute]
                if(r>=0):
                    calculated=1.0
                else:
                    calculated=-1.0
                if calculated != instance[-1]:
                    error = instance[-1] - calculated
                    weights[0] += lr * error
                    for i in range(len(weights)-1):
                        weights[i+1] += instance[i] * lr * error
    return weights