from apps.odds_seeker import Test_bool, match_team

Mock_list_1 = ["a"]
Mock_list_2 = ["a", "b", "c"]
Mock_list_3 = ["x"]

#valid_result = match_team(Mock_list_1, Mock_list_2)
#print(valid_result)
#for item in Mock_list_1:
#    def test_match_team():
#        valid_result = match_team(item, Mock_list_2)
#        assert valid_result == True
#for item in Mock_list_3:
#        failed_result = match_team(Mock_list_3, Mock_list_2)
#        assert failed_result == False
def test_match_team():
    #Test_bool = False
    for item in Mock_list_1:
        match_team(Mock_list_1, Mock_list_2, Test_bool)
        assert Test_bool == True
def test_match_fail():
    #Test_bool = True
    for item in Mock_list_3:
        match_team(Mock_list_3, Mock_list_2, Test_bool)
        assert Test_bool == False



#
#{'id': '4a9ed825a03eb8693840a6752ff450bd', 'sport_key': 'baseball_mlb', 'sport_nice': 'MLB', 'teams': ['Cincinnati Reds', 'San Francisco Giants'], 'commence_time': 1621291260, 'home_team': 'Cincinnati Reds', 'sites': [{'site_key': 'betonlineag', 'site_nice': 'BetOnline.ag', 'last_update': 1621265315, 'odds': {'spreads': {'odds': [2.5, 1.58], 'points': ['-1.5', '1.5']}}}, {'site_key': 'pointsbetus', 'site_nice': 'PointsBet (US)', 'last_update': 1621265325, 'odds': {'spreads': {'odds': [2.45, 1.58], 'points': ['-1.5', '1.5']}}}, {'site_key': 'williamhill_us', 'site_nice': 'William Hill (US)', 'last_update': 1621265243, 'odds': {'spreads': {'odds': [2.45, 1.59], 'points': ['-1.5', '1.5']}}}, {'site_key': 'lowvig', 'site_nice': 'LowVig.ag', 'last_update': 1621265358, 'odds': {'spreads': {'odds': [2.55, 1.59], 'points': ['-1.5', '1.5']}}}, {'site_key': 'gtbets', 'site_nice': 'GTbets', 'last_update': 1621265230, 'odds': {'spreads': {'odds': [2.51, 1.58], 'points': ['-1.5', '1.5']}}}, {'site_key': 'sugarhouse', 'site_nice': 'SugarHouse', 'last_update': 1621265337, 'odds': {'spreads': {'odds': [2.55, 1.53], 'points': ['-1.5', '1.5']}}}, {'site_key': 'betrivers', 'site_nice': 'BetRivers', 'last_update': 1621265346, 'odds': {'spreads': {'odds': [2.55, 1.53], 'points': ['-1.5', '1.5']}}}, {'site_key': 'unibet', 'site_nice': 'Unibet', 'last_update': 1621265213, 'odds': {'spreads': {'odds': [2.08, 1.78], 'points': ['-1.0', '1.0']}}}, {'site_key': 'barstool', 'site_nice': 'Barstool Sportsbook', 'last_update': 1621265353, 'odds': {'spreads': {'odds': [2.55, 1.53], 'points': ['-1.5', '1.5']}}}, {'site_key': 'mybookieag', 'site_nice': 'MyBookie.ag', 'last_update': 1621265468, 'odds': {'spreads': {'odds': [2.5, 1.56], 'points': ['-1.5', '1.5']}}}, {'site_key': 'intertops', 'site_nice': 'Intertops', 'last_update': 1621265344, 'odds': {'spreads': {'odds': [2.5, 1.59], 'points': ['-1.50', '1.50']}}}], 'sites_count': 11}