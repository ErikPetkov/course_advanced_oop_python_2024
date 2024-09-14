import unittest

from project.hero import Hero


class HeroTest(unittest.TestCase):
    username = 'Test Hero'
    level = 5
    health = 50.5
    damage = 10.6

    def setUp(self):
        self.hero = Hero(self.username, self.level, self.health, self.damage)

    def test_init(self):
        self.assertEqual(self.username, self.hero.username)
        self.assertEqual(self.level, self.hero.level)
        self.assertEqual(self.health, self.hero.health)
        self.assertEqual(self.damage, self.hero.damage)

    def test_enemy_hero_has_the_same_name(self):
        enemy = Hero(self.username, 3, 333.3, 33.3)
        with self.assertRaises(Exception) as ex:
            self.hero.battle(enemy)
        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_hero_health_is_not_enough(self):
        self.hero.health = 0
        enemy = Hero("Enemy", 12, 30, 50)

        with self.assertRaises(ValueError) as e:
            self.hero.battle(enemy)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(e.exception))

        self.hero.health = -1
        with self.assertRaises(ValueError) as e:
            self.hero.battle(enemy)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(e.exception))

    def test_enemy_health_is_not_enough(self):
        enemy = Hero("Enemy", 12, 0, 50)

        with self.assertRaises(ValueError) as e:
            self.hero.battle(enemy)
        self.assertEqual("You cannot fight Enemy. He needs to rest", str(e.exception))

        enemy.health = -1
        with self.assertRaises(ValueError) as e:
            self.hero.battle(enemy)
        self.assertEqual("You cannot fight Enemy. He needs to rest", str(e.exception))

    def test_draw(self):
        enemy = Hero("Enemy", self.level, self.health, self.damage)

        result = self.hero.battle(enemy)
        self.assertEqual(5, self.hero.level)
        self.assertEqual(-2.5, self.hero.health)
        self.assertEqual(10.6, self.hero.damage)
        self.assertEqual("Draw", result)

    def test_hero_win(self):
        enemy = Hero("Enemy", 1, 1, 1)

        result = self.hero.battle(enemy)
        self.assertEqual(6, self.hero.level)
        self.assertEqual(54.5, self.hero.health)
        self.assertEqual(15.6, self.hero.damage)
        self.assertEqual("You win", result)

    def test_hero_lose(self):
        self.hero.health = 10
        self.hero.damage = 10
        enemy = Hero("Enemy", 100, 100, 100)

        result = self.hero.battle(enemy)
        self.assertEqual(101, enemy.level)
        self.assertEqual(55, enemy.health)
        self.assertEqual(105, enemy.damage)
        self.assertEqual("You lose", result)

    def test_str(self):
        expected = f"Hero {self.username}: {self.level} lvl\n" \
                   f"Health: {self.health}\n" \
                   f"Damage: {self.damage}\n"
        self.assertEqual(expected, str(self.hero))


if __name__ == '__main__':
    unittest.main()