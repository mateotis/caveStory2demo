def loadGame(): #This actually implements AFTER loadLevel() does. It determines the CLASS TYPES and VARIABLE ATTRIBUTE VALUES for all objects at spawn points specified by the loadLevel() function.
	#Start with the Game Class. The file must contain the info needed for every oibject in the game as such, the file must know firsthand how many objects are present in the level...
	gameReader = open("CaveStory2Files.txt", 'r')

	gameDictionary = {"Width":1024, "Height":768, "Ground":600} #Creates a dictionary to store info specific to the "Game" class in the script.
	gameReader.readline().readline() #Skips the Level record at the top of the file, and the first header included in the text file for the "Game" class' only variable-value attribute, which is: "GAME:".
	for key in quoteDictionary:
		rawInfo = gameReader.readline().strip() #Reads the first line containg the Game Class' info, whcih is the Ground position.
		gameDictionary[key] = int(rawInfo[rawInfo.index(':') + 1:rawInfo.index('#') + 1]) #Assigns the value stored in the file for the ground's current position to the relevant gameDictionary key
	gameReader.readline() #Skips the whitespace between different object info paragraphs.

	quoteDictionary = {"XPos":50, "YPos":525, "colliderRadius":75, "Q'sGround":600, "currentSprite":"quote.png", "spriteWidth":120, "spriteHeight":120, "frameCount":4, "DirFaced":1, "currentLives":3, "currentHealth":100, "currentEXP":0}
	gameReader.readline()
	for key in quoteDictionary:
		rawInfo = gameReader.readline().strip()
		if rawInfo[rawInfo.index('#') - 1].isdigit(): 
			quoteDictionary[key] = int(rawInfo[rawInfo.index(':') + 1:rawInfo.index('#') + 1])
		else:
			quoteDictionary[key] = rawInfo[rawInfo.index(':') + 1:rawInfo.index('#') + 1]
	gameReader.readline()

	curlyBraceDictionary = {"XPos":50, "YPos":525, "colliderRadius":75, "Q'sGround":600, "currentSprite":"quote.png", "spriteWidth":120, "spriteHeight":120, "frameCount":4, "DirFaced":1}
	gameReader.readline()
	for key in curlyBraceDictionary:
		rawInfo = gameReader.readline().strip()
		if rawInfo[rawInfo.index('#') - 1].isdigit(): 
			curlyBraceDictionary[key] = int(rawInfo[rawInfo.index(':') + 1:rawInfo.index('#') + 1])
		else:
			curlyBraceDictionary[key] = rawInfo[rawInfo.index(':') + 1:rawInfo.index('#') + 1]
	gameReader.readline()

	balrogDictionary = {"XPos":50, "YPos":525, "colliderRadius":75, "BRog'sGround":600, "currentSprite":"balrog.png", "spriteWidth":120, "spriteHeight":120, "frameCount":4, "DirFaced":1}
	gameReader.readline()
		for key in balrogDictionary:
			rawInfo = gameReader.readline().strip()
			if rawInfo[rawInfo.index('#') - 1].isdigit(): 
				balrogDictionary[key] = int(rawInfo[rawInfo.index(':') + 1:rawInfo.index('#') + 1])
			else:
				balrogDictionary[key] = rawInfo[rawInfo.index(':') + 1:rawInfo.index('#') + 1]
		gameReader.readline()

	miseryNPCDictionary = {"XPos":50, "YPos":525, "colliderRadius":75, "M_NPC'sGround":600, "currentSprite":"misery.png", "spriteWidth":120, "spriteHeight":120, "frameCount":4, "DirFaced":1}
	gameReader.readline()
	for key in miseryNPCDictionary:
		rawInfo = gameReader.readline().strip()
		if rawInfo[rawInfo.index('#') - 1].isdigit(): 
			miseryNPCDictionary[key] = int(rawInfo[rawInfo.index(':') + 1:rawInfo.index('#') + 1])
		else:
			miseryNPC[key] = rawInfo[rawInfo.index(':') + 1:rawInfo.index('#') + 1]
	gameReader.readline()

	miseryBossDictionary = {"XPos":50, "YPos":525, "colliderRadius":75, "M_Boss'sGround":600, "currentSprite":"misery.png", "spriteWidth":120, "spriteHeight":120, "frameCount":4, "DirFaced":1}
	gameReader.readline()
	for key in miseryBossDictionary:
		rawInfo = gameReader.readline().strip()
		if rawInfo[rawInfo.index('#') - 1].isdigit(): 
			miseryBossDictionary[key] = int(rawInfo[rawInfo.index(':') + 1:rawInfo.index('#') + 1])
		else:
			miseryBossDictionary[key] = rawInfo[rawInfo.index(':') + 1:rawInfo.index('#') + 1]
	gameReader.readline()

	polarStarDictionary = {"XPos":200, "YPos":600, "colliderRadius":30, "PS'sGround":600, "gunDamage":5}
	gameReader.readline()
	for key in miseryBossDictionary:
		rawInfo = gameReader.readline().strip()
		if rawInfo[rawInfo.index('#') - 1].isdigit(): 
			polarStarDictionary[key] = int(rawInfo[rawInfo.index(':') + 1:rawInfo.index('#') + 1])
		else:
			polarStarDictionary[key] = rawInfo[rawInfo.index(':') + 1:rawInfo.index('#') + 1]
	gameReader.readline()

	'''machineGunDictionary = {"XPos":200, "YPos":600, "colliderRadius":30, "MG'sGround":600, "gunDamage":5}
	gameReader.readline()
	for key in miseryBossDictionary:
		rawInfo = gameReader.readline().strip()
		if rawInfo[rawInfo.index('#') - 1].isdigit(): 
			polarStarDictionary[key] = int(rawInfo[rawInfo.index(':') + 1:rawInfo.index('#') + 1])
		else:
			polarStarDictionary[key] = rawInfo[rawInfo.index(':') + 1:rawInfo.index('#') + 1]
	gameReader.readline()'''


