#import pandas as pd
#from _typeshed import NoneType
import os
import csv
import time
import json
import requests
from dotenv import load_dotenv
from datetime import datetime, timedelta, date
import time
#from re import search

load_dotenv()
apikey = os.environ.get("API_KEY")

a = []
b = []
teams = []
teams_playing = []
Test_bool = True
check = True


def match_team(teams_playing, teams):
    """
    Format: strings in lists

    This function takes the string item(s) input and searches
    if any of these strings match the list of home teams.

    Example: Is the list ["New", "York"] in the list ["New", "York", "Yankees"]
    """
    check = all(items in teams_playing for items in teams)
    if check is True:
        Test_bool = True
        a.append(item['teams'])
        b.append(item['teams'])
        print("")
        print(f"For the game between {item['teams']} that starts at {newStartTime} EST on {newStartDate},")
        #time.sleep(delay)
        for site in item["sites"]:
            print(f"The odds on  {site['site_nice']} are {site['odds']['spreads']['odds']}")
        teams_playing.clear()

    if check is False:
        pass
        teams_playing.clear()
        Test_bool =False
    return Test_bool
#def find_team(home, away, Team_name, check):
    #if search(Team_name, home):
    #    check is True
    #else:
    #    if search(Team_name, away):
    #        check is True
    #    else:
    #        check is False


if __name__ == "__main__":




    #data_1 = pd.read_csv('SportsBetting.csv')
    #print(data_1)

    delay = 1.5

    # An api key is emailed to you when you sign up to a plan


    AbbrevList = []
    with open("SportsInfo.csv", "r") as csv_file:
        read_csv = csv.reader(csv_file, delimiter =',')
        for lines in read_csv:
            AbbrevList.append(lines[1])
    AbbrevList.pop(0)        
    #print(AbbrevList)

    StateList = []
    with open("SportsInfo.csv", "r") as csv_file:
        read_csv = csv.reader(csv_file, delimiter =',')
        for lines in read_csv:
            StateList.append(lines[0])
    StateList.pop(0)        
    #print(StateList)

    LegalList = []
    with open("SportsInfo.csv", "r") as csv_file:
        read_csv = csv.reader(csv_file, delimiter =',')
        for lines in read_csv:
            LegalList.append(lines[2])
    LegalList.pop(0)        
    #print(LegalList)

    OnlineList = []
    with open("SportsInfo.csv", "r") as csv_file:
        read_csv = csv.reader(csv_file, delimiter =',')
        for lines in read_csv:
            OnlineList.append(lines[3])
    OnlineList.pop(0)        
    #print(OnlineList)


    RegisterList = []
    with open("SportsInfo.csv", "r") as csv_file:
        read_csv = csv.reader(csv_file, delimiter =',')
        for lines in read_csv:
            RegisterList.append(lines[4])
    RegisterList.pop(0)        
    #print(RegisterList)

    FutureList = []
    with open("SportsInfo.csv", "r") as csv_file:
        read_csv = csv.reader(csv_file, delimiter =',')
        for lines in read_csv:
            FutureList.append(lines[5])
    FutureList.pop(0)        
    #print(FutureList)


    val = False


    while val == False:
        user_state = input("Please enter your state i.e. New York, NY: ").upper()

        if user_state in StateList:
            user_index = (StateList.index(user_state))
            val = True

        elif user_state in AbbrevList:
            user_index = (AbbrevList.index(user_state))
            val = True

        else:
            time.sleep(delay)
            print("Please input a valid state")
            time.sleep(delay)


    if OnlineList[user_index] == "Yes":
        time.sleep(delay)
        print("")
        print("It looks like online betting is legal in your area!")
        sport = input("Please select your Sport (baseball, football, hockey, or basketball): ").lower()

        valid_options = ['baseball', 'football', 'hockey', 'basketball']

        is_valid = sport not in valid_options

        try:
            if is_valid == True: 
                raise ValueError()
        except ValueError:
            print("Please enter a valid sport")
            #exit()`

        ## Can probably do this cleaner but its not raising an error if I don't make a new variable
        sport_selection = sport
        if sport_selection == 'baseball':
            sport_selection = 'baseball_mlb'
        elif sport_selection == 'football':
            sport_selection = 'americanfootball_nfl'
        elif sport_selection == 'hockey':
            sport_selection = 'icehockey_nhl'
        elif sport_selection == 'basketball':
            sport_selection = 'basketball_nba'


        odds_response = requests.get('https://api.the-odds-api.com/v3/odds', params={
            'api_key': apikey,                                                         
            'sport': sport_selection,                                                        
            'region': 'us', # uk | us | eu | au                                         
            'mkt': 'spreads', # h2h | spreads | totals           
            'dateFormat': 'unix'                      
        })
        odds_json = json.loads(odds_response.text)
        if not odds_json['success']:
            print(
                'There was a problem with the odds request, please try again',
                #odds_json['msg']
            )
        else:
            print("--------------------")
            print("Disclaimer: This app is not for gambling, it only compares odds from different gambling websites to give you the best information. you must go to the websites displayed to place your bet.")
            print("--------------------")
            print("Understanding the Odds: These odds show your potential winnings on different websites. If you bet one dollar on the team on the left or right, and they win, you will recieve the corresponding winnings in return. If your team loses, you recieve nothing. Good Luck Betting!")
            print("--------------------")


            a = []
            b = []
            teams = []
            teams_playing = []
            if odds_json['success'] == True:
                Team_name = input("Enter the name of the team you are looking for. Should you want to search for all teams in this sport, type 'Go': ").split()
                for word in Team_name:
                    name_cap = word.title()
                    teams.append(name_cap)
                print("---------------")
                for item in Team_name:
                    name_cap = item.capitalize()
                    teams.append(name_cap)
                #print(teams)
                for item in odds_json['data']:
                    #print(item.keys())
                    commence_datetime = item['commence_time']
                    ts = int(commence_datetime)
                    dt_utc = datetime.utcfromtimestamp(ts)
                    dt_diff = timedelta(hours=4)
                    dt_est = dt_utc - dt_diff
                    today = date.today()
                    game_start_date = dt_est.date()
                    newDateFormat =datetime.strptime(str(game_start_date), '%Y-%m-%d')
                    newStartDate = newDateFormat.strftime('%m-%d-%Y')

                    game_start_time = dt_est.time()
                    newTimeFormat =datetime.strptime(str(game_start_time), '%H:%M:%S' )
                    newStartTime = newTimeFormat.strftime('%I:%M %p')


                    if game_start_date == today:
                        home = item['teams'][0].split()
                        away = item['teams'][1].split()
                        #print(home)
                        #print(away)
                        #print(Team_name)
                        teams_playing.clear()
                        for word in home:
                            teams_playing.append(word)
                        for word in away:
                            teams_playing.append(word)
                        if 'Go' in Team_name:
                            print("Welcome")
                            check = True
                            a.append(item['teams'])
                            b.append(item['teams'])
                            print("")
                            print(f"For the game between {item['teams']} that starts at {newStartTime} EST on {newStartDate},")
                            for site in item["sites"]:
                                print(f"The odds on  {site['site_nice']} are {site['odds']['spreads']['odds']}")


                        #breakpoint()
                        match_team(teams_playing, teams)


#def find_team(home, away, Tea






                if not a:
                    print("We could not find the team you were looking for, here are all of the upcoming games in this league.")
                    print("---------------")
                    for item in odds_json['data']:
                        if game_start_date == today:
                            b.append(item['teams'])
                            print(f"For the game between {item['teams']} that starts at {newStartTime} EST on {newStartDate},")
                            for site in item["sites"]:
                                print(f"The odds on  {site['site_nice']} are {site['odds']['spreads']['odds']}")
                if not b:
                    print("---------------")
                    print("There are no upcoming games in this league")
            else:
                print(f"It appears there are no", sport, "games today, make sure", sport, "is in season or try another sport.")
 

            game_odds = (odds_json['data'][3])

            # Check your usage
            print()
            print('Remaining requests', odds_response.headers['x-requests-remaining'])
            print('Used requests', odds_response.headers['x-requests-used'])



        if RegisterList[user_index] == "Yes":
            time.sleep(delay)
            print("")
            print("Just a heads up! Your state requires that you register in-person before online gambling")

    else: 
        time.sleep(delay)
        print("")
        print("Hmm...online betting is not currently legal in your area")
        if FutureList[user_index] == "Yes":
            time.sleep(delay)
            print("")
            print("Based on current legislation, online gambling in your state should be available by the end of 2021")
        else: 
            time.sleep(delay)
            print("")
            print("It does not appear as though legislation will allow online gambling by the end of 2021")
        if LegalList[user_index] == "Yes":
            time.sleep(delay)
            print("")
            print("The good news is in-person gambling is legal in your state!")