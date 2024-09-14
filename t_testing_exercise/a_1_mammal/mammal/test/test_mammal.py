from project.mammal import Mammal
# All bewol is for judge
from unittest import TestCase,main
class TestMammal(TestCase):
    def setUp(self):
        self.m = Mammal('Tom', 'cat', 'Meow')

    def test_init(self):
        m = Mammal('Tom','cat','Meow')
        self.assertEqual('Tom',m.name)
        self.assertEqual('cat',m.type)
        self.assertEqual('Meow',m.sound)
        self.assertEqual('animals',m._Mammal__kingdom)

    def test_make_sound(self):
        sound = self.m.make_sound()
        self.assertEqual("Tom makes Meow",sound)

    def test_get_kingdom(self):
        kingdom = self.m.get_kingdom()
        self.assertEqual('animals',kingdom)

    def test_info(self):
        info = self.m.info()
        self.assertEqual('Tom is of type cat',info)
if __name__ == '__main__':
    main()