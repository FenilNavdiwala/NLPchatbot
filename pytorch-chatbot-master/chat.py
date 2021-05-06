import random
import json
import argparse
import torch
import sys
from model import NeuralNet
from nltk_utils import bag_of_words, tokenize, syn
from pymongo import MongoClient
from bson import ObjectId
# from train import ChatDataset
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

# Database Url nd Password
client = MongoClient(
    "mongodb+srv://admin:admin123@cluster1.ycoy8.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client["myFirstDatabase"]
# cahtbots is collection Name
collection = db["chatbots"]

y = collection.find({"_id": ObjectId("6051b174e1801a35d1336993")})
a = y.next()
K = a['intents']
A = []  # Tag
TP = []  # trainingphrase
R = []  # response
for i in range(len(K)):
    A.append(K[i]['intentName'])
    TP.append(K[i]['trainingPhrase'])
    R. append(K[i]['response'])

FILE = "data.pth"
data = torch.load(FILE)

input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data['all_words']
A = data['tags']
model_state = data["model_state"]

model = NeuralNet(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)

model.eval()

bot_name = "Fenil"
sentence = sys.argv[1]
# print(sentence)
_sentence = tokenize(sentence)
X = bag_of_words(_sentence, all_words)
X = X.reshape(1, X.shape[0])
X = torch.from_numpy(X).to(device)
output = model(X)


_, predicted = torch.max(output, dim=1)

tag = A[predicted.item()]

probs = torch.softmax(output, dim=1)
prob = probs[0][predicted.item()]


res = None
# print(prob.item())
if prob.item() > 0.75:
    for data in K:
        if data['intentName'] == sentence or sentence in data["trainingPhrase"]:
            res = data['response']
            print(res)
            break
    if not res:
        print(f"{bot_name}: I do not understand...")
