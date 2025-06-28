loc and iloc (3):
It's also possible to select only columns with loc and iloc. In both cases, you simply put a slice going from beginning to end in front of the comma:

cars.loc[:, 'country']
cars.iloc[:, 1]

cars.loc[:, ['country','drives_right']]
cars.iloc[:, [1, 2]]


Instructions:
Print out the drives_right column as a Series using loc or iloc.
Print out the drives_right column as a DataFrame using loc or iloc.
Print out both the cars_per_cap and drives_right column as a DataFrame using loc or iloc.