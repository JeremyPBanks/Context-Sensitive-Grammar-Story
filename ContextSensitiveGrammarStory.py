import random
import pymysql
import sys
import re
import myQueue
import myNode




#*************************************
#*  Functions for main user options  *
#*************************************
def viewRecordsFunc():
	userInput2 = raw_input("Write in a word that you would like to search for: ")
	userInput21 = userInput2.lower()
	boolIsInDB = False
	while boolIsInDB == False:
		if userInput21 == "back":
			return

		for x in listTables:
			try:
				query0 = "SELECT frequency FROM ",x," WHERE word=%s;"
				query = ''.join(query0)
				cur.execute(query,(userInput21))
				typeName = cur.fetchone()[0]
				boolIsInDB = True
				conn.commit()
				print "Number of times ",userInput21, " was used over all stories generated: ",typeName
				break
			except:
				continue
		if boolIsInDB == True:
			userInput2 = raw_input("Write in another word that you would like to search for: ")
			userInput21 = userInput2.lower()
			boolIsInDB = False
		else:
			userInput2 = raw_input("Word not found. Write in another word that you would like to search for: ")
			userInput21 = userInput2.lower()


def insertionFunc():
	userInput2 = raw_input("Which category of words would you like to insert into the database? Nouns, Proper Nouns, Pronouns, Articles, Verbs, Adjectives, Adverbs, Conjunctions, Prepositions, Exclamations, or Opening Phrases? ")
	userInput2 = userInput2.lower()
	print "\n"
	while 1:
		if userInput2 in dict2:
			dict2[userInput2]()
			break
		else:
			userInput2 = raw_input("Incorrect Input. Please enter a valid category [Nouns, Proper Nouns, Pronouns, Articles, Verbs, Adverbs, Conjunctions, Prepositions, Exclamations, or Opening Phrases]: ")

def generateFunc():
	stringStory = ""
	characterName = ""
	query = "SELECT COUNT(*) FROM ProperNouns;"
	cur.execute(query)
	countRows = cur.fetchone()[0]
	conn.commit()
	i=0
	
	#Randomly selecting our main character
	while 1:
		characterNameIndex = random.randint(1,countRows)
		query = "SELECT type FROM ProperNouns WHERE id=%s;"
		cur.execute(query,(characterNameIndex))
		typeName = cur.fetchone()[0]
		conn.commit()
		if typeName == "person":
			query = "SELECT word FROM ProperNouns WHERE id=%s;"
			cur.execute(query,(characterNameIndex))
			characterName = cur.fetchone()[0]
			conn.commit()
			query = "UPDATE ProperNouns SET frequency = frequency + 1 WHERE word=%s;"
			cur.execute(query,(characterName))
			conn.commit()
			break

	#Randomly selecting our opening phrase and, in turn, the tense for the story
	query = "SELECT COUNT(*) FROM OpeningPhrases;"
	cur.execute(query)
	countRows = cur.fetchone()[0]
	conn.commit()
	openingIndex = random.randint(1,countRows)
	query = "SELECT phrase FROM OpeningPhrases WHERE id=%s;"
	cur.execute(query,(openingIndex))
	openingPhrase = cur.fetchone()[0]
	conn.commit()
	query = "UPDATE OpeningPhrases SET frequency = frequency + 1 WHERE phrase=%s;"
	cur.execute(query,(openingPhrase))
	conn.commit()
	query = "SELECT tense FROM OpeningPhrases WHERE id=%s;"
	cur.execute(query,(openingIndex))
	tense = cur.fetchone()[0]
	conn.commit()

	openingObj = myNode.wordNode(openingPhrase.capitalize(),"OpeningPhrases")
	ParagraphQueue.enqueue(openingObj)		
	maxLen = random.randint(1,6)
	genStart(characterName,maxLen)
	printMyStory()
	sys.exit(0)

def printMyStory():
	strFin = ""
	while ParagraphQueue.isEmpty() == False:
		strFin += ParagraphQueue.dequeue().word
		if ParagraphQueue.isEmpty() != True:
			strFin += " "
	
	strFin = strFin.replace("  "," ")
	strFin = strFin.replace(" .",".")
	print strFin







#***********************************************
#*  Recursive functions for contextual states  *
#***********************************************
def genStart(characterName,maxLen):
	howToContinue = 3#random.randint(1,5)
	
	if howToContinue == 1:
		adverbObj = getAdverb()
		ParagraphQueue.enqueue(adverbObj)
		genS1(characterName,maxLen,False,1,"verb","",['action','change'],[])
	elif howToContinue == 2:
		exObj = getExclamation()
		exObj.word += "! Sorry, that was strange, anyway "
		ParagraphQueue.enqueue(exObj)
		genStart(characterName,maxLen)
	elif howToContinue == 3:
		artObj = getArticle()
		ParagraphQueue.enqueue(artObj)
		genS1(characterName,maxLen,False,1,"adjective",artObj.word,[],[])
	elif howToContinue == 4:
		adjObj = getAdjective(0,"")
		ParagraphQueue.enqueue(adjObj)
		genS1(characterName,maxLen,False,1,"noun","",[],['place','thing'])
	elif howToContinue == 5:
		prepObj = getPreposition()
		ParagraphQueue.enqueue(prepObj)
		genS1(characterName,maxLen,False,1,"article","",[],[])
	#elif howToContinue == 6:
	#	nObj = getNoun("yes",['person','place','thing'],"")
	#	ParagraphQueue.enqueue(nObj)
	#	genS1(characterName,maxLen,False,1,"verb","",['action','change','situation'],[])
	return
			

def genS1(characterName, maxLen, False, firstThrough, catToIf, art, verbL, nounL):
	if maxLen == 0:
		return

	queueLen = len(ParagraphQueue.paragraph)
	lastArticle = findMyLastArticle(queueLen)
	print "Last Article: ",lastArticle

	if catToIf == "verb":
		randElement = random.randint(1,4)
		vObj = getVerb(verbL,ParagraphQueue.paragraph[queueLen-1].tense)
		#if lastArticle != "an" and lastArticle != "":
		#	while vObj.word[0] in listVowels:
		#		vObj = getVerb(verbL,ParagraphQueue.paragraph[queueLen-1].tense)
		#else:
		#	while vObj.word[0] not in listVowels:
		#		vObj = getVerb(verbL,ParagraphQueue.paragraph[queueLen-1].tense)
		ParagraphQueue.enqueue(vObj)
		if randElement == 1:
			genS1(characterName,maxLen,False,1,"article",lastArticle,[],[])
		elif randElement == 2:
			genS1(characterName,maxLen,False,1,"preposition","",[],[])
		elif randElement == 3:
			genS1(characterName,maxLen,False,1,".","",[],[])
		else:
			genS1(characterName,maxLen,False,1,".",lastArticle,[],[])

	elif catToIf == "noun":
		randElement = random.randint(1,4)
		nObj = getNoun("no",['person','place','thing'],lastArticle)
		#if lastArticle != "an" and lastArticle != "":
		#	while nObj.word[0] in listVowels:
		#		nObj = getNoun("no",['person','place','thing'],art)
		#else:
		#	while nObj.word[0] not in listVowels:
		#		nObj = getNoun("no",['person','place','thing'],art)
		if randElement == 1:
			nObj = getNoun("yes",['person','place','thing'],lastArticle)
			#if lastArticle != "an" and lastArticle != "":
			#	while nObj.word[0] in listVowels:
					
			ParagraphQueue.enqueue(nObj)
			genS1(characterName,maxLen,False,1,"conjunctions",lastArticle,[],[])
		elif randElement == 2:
			ParagraphQueue.enqueue(nObj)
			genS1(characterName,maxLen,False,1,"adverb",lastArticle,[],[])
		elif randElement == 3:
			ParagraphQueue.enqueue(nObj)
			genS1(characterName,maxLen,False,1,".",lastArticle,[],[])
		else:
			ParagraphQueue.enqueue(nObj)
			genS1(characterName,maxLen,False,1,"verb",lastArticle,['action','change','situation'],[])

	elif catToIf == "adjective":
		adjObj = getAdjective(0, art)
		ParagraphQueue.enqueue(adjObj)
		genS1(characterName,maxLen,False,1,"noun","",[],['place','thing',])
		
	elif catToIf == "preposition":
		prepObj = getPreposition()
		ParagraphQueue.enqueue(prepObj)
		genS1(characterName,maxLen,False,1,"article",lastArticle,['person','place','thing'],[])

	elif catToIf == "article":
		artObj = getArticle()
		ParagraphQueue.enqueue(artObj)
		randElement = random.randint(1,2)
		if randElement == 1:
			genS1(characterName,maxLen,False,1,"adjective",lastArticle,[],[])
		else:
			genS1(characterName,maxLen,False,1,"noun",lastArticle,[],[])

	elif catToIf == "conjunctions":
		conObj = getConjunction()
		ParagraphQueue.enqueue(conObj)
		genS1(characterName,maxLen,False,1,"article",lastArticle,[],[])

	elif catToIf == "adverb":
		adverbObj = getAdverb()
		ParagraphQueue.enqueue(adverbObj)
		genS1(characterName,maxLen,False,1,"verb","",['action','change'],[])

	elif catToIf == ".":
		maxLen -= 1
		periodObj = myNode.wordNode(".",None)
		ParagraphQueue.enqueue(periodObj)
		return

	return


def findMyLastArticle(queueLen):
	while queueLen > 0:
		if ParagraphQueue.paragraph[queueLen-1].category == "Articles":
			return ParagraphQueue.paragraph[queueLen-1].word
		queueLen -= 1
	return None







#*********************************
#*  Functions for grabbing words *
#*********************************
def getAdverb():
	query = "SELECT COUNT(*) FROM Adverb;"
	cur.execute(query)
	countRows = cur.fetchone()[0]
	conn.commit()
	adverbIndex = random.randint(1,countRows)
	query = "SELECT word FROM Adverb WHERE id=%s;"
	cur.execute(query,(adverbIndex))
	strAdverb = cur.fetchone()[0]
	conn.commit()
	query = "UPDATE Adverb SET frequency = frequency + 1 WHERE word=%s;"
	cur.execute(query,(strAdverb))
	conn.commit()
	adverbObj = myNode.wordNode(strAdverb,"Adverb")
	return adverbObj

def getExclamation():
	query = "SELECT COUNT(*) FROM Exclamation;"
	cur.execute(query)
	countRows = cur.fetchone()[0]
	conn.commit()
	exIndex = random.randint(1,countRows)
	query = "SELECT word FROM Exclamation WHERE id=%s;"
	cur.execute(query,(exIndex))
	strEx = cur.fetchone()[0]
	conn.commit()
	query = "UPDATE Exclamation SET frequency = frequency + 1 WHERE word=%s;"
	cur.execute(query,(strEx))
	conn.commit()
	exObj = myNode.wordNode(strEx.upper(),"Exclamation")
	return exObj

def getArticle():
	query = "SELECT COUNT(*) FROM Articles;"
	cur.execute(query)
	countRows = cur.fetchone()[0]
	conn.commit()
	artIndex = random.randint(1,countRows)
	query = "SELECT word FROM Articles WHERE id=%s;"
	cur.execute(query,(artIndex))
	strArt = cur.fetchone()[0]
	conn.commit()
	query = "UPDATE Articles SET frequency = frequency + 1 WHERE word=%s;"
	cur.execute(query,(strArt))
	conn.commit()
	articleObj = myNode.wordNode(strArt,"Articles")
	return articleObj

def getAdjective(prevNum, art):
	howToContinue = random.randint(1,3)

	if howToContinue == 1:
		query = "SELECT COUNT(*) FROM Adjective;"
		cur.execute(query)
		countRows = cur.fetchone()[0]
		conn.commit()
		while 1:
			adjIndex = random.randint(1,countRows)
			query = "SELECT word FROM Adjective WHERE id=%s;"
			cur.execute(query,(adjIndex))
			strAdj = cur.fetchone()[0]
			conn.commit()
			if art == "an":
				if strAdj[:0] in listVowels:
					query = "UPDATE Adjective SET frequency = frequency + 1 WHERE word=%s;"
					cur.execute(query,(strAdj))
					conn.commit()
					break
				else:
					continue
			else:
				query = "UPDATE Adjective SET frequency = frequency + 1 WHERE word=%s;"
				cur.execute(query,(strAdj))
				conn.commit()
				break
		adjObj = myNode.wordNode(strAdj,"Adjective")
		return adjObj
	#elif howToContinue == 3 and prevNum != 0:
	#	return getConjunction() + " " + getAdjective(howToContinue,art)
	else:
		adjObj = myNode.wordNode("","Adjective")
		return adjObj

def getConjunction():
	query = "SELECT COUNT(*) FROM Conjunction;"
	cur.execute(query)
	countRows = cur.fetchone()[0]
	conn.commit()
	conIndex = random.randint(1,countRows)
	query = "SELECT word FROM Conjunction WHERE id=%s;"
	cur.execute(query,(conIndex))
	strCon = cur.fetchone()[0]
	conn.commit()
	query = "UPDATE Conjunction SET frequency = frequency + 1 WHERE word=%s;"
	cur.execute(query,(strCon))
	conn.commit()
	conObj = myNode.wordNode(strCon,"Conjunction")
	return conObj

def getPreposition():
	query = "SELECT COUNT(*) FROM Prepositions;"
	cur.execute(query)
	countRows = cur.fetchone()[0]
	conn.commit()
	conIndex = random.randint(1,countRows)
	query = "SELECT word FROM Prepositions WHERE id=%s;"
	cur.execute(query,(conIndex))
	strprep = cur.fetchone()[0]
	conn.commit()
	query = "UPDATE Prepositions SET frequency = frequency + 1 WHERE word=%s;"
	cur.execute(query,(strprep))
	conn.commit()
	prepObj = myNode.wordNode(strprep,"Prepositions")
	return prepObj

def getNoun(isPlural,typesToUse,art):
	#normalOrProper = random.randint(1,2)
	strn = ""
	if art == "a" or art == "an":
		query = "SELECT COUNT(*) FROM Nouns;"
		cur.execute(query)
		countRows = cur.fetchone()[0]
		conn.commit()

		firstChar = 'a'
		if art == 'a':
			while firstChar in listVowels:
				nounIndex = random.randint(1,countRows)
				query = "SELECT type FROM Nouns WHERE id=%s;"
				cur.execute(query,(nounIndex))
				typeName = cur.fetchone()[0]
				conn.commit()
				query = "SELECT isPlural FROM Nouns WHERE id=%s;"
				cur.execute(query,(nounIndex))
				selectIsPlural = cur.fetchone()[0]
				conn.commit()
				if typeName in typesToUse and selectIsPlural == isPlural:
					query = "SELECT word FROM Nouns WHERE id=%s;"
					cur.execute(query,(nounIndex))
					strn = cur.fetchone()[0]
					firstChar = strn[0]
		else:
			firstChar = 'c'
			while firstChar not in listVowels:
				nounIndex = random.randint(1,countRows)
				query = "SELECT type FROM Nouns WHERE id=%s;"
				cur.execute(query,(nounIndex))
				typeName = cur.fetchone()[0]
				conn.commit()
				query = "SELECT isPlural FROM Nouns WHERE id=%s;"
				cur.execute(query,(nounIndex))
				selectIsPlural = cur.fetchone()[0]
				conn.commit()
				if typeName in typesToUse and selectIsPlural == isPlural:
					query = "SELECT word FROM Nouns WHERE id=%s;"
					cur.execute(query,(nounIndex))
					strn = cur.fetchone()[0]
					firstChar = strn[0]
				
		query = "UPDATE Nouns SET frequency = frequency + 1 WHERE word=%s;"
		cur.execute(query,(strn))
		conn.commit()	
		nObj = myNode.wordNode(strn,"Nouns")
		return nObj

	else:#if normalOrProper == 1:
		query = "SELECT COUNT(*) FROM Nouns;"
		cur.execute(query)
		countRows = cur.fetchone()[0]
		conn.commit()
		while 1:
			nounIndex = random.randint(1,countRows)
			query = "SELECT type FROM Nouns WHERE id=%s;"
			cur.execute(query,(nounIndex))
			typeName = cur.fetchone()[0]
			conn.commit()
			query = "SELECT isPlural FROM Nouns WHERE id=%s;"
			cur.execute(query,(nounIndex))
			selectIsPlural = cur.fetchone()[0]
			conn.commit()
			if typeName in typesToUse and selectIsPlural == isPlural:
				query = "SELECT word FROM Nouns WHERE id=%s;"
				cur.execute(query,(nounIndex))
				strn = cur.fetchone()[0]
				conn.commit()
				query = "UPDATE Nouns SET frequency = frequency + 1 WHERE word=%s;"
				cur.execute(query,(strn))
				conn.commit()
				break
		nObj = myNode.wordNode(strn,"Nouns")
		return nObj
	#else:
	#	query = "SELECT COUNT(*) FROM ProperNouns;"
	#	cur.execute(query)
	#	countRows = cur.fetchone()[0]
	#	conn.commit()
	#	while 1:
	#		nounIndex = random.randint(1,countRows)
	#		query = "SELECT type FROM ProperNouns WHERE id=%s;"
	#		cur.execute(query,(nounIndex))
	#		typeName = cur.fetchone()[0]
	#		if typeName in typesToUse:
	#			query = "SELECT word FROM ProperNouns WHERE id=%s;"
	#			cur.execute(query,(nounIndex))
	#			strn = cur.fetchone()[0]
	#			conn.commit()
	#			query = "UPDATE ProperNouns SET frequency = frequency + 1 WHERE word=%s;"
	#			cur.execute(query,(strn))
	#			conn.commit()
	#			break
	#	nObj = myNode.wordNode(strn.title(),"ProperNouns")
	#	return nObj


def getVerb(verbL, tense):
	strv = ""
	query = "SELECT COUNT(*) FROM Verbs;"
	cur.execute(query)
	countRows = cur.fetchone()[0]
	conn.commit()
	if tense is None:
		tenseLen = len(ParagraphQueue.paragraph)
		while tenseLen > 1 and tense is None:
			tenseLen -= 1
			tense = ParagraphQueue.paragraph[tenseLen-1].tense
		if tense is None:
			tense = "past"

	while 1:
		vIndex = random.randint(1,countRows)
		query = "SELECT type FROM Verbs WHERE id=%s;"
		cur.execute(query,(vIndex))
		typeName = cur.fetchone()[0]
		conn.commit()
		query = "SELECT tense FROM Verbs WHERE id=%s;"
		cur.execute(query,(vIndex))
		selectTense = cur.fetchone()[0]
		conn.commit()
		if typeName in verbL and tense == selectTense:
			query = "SELECT word FROM Verbs WHERE id=%s;"
			cur.execute(query,(vIndex))
			strv = cur.fetchone()[0]
			conn.commit()
			query = "UPDATE Verbs SET frequency = frequency + 1 WHERE word=%s;"
			cur.execute(query,(strv))
			conn.commit()
			break
		
	vObj = myNode.wordNode(strv,"Verbs")
	return vObj










#*****************************
#*  Functions for insertions *
#*****************************
def insertNouns():
	userInput3 = raw_input("Enter the noun you wish to be in the database: ")
	userInput3 = userInput3.lower()
	userInput4 = raw_input("Is this noun a person, place, thing, or idea? ")
	userInput4 = userInput4.lower()
	while 1:
		if userInput4 in listNoun:
			break
		else:
			userInput4 = raw_input("Incorrect Input. A noun can only be a person, place, thing, or idea: ")
			userInput4 = userInput4.lower()
	userInput5 = raw_input("Is this noun in plural form? Yes or no? ")
	userInput5 = userInput5.lower()
	while 1:
		if userInput5 in listYesorNo:
			break
		else:
			userInput5 = raw_input("Incorrect Input. Please answer yes or no: ")
			userInput5 = userInput5.lower()
	print "\n"
	cur.execute("INSERT INTO Nouns (word,type,frequency,isPlural) SELECT * FROM (SELECT %s,%s,0,%s) AS tmp WHERE NOT EXISTS (SELECT word FROM Nouns WHERE word = %s)LIMIT 1;",(userInput3,userInput4,userInput5,userInput3))
	conn.commit()

def insertProperNouns():
	userInput3 = raw_input("Enter the proper noun you wish to be in the database: ")
	userInput3 = userInput3.lower()
	userInput4 = raw_input("Is this proper noun a person, place, thing, or idea? ")
	userInput4 = userInput4.lower()
	while 1:
		if userInput4 in listNoun:
			break
		else:
			userInput4 = raw_input("Incorrect Input. A noun can only be a person, place, thing, or idea: ")
			userInput4 = userInput4.lower()
	print "\n"
	cur.execute("INSERT INTO ProperNouns (word,type,frequency) SELECT * FROM (SELECT %s,%s,0) AS tmp WHERE NOT EXISTS (SELECT word FROM ProperNouns WHERE word = %s)LIMIT 1;",(userInput3,userInput4,userInput3))
	conn.commit()

def insertPronouns():
	userInput3 = raw_input("Enter the pronoun you wish to be in the database: ")
	userInput3 = userInput3.lower()
	userInput4 = raw_input("Is this pronoun subjective, objective, reflexive, or possessive? ")
	userInput4 = userInput4.lower()
	while 1:
		if userInput4 in listPronoun:
			break
		else:
			userInput4 = raw_input("Incorrect Input. A pronoun can only be subjective, objective, reflexive, or possessive: ")
			userInput4 = userInput4.lower()
	print "\n"
	cur.execute("INSERT INTO Pronoun (word,type,frequency) SELECT * FROM (SELECT %s,%s,0) AS tmp WHERE NOT EXISTS (SELECT word FROM Pronoun WHERE word = %s)LIMIT 1;",(userInput3,userInput4,userInput3))
	conn.commit()

def insertArticles():
	userInput3 = raw_input("Enter the article you wish to be in the database: ")
	userInput3 = userInput3.lower()
	userInput4 = raw_input("Is this definite or indefinite? ")
	userInput4 = userInput4.lower()
	while 1:
		if userInput4 in listArticles:
			cur.execute("INSERT INTO Articles (word,type,frequency) SELECT * FROM (SELECT %s,%s,0) AS tmp WHERE NOT EXISTS (SELECT word FROM Articles WHERE word = %s)LIMIT 1;",(userInput3,userInput4,userInput3))
			conn.commit()
			break
		else:
			userInput4 = raw_input("Incorrect Input. An article can only be definite or indefinite: ")
			userInput4 = userInput4.lower()
	print "\n"

def insertVerbs():
	userInput3 = raw_input("Enter the verb you wish to be in the database: ")
	userInput3 = userInput3.lower()
	userInput4 = raw_input("Is this an action, event, situation, or change? ")
	userInput4 = userInput4.lower()
	while 1:
		if userInput4 in listVerbs:
			break
		else:
			userInput4 = raw_input("Incorrect Input. A verb is defined as an action, event, situation, or change: ")
			userInput4 = userInput4.lower()
	userInput5 = raw_input("Is this verb in present or past tense? ")
	userInput5 = userInput5.lower()
	while 1:
		if userInput5 in listVerbTense:
			cur.execute("INSERT INTO Verbs (word,type,frequency,tense) SELECT * FROM (SELECT %s,%s,0,%s) AS tmp WHERE NOT EXISTS (SELECT word FROM Verbs WHERE word = %s)LIMIT 1;",(userInput3,userInput4,userInput5,userInput3))
			conn.commit()
			break
		else:
			userInput5 = raw_input("Incorrect Input. A verb itself can be in past or present tense: ")
			userInput5 = userInput5.lower()	
	print "\n"

def insertAdjectives():
	userInput3 = raw_input("Enter the adjective you wish to be in the database: ")
	userInput3 = userInput3.lower()
	cur.execute("INSERT INTO Adjective (word,frequency) SELECT * FROM (SELECT %s,0) AS tmp WHERE NOT EXISTS (SELECT word FROM Adjective WHERE word = %s)LIMIT 1;",(userInput3,userInput3))
	conn.commit()
	print "\n"

def insertAdverbs():
	userInput3 = raw_input("Enter the adverb you wish to be in the database: ")
	userInput3 = userInput3.lower()
	cur.execute("INSERT INTO Adverb (word,frequency) SELECT * FROM (SELECT %s,0) AS tmp WHERE NOT EXISTS (SELECT word FROM Adverb WHERE word = %s)LIMIT 1;",(userInput3,userInput3))
	conn.commit()
	print "\n"

def insertConjunctions():
	userInput3 = raw_input("Enter the conjunction you wish to be in the database: ")
	userInput3 = userInput3.lower()
	cur.execute("INSERT INTO Conjunction (word,frequency) SELECT * FROM (SELECT %s,0) AS tmp WHERE NOT EXISTS (SELECT word FROM Conjunction WHERE word = %s)LIMIT 1;",(userInput3,userInput3))
	conn.commit()
	print "\n"

def insertExclamations():
	userInput3 = raw_input("Enter the exclamation you wish to be in the database: ")
	userInput3 = userInput3.lower()
	cur.execute("INSERT INTO Exclamation (word,frequency) SELECT * FROM (SELECT %s,0) AS tmp WHERE NOT EXISTS (SELECT word FROM Exclamation WHERE word = %s)LIMIT 1;",(userInput3,userInput3))
	conn.commit()
	print "\n"

def insertPrepositions():
	userInput3 = raw_input("Enter the preposition you wish to be in the database: ")
	userInput3 = userInput3.lower()
	cur.execute("INSERT INTO Prepositions (word,frequency) SELECT * FROM (SELECT %s,0) AS tmp WHERE NOT EXISTS (SELECT word FROM Prepositions WHERE word = %s)LIMIT 1;",(userInput3,userInput3))
	conn.commit()
	print "\n"

def insertPhrases():
	userInput3 = raw_input("Enter the opening phrase you wish to be in the database: ")
	userInput3 = userInput3.lower()
	userInput4 = raw_input("Is this phrase in present or past tense? ")
	userInput4 = userInput4.lower()
	while 1:
		if userInput4 in listVerbTense:
			cur.execute("INSERT INTO OpeningPhrases (phrase,frequency,tense) SELECT * FROM (SELECT %s,0,%s) AS tmp WHERE NOT EXISTS (SELECT phrase FROM OpeningPhrases WHERE phrase = %s)LIMIT 1;",(userInput3,userInput4,userInput3))
			conn.commit()
			break
		else:
			userInput4 = raw_input("Incorrect Input. The phrase has to be in past or present tense: ")
			userInput4 = userInput4.lower()		
	conn.commit()
	print "\n"

	





#*********
#* Main  *
#*********
dict = {'insert':insertionFunc, 'generate':generateFunc, 'view':viewRecordsFunc}
dict2 = {'nouns':insertNouns,'proper nouns':insertProperNouns,'pronouns':insertPronouns,'articles':insertArticles,'verbs':insertVerbs,'adverbs':insertAdverbs,'conjunctions':insertConjunctions,'prepositions':insertPrepositions, 'exclamations':insertExclamations,'adjectives':insertAdjectives,'opening phrases':insertPhrases}
options = ['insert','view','generate']
listNoun = ['person','place','thing','idea']
listPronoun = ['subjective','objective','reflexive','possessive']
listArticles = ['definite','indefinite']
listVerbs = ['action','event','situation','change']
listVerbTense = ['present','past']
listVowels = ['a','i','e','o','u']
listYesorNo = ['yes','no']
listTables = ['Nouns','Adjective','Adverb','Articles','Conjunction','Exclamation','OpeningPhrases','Prepositions','Pronoun','ProperNouns','Verbs']
ParagraphQueue = myQueue.wordQueue()

conn = pymysql.connect(host='localhost',port=3306,user='user1',password='password',db='contextFreeGrammar')
cur = conn.cursor()
userInput = raw_input("Welcome to the Context-Sensitive Grammar Story Generator, where everyone's story is unique!\nWould you like to insert words into the database, view records, or generate a story?[insert/view/generate]: ")
userInput = userInput.lower()
while 1:
	if userInput in options:
		dict[userInput]()
		userInput = raw_input("Would you like to insert words into the database, view records, or generate a story?[insert/view/generate]: ")
		userInput = userInput.lower()
	else:
		userInput = raw_input("Incorrect Input [insert/view/generate]: ")

cur.close()
conn.close()
