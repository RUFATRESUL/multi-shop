from random import randint
import sys

count = int(sys.argv[1])

result = ''

for i in range(count):
    char_code = randint(33,125)
    result += chr(char_code)
    

print(result)