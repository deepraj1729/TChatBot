[![TChatBot](https://img.shields.io/badge/TChatBot-v0.1.0-blue)](https://pypi.org/project/TChatBot/0.1.0/)  [![license](https://img.shields.io/badge/License-MIT-yellow)](https://github.com/deepraj1729/TChatBot/blob/master/LICENSE) [![dependencies](https://img.shields.io/badge/dependencies-packages-orange)](https://github.com/deepraj1729/TChatBot/blob/master/requirements.txt)
[![pull](https://img.shields.io/badge/pull--requests-requests-green)](https://github.com/deepraj1729/TChatBot/pulls) [![issues](https://img.shields.io/badge/issues-issues-red)](https://github.com/deepraj1729/TChatBot/issues) ![python](https://img.shields.io/badge/python-3.5%20%7C%203.6%20%7C%203.7-blue)


# TChatBot
A ChatBot framework to make customizable all purpose Chatbots using NLP, Tensorflow, Speech Recognition 

# Basic Requirements: 
1. RAM > 4GB (For training the model)
2. Storage Space > 200MB
3. GPU RAM >=4 GB (optional)
4. Python >= 3.5

# Installation

(a). Install using `pip` 
(b). Clone the repository (dev testing)

## (a) Install Using `pip`:

# Pre-Requisites:
1. An Empty folder
2. A virtual environment (using normal python or conda python)


## Setting up the Pre-Requisites:
### Step 1: Create an empty folder say `Demo`.

### Step 2: Open the folder and open terminal from that folder location.

### Step 3: Create Virtual Environment
1. Either Using `virtualenv` (strictly for non-conda users, optional for conda users)
2. Or Using conda (for conda users only)

## Choose any one of the above 2 steps based on conda or non-conda users
### 1. Install virtualenv using `pip` (for both non-conda and conda users)

        pip install virtualenv>=20.0.14
        
### (1.a) Run the command to create virtual environment: 

        virtualenv .

### (1.b) Activate virtual environment by running the command:
        
        .\Scripts\activate

### (1.c) `(Demo)` in the left of terminal indicates that the environment is activated

### 2. Create virtual environment (for conda users only), skip if above step is done: 

        conda create -n TChatBot

### (2.a) Activate virtual environment by running the command:

        conda activate TChatBot

### (2.b) `(TChatBot)` in the left of terminal shows that the environment is activated
                 

## Install the latest `TChatBot` package using `pip`:
        
        pip install TChatBot
        
### Congrats, You installed all the required dependencies :) 

# Usage:
#### (Must run within the virtual environment):

### Chat with TensorChat Bot:

        tchat -chat

### Train the Chatbot:

        tchat -train

### Create Custom Dataset commandline

        tchat -create

### Check Model Pipeline Configurations

        tchat --config

### Check Version:
        
        tchat -v
    


