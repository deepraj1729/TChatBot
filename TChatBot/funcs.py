import nltk
from nltk.stem.lancaster import LancasterStemmer
import numpy as np
import random
import json
import pickle
from pathlib import Path
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
root = Path(dir_path)
classes_path = root / "input" / "classes.txt"
pickle_path = root / "input" / "data.pickle"
tokenizer_path = root / "input" / "tokenizer.txt"

def check_tokenizer():
    try:
        with open(tokenizer_path,"r") as f:
            found = f.read()
        if(found == 'True'):
            return
    except:
        try:
            data = nltk.data.find('tokenizers/punkt')
            print("Found punkt tokenizer at {}".format(data))
            with open(tokenizer_path,"w") as f:
                f.write("True")
        except LookupError:
            print("Downloading tokenizer for processing data for the ChatBot")
            nltk.download('punkt')
            with open(tokenizer_path,"w") as f:
                f.write("True")

def load_JSON(path): 
    data = None
    try:
        with open(path) as f:
            data  = json.load(f)
        print("\nLoaded JSON file: {} successfully".format(path))
    except:
        print("\nFile not found in the path specified.Dataset not loaded successfully")
        exit()
    return data

def getClasses():
    with open(classes_path,"r") as f:
        tags = f.readlines()
    tags = [x.strip() for x in tags] 
    return tags

def ProcessData(data,train = False):
    check_tokenizer()
    if(train == False):
        try:
            with open(pickle_path,"rb") as f:
                words,labels,training,output = pickle.load(f)
            print("Loaded stemmed data from pickle")
        except:
            print("Stemming data from the intents.json file")
            stemmer = LancasterStemmer()
            words = []
            labels = []
            docs_X = []
            docs_y = []

            
            with open(classes_path,"w") as f:
                f.write("")

            for intent in data["intents"]:
                for pattern in intent["patterns"]:
                    wrds = nltk.word_tokenize(pattern)
                    words.extend(wrds)
                    docs_X.append(wrds)
                    docs_y.append(intent["tag"])

                if intent["tag"] not in labels:
                    labels.append(intent["tag"])
                with open(classes_path,"a") as f:
                    f.write(intent["tag"]+"\n")


            #List of non-redundant words the model has seen
            words = [stemmer.stem(w.lower()) for w in words if w != "?"]
            words = np.array(words)
            words = sorted(np.unique(words))



            #labels (sorted)
            labels = sorted(labels)


            training = []
            output = []

            out_empty = [0 for _ in range(len(labels))]


            for x,doc in enumerate(docs_X):
                bag = np.array([])
                wrds = [stemmer.stem(w.lower()) for w in doc if w != "?"]
                
                for w in words:
                    if w in wrds:
                        bag = np.append(bag,np.array([1]))
                    else:
                        bag = np.append(bag,np.array([0]))
                
                output_row = out_empty[:]
                output_row[labels.index(docs_y[x])] = 1

                training.append(bag)
                output.append(np.argmax(output_row))
                


            #into np arrays
            training = np.asarray(training)
            output = np.asarray(output)


            with open(pickle_path,"wb") as f:
                print("Stemmed data saved in pickle file...")
                pickle.dump((words,labels,training,output),f)
    else:
        with open(classes_path,"w") as f:
                f.write("")
        print("Stemming data from the intents.json file")
        stemmer = LancasterStemmer()
        words = []
        labels = []
        docs_X = []
        docs_y = []

        for intent in data["intents"]:
            for pattern in intent["patterns"]:
                wrds = nltk.word_tokenize(pattern)
                words.extend(wrds)
                docs_X.append(wrds)
                docs_y.append(intent["tag"])

            if intent["tag"] not in labels:
                labels.append(intent["tag"])

            with open(classes_path,"a") as f:
                f.write(intent["tag"]+"\n")


        #List of non-redundant words the model has seen
        words = [stemmer.stem(w.lower()) for w in words if w != "?"]
        words = np.array(words)
        words = sorted(np.unique(words))



        #labels (sorted)
        labels = sorted(labels)


        training = []
        output = []

        out_empty = [0 for _ in range(len(labels))]


        for x,doc in enumerate(docs_X):
            bag = np.array([])
            wrds = [stemmer.stem(w.lower()) for w in doc if w != "?"]
            
            for w in words:
                if w in wrds:
                    bag = np.append(bag,np.array([1]))
                else:
                    bag = np.append(bag,np.array([0]))
            
            output_row = out_empty[:]
            output_row[labels.index(docs_y[x])] = 1

            training.append(bag)
            output.append(np.argmax(output_row))
            


        #into np arrays
        training = np.asarray(training)
        output = np.asarray(output)


        with open(pickle_path,"wb") as f:
            print("Stemmed data saved in pickle file...")
            pickle.dump((words,labels,training,output),f)
    return words,labels,training,output


def bagOfWords(s,words):
    stemmer = LancasterStemmer()
    bag = [0 for _ in range(len(words))]

    s_words = nltk.word_tokenize(s)
    s_words = [stemmer.stem(word.lower()) for word in s_words if word != "?"]
    s_words = np.array(s_words)

    for se in s_words:
        for i,w in enumerate(words):
            if w == se:
                bag[i] = 1

    bag = np.array(bag)
    bag.shape = (1,bag.shape[0])
    return bag



