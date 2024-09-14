from s_testing_lab.b_2_test_cat import Cat
#Paste all bewol to judge
from unittest import TestCase,main
class Test_cat(TestCase):

    def test_init_on_cat(self):
        c = Cat('Eva')
        self.assertEqual('Eva',c.name)
        self.assertEqual(False,c.fed)
        self.assertEqual(False,c.sleepy)
        self.assertEqual(0,c.size)

    def test_eat_cat(self):
        c = Cat('Eva')
        self.assertEqual(False, c.fed)
        self.assertEqual(False, c.sleepy)
        self.assertEqual(0, c.size)
        c.eat()
        self.assertEqual(True, c.fed)
        self.assertEqual(True, c.sleepy)
        self.assertEqual(1, c.size)
    def test_eat_cat_already_fed(self):
        c = Cat('Eva')
        c.eat()
        with self.assertRaises(Exception) as ex:
            c.eat()
        self.assertEqual('Already fed.',str(ex.exception))

    def test_sleep_not_fed_error(self):
        c = Cat('Eva')
        with self.assertRaises(Exception) as ex:
            c.sleep()
        self.assertEqual('Cannot sleep while hungry',str(ex.exception))

    def test_cat_sleep_succses(self):
        c = Cat('Eva')
        c.eat()
        c.sleep()
        self.assertEqual(False,c.sleepy)


if __name__ == '__main__':
    main()