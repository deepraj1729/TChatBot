from TChatBot.model import ChatBotModel
from TChatBot.funcs import load_JSON,ProcessData,getClasses
from prettytable import PrettyTable
import time
from pathlib import Path
import os 

dir_path = os.path.dirname(os.path.realpath(__file__))
root = Path(dir_path)
json_path = root / "input" / "intents.json"
    
def TrainChatBot(epochs = 50,test_size = 0.1,batch_size = 8):
    model = ChatBotModel()

    #load JSON data
    data = load_JSON(json_path)

    # #Load stemmed data from pickle from the training dataset
    words,labels,training,output = ProcessData(data,train = True)
    time.sleep(2)

    #load classes (tags)
    tags = getClasses()
    ta_class = PrettyTable(['Classes'])
    for i in range(len(tags)):
        ta_class.add_row([tags[i]])
    print("\n\n{}\n\n".format(ta_class))
    time.sleep(2)


    #Train model
    model.trainModel(training,output,epochs,test_size,batch_size)