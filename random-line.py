from random import randrange as randrange
from linecache import getline as getline

def get_line(path):
	file = open(path, 'r', encoding='utf-8')
	num_lines = sum(1 for line in file)
	random = randrange(num_lines)
	line = getline(path, random)
	file.close()
	return line[0:-1]

print(get_line('rappers.txt'))