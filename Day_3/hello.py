
import demo_functions
import demo_functions as t
from demo_functions import add as f

print(demo_functions.add(2, 4))     # basic import
print(t.add(2, 4))                  # import with rename
print(f(2, 4))                      # specific import

