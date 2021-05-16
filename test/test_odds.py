from app.odds_seeker import Match_Team

Mock_list_1 = ["a", "b", "c"]
Mock_list_2 = ["f", "e", "d", "c", "b", "a"]
Mock_list_3 = ["x", "y", "z"]

def Test_if_Teams_Match():
    assert Match_Team(Mock_list_1, Mock_list_2) == True
    assert Match_Team(Mock_list_3, Mock_list_2) == False