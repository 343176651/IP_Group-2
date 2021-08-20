import random
for i in range(10) :
    print(random.randint(1,3))

import re
pattern = re.compile('^([0-3])$')
str = '3'
print(pattern.search(str))
print(5)