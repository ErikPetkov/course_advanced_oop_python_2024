from project.hero import Hero
from unittest import TestCase,main

class TestHero(TestCase):

    def setUp(self):
        self.hero = Hero('Ivo',5,10.0,2.5)

    def test_init(self):
        self.assertEqual('Ivo',self.hero.username)
        self.assertEqual(5,self.hero.level)
        self.assertEqual(10,self.hero.health)
        self.assertEqual(2.5,self.hero.damage)

    def test_battle_hero_fights_himself_raises(self):
        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.hero)
        self.assertEqual("You cannot fight yourself",str(ex.exception))

    def test_batlle_hero_has_less_health_or_equal_to_zero(self):
        h = Hero('Test', 5, 0, 2.5)
        with self.assertRaises(ValueError) as ex:
            h.battle(self.hero)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest",str(ex.exception))

        # Less than zero health
        h = Hero('Test', 5, -1, 2.5)
        with self.assertRaises(ValueError) as ex:
            h.battle(self.hero)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ex.exception))

    def test_batlle_enemy_has_less_health_or_equal_to_zero(self):
        e = Hero('Test', 5, 0, 2.5)
        with self.assertRaises(ValueError) as ex:
            self.hero.battle(e)
        self.assertEqual("You cannot fight Test. He needs to rest",str(ex.exception))

        # Less than zero health
        e = Hero('Test', 5, -1, 2.5)
        with self.assertRaises(ValueError) as ex:
            self.hero.battle(e)
        self.assertEqual("You cannot fight Test. He needs to rest", str(ex.exception))

    def test_battle_hero_draw(self):
        e = Hero('Test', 5, 10, 2.5)
        self.assertEqual('Draw',self.hero.battle(e))

    def test_battle_hero_wins(self):
        e = Hero('Test', 1, 5, 1)
        self.assertEqual('You win',self.hero.battle(e))

    def test_battle_hero_lose(self):
        e = Hero('Test', 5, 20, 2.5)
        self.assertEqual('You lose',self.hero.battle(e))


if __name__ == '__main__':
    main()
