# SportsBetting


## Setup

Clone or download repo from https://github.com/jpo52/SportsBetting onto your desktop

Nagivate from command line:
```sh
cd Desktop/SportsBetting
```

Obtain a unique API key from The-Odds-API: 
https://the-odds-api.com/#get-access

Create a file called .env within the local repo:

Within .env file, assign your unique API to the enviroment variable API_KEY

```sh 
API_KEY="abc123"
```
Substitute your unique API Key for "abc123"


## Environment Setup

Use Anaconda to create and activate a new virtual environment, called "betting-env": 
```sh
conda create -n betting-env python=3.8
conda activate betting-env 
```

from inside virtual environment, install package dependencies:
```sh
pip install -r requirements.text
```

> NOTE: If installation causes an error message, make sure you are navigating within the repository's root directiory, where the requirements.txt file exists 



## Usage
To run the program, in the command line:

```py
python -m apps.odds_seeker
```