#strings built-in functions
s='Hello, World!'
print(s.upper()) #HELLO, WORLD!
print(s.lower()) #hello, world!
print(s.capitalize()) #Hello, world!
print(s.title()) #Hello, World!
print(s.strip('!')) #Hello, World
print(s.replace('World', 'Python')) #Hello, Python!
print(s.split(', ')) #['Hello', 'World!']
print(s.find('World')) #7
print(s.startswith('Hello')) #True
print(s.endswith('!')) #True
print(s.count('o')) #2
print(s.isalpha()) #False
print(s.isdigit()) #False
print(s.isalnum()) #False
print(s.islower()) #False
print(s.isupper()) #False
print(s.isprintable()) #True
print(s.isascii()) #True
print(s.center(20, '*')) #***Hello, World!****
print(s.ljust(20, '-')) #Hello, World!------
print(s.rjust(20, '-')) #------Hello, World!
print(s.zfill(20)) #000000Hello, World!
print(s.encode('utf-8')) #b'Hello, World!'
print(s.format()) #Hello, World!
print(s.format_map({})) #Hello, World!
print(s.join(['Hello', 'World'])) #Hello, World
print(s.partition(', ')) #('Hello', ', ', 'World!')
print(s.rpartition(', ')) #('Hello', ', ', 'World!')
print(s.splitlines()) #['Hello, World!']
print(s.swapcase()) #hELLO, wORLD!  
print(s.translate(str.maketrans('H', 'h'))) #hello, World!
print(s.zfill(30)) #000000000000000000000000Hello, World!
