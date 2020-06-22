#Generate Dataset for users
import os
import json
from pathlib import Path
import platform

dir_path = os.path.dirname(os.path.realpath(__file__))
root = Path(dir_path)
json_file = root / "input" / "intents.json"

def checkOS():
    return platform.system()

def clearScreen():
    sys = checkOS()
    if(sys == 'Windows'):   #windows
        os.system('cls')
    else:
        os.system('clear')  #Linux and OSX

def load_JSON(path): 
    data = None
    try:
        with open(path) as f:
            data  = json.load(f)
    except:
        print("\nFile not found in the path specified")
        exit()
    return data


def saveJSONFormat(tag,patterns,responses):
    new_json_data = {"tag":tag,"patterns":patterns,"responses":responses}
    try:
        intents_data = load_JSON(json_file)

        intents_data["intents"].append(new_json_data)

        with open(json_file,"w") as f:
            json.dump(intents_data,f,indent=3)

        print("\n-----+-----+-----+-----+-----+-----+-----+------+------+-----+------+------")
        print("                      Dataset saved for {} tag".format(tag))
        print("\n-----+-----+-----+-----+-----+-----+-----+------+------+-----+------+------")
        print("Saved updated dataset to intents.JSON")
    except Exception as e:
        print("Ooops something went wrong while handling dataset")
        print(e)



def appendNewDataset():
    try:
        clearScreen()
        tag = ""
        patterns = []
        responses = []

        print("-----+-----+-----+-----+-----+-----+-----+------+------+-----+------+------")
        print("                              Dataset format")
        print("-----+-----+-----+-----+-----+-----+-----+------+------+-----+------+------")
        json_data = {"tag":tag,"patterns":patterns,"responses":responses}
        data = json.dumps(json_data, indent=3)
        print(data)
        print("-----+-----+-----+-----+-----+-----+-----+------+------+-----+------+------")
        print("The dataset must contain these labels:")
        print("(a) Tag (say greeting)")
        print("(b) Patterns (a list of input questions)")
        print("(c) Responses (a list of common responses based on the input questions)")
        print("-----+-----+-----+-----+-----+-----+-----+------+------+-----+------+------")
        
        tag = input("(Tag) Enter a tag name: ")
        clearScreen()
    
        while True:
            print("\n-----+-----+-----+-----+-----+-----+-----+------+------+-----+------+------")
            print("Enter some Patterns (simple chats related to '{}' tag)".format(tag))
            print("\n------------------------------Main Menu----------------------------------")
            print("Type \'done' once completed")
            print("Press s to show inputs")
            print("Press d to delete last input")
            print("Press q to exit session (dataset will not be updated)")
            print("-----+-----+-----+-----+-----+-----+-----+------+------+-----+------+------")
            pattern = input("(Patterns) Type here: ")
            if(pattern.lower() == 'q'):
                clearScreen()
                print("\n---------------------------------------------------------------------------")
                print("                        Exiting TChatBot session")
                print("---------------------------------------------------------------------------")
                print("Session exited... dataset not saved")
                exit()
            elif pattern.lower()=='done':
                clearScreen()
                break
            elif(pattern.lower() == 'd'):
                if(len(patterns) == 0):
                    clearScreen()
                    print("Dataset is empty. Insert something......")
                else:
                    clearScreen()
                    patterns.pop()
            elif(pattern.lower()=='s'):
                clearScreen()
                json_data = {"tag":tag,"patterns":patterns,"responses":responses}
                data = json.dumps(json_data, indent=3)
                print(data)
            else:
                clearScreen()
                patterns.append(pattern)
                print("-----+-----+-----+-----+-----+-----+-----+------+------+-----+------+------")
                print("\n                               Pattern  Saved")
        
        if(len(patterns)==0):
            print("Patterns can't be empty for '{}' tag".format(tag))
            return
        
        while True:
            print("-----+-----+-----+-----+-----+-----+-----+------+------+-----+------+------")
            print("Enter some Responses (simple replies related to '{}' tag)".format(tag))
            print("\n------------------------------Main Menu----------------------------------")
            print("Type 'done' once completed")
            print("Press 's' to show inputs")
            print("Press 'd' to delete last input")
            print("Press 'q' to exit session (dataset will not be updated)")
            print("-----+-----+-----+-----+-----+-----+-----+------+------+-----+------+------")
            response = input("(Responses) Enter some responses related to {}: ".format(tag))
            if(response.lower() == 'q'):
                clearScreen()
                print("\n---------------------------------------------------------------------------")
                print("                        Exiting TChatBot session")
                print("---------------------------------------------------------------------------")
                print("Session exited... dataset not saved")
                exit()
            elif response.lower()=='done':
                clearScreen()
                break
            elif(response.lower() == 'd'):
                if(len(responses) == 0):
                    clearScreen()
                    print("Replies are empty. Insert some replies......")
                else:
                    clearScreen()
                    responses.pop()
            elif(response.lower()=='s'):
                clearScreen()
                json_data = {"tag":tag,"patterns":patterns,"responses":responses}
                json_data = {"tag":tag,"patterns":patterns,"responses":responses}
                data = json.dumps(json_data, indent=3)
                print(data)
            else:
                clearScreen()
                responses.append(response)
                print("-----+-----+-----+-----+-----+-----+-----+------+------+-----+------+------")
                print("\n                                Reply  Saved")

        if(len(responses)==0):
            print("Responses can't be empty")
            return

        saveJSONFormat(tag,patterns,responses)

    except Exception as e:
        print("Oops an error occurred...")
        print(e)


def appendSpecificData():
    print("-----+-----+-----+-----+-----+-----+-----+------+------+-----+------+------")
    print("                    functionality to be updated soon")
    print("---------------------------------------------------------------------------")

    
def currentTags():
    print("-----+-----+-----+-----+-----+-----+-----+------+------+-----+------+------")
    print("                     Current Tags in the dataset")
    print("---------------------------------------------------------------------------")
    json_data = load_JSON(json_file)
    data = json_data["intents"]

    for i in range(len(data)):
        print(data[i]['tag'])

def checkTagExist():
    print("-----+-----+-----+-----+-----+-----+-----+------+------+-----+------+------")
    print("                    functionality to be updated soon")
    print("---------------------------------------------------------------------------")

def createNewDataset():
    print("-----+-----+-----+-----+-----+-----+-----+------+------+-----+------+------")
    print("                    functionality to be updated soon")
    print("---------------------------------------------------------------------------")

def menu():
    print("\n--------------------------------Main Menu----------------------------------")
    print("1. Press 1 to append custom data to the existing dataset.")
    print("2. Press 2 to create a brand new custom dataset (current data will be erased)")
    print("3. Press 3 to add specific data (say some extra responses to a tag) into existing dataset")
    print("4. Press 4 to check existing tags/classes in the dataset")
    print("6. Press 'q' to exit")
    print("-----+-----+-----+-----+-----+-----+-----+------+------+-----+------+------")

## Final function to generate dataset

def generateData():
    print("\n-----+-----+-----+-----+-----+-----+-----+------+------+-----+------+------")
    print("                Initializing TChatBot Dataset configurations")
    print("-----+-----+-----+-----+-----+-----+-----+------+------+-----+------+------")
    print("\nGenerate training data for your customized Chatbot")
    # print("---------------------------------------------------------------------------")
    while True:
        menu()
        try:
            inp = input("Type your response: ")
            clearScreen()
            if(inp.lower() == 'q'):
                print("\n\n-----+-----+-----+-----+-----+-----+-----+------+------+-----+------+------")
                print("                        Exiting TChatBot session")
                print("---------------------------------------------------------------------------")
                exit()
            elif(int(inp) ==1):
                appendNewDataset()
            elif(int(inp)==2):
                createNewDataset()
            elif(int(inp) ==3):
                appendSpecificData()
            elif(int(inp)==4):
                currentTags()
            else:
                print("\n\n-----+-----+-----+-----+-----+-----+-----+------+------+-----+------+------")
                print("                            Option not found")
                print("---------------------------------------------------------------------------")
        except Exception as e:
            print("\n\n-----+-----+-----+-----+-----+-----+-----+------+------+-----+------+------")
            print("                                 Error Occurred")
            print("---------------------------------------------------------------------------")
            print(e)
            print("\n---------------------------------------------------------------------------")
            print("                           Exiting TensorChat session")
            print("---------------------------------------------------------------------------")
            exit()