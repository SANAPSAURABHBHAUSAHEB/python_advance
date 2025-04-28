
some_list = [i for i in range(3, 33, 3)]

iter_here = iter(some_list)

print(f"the list is here --> {some_list}")
for count, i in enumerate(range(0, len(some_list))):
    print(f"{count} element --> {next(iter_here)}")

# StopIteration Exception for end of iterator

