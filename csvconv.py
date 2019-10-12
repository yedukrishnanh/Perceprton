#convert csv to float list
def tofloat(csvfile):
    floatdata=list()
    with open(csvfile) as f:
        content = f.readlines()
        for item in content:
            row = [float(el) for el in item.split(',')]
            floatdata.append(row)
    return floatdata