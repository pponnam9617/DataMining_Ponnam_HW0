#§ submit the Python code that does the following:
#using the code and the 5 books provided above, explore and apply the very nice Python library called
#collections. Use the Counter class to load the word frequencies of each book into a Python dictionary.

#FUNCTION
def gutenberg_get_words(url="http://www.gutenberg.org/cache/epub/1232/pg1232.txt",range=slice(0,None), stopwords=[]):
 r = requests.get(url)
 data = re.sub(r'[^\w\s]', '', str(r.text)).lower()
 return \
 [w for w in data.split() if w not in stopwords]


#---------------------------------------import statements------------------------
import requests
import re
import sys
import operator
#---------------------------------------import counter from collections------------------------
from collections import Counter
reload(sys)
sys.setdefaultencoding('utf-8')
US_STOPWORDS = ["a", "about", "above", "above", "across", "after", "afterwards", "again", "against", "all", "almost", "alone", "along", "already", "also","although","always","am","among", "amongst", "amoungst", "amount", "an", "and", "another", "any","anyhow","anyone","anything","anyway", "anywhere", "are", "around", "as", "at", "back","be","became", "because","become","becomes", "becoming", "been", "before", "beforehand", "behind", "being", "below", "beside", "besides", "between", "beyond", "bill", "both", "bottom","but", "by", "call", "can", "cannot", "cant", "co", "con", "could", "couldnt", "cry", "de", "describe", "detail", "do", "done", "down", "due", "during", "each", "eg", "eight", "either", "eleven","else", "elsewhere", "empty", "enough", "etc", "even", "ever", "every", "everyone", "everything", "everywhere", "except", "few", "fifteen", "fify", "fill", "find", "fire", "first", "five", "for", "former", "formerly", "forty", "found", "four", "from", "front", "full", "further", "get", "give", "go", "had", "has", "hasnt", "have", "he", "hence", "her", "here", "hereafter", "hereby", "herein", "hereupon", "hers", "herself", "him", "himself", "his", "how", "however", "hundred", "ie", "if", "in", "inc", "indeed", "interest", "into", "is", "it", "its", "itself", "keep", "last", "latter", "latterly", "least", "less", "ltd", "made", "many", "may", "me", "meanwhile", "might", "mill", "mine", "more", "moreover", "most", "mostly", "move", "much", "must", "my", "myself", "name", "namely", "neither", "never", "nevertheless", "next", "nine", "no", "nobody", "none", "noone", "nor", "not", "nothing", "now", "nowhere", "of", "off", "often", "on", "once", "one", "only", "onto", "or", "other", "others", "otherwise", "our", "ours", "ourselves", "out", "over", "own","part", "per", "perhaps", "please", "put", "rather", "re", "same", "see", "seem", "seemed", "seeming", "seems", "serious", "several", "she", "should", "show", "side", "since", "sincere", "six", "sixty", "so", "some", "somehow", "someone", "something", "sometime", "sometimes", "somewhere", "still", "such", "system", "take", "ten", "than", "that", "the", "their", "them", "themselves", "then", "thence", "there", "thereafter", "thereby", "therefore", "therein", "thereupon", "these", "they", "thickv", "thin", "third", "this", "those", "though", "three", "through", "throughout", "thru", "thus", "to", "together", "too", "top", "toward", "towards", "twelve", "twenty", "two", "un", "under", "until", "up", "upon", "us", "very", "via", "was", "we", "well", "were", "what", "whatever", "when", "whence", "whenever", "where", "whereafter", "whereas", "whereby", "wherein", "whereupon", "wherever", "whether", "which", "while", "whither", "who", "whoever", "whole", "whom", "whose", "why", "will", "with", "within", "without", "would", "yet", "you", "your", "yours", "yourself", "yourselves", "the"]
#Returns list of words from page urls 
d1 = gutenberg_get_words("http://www.gutenberg.org/cache/epub/84/pg84.txt",stopwords=US_STOPWORDS)
d2 = gutenberg_get_words("http://www.gutenberg.org/cache/epub/2500/pg2500.txt",stopwords=US_STOPWORDS)
d3 = gutenberg_get_words("http://www.gutenberg.org/cache/epub/1497/pg1497.txt",stopwords=US_STOPWORDS)
d4= gutenberg_get_words("http://www.gutenberg.org/cache/epub/1404/pg1404.txt",stopwords=US_STOPWORDS)
d5 = gutenberg_get_words("http://www.gutenberg.org/cache/epub/1232/pg1232.txt",stopwords=US_STOPWORDS)

#FREQUENCY_COUNTER
freq1 = Counter(d1)
freq2 = Counter(d2)
freq3 = Counter(d3)
freq4 = Counter(d4)
freq5 = Counter(d5)


#SORTING OF WORD FREQUENCIES
s_1=sorted(freq1.items(),key=operator.itemgetter(1),reverse=True)
s_2=sorted(freq2.items(),key=operator.itemgetter(1),reverse=True)
s_3=sorted(freq3.items(),key=operator.itemgetter(1),reverse=True)
s_4=sorted(freq4.items(),key=operator.itemgetter(1),reverse=True)
s_5=sorted(freq5.items(),key=operator.itemgetter(1),reverse=True)









#§ turn in at least 2 sentences and any code if you used code to answering the following:

#TOP 30 words and frequencies of 5 text documents in the URLs
top1 = dict(s_1[:30])
top2 = dict(s_2[:30])
top3 = dict(s_3[:30])
top4 = dict(s_4[:30])
top5 = dict(s_5[:30])

#LISTS[]------>used for storing lists(top1 to top5) as a multi dimensional list of lists
lists=[]
#CW------------->common words in all % documents
cw=[]

lists.append(top1.keys())
lists.append(top2.keys())
lists.append(top3.keys())
lists.append(top4.keys())
lists.append(top5.keys())

print "all words",
print(lists)
for x in lists[0]:
 if x in lists[1]:
  if x in lists[2]:
   if x in lists[3]:
    if x in lists[4]:
     cw.append(x)

#COMMON WORDS
print "same words in Top 30:",
print(cw)    
