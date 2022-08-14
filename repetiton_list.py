mylist = [5, 3, 5, 2, 1, 6, 6, 4] # the original list of integers with duplicates

dump = {x for x in mylist if mylist.count(x) > 1}
""""curly braces simplifies a set so no duplicates""""

print(dump)
