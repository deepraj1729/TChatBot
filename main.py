from prettytable import PrettyTable

""" Starting display message"""
display = PrettyTable(['TChatBot initializing.....'])
display.add_row(['Initializing tensorflow environment for running TChatBot....'])
print(display)

# from TensorChat.funcs import load_JSON,ProcessData
from TChatBot.train import TrainChatBot
from TChatBot.chat import RunChatBot
from TChatBot.generate import generateData,currentTags
from TChatBot.config import modelConfig
import argparse

version = '0.1.0'

def main():
    #parsing commadline args
    parser = argparse.ArgumentParser(description="TChatBot is a complex AI chatbot that can learn anything based on given input")

    #running commands
    subparser = parser.add_subparsers(title="commands", dest="command")

    #Version
    parser.add_argument('-v', action='version', version=version)

    """  Run ChatBot  """
    parser.add_argument('-chat',action='store_true',help = "Start Chat session with TChatBot")

    """  Train ChatBot  """
    parser.add_argument('-train',action='store_true',help = "Train TChatBot based on given input")

    """  Create Dataset  """
    parser.add_argument('-create',action='store_true',help = "Create dataset for training Bot")

    """  Classes trained  """
    parser.add_argument('-classes',action='store_true',help = "TChatBot classes trained till now")

    """  Model Configuration  """
    parser.add_argument('--config',action='store_true',help = "TChatBot Model configuration or pipeline")


    args = parser.parse_args()
    try:
        if(args.chat == True):
            RunChatBot()
        elif(args.train == True):
            TrainChatBot(epochs = 100,test_size = 0.1,batch_size = 8)
        elif(args.create == True):
            generateData()
        elif(args.config == True):
            modelConfig()
        elif(args.classes == True):
            currentTags()
            
    except ImportError as i:
        print("Oops some error occurred")
        print(i)
    except FileNotFoundError as f:
        print("Oops some error occurred")
        print(f)
    except AttributeError as a:
        print("Oops some error occurred")
        print(a)
    except Exception as e:   ## For some other exceptions
        print("Oops some error occurred")
        print(e)

if __name__ == "__main__":
    main()

