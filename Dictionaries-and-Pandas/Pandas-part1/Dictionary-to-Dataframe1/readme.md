Dictionary to DataFrame (1):
Pandas is an open source library, providing high-performance, easy-to-use data structures and data analysis tools for Python. Sounds promising!

The DataFrame is one of Pandas' most important data structures. It's basically a way to store tabular data where you can label the rows and the columns. One way to build a DataFrame is from a dictionary.

In the exercises that follow you will be working with vehicle data from different countries. Each observation corresponds to a country and the columns give information about the number of vehicles per capita, whether people drive left or right, and so on.

Three lists are defined in the script:

names, containing the country names for which data is available.
dr, a list with booleans that tells whether people drive left or right in the corresponding country.
cpc, the number of motor vehicles per 1000 people in the corresponding country.
Each dictionary key is a column label and each value is a list which contains the column elements.

Instructions:
Import pandas as pd.
Use the pre-defined lists to create a dictionary called my_dict. There should be three key value pairs:
key 'country' and value names.
key 'drives_right' and value dr.
key 'cars_per_cap' and value cpc.
Use pd.DataFrame() to turn your dict into a DataFrame called cars.
Print out cars and see how beautiful it is.