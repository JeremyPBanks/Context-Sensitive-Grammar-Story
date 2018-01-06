# Context-Sensitive-Grammar-Story
An unfinished program utilizing Python and MySQL to randomly generate a story algorithmatically, using the concept of Context-Sensitive Grammars.

Users can enter any words or phrases, separated by type, they want to be in the story into a database. The program radnomly selects strings from the database and stores them in a Queue to display them in the story in a grammatically correct way. The actual selection process is determined by the context of the word given its current situation in the sentence, and the next type of word is randomly selected with the use of Python's random library.

As of now, the only functional segment of the code is the database entry/retrieval, with the algoithms for creating the story still under contruction. This project was also constructed in Python 2.7 (could not get MySQL connection to properly work for more current iterations) in a Linux environment, and has yet to be tested under other circumstances.

This project is unfinished at the moment; check back when it's completed!

