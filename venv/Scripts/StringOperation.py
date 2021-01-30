print( 'plane' in 'The worlds fastest plane' )
print('The worlds fastest plane'.find('plane'))
'The worlds fastest plane'.find('plane')
str = 'The worlds fastest plane'
print(str.find('plane'))
c = str.split(" ")
print(c)
e = " ".join(reversed(c))
print(e)
string = 'Hello 1 World 2'
vowels = ('a','e','i','o','u')
print("".join(c for c in string if c not in vowels))