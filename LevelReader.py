def loadLevel(levelNum, level):
	
	level = {"Quote":[], "Bats":[], "Critters":[], "S":[], "T_S":[], "Capsules":[], "Spikes":[], "Misery":[], "Balrog":[], "CurlyBrace":[]}
	
	levelReader = open("csLevel_" + str(levelNum) + ".csv", 'r')
	dimsList = levelReader.readline().split(",")
	rowCount = dimsList[0]
	colCount = dimsList[1]

	for row in range(rowCount):
		line = lineReader.readline().split(",")
		stoneSwitch = False
		transStoneSwitch = False
		for cell in range(colCount):
			if line[cell] == 's':
				level["S"].append([row, cell])
				stoneSwitch = not stoneSwitch
			elif line[cell] == 's*':
				level["T_S"].append([row, cell])
				transStoneSwitch = not transStoneSwitch
			elif line[cell] == "ss":
				level["S"].append([row, cell])
			elif line[cell] == "":
				if stoneSwitch:
					level["S"].append([row, cell])
				elif transStoneSwitch:
					level["T_S"].append([row, cell])
			elif line[cell] == 'Q':
				level["Quote"].append([row, cell])
			elif line[cell] == 'C':
				level["Critters"].append(row, cell)
			elif line[cell] == 'B':
				level["Bats"].append([row, cell])
			elif line[cell] == 'hc':
				level["Capsules"].append([row, cell])
			elif line[cell] == 'M':
				level["Misery"].append([row, cell])
			elif line[cell] == 'spk':
				level["Spikes"].append([row, cell])
			elif line[cell] == "BAL":
				level["Balrog"].append([row, cell])
			elif line[cell] == "CRLY":
				level["CurlyBrace"].append([row, cell])

'''

	gameWriter = open("CaveStory2Files.txt", 'w')
	gameWriter.write("LEVEL: " + levelNum + "#\n")

	gameWriter.write("GAME:\n")
	gameWriter.write("#")

	gameWriter.write("Quote:\n")
	gameWriter.write("#")

	gameWriter.write("Curly Brace:\n")
	gameWriter.write("#")

	gameWriter.write("Balrog:\n")
	gameWriter.write("#")

	gameWriter.write("MiseryNPC:\n")
	gameWriter.write("#")

	#gameWriter.write("MiseryBoss:\n")
	#gameWriter.write("#")

'''

	'''
	MiseryBoss:
- XPos:200#
- YPos:50#
- colliderRadius:75#	*Depends on sprite dimensions, which depends on the sprite currently being used
- M_Boss'sGround:600#
- currentSprite:misery.png#	*Changes when you acquire a gun or switch between them
- spriteWidth:125#
- spriteHeight:125#
- frameCount:6#	*Depends on sprite currently in use, I think?
- DirFaced:-1#
#MiseryBoss Left-outs: XVelocity, YVelocity, collideChecker_L, collideChecker_R, collideChecker_T, collideChecker

	PolarStar:
- XPos:200#
- YPos:600#
- colliderRadius:30#
- PS'sGround:600#
- gunDamage:5#
#Polar Star Left-outs: 

	MachineGun:
- XPos:200#
- YPos:600#
- colliderRadius:30#
- MG'sGround:600#
- gunDamage:5#

	'''
