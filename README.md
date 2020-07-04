[![TChatBot](https://img.shields.io/badge/TChatBot-v0.1.0-blue)](https://pypi.org/project/TChatBot/0.1.0/)  [![license](https://img.shields.io/badge/License-MIT-yellow)](https://github.com/deepraj1729/TChatBot/blob/master/LICENSE) [![dependencies](https://img.shields.io/badge/dependencies-packages-orange)](https://github.com/deepraj1729/TChatBot/blob/master/requirements.txt)
[![pull](https://img.shields.io/badge/pull--requests-requests-green)](https://github.com/deepraj1729/TChatBot/pulls) [![issues](https://img.shields.io/badge/issues-issues-red)](https://github.com/deepraj1729/TChatBot/issues) ![python](https://img.shields.io/badge/python-3.5%20%7C%203.6%20%7C%203.7-blue)


# TChatBot
A ChatBot framework to make customizable all purpose Chatbots using NLP, Tensorflow, Speech Recognition 

# Models:
- DNN (Deep Neural Network)
- CNN (Convolutional Neural Network - 1D)
- RNN (Recurrent Neural Network)
- LSTM (Long Short Term Memory)

# Commands:

1. To Chat with the trained model (default architecture = `DNN`):

        python main.py -chat
2. To chat with the trained model with a specific architecture:
        
        python main.py -chat -arch archName
where archName can be out of `DNN, CNN, RNN, LSTM` e.g:    

        python main.py -chat -arch dnn
3. To train with default intents JSON data (default architecture = `DNN`):

        python main.py -train
4. To train with default intents JSON data with a specific model architecture:

        python main.py -train -arch archName
where archName can be out of `DNN, CNN, RNN, LSTM` e.g:    

        python main.py -train -arch cnn
5. Create Custom Dataset command-line for retraining the Bot

        python main.py -create    
6. Check Current classes trained

        python main.py -classes
7. Check Model Pipeline Configurations (default architecture = `DNN`)

        python main.py -config 
8. Check specific Model Pipeline Configuration (if trained model exists):

        python main.py -config -arch archName
where archName can be out of `DNN, CNN, RNN, LSTM` e.g:  

        python main.py -config -arch cnn
8. Check Version:
        
        python main.py -v
9. For any help regarding commands:

        python main.py -h