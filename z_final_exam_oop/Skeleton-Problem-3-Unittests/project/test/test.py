import unittest
from project.soccer_player import SoccerPlayer


class TestSoccerPlayer(unittest.TestCase):

    def setUp(self):
        self.player = SoccerPlayer("Lionel Messi", 34, 700, "Barcelona")

    def test_initialization(self):
        self.assertEqual(self.player.name, "Lionel Messi")
        self.assertEqual(self.player.age, 34)
        self.assertEqual(self.player.goals, 700)
        self.assertEqual(self.player.team, "Barcelona")
        self.assertEqual(self.player.achievements, {})

    def test_name_setter_too_short(self):
        with self.assertRaises(ValueError) as context:
            self.player.name = "Leo"
        self.assertEqual(str(context.exception), "Name should be more than 5 symbols!")

    def test_name_setter_valid(self):
        self.player.name = "Neymar"
        self.assertEqual(self.player.name, "Neymar")

    def test_age_setter_too_young(self):
        with self.assertRaises(ValueError) as context:
            self.player.age = 15
        self.assertEqual(str(context.exception), "Players must be at least 16 years of age!")

    def test_age_setter_valid(self):
        self.player.age = 25
        self.assertEqual(self.player.age, 25)

    def test_goals_setter_negative(self):
        self.player.goals = -5
        self.assertEqual(self.player.goals, 0)

    def test_goals_setter_valid(self):
        self.player.goals = 100
        self.assertEqual(self.player.goals, 100)

    def test_team_setter_invalid_team(self):
        with self.assertRaises(ValueError) as context:
            self.player.team = "Invalid Team"
        self.assertEqual(str(context.exception), "Team must be one of the following: Barcelona, Real Madrid, Manchester United, Juventus, PSG!")

    def test_team_setter_valid(self):
        self.player.team = "Real Madrid"
        self.assertEqual(self.player.team, "Real Madrid")

    def test_change_team_success(self):
        result = self.player.change_team("Real Madrid")
        self.assertEqual(self.player.team, "Real Madrid")
        self.assertEqual(result, "Team successfully changed!")

    def test_change_team_invalid(self):
        result = self.player.change_team("Invalid Team")
        self.assertEqual(self.player.team, "Barcelona")
        self.assertEqual(result, "Invalid team name!")

    def test_add_new_achievement(self):
        result = self.player.add_new_achievement("Ballon d'Or")
        self.assertEqual(self.player.achievements["Ballon d'Or"], 1)
        self.assertEqual(result, "Ballon d'Or has been successfully added to the achievements collection!")

    def test_add_existing_achievement(self):
        self.player.add_new_achievement("Ballon d'Or")
        result = self.player.add_new_achievement("Ballon d'Or")
        self.assertEqual(self.player.achievements["Ballon d'Or"], 2)
        self.assertEqual(result, "Ballon d'Or has been successfully added to the achievements collection!")

    def test_add_achievement_edge_case(self):
        long_achievement_name = "A" * 1000
        result = self.player.add_new_achievement(long_achievement_name)
        self.assertEqual(result, f"{long_achievement_name} has been successfully added to the achievements collection!")
        self.assertEqual(self.player.achievements[long_achievement_name], 1)

    def test_lt_operator(self):
        other_player = SoccerPlayer("Cristiano Ronaldo", 36, 750, "Juventus")
        result = self.player < other_player
        self.assertEqual(result, "Cristiano Ronaldo is a top goal scorer! S/he scored more than Lionel Messi.")

        other_player.goals = 600
        result = self.player < other_player
        self.assertEqual(result, "Lionel Messi is a better goal scorer than Cristiano Ronaldo.")

    def test_lt_operator_equal_goals(self):
        player2 = SoccerPlayer("Another Player", 30, 700, "PSG")
        result = self.player < player2
        self.assertEqual(result, "Lionel Messi is a better goal scorer than Another Player.")

    def test_lt_operator_equal_goals_different_ages(self):
        younger_player = SoccerPlayer("Young Player", 20, 700, "Barcelona")
        result = self.player < younger_player
        self.assertEqual(result, "Lionel Messi is a better goal scorer than Young Player.")

    def test_lt_operator_equal_goals_different_teams(self):
        player_different_team = SoccerPlayer("Different Team Player", 34, 700, "PSG")
        result = self.player < player_different_team
        self.assertEqual(result, "Lionel Messi is a better goal scorer than Different Team Player.")


if __name__ == '__main__':
    unittest.main()