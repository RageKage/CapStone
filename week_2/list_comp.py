# classes_registered = ["ITEC 1150", "ITEC 1235", "ENGL 1340", "MATH 1231"]

# only_ITEC = [ c.lower() for c in classes_registered if c.startswith("ITEC") ]


# print(only_ITEC) # ['ITEC 1150', 'ITEC 1235']


# # record of temperature values for every day

# high_temps = [-1,78,21,2,3,51,2,-5,55,76,36,78,67,93,23,-1]

# only_true = [ t for t in high_temps if t > 0 ]

# print(only_true) # [78, 21, 2, 3, 51, 2, 55, 76, 36, 78, 67, 93, 23]

# convert_C = [ (t-32) * 5/9.  for t in high_temps if t > 0 ]

# print([f"{temp:.1f}" for temp in convert_C])

# avg = sum(convert_C) / len(convert_C)

# print(f"{avg:.1f}")

a = ["I 1", "K 2", "N 3", "I 4", "I 5"]

b = [ n for n in a if n.startswith("I")]

print(b)
