from apps.odds_seeker import match_team


Mock_list_1 = ["a", "b", "c"]
Mock_list_2 = ["x", "y", "z"]



def test_match_fail():
    for item in Mock_list_2:
        assert match_team(Mock_list_1, Mock_list_2) == False