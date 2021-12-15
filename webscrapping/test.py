from pandas import read_csv
from itertools import chain
print(list(read_csv("./emails.csv").to_dict()["emails"].values()))



[print(i) for i in dir(read_csv("./emails.csv")) if i.startswith("to")]