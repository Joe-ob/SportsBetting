from apps.odds_seeker import match_team

Mock_list_1 = ["a", "b", "c"]
Mock_list_2 = ["a", "b", "c", "d", "e", "f"]
Mock_list_3 = ["x", "y", "z"]

#valid_result = match_team(Mock_list_1, Mock_list_2)
#print(valid_result)
def test_match_team():
    valid_result = match_team(Mock_list_1, Mock_list_2)
    assert valid_result == True
    assert match_team(Mock_list_3, Mock_list_2) == False