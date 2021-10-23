# Let's define general python function
>>> def doubleOrNothing(num):
...     return num * 2

# now use Map on it.
>>> map(doubleOrNothing, [1,2,3,4,5])
<map object at 0x7ff5b2bc7d00>

# apply built-in list method on Map Object
>>> list(map(doubleOrNothing, [1,2,3,4,5])
[2, 4, 6, 8, 10]

# using lambda function
>>> list(map(lambda x: x*2, [1,2,3,4,5]))
[2, 4, 6, 8, 10]