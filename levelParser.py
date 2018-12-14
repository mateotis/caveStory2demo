rawLevel = open("levelTest.csv", "r")
convLevel = open("levelCode.txt", "w")

print(rawLevel)
for line in rawLevel:
	line = line.strip().split(",")
	x = 0
	y = 0
	for element in line:
		for o in element:
			print(o)
			if o == "T":
				print('true')
				convLevel.write("self.tiles.append(Tile(" + str(x) +"," + str(y) + "," + "100, 100, 50))")
				convLevel.write('\n')
				x += 100
			#y += 100

convLevel.close()

convLevel = open("levelCode.txt", "r")

for line in convLevel:
	#line = line.strip().split(",")
	print(line)