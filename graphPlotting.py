'''
Q1. Given two integer arrays, X and Y. Plot the graph between X and Y. Please consider.
x = np.array([0,1,2,3,4,5,6,7,9,10])
y=np.array([1,2,5,10,17,26,37,50,82,101])
From the help of graph, determine the range of Y when the value of X is 8.
Plot and print the range of Y.
Note: Here lower limit and upper limit of range must be multiple of 10 and difference between upper limit and lower limit must be equal to 10.


Output Format
lower_limit to upper_limit
'''

## Sol 1.
# import numpy as np
# import matplotlib.pyplot as plt

# x = np.array([0,1,2,3,4,5,6,7,9,10])
# y=np.array([1,2,5,10,17,26,37,50,82,101])

# plt.plot(x,y)
# plt.show()

# #range of y
# print("60 to 70")

'''
Q2. our task is to find the point of inclination by visualizing the plot for the given points on the x and y-axis.
You need to follow these steps:
    1. Create two arrays, x and y. 
    2. x should hold the first 20 even points starting from 0 and y should be an exponentiation array where 
                            y[i] = 2^x[i]. 
    3. Plot a line graph, the line should be of the color blue and it should be a dashed line (like -----). 
    4. Find the value of x from where there is a slight increase in the value of y as shown in your plot.
    Expected Output
    Plot and print the value of x.

**Note**: Printed x must be a multiple of 5.
Output Format
x
'''
## Sol 2.
# import matplotlib.pyplot as plt
# import numpy as np

# x = np.arange(0, 40, 2)
# y = 2**(x)
# plt.plot(x,y,"--",color="b")
# plt.grid()
# plt.show()
# print(30)


'''
Q3. Plot the two graphs on same plot.The graph between the two given integer array X and Y and the graph between two integer array X and Y where X should hold 20 even points starting from 0 and y should be equal to X where 
y[i] = .Plot should have x label and y label and the legend to differentiate between the two graphs. Consider,
x1 =[0,1,2,3,4,5,6,7,9,10]
y1=[1,2,5,10,17,26,37,50,82,101]
and

x2=np.arange(0,40,2)
y2=2*x2
Find the value x (in the range of 10) of both the plots when the value of y is 60
For each plot print the output to new line.
Output Format
lower_limit to upper_limit
lower_limit to upper_limit
'''
## Sol 3.
# import matplotlib.pyplot as plt
# import numpy as np

# x1 =[0,1,2,3,4,5,6,7,9,10]
# y1=[1,2,5,10,17,26,37,50,82,101]

# x2= np.arange(0,40,2)
# y2=2*x2

# plt.plot(x1,y1, "r", label="line_graph1")
# plt.plot(x2,y2, label = "line_graph2")
# plt.grid()
# plt.show()
# print("0 to 10","\n","25 to 35")

'''Q4. We are given data of Microsoft Corporations, it contains the gross annual revenue in billion U.S dollar and the number of employees in thousands and year. Plot a bubble graph to visualise how revenue and number of 
employee changed with year.
Find years where there is a drastic increase in gross revenue of Microsoft Corporations (from previous and next year both). Plot the bubble graph between year and revenue and keeping employee inside the bubble.
Print the year, revenue and number of the employee where there is a drastic increase in revenue ( Top 2 ).
Note:For finding the year where there is a drastic increase in gross revenue check whether the revenue of that year is greater than in previous years and greater than next year. Here years should be printed in ascending order.
Output Format:
year1 revenue1 employee1
year2 revenue2 employee2
. . . 
. . .
. . .

Given:-
e=[61,71,79,91,93,89,90,94,99,128,118,114,124,131]
y=[2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018]
r=[39.79,44.28,51.12,60.42,58.44,62.48,69.94,73.72,77.85,86.83,93.58,85.32,89.95,110.36]
'''

## Sol 4.


'''
Q5. Given data is having distribution of sales of different laptops for the year 2018 in India (it has company name and number of laptops sold).
Plot a pie graph to show the %age distribution for the year 2018 and also print the value of %age distribution of individual companies.
Note: Output should have company name and %age distribution (%age value should be upto 1 decimal place without the % sign) , it should be in the same order as it is given.
Output Format:
company_name1 percentage1
company_name2 percentage2
. . .
. . . 
. . .

Given:-
company=['HP','Dell','Lenovo','Asus','Apple','Acer']
sold=[20000,43000,15000,17000,22000,13000]
'''

'''
Q6. Given height (in centimetre) and weight (in kilograms) of 20 students, Plot a two different histogram of height and weight. whereas divide the data in 5 bins.
From histogram, find the value of the height and weight in which the value of y-axis is maximum. Print starting value of bin where y is maximum. For eg. if for height with range 50 to 55 is maximum, 
then print 50. Print the value as integer (after rounding off). (to answer this please look closely to the graph)
Plot the histogram and print the value.
Output Format
height_value weight_value

Given:-
height=[189,185,195,149,189,147,154,174,169,195,159,192,155,191,153,157,140,144,172,157]
## Weight
weight=[87,110,104,61,104,92,111,90,103,81,80,101,51,79,107,110,129,145,139,110]
'''