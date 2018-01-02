import pymysql

class wordNode:
	#tenseList = ['Verbs','OpeningPhrases']
	#typeList = ['Articles','Nouns','Pronoun','ProperNouns','Verbs']

	def __init__(self,word1,category):
		self.word = word1
		self.category = category
		
		conn2 = pymysql.connect(host='localhost',port=3306,user='user1',password='password',db='contextFreeGrammar')
		cur2 = conn2.cursor()

		if category in ['Verbs','OpeningPhrases']:
			try:
				query0 = "SELECT tense FROM ",category," WHERE word=%s;"
				query = ''.join(query0)
				cur2.execute(query,(word1))
				self.tense = cur2.fetchone()[0]
			except:
				query0 = "SELECT tense FROM ",category," WHERE phrase=%s;"
				query = ''.join(query0)
				cur2.execute(query,(word1))
				self.tense = cur2.fetchone()[0]
			conn2.commit()
		else:
			self.tense = None
		
		if category in ['Articles','Nouns','Pronoun','ProperNouns','Verbs']:
			query0 = "SELECT type FROM ",category," WHERE word=%s;"
			query = ''.join(query0)
			cur2.execute(query,(word1))
			self.type = cur2.fetchone()[0]
			conn2.commit()
		else:
			self.type = None

		if category == "Nouns":
			query0 = "SELECT isPlural FROM Nouns WHERE word=%s;"
			query = ''.join(query0)
			cur2.execute(query,(word1))
			bIsPlural = cur2.fetchone()[0]
			if bIsPlural == "yes":
				self.isPlural = True
			else:
				self.isPlural = False
			conn2.commit()
		else:
			self.isPlural = False

		cur2.close()
		conn2.close()
