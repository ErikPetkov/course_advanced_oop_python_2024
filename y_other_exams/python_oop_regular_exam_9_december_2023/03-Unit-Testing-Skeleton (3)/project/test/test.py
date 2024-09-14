from project.railway_station import RailwayStation
from unittest import TestCase,main
from collections import deque

class TestRailwayStation(TestCase):
    def setUp(self):
        self.stancion = RailwayStation('Sofia')

    def test_init(self):
        self.assertEqual('Sofia',self.stancion.name)
        self.assertEqual(deque(),self.stancion.arrival_trains)
        self.assertEqual(deque(),self.stancion.departure_trains)


    def test_name_setter(self):
        with self.assertRaises(ValueError) as ex:
            RailwayStation('po')
        self.assertEqual("Name should be more than 3 symbols!",str(ex.exception))
        with self.assertRaises(ValueError) as ex:
            RailwayStation('pol')
        self.assertEqual("Name should be more than 3 symbols!", str(ex.exception))

    def test_new_arrival_on_board(self):
        self.stancion.arrival_trains.append('train1')
        expect = deque()
        expect.append('train1')
        self.assertEqual(expect,self.stancion.arrival_trains)

    def test_train_has_arrived(self):
        self.stancion.arrival_trains.append('train1')
        result = self.stancion.train_has_arrived('train1')
        self.assertEqual("train1 is on the platform and will leave in 5 minutes.",result)

    def test_train_has_arrived_sooner(self):
        self.stancion.arrival_trains.append('train1')
        self.stancion.arrival_trains.append('train2')
        result = self.stancion.train_has_arrived('train2')
        self.assertEqual("There are other trains to arrive before train2.",result)

    def test_train_has_left_sucsesfuly(self):
        self.stancion.arrival_trains.append('train2')
        self.stancion.train_has_arrived('train2')
        result = self.stancion.train_has_left('train2')
        self.assertEqual(True,result)

    def test_train_has_left_sucsesfuly(self):
        self.stancion.arrival_trains.append('train1')
        self.stancion.arrival_trains.append('train2')
        self.stancion.train_has_arrived('train2')
        result = self.stancion.train_has_left('train1')
        self.assertEqual(False,result)

if __name__ == '__main__':
    main()