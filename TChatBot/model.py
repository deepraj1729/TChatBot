import os
#Remove Tensorflow Messages
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'  # or any {'0', '1', '2'}
from tensorflow.python.util import deprecation
#Avoid Deprecation warnings
deprecation._PRINT_DEPRECATION_WARNINGS = False
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Input, Dense, BatchNormalization, Flatten, Conv1D, AveragePooling1D, MaxPooling1D, Dropout
from sklearn import model_selection
import numpy as np
from TChatBot.funcs import getClasses,bagOfWords
from TChatBot.generate import clearScreen
from prettytable import PrettyTable
import random
import time
from pathlib import Path



dir_path = os.path.dirname(os.path.realpath(__file__))
root = Path(dir_path)

saved_model_path = root / "saved_model" 
model_name = "TChatBot"
model_version = "v1"


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

        """DNN Architecture"""
        self.model = Sequential()
        self.model.add(Flatten(input_shape=(inp_shape,)))
        self.model.add(Dense(300,activation = "relu"))
        self.model.add(Dense(200,activation = "relu"))
        self.model.add(Dense(40,activation = "relu"))
        self.model.add(Dense(len(self.classes),activation = "sigmoid"))

        """CNN Architecture"""
        # self.model = Sequential()
        # self.model.add(Conv1D(filters=64, kernel_size=1, activation='relu', input_shape=inp_shape))
        # self.model.add(Conv1D(filters=32, kernel_size=1, activation='relu'))
        # self.model.add(MaxPooling1D(pool_size=1))
        # self.model.add(Flatten())
        # self.model.add(Dense(100, activation='relu'))
        # self.model.add(Dense(len(self.classes), activation='sigmoid'))

        self.model.compile(optimizer = "adam",
            loss = 'sparse_categorical_crossentropy',
            metrics=['accuracy'])

        disp.add_row(['Laying the pipeline for the model'])
        print("\n{}\n".format(disp))
        self.model.summary()
        print("\n\n")
        time.sleep(1)
        

        self.model.fit(x_train ,y_train , epochs =epochs,batch_size = batch_size)

        path_to_model = saved_model_path / model_name
        path = os.path.join(path_to_model,model_version) 

        try:  
            os.makedirs(path, exist_ok = True)
            tf.saved_model.save(self.model,path)

            print("\n\n-----+-----+-----+-----+-----+-----+-----+------+------+-----+------+------")
            print("                         Saving trained Model version {}......".format(model_version))
            print("-----+-----+-----+-----+-----+-----+-----+------+------+-----+------+------")
            print("Model saved in disc as \'saved_model.pb\' file in path: {}".format("saved_model/{}".format(model_name)+"/"+model_version))
            print("-----+-----+-----+-----+-----+-----+-----+------+------+-----+------+------\n")  
        except OSError as error:  
            print("Path already exists") 

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
            tag = self.classes[argMax]
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
            tag = self.classes[argMax]
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
            
            
