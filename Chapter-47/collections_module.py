# counter function of collections module
# Counter is a dict sub class that allows you to easily count objects | calculating frequency pf objects
import collections
from collections import OrderedDict
list = [1, 2, 3, 3, 3, 2, 1, 1, 1, 1, 1, 1, 1, 6, 7 ,8 , 8]
print(collections.Counter(list))

# letter counter
character_list = "Deepali Ghadia"
print(collections.Counter(character_list))

# word counter
words = "The built-in collections package provides several specialized, flexible collection types that are both high-performance and provide alternatives to the general collection types of dict, list, tuple and set. The module also defines abstract base classes describing different types of collection functionality"
print(collections.Counter(words.split()))


# OrderedDict function of collections module
# The order of keys in Python dictionaries is arbitrary: they are not governed by the order in which you add them.
# The collections.OrderedDict class provides dictionary objects that retain the order of keys.
ordered_dictionary = OrderedDict([(1, "A"),(2, "B") ])
print(ordered_dictionary)