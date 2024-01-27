a = input()
import re
print(int(re.sub('\D', '', a)) + 1)


