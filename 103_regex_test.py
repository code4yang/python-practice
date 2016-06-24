import re

str = 'this is a string test'
g = re.findall(r'\b[a-z]+\b', str)
print(g)

# greedy match
g = re.findall(r'\b.+\b', str)
print(g)

# use ? stop greedy match
g = re.findall(r'\b.+?\b', str)
print(g)

# match a string end with a 't'
g = re.match(r'(?:.+t)*', str)
print(g.group(0))

g = re.search(r'(?!.net)', 'follow a .net')
print(g)
g = re.search(r'(?!.net)', '.net not follow')
print(g)
g = re.search(r'(?!.net)', str)
print(g)

