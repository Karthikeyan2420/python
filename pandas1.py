import pandas as pd
#
mydataset = {
    'cars': ["BMW", "Volvo", "Ford"],
    'passings': [3, 7, 2]
}
print(mydataset)
myvar = pd.DataFrame(mydataset)
print(myvar)