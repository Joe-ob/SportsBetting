from app.odds_seeker import match_team

Mock_list_1 = ["a", "b", "c"]
Mock_list_2 = ["a", "b", "c", "d", "e", "f"]
Mock_list_3 = ["x", "y", "z"]

def Test_if_Teams_Match():
    assert match_team(Mock_list_1, Mock_list_2) == True
    assert match_team(Mock_list_3, Mock_list_2) == False