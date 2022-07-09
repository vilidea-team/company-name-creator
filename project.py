import whois
import random

from english import prefixes, prefixesCommon, suffixes, alphabet, foods, nouns, moreNouns, prepositions, english

# Favorites are used to be a foundation that we then combine with suffixes and prefixes
favorites = ["pie", "berry", "cake", "sauce", "love", "drea"]

# CORE FUNCTION USED TO GET WHOIS
def getStatus(name):
	try:
		domain = whois.whois(f"{ name }.com")
		# Domain is taken :(
		print(f"----------------- { name }.com -> { domain.whois_server }" )
	except:
		# Domain is available!
		print(f"{ name }.com")

# Checks if a .com is available for every letter in the alphabet before & after the word
def searchAlphabet(word):
	for i, letter in enumerate(alphabet):
		getStatus(f"{ letter }{ word }")
		getStatus(f"{ word }{ letter }")





# Chooses a specified amount to generate from prefixes
def randomCom(amount):
	for i in range(amount):
		random1 = random.choice(prefixes)
		random2 = random.choice(english)
		getStatus(f"{ random1 }{ random2 }")


# Choose a list of words (ie. "favorites") to add to every letter in the alphabet at the beginning and the end
def combineArrayWithAlphabet(array):
	for i, text in enumerate(array):
		searchAlphabet(text)


# Use your own word and then search for a specific amount of combinations with an array (by default we use english array)
def customSuffix(word, amount, array=english):
	if amount >= len(array):
		for i, random in enumerate(array):
			getStatus(f"{ word }{ random }")	
	else:
		for i in range(amount):
			random = random.choice(array)
			getStatus(f"{ word }{ random }")




# Combine an array with your favorites, this is the big daddy function!
# you can take your favorite / brand specific words and combine them with other words, prefixes, and suffixes
def combineArrayWithFavorites(array):
	for i, text in enumerate(array):
		for i, favorite in enumerate(favorites):
			getStatus(f"{ favorite }{ text }")
			getStatus(f"{ text }{ favorite }")

# Baby function, take all your favorites and combine them with another piece of text
def combineWithFavorites(text):
	for favorite in favorites:
		getStatus(f"{ favorite }{ text }")
		getStatus(f"{ text }{ favorite }")


#
# Example: 
# To discover the name "vilidea" this function was used...
#
# combineWithFavorites('vil')
#
# and inside my favorites was the word "idea" so just like that vil+idea+.com was available!
#

