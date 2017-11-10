f = open('myTextFile.txt', "r")
lines = f.readlines()
f.close()

lines.sort()

g = open("sortedfriends.txt", "w")
for v in lines:
	g.write(v)
g.close()


outFile = open('sample.txt', 'w')
outFile.write('My first output file!')
outFile.close()


