import csv
from sktime.utils import all_estimators
from sktime.forecasting import arima

#all_estimators._is_in_estimator_types("LinearRegression", "LinearModel")
estimators = all_estimators(estimator_types="forecaster")
print(estimators)
#for (name, estimator) in all_estimators():
#    print(name, estimator)


authors = arima.__author__
algo = arima.__all__


with open("author_list.csv", "w+", newline='') as csvfile:
    write = csv.writer(csvfile, delimiter=",")
    write.writerow(["Algorithm", "Algorithm2", "Author1", "Author2"])
    write.writerow(algo + authors)

from mdtable import MDTable
markdown = MDTable('author_list.csv')
markdown_string_table = markdown.get_table()
markdown.save_table('author_list_out.csv')


#with open("author_list_out.csv", "r+", newline="") as csvread:
#    reader= csv.reader(csvread)
#    print(reader)
