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
	if strFin[len(strFin)-1] != '.':
		strFin += "."
	strFin = strFin.replace("    "," ")
	strFin = strFin.replace("   "," ")
	strFin = strFin.replace("  "," ")
	strFin = strFin.replace(" .",".")
	print strFin








#***********************************************
#*  Recursive functions for contextual states  *
#***********************************************
def genStart(characterName,maxLen):
	if maxLen == 0:
		return

	howToContinue = random.randint(2,3)
	queueLen = len(ParagraphQueue.paragraph)
	
	if howToContinue == 1:
		exObj = getExclamation()
		exObj.word += "! Sorry, that was strange, anyway "
		ParagraphQueue.enqueue(exObj)
		genStart(characterName,maxLen)
	elif howToContinue == 2:
		artObj = getArticle()
		ParagraphQueue.enqueue(artObj)
		genS1(characterName,maxLen)
	elif howToContinue == 3:
		nObj = getNoun("yes","",True)
		ParagraphQueue.enqueue(nObj)
		if findMyLastPrep(queueLen,"word") is None:
			genS2(characterName,maxLen)
		else:
			genS5(characterName,maxLen)
	return
			

def genS1(characterName, maxLen):
	if maxLen == 0:
		return

	catToIf = random.randint(1,2)
	queueLen = len(ParagraphQueue.paragraph)
	lastArticle = findMyLastArticle(queueLen)
	#print "Last Article: ",lastArticle

	if catToIf == 1:
		if lastArticle == "the":
			randElement = random.randint(1,2)
			if randElement == 1:
				nObj = getNoun("yes",lastArticle,False)		
				ParagraphQueue.enqueue(nObj)
				if findMyLastPrep(queueLen,"word") is None:
					genS2(characterName,maxLen)
				else:
					genS5(characterName,maxLen)
			elif randElement == 2:
				nObj = getNoun("no",lastArticle,False)
				ParagraphQueue.enqueue(nObj)
				if findMyLastPrep(queueLen,"word") is None:
					genS2(characterName,maxLen)
				else:
					genS5(characterName,maxLen)
		else:
			nObj = getNoun("no",lastArticle,False)
			ParagraphQueue.enqueue(nObj)
			if findMyLastPrep(queueLen,"word") is None:
				genS2(characterName,maxLen)
			else:
				genS5(characterName,maxLen)

	elif catToIf == 2:
		adjObj = getAdjective(lastArticle)
		if queueLen > 1:
			if ParagraphQueue.paragraph[queueLen-1].word is adjObj.word:
				genS1(characterName,maxLen)
				return
		ParagraphQueue.enqueue(adjObj)
		genS1(characterName,maxLen)

	elif catToIf == ".":
		maxLen -= 1
		periodObj = myNode.wordNode(".",None)
		ParagraphQueue.enqueue(periodObj)

	return


def genS2(characterName, maxLen):
	if maxLen == 0:
		return

	queueLen = len(ParagraphQueue.paragraph)
	vObj = getVerb(False, ParagraphQueue.paragraph[0].tense)
	bShouldIAddAnS = findMyLastNounPlural(queueLen)
	if bShouldIAddAnS is True and ParagraphQueue.paragraph[0].tense == "present":
		vObj.word += "s"
	ParagraphQueue.enqueue(vObj)
	genS3(characterName, maxLen)
	return
	

def genS3(characterName, maxLen):
	if maxLen == 0:
		return
	genRand = random.randint(1,2)

	if genRand == 1:
		prepObj = getPreposition()
		ParagraphQueue.enqueue(prepObj)
		genStart(characterName, maxLen)
	elif genRand == 2:
		adverbObj = getAdverb()
		ParagraphQueue.enqueue(adverbObj)
		prepObj = getPreposition()
		ParagraphQueue.enqueue(prepObj)
		genStart(characterName, maxLen)
	return


def genS4(characterName, maxLen):
	if maxLen == 0:
		return
	genRand = random.randint(1,2)
	if genRand == 1:
		conObj = getConjunction()
		ParagraphQueue.enqueue(conObj)
		genStart(characterName, maxLen)
	elif genRand == 2:
		maxLen -= 1
		periodObj = myNode.wordNode(".",None)
		ParagraphQueue.enqueue(periodObj)
	return


def genS5(characterName,maxLen):
	if maxLen == 0:
		return

	queueLen = len(ParagraphQueue.paragraph)
	myPrep = findMyLastPrep(queueLen,"cat")

	if myPrep is not None:
		if myPrep == "instruments":
			genRand = 2
		else:
			genRand = random.randint(1,2)
	else:
		genRand = random.randint(1,2)

	if genRand == 1:
		maxLen -= 1
		periodObj = myNode.wordNode(".",None)
		ParagraphQueue.enqueue(periodObj)
	elif genRand == 2:
		prepObj = getPreposition()
		ParagraphQueue.enqueue(prepObj)
		genStart(characterName, maxLen)
	return


def findMyLastArticle(queueLen):
	while queueLen > 0:
		if ParagraphQueue.paragraph[queueLen-1].category == "Articles":
			return ParagraphQueue.paragraph[queueLen-1].word
		queueLen -= 1
	return None


def findMyLastNounPlural(queueLen):
	while queueLen > 0:
		if ParagraphQueue.paragraph[queueLen-1].category == "Nouns" or ParagraphQueue.paragraph[queueLen-1].category == "ProperNouns":
			if ParagraphQueue.paragraph[queueLen-1].category == "ProperNouns" or ParagraphQueue.paragraph[queueLen-1].isPlural == False:
				return True
			else:
				return False
		queueLen -= 1
	return False

def findMyLastPrep(queueLen,wordOrCategory):
	while queueLen > 0:
		if ParagraphQueue.paragraph[queueLen-1].category == "Prepositions":
			if wordOrCategory == "word":
				return ParagraphQueue.paragraph[queueLen-1].word
			else:
				return ParagraphQueue.paragraph[queueLen-1].type
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

def getAdjective(art):
	howToContinue = random.randint(1,3)

	if howToContinue == 1:
		if art == "an":
			query = "SELECT COUNT(word) FROM Adjective WHERE LEFT(word,1) = 'a' OR LEFT(word,1) = 'i' OR LEFT(word,1) = 'e' OR LEFT(word,1) = 'o' OR LEFT(word,1) = 'u';"
			cur.execute(query)
			countRows = cur.fetchone()[0]
			conn.commit()
			adjIndex = random.randint(0,countRows-1)
			query = "SELECT word FROM Adjective WHERE LEFT(word,1) = 'a' OR LEFT(word,1) = 'i' OR LEFT(word,1) = 'e' OR LEFT(word,1) = 'o' OR LEFT(word,1) = 'u' ORDER BY word DESC LIMIT 1 OFFSET %s;"
			cur.execute(query,(adjIndex))
			strAdj = cur.fetchone()[0]
			conn.commit()
		elif art == "a":
			query = "SELECT COUNT(word) FROM Adjective WHERE LEFT(word,1) != 'a' OR LEFT(word,1) != 'i' OR LEFT(word,1) != 'e' OR LEFT(word,1) != 'o' OR LEFT(word,1) != 'u';"
			cur.execute(query)
			countRows = cur.fetchone()[0]
			conn.commit()
			adjIndex = random.randint(0,countRows-1)
			query = "SELECT word FROM Adjective WHERE LEFT(word,1) != 'a' AND LEFT(word,1) != 'i' AND LEFT(word,1) != 'e' AND LEFT(word,1) != 'o' AND LEFT(word,1) != 'u' ORDER BY word DESC LIMIT 1 OFFSET %s;"
			cur.execute(query,(adjIndex))
			strAdj = cur.fetchone()[0]
			conn.commit()
		else:
			query = "SELECT COUNT(word) FROM Adjective"
			cur.execute(query)
			countRows = cur.fetchone()[0]
			conn.commit()
			adjIndex = random.randint(0,countRows-1)
			query = "SELECT word FROM Adjective ORDER BY word DESC LIMIT 1 OFFSET %s;"
			cur.execute(query,(adjIndex))
			strAdj = cur.fetchone()[0]
			conn.commit()
		query = "UPDATE Adjective SET frequency = frequency + 1 WHERE word=%s;"
		cur.execute(query,(strAdj))
		conn.commit()
		adjObj = myNode.wordNode(strAdj,"Adjective")
		return adjObj
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

def getNoun(isPlural,art,isProper):
	strn = ""
	queueLen = len(ParagraphQueue.paragraph)
	myPrep = findMyLastPrep(queueLen,"cat")
	if isProper is False:
		if art == "a":
			if myPrep is not None:
				if myPrep == "time":
					query = "SELECT COUNT(word) FROM Nouns WHERE (LEFT(word,1) != 'a' AND LEFT(word,1) != 'i' AND LEFT(word,1) != 'e' AND LEFT(word,1) != 'o' AND LEFT(word,1) != 'u') AND isPlural = %s AND type = 'idea';"
					cur.execute(query,(isPlural))
					countRows = cur.fetchone()[0]
					conn.commit()
					nounIndex = random.randint(0,countRows-1)
					query = "SELECT word FROM Nouns WHERE (LEFT(word,1) != 'a' AND LEFT(word,1) != 'i' AND LEFT(word,1) != 'e' AND LEFT(word,1) != 'o' AND LEFT(word,1) != 'u') AND isPlural = %s AND type = 'idea' ORDER BY word DESC LIMIT 1 OFFSET %s;"
				elif myPrep == "place" or myPrep == "direction":
					query = "SELECT COUNT(word) FROM Nouns WHERE (LEFT(word,1) != 'a' AND LEFT(word,1) != 'i' AND LEFT(word,1) != 'e' AND LEFT(word,1) != 'o' AND LEFT(word,1) != 'u') AND isPlural = %s AND type = 'place';"
					cur.execute(query,(isPlural))
					countRows = cur.fetchone()[0]
					conn.commit()
					nounIndex = random.randint(0,countRows-1)
					query = "SELECT word FROM Nouns WHERE (LEFT(word,1) != 'a' AND LEFT(word,1) != 'i' AND LEFT(word,1) != 'e' AND LEFT(word,1) != 'o' AND LEFT(word,1) != 'u') AND isPlural = %s AND type = 'place' ORDER BY word DESC LIMIT 1 OFFSET %s;"
				elif myPrep == "agent":
					query = "SELECT COUNT(word) FROM Nouns WHERE (LEFT(word,1) != 'a' AND LEFT(word,1) != 'i' AND LEFT(word,1) != 'e' AND LEFT(word,1) != 'o' AND LEFT(word,1) != 'u') AND isPlural = %s AND type = 'person';"
					cur.execute(query,(isPlural))
					countRows = cur.fetchone()[0]
					conn.commit()
					nounIndex = random.randint(0,countRows-1)
					query = "SELECT word FROM Nouns WHERE (LEFT(word,1) != 'a' AND LEFT(word,1) != 'i' AND LEFT(word,1) != 'e' AND LEFT(word,1) != 'o' AND LEFT(word,1) != 'u') AND isPlural = %s AND type = 'person' ORDER BY word DESC LIMIT 1 OFFSET %s;"
				elif myPrep == "instruments":
					query = "SELECT COUNT(word) FROM Nouns WHERE (LEFT(word,1) != 'a' AND LEFT(word,1) != 'i' AND LEFT(word,1) != 'e' AND LEFT(word,1) != 'o' AND LEFT(word,1) != 'u') AND isPlural = %s AND type = 'thing';"
					cur.execute(query,(isPlural))
					countRows = cur.fetchone()[0]
					conn.commit()
					nounIndex = random.randint(0,countRows-1)
					query = "SELECT word FROM Nouns WHERE (LEFT(word,1) != 'a' AND LEFT(word,1) != 'i' AND LEFT(word,1) != 'e' AND LEFT(word,1) != 'o' AND LEFT(word,1) != 'u') AND isPlural = %s AND type = 'thing' ORDER BY word DESC LIMIT 1 OFFSET %s;"
			else:
				query = "SELECT COUNT(word) FROM Nouns WHERE (LEFT(word,1) != 'a' AND LEFT(word,1) != 'i' AND LEFT(word,1) != 'e' AND LEFT(word,1) != 'o' AND LEFT(word,1) != 'u') AND isPlural = %s;"
				cur.execute(query,(isPlural))
				countRows = cur.fetchone()[0]
				conn.commit()
				nounIndex = random.randint(0,countRows-1)
				query = "SELECT word FROM Nouns WHERE (LEFT(word,1) != 'a' AND LEFT(word,1) != 'i' AND LEFT(word,1) != 'e' AND LEFT(word,1) != 'o' AND LEFT(word,1) != 'u') AND isPlural = %s ORDER BY word DESC LIMIT 1 OFFSET %s;"
			#print "Query 1: ",query
			cur.execute(query,(isPlural,nounIndex))
			strn = cur.fetchone()[0]
		elif art == "an":
			if myPrep is not None:
				if myPrep == "time":
					query = "SELECT COUNT(word) FROM Nouns WHERE (LEFT(word,1) = 'a' OR LEFT(word,1) = 'i' OR LEFT(word,1) = 'e' OR LEFT(word,1) = 'o' OR LEFT(word,1) = 'u') AND isPlural = %s AND type = 'idea';"
					cur.execute(query,(isPlural))
					countRows = cur.fetchone()[0]
					conn.commit()
					nounIndex = random.randint(0,countRows-1)
					query = "SELECT word FROM Nouns WHERE (LEFT(word,1) = 'a' OR LEFT(word,1) = 'i' OR LEFT(word,1) = 'e' OR LEFT(word,1) = 'o' OR LEFT(word,1) = 'u') AND isPlural = %s AND type = 'idea' ORDER BY word DESC LIMIT 1 OFFSET %s;"
				elif myPrep == "place" or myPrep == "direction":
					query = "SELECT COUNT(word) FROM Nouns WHERE (LEFT(word,1) = 'a' OR LEFT(word,1) = 'i' OR LEFT(word,1) = 'e' OR LEFT(word,1) = 'o' OR LEFT(word,1) = 'u') AND isPlural = %s AND type = 'place';"
					cur.execute(query,(isPlural))
					countRows = cur.fetchone()[0]
					conn.commit()
					nounIndex = random.randint(0,countRows-1)
					query = "SELECT word FROM Nouns WHERE (LEFT(word,1) = 'a' OR LEFT(word,1) = 'i' OR LEFT(word,1) = 'e' OR LEFT(word,1) = 'o' OR LEFT(word,1) = 'u') AND isPlural = %s AND type = 'place' ORDER BY word DESC LIMIT 1 OFFSET %s;"
				elif myPrep == "agent":
					query = "SELECT COUNT(word) FROM Nouns WHERE (LEFT(word,1) = 'a' OR LEFT(word,1) = 'i' OR LEFT(word,1) = 'e' OR LEFT(word,1) = 'o' OR LEFT(word,1) = 'u') AND isPlural = %s AND type = 'person';"
					cur.execute(query,(isPlural))
					countRows = cur.fetchone()[0]
					conn.commit()
					nounIndex = random.randint(0,countRows-1)
					query = "SELECT word FROM Nouns WHERE (LEFT(word,1) = 'a' OR LEFT(word,1) = 'i' OR LEFT(word,1) = 'e' OR LEFT(word,1) = 'o' OR LEFT(word,1) = 'u') AND isPlural = %s AND type = 'person' ORDER BY word DESC LIMIT 1 OFFSET %s;"
				elif myPrep == "instruments":
					query = "SELECT COUNT(word) FROM Nouns WHERE (LEFT(word,1) = 'a' OR LEFT(word,1) = 'i' OR LEFT(word,1) = 'e' OR LEFT(word,1) = 'o' OR LEFT(word,1) = 'u') AND isPlural = %s AND type = 'thing';"
					cur.execute(query,(isPlural))
					countRows = cur.fetchone()[0]
					conn.commit()
					nounIndex = random.randint(0,countRows-1)
					query = "SELECT word FROM Nouns WHERE (LEFT(word,1) = 'a' OR LEFT(word,1) = 'i' OR LEFT(word,1) = 'e' OR LEFT(word,1) = 'o' OR LEFT(word,1) = 'u') AND isPlural = %s AND type = 'thing' ORDER BY word DESC LIMIT 1 OFFSET %s;"
			else:
				query = "SELECT COUNT(word) FROM Nouns WHERE (LEFT(word,1) = 'a' OR LEFT(word,1) = 'i' OR LEFT(word,1) = 'e' OR LEFT(word,1) = 'o' OR LEFT(word,1) = 'u') AND isPlural = %s;"
				cur.execute(query,(isPlural))
				countRows = cur.fetchone()[0]
				conn.commit()
				nounIndex = random.randint(0,countRows-1)
				query = "SELECT word FROM Nouns WHERE (LEFT(word,1) = 'a' OR LEFT(word,1) = 'i' OR LEFT(word,1) = 'e' OR LEFT(word,1) = 'o' OR LEFT(word,1) = 'u') AND isPlural = %s ORDER BY word DESC LIMIT 1 OFFSET %s;"
			#print "Query 2: ",query
			cur.execute(query,(isPlural,nounIndex))
			strn = cur.fetchone()[0]
		else:
			if myPrep is not None:
				if myPrep == "time":
					query = "SELECT COUNT(word) FROM Nouns WHERE isPlural = %s AND type = 'idea';"
					cur.execute(query,(isPlural))
					countRows = cur.fetchone()[0]
					conn.commit()
					nounIndex = random.randint(0,countRows-1)
					query = "SELECT word FROM Nouns WHERE isPlural = %s AND type = 'idea' ORDER BY word DESC LIMIT 1 OFFSET %s;"
				elif myPrep == "place" or myPrep == "direction":
					query = "SELECT COUNT(word) FROM Nouns WHERE isPlural = %s AND type = 'place';"
					cur.execute(query,(isPlural))
					countRows = cur.fetchone()[0]
					conn.commit()
					nounIndex = random.randint(0,countRows-1)
					query = "SELECT word FROM Nouns WHERE isPlural = %s AND type = 'place' ORDER BY word DESC LIMIT 1 OFFSET %s;"
				elif myPrep == "agent":
					query = "SELECT COUNT(word) FROM Nouns WHERE isPlural = %s AND type = 'person';"
					cur.execute(query,(isPlural))
					countRows = cur.fetchone()[0]
					conn.commit()
					nounIndex = random.randint(0,countRows-1)
					query = "SELECT word FROM Nouns WHERE isPlural = %s AND type = 'person' ORDER BY word DESC LIMIT 1 OFFSET %s;"
				elif myPrep == "instruments":
					query = "SELECT COUNT(word) FROM Nouns WHERE isPlural = %s AND type = 'thing';"
					cur.execute(query,(isPlural))
					countRows = cur.fetchone()[0]
					conn.commit()
					nounIndex = random.randint(0,countRows-1)
					query = "SELECT word FROM Nouns WHERE isPlural = %s AND type = 'thing' ORDER BY word DESC LIMIT 1 OFFSET %s;"
			else:
				query = "SELECT COUNT(word) FROM Nouns WHERE isPlural = %s;"
				cur.execute(query,(isPlural))
				countRows = cur.fetchone()[0]
				conn.commit()
				nounIndex = random.randint(0,countRows-1)
				query = "SELECT word FROM Nouns WHERE isPlural = %s ORDER BY word DESC LIMIT 1 OFFSET %s;"
			#print "Query 3: ",query
			cur.execute(query,(isPlural,nounIndex))
			strn = cur.fetchone()[0]
		query = "UPDATE Nouns SET frequency = frequency + 1 WHERE word=%s;"
		cur.execute(query,(strn))
		conn.commit()
		nObj = myNode.wordNode(strn,"Nouns")
		return nObj
	else:
		if myPrep is not None:
			if myPrep == "time":
				query = "SELECT COUNT(word) FROM ProperNouns WHERE type = 'idea';"
				cur.execute(query)
				countRows = cur.fetchone()[0]
				conn.commit()
				nounIndex = random.randint(0,countRows-1)
				query = "SELECT word FROM ProperNouns WHERE type = 'idea' ORDER BY word DESC LIMIT 1 OFFSET %s;"
			elif myPrep == "place" or myPrep == "direction":
				query = "SELECT COUNT(word) FROM ProperNouns WHERE type = 'place';"
				cur.execute(query)
				countRows = cur.fetchone()[0]
				conn.commit()
				nounIndex = random.randint(0,countRows-1)
				query = "SELECT word FROM ProperNouns WHERE type = 'place' ORDER BY word DESC LIMIT 1 OFFSET %s;"
			elif myPrep == "agent":
				query = "SELECT COUNT(word) FROM ProperNouns WHERE type = 'person';"
				cur.execute(query)
				countRows = cur.fetchone()[0]
				conn.commit()
				nounIndex = random.randint(0,countRows-1)
				query = "SELECT word FROM ProperNouns WHERE type = 'person' ORDER BY word DESC LIMIT 1 OFFSET %s;"
			elif myPrep == "instruments":
				query = "SELECT COUNT(word) FROM ProperNouns WHERE type = 'thing';"
				cur.execute(query)
				countRows = cur.fetchone()[0]
				conn.commit()
				nounIndex = random.randint(0,countRows-1)
				query = "SELECT word FROM ProperNouns WHERE type = 'thing' ORDER BY word DESC LIMIT 1 OFFSET %s;"
		else:
			query = "SELECT COUNT(word) FROM ProperNouns;"
			cur.execute(query)
			countRows = cur.fetchone()[0]
			conn.commit()
			nounIndex = random.randint(0,countRows-1)
			query = "SELECT word FROM ProperNouns ORDER BY word DESC LIMIT 1 OFFSET %s;"
		#print "Query 4: ",query
		cur.execute(query,(nounIndex))
		strn = cur.fetchone()[0]
		query = "UPDATE ProperNouns SET frequency = frequency + 1 WHERE word=%s;"
		cur.execute(query,(strn))
		conn.commit()
		nObj = myNode.wordNode(strn.title(),"ProperNouns")
		if nObj.kind is not None:
			if nObj.kind == "product":
				if nObj.word[0] in listVowels:
					nObj.word = "an " + nObj.word
				else:
					nObj.word = "a " + nObj.word
			elif nObj.kind == "title":
				randIntro = random.randint(1,2)
				if randIntro == 1:
					nObj.word = "a weird version of " + nObj.word
				else:
					nObj.word = "a copy of " + nObj.word
			elif nObj.kind == "group":
				if nObj.word[len(nObj.word)-1] == 's' and nObj.word.startswith('the ') == False:
					nObj.word = "the " + nObj.word
		return nObj




def getVerb(isSituation, tense):
	if tense is None:
		tenseLen = len(ParagraphQueue.paragraph)
		while tenseLen > 1 and tense is None:
			tenseLen -= 1
			tense = ParagraphQueue.paragraph[tenseLen-1].tense
		if tense is None:
			tense = "past" 
	countRows = 0
	vIndex = 0
	if not isSituation:
		query = "SELECT COUNT(tense) FROM Verbs WHERE tense=%s AND type != 'situation';"
		cur.execute(query,(tense))
		countRows = cur.fetchone()[0]
		conn.commit()
		vIndex = random.randint(0,countRows-1)
		query = "SELECT word FROM Verbs WHERE tense=%s AND type != 'situation' ORDER BY tense DESC LIMIT 1 OFFSET %s;"
	else:
		query = "SELECT COUNT(tense) FROM Verbs WHERE tense=%s AND type = 'situation';"
		cur.execute(query,(tense))
		countRows = cur.fetchone()[0]
		conn.commit()
		vIndex = random.randint(0,countRows-1)
		query = "SELECT word FROM Verbs WHERE tense=%s AND type = 'situation' ORDER BY tense DESC LIMIT 1 OFFSET %s;"

	cur.execute(query,(tense,vIndex))
	strv = cur.fetchone()[0]
	conn.commit()
	query = "UPDATE Verbs SET frequency = frequency + 1 WHERE word=%s;"
	cur.execute(query,(strv))
	conn.commit()
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
			if userInput4 == "thing":
				while 1:
					userInput5 = raw_input("Is this thing a product, title, or group? ")
					userInput5 = userInput5.lower()
					if userInput5 in listThingKinds:
						cur.execute("INSERT INTO ProperNouns (word,type,frequency,kind) SELECT * FROM (SELECT %s,%s,0,%s) AS tmp WHERE NOT EXISTS (SELECT word FROM ProperNouns WHERE word = %s)LIMIT 1;",(userInput3,userInput4,userInput5,userInput3))
						conn.commit()
						print "\n"
						return
			break
		else:
			userInput4 = raw_input("Incorrect Input. A noun can only be a person, place, thing, or idea: ")
			userInput4 = userInput4.lower()
	print "\n"
	cur.execute("INSERT INTO ProperNouns (word,type,frequency,kind) SELECT * FROM (SELECT %s,%s,0,NULL) AS tmp WHERE NOT EXISTS (SELECT word FROM ProperNouns WHERE word = %s)LIMIT 1;",(userInput3,userInput4,userInput3))
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
			break
		else:
			userInput5 = raw_input("Incorrect Input. A verb itself can be in past or present tense: ")
			userInput5 = userInput5.lower()
	userInput6 = raw_input("Does this verb describe a direction, place, time, agent, or instruments? Or None of the above? ")
	userInput6 = userInput6.lower()
	while 1:
		if userInput6 in listPreps or userInput6 == "none":
			if userInput6 == "none":
				userInput6 = "NULL"
			break
		else:
			userInput6 = raw_input("Incorrect Input. Does this verb describe a direction, place, time, agent, or instruments? Or None of the above? ")
			userInput6 = userInput6.lower()
	cur.execute("INSERT INTO Verbs (word,type,frequency,tense,kind) SELECT * FROM (SELECT %s,%s,0,%s,%s) AS tmp WHERE NOT EXISTS (SELECT word FROM Verbs WHERE word = %s)LIMIT 1;",(userInput3,userInput4,userInput5,userInput6,userInput3))
	conn.commit()
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
	userInput4 = raw_input("Is this adverb of type manner, degree, time, frequency, or place? ")
	userInput4 = userInput4.lower()
	while 1:
		if userInput4 in listAdverbs:
			cur.execute("INSERT INTO Adverb (word,type,frequency) SELECT * FROM (SELECT %s,%s,0) AS tmp WHERE NOT EXISTS (SELECT word FROM Prepositions WHERE word = %s)LIMIT 1;",(userInput3,userInput4,userInput3))
			conn.commit()
			break
		else:
			userInput4 = raw_input("Incorrect Input. An adverb must be of type manner, degree, time, frequency, or place: ")
			userInput4 = userInput4.lower()
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
	userInput4 = raw_input("Does it refer to time, place, direction, agent, or instruments? ")
	userInput4 = userInput4.lower()
	while 1:
		if userInput4 in listPreps:
			cur.execute("INSERT INTO Prepositions (word,type,frequency) SELECT * FROM (SELECT %s,%s,0) AS tmp WHERE NOT EXISTS (SELECT word FROM Prepositions WHERE word = %s)LIMIT 1;",(userInput3,userInput4,userInput3))
			conn.commit()
			break
		else:
			userInput4 = raw_input("Incorrect Input. A preposition must refer to a time, place, direction, agent, or instruments: ")
			userInput4 = userInput4.lower()
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
listPreps = ['time','place','direction','agent','instruments','none']
listVerbs = ['action','event','situation','change']
listAdverbs = ['manner','time','place','degree','frequency']
listThingKinds = ['product','title','group']
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
