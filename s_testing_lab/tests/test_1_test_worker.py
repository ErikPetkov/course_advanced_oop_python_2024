# Do not submit in judge
from s_testing_lab.a_1_test_worker import Worker
#All below submit in judge

from unittest import TestCase,main

class TestWorker(TestCase):
    def test_init_worker(self):
        #Act
        w = Worker('Test', 1000,100)
        #Assert
        self.assertEqual('Test',w.name)
        self.assertEqual(1000,w.salary)
        self.assertEqual(100,w.energy)
        self.assertEqual(0,w.money)

    def test_work_worker_does_not_have_energy(self):
        #Arrange
        w = Worker('Test',1000,0)
        self.assertEqual(0, w.energy)
        self.assertEqual(0, w.money)
        #Act
        with self.assertRaises(Exception) as ex:
            w.work()

        #Assert
        self.assertEqual('Not enough energy.',str(ex.exception))
        self.assertEqual(0, w.energy)
        self.assertEqual(0, w.money)

        w = Worker('Test', 1000, -1)
        self.assertEqual(-1, w.energy)
        self.assertEqual(0, w.money)

        # Act
        with self.assertRaises(Exception) as ex:
            w.work()


        # Assert
        self.assertEqual('Not enough energy.', str(ex.exception))
        self.assertEqual(-1, w.energy)
        self.assertEqual(0, w.money)

    def test_work_worker_works(self):
        #Arrange
        w = Worker('Test', 1000, 100)
        self.assertEqual(0,w.money)
        self.assertEqual(100,w.energy)

        #Act
        w.work()

        #Assert
        self.assertEqual(1000,w.money)
        self.assertEqual(99,w.energy)

        # Act
        w.work()

        # Assert
        self.assertEqual(2000, w.money)
        self.assertEqual(98, w.energy)

    def test_rest_worker_energy_increases(self):
        #Arrange
        w = Worker('Test', 1000, 100)
        w.rest()
        self.assertEqual(101, w.energy)

    def test_get_info(self):
        w = Worker('Test', 1000, 98)
        res = w.get_info()
        self.assertEqual(f'Test has saved 0 money.',res)


        w.work()
        self.assertEqual(w.salary,w.money)
        res = w.get_info()
        self.assertEqual(f'Test has saved 1000 money.',res)





if __name__ == '__main__':
    main()