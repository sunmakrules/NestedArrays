#function to flatten a nested array
flatten = lambda x: [y for l in x for y in flatten(l)] if type(x) is list else [x]

a = [1, 2, [3, 4], [[5, 6], [7, 8]]]
print(flatten(a)) #Calls flatten function


