## Model Configuration
from TChatBot.model import ChatBotModel
from pathlib import Path
from prettytable import PrettyTable
import os

saved_model_dir = "saved_model" 
model_name = "TChatBot"
model_version = "v1"

dir_path = os.path.dirname(os.path.realpath(__file__))
root = Path(dir_path)

def modelConfig():
    # #model path
    model_path = "TChatBot/" + saved_model_dir + "/" + model_name + "/" + model_version

    model = ChatBotModel()

    display = PrettyTable(['TChatBot Model Initializing.......'])
    display.add_row(['ChatBotModel initialized successfully'])

    #If trained model exists
    try:
        model.loadModel(model_path)
        display.add_row(["Found Trained model at {}".format(model_path)])
        print("{}\n\n".format(display))
    except Exception as e:
        display.add_row(["Trained model not found at {}".format(model_path)])
        print("{}\n\n".format(display))
        exit()

    model.model_config(model_path)