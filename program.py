!pip install dc_stat_think
import pandas as pd
import matplotlib.pyplot as plt
import dc_stat_think as dcst
import numpy as np

pop = pd.read_csv("co-est2019-alldata.csv", encoding='latin-1')
pop.head(5)

pop.shape

pop.isna().count()

pop.isnull().sum()

box_pop = pop[['CENSUS2010POP', 'POPESTIMATE2015', 'POPESTIMATE2019']]
box_pop.head(5)

box_pop.describe()

box_pop.shape

box_pop.boxplot(figsize=(10,5))
plt.ticklabel_format() 
plt.ylabel("Population Count")
plt.title("Box Plot: CENSUS2010POP & POPESTIMATE2015 & POPESTIMATE2019")
plt.show()

box_pop['CENSUS2010POP'].describe()

hist_pop = pop[['CENSUS2010POP']]

hist_pop.shape

hist_pop.hist(grid=False)

ecdf = pop['CENSUS2010POP']

x,y = dcst.ecdf(ecdf)
_ = plt.plot(x, y*100, linestyle='--', lw = 2)
plt.xlabel("CENSUS2010POP")
plt.ylabel("Percentage")

"""Part 2"""

pop_estimate = pop[['CENSUS2010POP', 'POPESTIMATE2019']]
ax1 = pop_estimate.plot.scatter(x='POPESTIMATE2019',y='CENSUS2010POP')
plt.title("POPESTIMATE2019 VS. CENSUS2010POP")
plt.show()

from scipy import stats
import numpy as np

census = box_pop[['CENSUS2010POP']]

Q1 = census.quantile(0.25)
Q3 = census.quantile(0.75)
IQR = Q3 - Q1
print(IQR)

(census < (Q1 - 1.5 * IQR)) |(census > (Q3 + 1.5 * IQR))

census.shape

census_iqr = census[~((census < (Q1 - 1.5 * IQR)) |(census > (Q3 + 1.5 * IQR))).any(axis=1)]
census_iqr.shape

census_iqr.boxplot()

census_pop_iqr = box_pop[~((box_pop < (Q1 - 1.5 * IQR)) |(box_pop > (Q3 + 1.5 * IQR))).any(axis=1)]
census_pop_iqr.shape

census_pop_iqr.boxplot()

census_iqr.hist(grid=False,bins=9, figsize=(10,5))
plt.ylabel("Population Count")
plt.title("Frequency for CENSUS2010POP")
plt.xlabel("CENSUS2010POP")