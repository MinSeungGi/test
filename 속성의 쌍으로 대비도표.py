import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plot
target_url =("http://archive.ics.uci.edu/ml/machine-learning/databses-"
             "databases/undocumented/connectionist-bench/sonar/sonar.all-data")

rocksVMines = pd.read_csv(target_url, header=None, prefix="V")

dataRow2=rocksVMines.iloc[1,0:60]
dataRow3=rockVMines.iloc[2,0:60]

plot.scatter(dataRow2, dataRow3)

plot.xlabel("2nd Attribute")
plot.ylabel(("3rd Attribute"))
plot.show()

datRow21 = rocksVMines.iloc[20,0:60]

plot.scatter(dataRow2, dataRow21)

plot.xlabel("2nd Attribute")
plot.ylabel(("21st Attribute"))
plot.show()
