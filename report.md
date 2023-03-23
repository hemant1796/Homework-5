HomeWork 5

================

Due: Thursday, March 23, 2023 by 11:59pm **Submitted by : ** Hemant
kumar

UIN 01243485

## Part 1: Create Distribution Charts

For this part, I used Python to manipulate the data set and to create
the distribution charts. I have chosen the first data set (US Census
Bureau County Population).

Source:
<https://www.census.gov/data/datasets/time-series/demo/popest/2010s-counties-total.html#par_textimage_70769902>

Here is the following Python code to box plot between
CENSUS2010POP,POPESTIMATE2015,and POPESTIMATE2019 :

``` python
import pandas as pd
import matplotlib.pyplot as plt
import dc_stat_think as dcst
import numpy as np
```

The following libraries that I have used to process and visualize the
dataset are Pandas, Matplotlib, dc_stat_think, and numpy. Pandas is an
open-source Python software library that is used data processing or
manipulation. Matplotlib is a plotting library for Python.Dc_stat_think
is a statistical Python library used for computing ecdf and confidence
intervals. Numpy is a Python library that provides a multidimensional
array object, which also includes shape manipulation, sorting, and many
more.

``` python
pop = pd.read_csv("co-est2019-alldata.csv", encoding='latin-1')
pop.head(5)
```

    ##    SUMLEV  REGION  DIVISION  ...  RNETMIG2017  RNETMIG2018 RNETMIG2019
    ## 0      40       3         6  ...     1.090366     1.773786    2.483744
    ## 1      50       3         6  ...     0.849656     0.540916    4.560062
    ## 2      50       3         6  ...    22.398256    24.727215   24.380567
    ## 3      50       3         6  ...   -24.998528    -8.754922   -5.165664
    ## 4      50       3         6  ...    -3.234669    -6.857092    1.831952
    ## 
    ## [5 rows x 164 columns]

``` python
pop.shape
```

    ## (3193, 164)

The first element of the tuple is the number of rows(3193, 164) and the
second element is the number of columns in the DataFrame

``` python
pop.isna().count()
```

    ## SUMLEV         3193
    ## REGION         3193
    ## DIVISION       3193
    ## STATE          3193
    ## COUNTY         3193
    ##                ... 
    ## RNETMIG2015    3193
    ## RNETMIG2016    3193
    ## RNETMIG2017    3193
    ## RNETMIG2018    3193
    ## RNETMIG2019    3193
    ## Length: 164, dtype: int64

I have used pandas to read the csv “co-est2019-alldata.csv”. Using the
shape command, I could I find how many columns and rows are in the data
set. The csv file contains 3193 rows and 164 columns. I utilized
“.isna().count()” to detect if there are any missing or null values in
the csv file and to count how many null values are found in each column.

``` python
box_pop = pop[['CENSUS2010POP', 'POPESTIMATE2015', 'POPESTIMATE2019']]
box_pop.head(5)
```

    ##    CENSUS2010POP  POPESTIMATE2015  POPESTIMATE2019
    ## 0        4779736          4852347          4903185
    ## 1          54571            54864            55869
    ## 2         182265           202939           223234
    ## 3          27457            26283            24686
    ## 4          22915            22566            22394

``` python
box_pop.describe()
```

box_pop.describe() would return descriptive statistics of a Pandas
DataFrame called box_pop. This method computes various summary
statistics, including measures of central tendency, dispersion, and
shape of the dataset’s distribution. \## CENSUS2010POP POPESTIMATE2015
POPESTIMATE2019 \## count 3.193000e+03 3.193000e+03 3.193000e+03 \##
mean 1.933871e+05 2.008363e+05 2.055995e+05 \## std 1.176201e+06
1.230056e+06 1.260310e+06 \## min 8.200000e+01 8.800000e+01 8.600000e+01
\## 25% 1.129900e+04 1.113600e+04 1.112800e+04 \## 50% 2.642400e+04
2.634200e+04 2.651600e+04 \## 75% 7.140400e+04 7.241300e+04 7.330900e+04
\## max 3.725396e+07 3.891804e+07 3.951222e+07

``` python
box_pop.boxplot(figsize=(10,5))
plt.ylabel("Population Count")
plt.title("CENSUS2010POP & POPESTIMATE2015 & POPESTIMATE2019")
```

![unnamed-chunk-3-1](https://user-images.githubusercontent.com/31125760/227323149-a0e26f75-ad11-4174-93cb-023750581377.png)

To plot the box plot. First, I have filtered out three columns, which
are CENSUS2010POP, POPESTIMATE2015, and POPESTIMATE2019. After that, I
described the data to observe the five major values (minimum,
maximum,mean, 25%, 50%, and 75% quartiles). To plot the box plot, I have
invoked both Pandas and Matplotlib libraries. I utilized Pandas to
create the box plot distribution and to increase the figure size of the
chart and Matplotlib to label the y-axis and add a title to the chart.

| Idiom:        | Boxplots                                                                                                                            |
|---------------|-------------------------------------------------------------------------------------------------------------------------------------|
| What: Data    | Table: many quantitative value attribute                                                                                            |
| What: Derived | Five quantitative attributes for each original attribute, representing its distribution.                                            |
| How: Encode   | One glyph/one attribute and multiple glyphs for each attribute expressing derived attribute values using vertical spatial position. |
| Why           | Find outliers, extremes, averages; identify skew.                                                                                   |

A box plot is a graph that provides good indication of how the values in
the data are spread out. Box plots are also a standardized way of
displaying the distribution based on the **five quantitative
attributes**( “minimum”, first quartile (Q1), median, third quartile
(Q3), and “maximum”). Instead of the single number encoded by the linear
mark in a bar chart, box plots employ a glyph to show five quantitative
attributes.

### Observations:

When analyzing the box plot, I have identified two observations:

1.  I could not identify the five quantitative values.
2.  There are significant amount of outliers in the glyph.
3.  The IQR and range are not properly distinguished.

**Advantages:**

According to the glyph, it has a poor visualization. Therefore, I can’t
identify any advantages.

**Disadvantages:**

1.  The IQR and range are not properly distinguished.
2.  Not able to identify statistical values.
3.  A lot of outliers are displayed. Therefore, the data manipulation
    needs to be further manually cleaned.

``` python
ecdf = pop['CENSUS2010POP'] 
x,y = dcst.ecdf(ecdf)
_ = plt.plot(x, y*100, linestyle='--', lw = 2)
plt.xlabel("CENSUS2010POP")
plt.ylabel("Percentage")
plt.show()
```

![unnamed-chunk-4-3](https://user-images.githubusercontent.com/31125760/227323225-c3dfc51a-b681-47a0-b136-9a4783dc0f9e.png)

To plot the ecdf. First, I have filtered out only one column, which is
CENSUS2010POP. An ECDF is a Cumulative Distribution Function estimator.
The ECDF essentially allows you to plot a data feature from least to
greatest and show the entire feature as if it were dispersed over the
data set. To plot the ecdf, I have invoked the dc_stat_think library. In
this library, I used the ecdf functionality to calculate the empirical
cumulative distribution function. I utilized Matplotlib forplotting the
cdf based on x to be ecdf values and y to be the percentage adding
dashes rather a complete line with line width of 2. Also, labeling the
y-axis, x-axis, and title to the chart.

| Idiom:      | eCDF (step graph)                                 |
|-------------|---------------------------------------------------|
| What: Data  | Two quantitative value attributes                 |
| How: Encode | line chart with connecting marks                  |
| Why         | Shows continuous and break values                 |
| X-axis:     | Data ‘x’ in the chosen attribute (Column)         |
| Y-axis:     | Percentage (cumulative density corresponding ‘x’) |

### Observations:

I could observe that there is a continuous step graph between the x-axis
( ecdf) and y-axis(percentages). But when I further clean the outliers,
I would have a better visualization.

**Advantages:**

1.  Was able to plot the entire data across the x-axis.

**Disadvantages:**

1.  The above chart has a lot of outliers.
2.  The distributions between the values can’t be observed.

``` python
hist_pop = pop[['CENSUS2010POP']]
hist_pop.hist(grid=False)
```

![unnamed-chunk-5-7](https://user-images.githubusercontent.com/31125760/227323330-2334cf74-0b62-4508-ac58-8029d492b084.png)

To plot the histogram. First, I have filtered out only one column, which
is CENSUS2010POP. After that, I described the data to observe the five
major values (minimum, maximum, mean, 25%, 50%, and 75% quartiles). To
plot the histogram, I have invoked both Pandas and Matplotlib libraries.
I utilized Pandas to create the histogram distribution and to increase
the figure size of the chart and Matplotlib to label the y-axis and add
a title to the chart.

**Advantages:**

According to the glyph, it has a poor visualization. Therefore, I can’t
identify any advantages.

**Disadvantages:**

1.  The histogram has only got data on the very left hand side.
2.  There is no sense of pattern or relationship that can be established
    making this histogram very unreliable and ambiguous.
3.  There are many outliers in the data set making the data less
    accurate and reliable.

## Part 2: Further Analysis

For the second part of this assignment, I have also used Python to
further investigate the data set and to create extra charts or graphs. I
chose the first data set (US Census Bureau County Population).

Source:
<https://www.census.gov/data/datasets/time-series/demo/popest/2010s-counties-total.html#par_textimage_70769902>

Here is the following Python code to further investigate the data set
and to create extra graphs :

``` python
pop_estimate = pop[['CENSUS2010POP', 'POPESTIMATE2019']]
ax1 = pop_estimate.plot.scatter(x='POPESTIMATE2019',y='CENSUS2010POP')
plt.title("POPESTIMATE2019 VS. CENSUS2010POP")
plt.show()
```

![unnamed-chunk-6-9](https://user-images.githubusercontent.com/31125760/227323391-c625c983-e9a3-4b9c-a4a6-1d3b5b05fc50.png)

By analyzing part 1 graphs, I asked myself the first question, which is
what is the correlation between Population Estimate 2019 and CENSUS 2010
Population, so I decided to make a plot of this. Scatter plot is
well-suitable for this kind of finding, due to having two quantitative
values and to find the correlation or relation between the columns. It
can be observed from the figure that the Population Estimate 2019 (the
x-axis) compared to the CENSUS 2010 Population (the y-axis) has a clear
direct proportion as the plots are in line and are forming a positive
gradient. A visual line of best fit would go through most of the points
suggesting the magnitude of how accurate the data points are. What made
me choose Population Estimate 2019 and CENSUS 2010 Population as my two
axis in the first place was to identify and determine the correlation
between them, and after observing and analyzing the result, I found a
strong relationship and correlation as I mentioned above and can be seen
in the figure.

| Idiom:      | Scatterplots                                                                 |
|-------------|------------------------------------------------------------------------------|
| What: Data  | Table: two quantitative value attributes                                     |
| How: Encode | Express values with horizontal and vertical spatial position and point marks |
| Why: Task   | Shows continuous and break values                                            |
| Scale:      | Items:hundreds                                                               |

``` python
census = box_pop[['CENSUS2010POP']]
Q1 = census.quantile(0.25)
Q3 = census.quantile(0.75)
IQR = Q3 - Q1
print(IQR)
(census < (Q1 - 1.5 * IQR)) |(census > (Q3 + 1.5 * IQR))
census_iqr = census[~((census < (Q1 - 1.5 * IQR)) |(census > (Q3 + 1.5 * IQR))).any(axis=1)]
census_iqr.shape
census_iqr.hist(grid=False,bins=9, figsize=(10,5))
plt.ylabel("Population Count")
plt.title("Frequency for CENSUS2010POP")
plt.xlabel("CENSUS2010POP")
```

![unnamed-chunk-7-13](https://user-images.githubusercontent.com/31125760/227323431-f44b5b43-43c9-45e5-8912-99e9f809b11b.png)

The second analysis that came to my mind was the Frequency of the
Population Count for CENSUS2010POP. I was very curious to find what
results I would obtain. Looking at the figure, it shows a clear pattern
of a decrease in Population Count (the y-axis) as the CENSUS2010POP (the
x-axis) increases. It was also found that the Population Count was at
its peak (around 1200) when the CENSUS2010POP was at its lowest (around
0-20000). It was found after several tweakings that 9 bins was the most
accurate representation of the Histogram in terms of pattern. I needed
to calculate the Inter-Quartile Range (IQR) since I will use it in the
equation later. I calculated IQR by subtracting the third quartile (Q3)
from the first quartile (Q1). Next, I had to remove any that was either
from the upper quartile or the lower quartile from the CENSUS2010POP so
that the Histogram shows the CENSUS2010POP within the IQR. I have
invoked both Pandas and Matplotlib libraries. I utilized Pandas to
create the histogram distribution and to increase the figure size of the
chart, adjust the bins and Matplotlib to label the y-axis and add a
title to the chart.

## References:

1.  Understanding what is ecdf:
    <https://towardsdatascience.com/what-why-and-how-to-read-empirical-cdf-123e2b922480>

2.  How to generate ecdf using Python:
    <https://medium.com/the-researchers-guide/how-to-generate-ecdf-plot-using-python-and-r-247ef81fbf3f>

3.  For Data:
    <https://www.census.gov/data/datasets/time-series/demo/popest/2010s-counties-total.html#par_textimage_70769902>
