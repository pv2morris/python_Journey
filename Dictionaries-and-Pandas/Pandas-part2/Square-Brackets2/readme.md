Square Brackets (2):
Square brackets can do more than just selecting columns. You can also use them to get rows, or observations, from a DataFrame. The following call selects the first five rows from the cars DataFrame:

cars[0:5]
The result is another DataFrame containing only the rows you specified.

Pay attention: You can only select rows using square brackets if you specify a slice, like 0:4. Also, you're using the integer indexes of the rows here, not the row labels!

Instructions:
Select the first 3 observations from cars and print them out.
Select the fourth, fifth and sixth observation, corresponding to row indexes 3, 4 and 5, and print them out.