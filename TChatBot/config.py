## Model Configuration
from TChatBot.model import ChatBotModel
from pathlib import Path
from prettytable import PrettyTable
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
root = Path(dir_path)

def modelConfig():
    # #model path
    model_path = root / "saved_model" / "model.h5"

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