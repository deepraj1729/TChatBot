from TChatBot.funcs import load_JSON,ProcessData,getClasses
from TChatBot.model import ChatBotDNN,ChatBotCNN
from pathlib import Path
from prettytable import PrettyTable
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
root = Path(dir_path)

saved_model_dir = "saved_model" 
model_name = "TChatBot"
model_architecture = ['DNN','CNN','RNN','LSTM'] 
model_version = "v1"

def RunChatBot(arch= None):
    model = None
    model_path = None
    if(arch == None):
        print("Model architecture not provided...")
        print("Showing default DNN model configuration")
        arch = "DNN"
        model = ChatBotDNN()

        #model path
        model_path = "TChatBot/" + saved_model_dir + "/" + model_name + "/" + model_architecture[0] + "/" + model_version
    
    elif(arch == 'dnn'):
        arch = "DNN"
        model = ChatBotDNN()
        #model path
        model_path = "TChatBot/" + saved_model_dir + "/" + model_name + "/" + model_architecture[0] + "/" + model_version
    
    elif(arch == 'cnn'):
        arch = "CNN"
        model = ChatBotCNN()

        #model path
        model_path = "TChatBot/" + saved_model_dir + "/" + model_name + "/" + model_architecture[1] + "/" + model_version
    
    else:
        print("Architecture provided doesn't match with existing one's...")
        print("Showing default DNN model configuration")
        arch = "DNN"
        model = ChatBotDNN()

        #model path
        model_path = "TChatBot/" + saved_model_dir + "/" + model_name + "/" + model_architecture[0] + "/" + model_version

   
    display = PrettyTable(['TChatBot Model Initializing.......'])
    display.add_row(['ChatBotModel initialized successfully'])

    #If trained model exists
    try:
        model.loadModel(model_path)
        display.add_row(["Found trained model at {}".format(model_path)])
        print(display)
    except Exception as e:
        display.add_row(["Trained model not found at {}".format(model_path)])
        print(display)
        exit()

    #load JSON data
    json_path = root / "input" / "intents.json"
    data = load_JSON(json_path)

    #Load stemmed data from pickle from the training dataset
    words,labels,training,output = ProcessData(data,train = False)

    #Call ChatBot TensorChat
    model.chat(words,data)