from project.tennis_player import TennisPlayer
from unittest import TestCase,main

class TestTennisPlayer(TestCase):
    def setUp(self):
        self.tplayer1 = TennisPlayer('Ivo',20,400)
        self.tplayer2 = TennisPlayer('Emo',25,600)
        self.tplayer3 = TennisPlayer('Iva',24,800)

    def test_init(self):
        self.assertEqual('Ivo',self.tplayer1.name)
        self.assertEqual(20, self.tplayer1.age)
        self.assertEqual(400, self.tplayer1.points)
        self.assertEqual([], self.tplayer1.wins)

    def test_name_seter_raises(self):
        with self.assertRaises(ValueError) as ex:
            TennisPlayer('Iv',20,400)
        self.assertEqual("Name should be more than 2 symbols!",str(ex.exception))

        # with one leter
        with self.assertRaises(ValueError) as ex:
            TennisPlayer('I',20,400)
        self.assertEqual("Name should be more than 2 symbols!",str(ex.exception))

    def test_age_seter_raises(self):
        with self.assertRaises(ValueError) as ex:
            TennisPlayer('Ivo',17,400)
        self.assertEqual("Players must be at least 18 years of age!",str(ex.exception))

    def test_add_new_win_to_not_existing_player_shoud_add(self):
        result = self.tplayer1.add_new_win('Brishbase 2024')
        self.assertEqual(['Brishbase 2024'],self.tplayer1.wins)
        self.assertIsNone(result)


    def test_add_same_win_to_player(self):
        self.tplayer1.add_new_win('Brishbase 2024')
        result = self.tplayer1.add_new_win('Brishbase 2024')
        self.assertEqual('Brishbase 2024 has been already added to the list of wins!',result)

    def test_lt_other_is_beter_than_self(self):
        result = self.tplayer1.__lt__(self.tplayer2)
        self.assertEqual('Emo is a top seeded player and he/she is better than Ivo',result)

    def test_lt_self_is_beter_than_other(self):
        result = self.tplayer2.__lt__(self.tplayer1)
        self.assertEqual('Emo is a better player than Ivo',result)

    def test_str_representation(self):
        self.tplayer1.add_new_win('Brishbase 2024')
        self.tplayer1.add_new_win('Brishbase 2023')
        result = self.tplayer1.__str__()
        self.assertEqual("Tennis Player: Ivo\nAge: 20\nPoints: 400.0\nTournaments won: Brishbase 2024, Brishbase 2023",result)


if __name__ == '__main__':
    main()