import os
#Remove Tensorflow Messages
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'  # or any {'0', '1', '2'}
from tensorflow.python.util import deprecation
#Avoid Deprecation warnings
deprecation._PRINT_DEPRECATION_WARNINGS = False
import tensorflow as tf
from sklearn import model_selection
from tensorflow import keras
import numpy as np
from TChatBot.funcs import getClasses,bagOfWords
from TChatBot.generate import clearScreen
from prettytable import PrettyTable
import random
import time
from pathlib import Path


dir_path = os.path.dirname(os.path.realpath(__file__))
root = Path(dir_path)
saved_model_path = root / "saved_model" / "model.h5"


#Model
class ChatBotModel:
    def __init__(self):
        self.classes = ['']
        self.model = None
        print("\n")

    def model_config(self,model_path):
        self.model = tf.keras.models.load_model(model_path)
        self.model.summary()

    def loadModel(self,model_path):
        self.model = tf.keras.models.load_model(model_path)

    def trainModel(self,x,y,epochs = 50,test_size = 0.2,batch_size = 10):
        disp = PrettyTable(['Training TChatBot model.....'])

        self.classes = sorted(getClasses())
        inp_shape = len(x[0])
        x_train ,x_test , y_train, y_test = model_selection.train_test_split(x,y, test_size = test_size)

        self.model = tf.keras.models.Sequential()
        self.model.add(tf.keras.layers.Flatten(input_shape=(inp_shape,)))
        self.model.add(tf.keras.layers.Dense(300,activation = "relu"))
        self.model.add(tf.keras.layers.Dense(200,activation = "relu"))
        self.model.add(tf.keras.layers.Dense(40,activation = "relu"))
        # model.add(tf.keras.layers.Dense(10,activation = "relu"))
        self.model.add(tf.keras.layers.Dense(len(self.classes),activation = "sigmoid"))

        self.model.compile(optimizer = "adam",
            loss = 'sparse_categorical_crossentropy',
            metrics=['accuracy'])

        disp.add_row(['Laying the pipeline for the model'])
        print("\n{}\n".format(disp))
        self.model.summary()
        print("\n\n")
        time.sleep(1)
        

        self.model.fit(x_train ,y_train , epochs =epochs,batch_size = batch_size)

        self.model.save(saved_model_path)
        print("\n\n-----+-----+-----+-----+-----+-----+-----+------+------+-----+------+------")
        print("                         Saving trained Model......")
        print("-----+-----+-----+-----+-----+-----+-----+------+------+-----+------+------")
        print("Model saved in disc as \'model.h5\' file in path: {}".format(saved_model_path))
        print("-----+-----+-----+-----+-----+-----+-----+------+------+-----+------+------\n")

    def validateModel(self,x,y):
        print("\n\nValidating Model")
        print("\nLoaded pre-trained model from disc")

        self.classes = sorted(getClasses())

        #validation
        val_loss,val_acc = self.model.evaluate(x,y)
        ta_val = PrettyTable(['Loss (%)', 'Accuracy (%)'])
        ta_val.add_row([val_loss*100,val_acc*100])

        #validation table
        print("\n\n{}".format(ta_val))

        #prediction
        predict = self.model.predict(x)
        print("\n\nPrediction:\n")

        t_tot = PrettyTable(['Sl.No.', 'Argmax Value','Expected Value','Predicted Tag','Expected Tag','Result'])
        for i in range(len(predict)):
            argMax = np.argmax(predict[i])
            tag = classes[argMax]
            result = "Correct" if y[i] == argMax else "Wrong"
            t_tot.add_row([i+1,argMax,y[i],tag,y[i],result])

        #Total table
        print(t_tot)
        return predict,val_loss,val_acc


    def predictModel(self,x):
        print("Loaded pre-trained model from disc")

        self.classes = getClasses()
        tags = []
        tag_indices = []


        #prediction
        predict = self.model.predict(x)
        print("Prediction:\n")
        t_pred = PrettyTable(['Sl.No.', 'Argmax Value','Predicted Tag'])
        for i in range(len(predict)):
            argMax = np.argmax(predict[i])
            tag_indices.append(argMax)
            tag = classes[argMax]
            tags.append(tag)
            t_pred.add_row([i+1,argMax,tag])
        print(t_pred)
        return predict,tags,tag_indices
    
    def chat(self,words,data):
        time.sleep(1)
        clearScreen()
        print("------+------+-----+------+-----+-----+-----+------+------")
        print("                TChatBot Session Initializing......")
        print("------+------+-----+------+-----+-----+-----+------+------\n")
        time.sleep(2)
        print("TChatBot Session started at : {} ".format(time.ctime()))
        print("Type \'quit\' to end chat session")
        print("\n------+------+-----+------+-----+-----+-----+------+------")
        time.sleep(1)
        print("\nTChatBot (Bot): Hey! I'm TChatBot :)")
        classes = getClasses()
        sort_classes = sorted(classes)


        while True:
            time.sleep(1)
            inp = input("You: ")
            if(inp.lower()=='quit'):
                print("\n\n------+------+-----+------+-----+-----+-----+------+------")
                print("TChatBot (Bot): Comeback again next time ;)")
                print("TChatBot session expired at : {} ".format(time.ctime()))
                print("------+------+-----+------+-----+-----+-----+------+------\n")
                
                break

            chatOut = self.model.predict([bagOfWords(inp,words)])[0]
            chatOut_index = np.argmax(chatOut)
            tag = sort_classes[chatOut_index]
            intents = data["intents"]
            # confidence = chatOut[chatOut_index]

            #Loop to randomly choose a reply
            for i in range(len(intents)):
                if intents[i]["tag"] == tag:
                    responses = intents[i]["responses"]
                    reply = np.random.choice(responses, 1, replace=False)[0]  
                    print("\nTChatBot (Bot): {}".format(reply))
            
            