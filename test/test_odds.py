from apps.odds_seeker import match_team

Mock_list_1 = ["a", "b", "c"]
Mock_list_2 = ["a", "b", "c", "d", "e", "f"]
Mock_list_3 = ["x", "y", "z"]

#valid_result = match_team(Mock_list_1, Mock_list_2)
#print(valid_result)
for item in Mock_list_1:
    def test_match_team():
        valid_result = match_team(item, Mock_list_2)
        assert valid_result == True
#for item in Mock_list_3:
#        failed_result = match_team(Mock_list_3, Mock_list_2)
#        assert failed_result == False