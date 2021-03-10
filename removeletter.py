# import nltk
# import numpy as np
# import random
# import string # to process standard python strings
# import matplotlib.pyplot as plt
# import sys
# # import torch.optim as optim
# from nltk.corpus import wordnet 
# # import RegexpTokenizer() method from nltk 
# from nltk.tokenize import RegexpTokenizer 
# # Evaluate using Leave One Out Cross Validation
# import pandas
# from sklearn import model_selection
# from sklearn.linear_model import LogisticRegression

# # SVM for multi-class classification using one-vs-one
# from sklearn.datasets import make_classification
# from sklearn.svm import SVC
# from sklearn.multiclass import OneVsOneClassifier

# from textblob import TextBlob
# import warnings
# warnings.filterwarnings('ignore')
# # Create a reference variable for Class RegexpTokenizer 
# tk = RegexpTokenizer('\s+', gaps = True) 
# f=open('ai1.txt','r',errors = 'ignore')
# raw=f.read()
# raw=raw.lower()# converts to lowercase
# rawlist = []
# sent_tokens = nltk.sent_tokenize(raw) # converts to list of sentences 
# # print(type(sent_tokens))
# for i in range(0,len(sent_tokens)):
#     rawlist.append(sent_tokens[i])

# word_tokens = nltk.word_tokenize(raw) # converts to list of words
# # print(word_tokens)
# lemmer = nltk.stem.WordNetLemmatizer()
# #WordNet is a semantically-oriented dictionary of English included in NLTK.
# def LemTokens(tokens):
#     return [lemmer.lemmatize(token) for token in tokens]
# remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)
# def LemNormalize(text):
#     return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))

# # Keyword Matching
# GREETING_INPUTS = ("hello", "hi", "greetings", "sup", "what's up","hey",)
# GREETING_RESPONSES = ["hi", "hey", "*nods*", "hi there", "hello", "I am glad! You are talking to me"]

# from nltk.sentiment import SentimentIntensityAnalyzer
# sia = SentimentIntensityAnalyzer()
# sia.polarity_scores("Wow, NLTK is really powerful!")
# from statistics import mean



# def greeting(sentence):
#      #If user's input is a greeting, return a greeting response
#     for word in sentence.split():
#         if word.lower() in GREETING_INPUTS:
#             return random.choice(GREETING_RESPONSES)

# from sklearn.feature_extraction.text import TfidfVectorizer

# from sklearn.metrics.pairwise import cosine_similarity
# from numpy.random.mtrand import shuffle
# from PIL import features
# from sklearn.feature_extraction import text


# # Generating response
# def response(user_response):
#     robo_response=''
#     sent_tokens.append(user_response)
#     TfidfVec = TfidfVectorizer(tokenizer=LemNormalize)
#     tfidf = TfidfVec.fit_transform(sent_tokens)
#     vals = cosine_similarity(tfidf[-1], tfidf)
#     idx=vals.argsort()[0][-2]
#     flat = vals.flatten()
#     flat.sort()
#     req_tfidf = flat[-2]
#     sentence=user_response
#     word=nltk.word_tokenize(sentence)
#     new_word=[word for word in word if word.isalnum()]
#     if(req_tfidf==0):
#         a = user_response
#         print(str(a))
#         b = TextBlob(a)
#         user_response = b.correct()
#         # prints the corrected spelling
#         print("corrected text: "+str(user_response))
#         synonyms = []   
#         for syn in wordnet.synsets(user_response):
#             for l in syn.lemmas(): 
#                 synonyms.append(l.name())
#             for i in range(len(synonyms)-1):
#                 out = response(synonyms[i+1])
#                 #print(out)
#                 return out
            
#     else:
#         return sent_tokens[idx]

# def extract_features(text):
#     features = dict()
#     wordcount = 0
#     compound_scores = list()
#     positive_scores = list()

#     for sentence in nltk.sent_tokenize(text):
#         for word in nltk.word_tokenize(sentence):
#             if word.lower():
#                 wordcount += 1
#         compound_scores.append(sia.polarity_scores(sentence)["compound"])
#     features["mean_compound"] = mean(compound_scores) + 1
#     features["wordcount"] = wordcount
#     print(features)
  
#     # define dataset
#     X, y = make_classification(n_samples=1000, n_features=10, n_informative=5, n_redundant=5, n_classes=3, random_state=1)
#     # define model
#     model = SVC()
#     # define ovo strategy
#     ovo = OneVsOneClassifier(model)
#     # fit model 
#     ovo.fit(X, y)
#     print(X)
#     # print(y)
#     # make predictions
#     yhat = ovo.predict(X)

# extract_features("response")

 

# flag=True
# print("ROBO: My name is Robo. I will answer your queries about Chatbots. If you want to exit, type Bye!")
# while(flag==True):
#     user_response = input()
#     user_response=user_response.lower()
#     if(user_response!='bye'):
#         if(user_response=='thanks' or user_response=='thank you' ):
#             flag=False
#             print("ROBO: You are welcome..")
#         else:
#             if(greeting(user_response)!=None):
#                 print("ROBO: "+greeting(user_response))
#             # elif (greeting(extract_features)!=None):
#             #     print("ROBO: "+greeting(extract_features(text)))
#             else:
#                 print("ROBO: ",end="")
#                 print(response(user_response))
#                 r = TextBlob(user_response)
#                 print(r.sentiment)
#                 # print(response())
#                 sent_tokens.remove(user_response)
#     else:
#         flag=False
#         print("ROBO: Bye! t
# 
# ake care..")






import argparse

parser = argparse.ArgumentParser()
print(parser)
parser.add_argument("-o", "--Output", help = "Show Output")
# parser.add_argument('--sum', dest='accumulate', action='store_const',
#                     const=sum, default=max,
#                     help='sum the integers (default: find the max)')

# # Read arguments from command line
args = parser.parse_args()
 
if args.Output:
    print("Diplaying Output as: % s" % args.Output)

args = parser.parse_args()
print(args)      




# Python program to demonstrate
# command line arguments


# import sys

# # total arguments
# n = len(sys.argv)
# print("Total arguments passed:", n)

# # Arguments passed
# print("\nName of Python script:", sys.argv[0])

# print("\nArguments passed:", end = " ")
# for i in range(1, n):
# 	print(sys.argv[i], end = " ")
	
# # Addition of numbers
# Sum = 0
# # Using argparse module
# for i in range(1, n):
# 	Sum += int(sys.argv[i])
	
# print("\n\nResult:", Sum)
