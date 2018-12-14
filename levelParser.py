rawLevel = open("levelTest.csv", "r")
convLevel = open("levelCode.txt", "w")
x = 0
y = 0
cnt = 0
for line in rawLevel:
	row = line.strip().split(",")
	for element in row:
		for o in element:
			#print(o)
			if o == "R":
				cnt += 1
				#print('true')
				convLevel.write("self.tiles.append(Tile(" + str(x) +"," + str(y) + "," + "223, 187, 50, 'caveRocks.png'))")
				convLevel.write('\n')
				print(x, y)
				x = 223 * cnt
		cnt = 0
		x = 0
	y += 187

convLevel.close()

convLevel = open("levelCode.txt", "r")

#for line in convLevel:
	#line = line.strip().split(",")
	#print(line)