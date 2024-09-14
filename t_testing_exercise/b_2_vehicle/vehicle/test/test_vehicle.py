from project.vehicle import Vehicle
from unittest import TestCase,main

class TestVehicle(TestCase):

    def setUp(self):
        self.v = Vehicle(100,100)

    def test_init(self):
        self.assertEqual(100,self.v.fuel)
        self.assertEqual(100,self.v.capacity)
        self.assertEqual(100,self.v.horse_power)
        self.assertEqual(1.25,self.v.fuel_consumption)

    def test_drive_fuel(self):
        self.v.drive(10)
        self.assertEqual(87.5,self.v.fuel)

    def test_drive_fuel_not_enought_raises(self):
        with self.assertRaises(Exception) as ex:
            self.v.drive(81)
        self.assertEqual("Not enough fuel",str(ex.exception))

    def test_fuel_refils(self):
        self.v.drive(10)
        self.assertEqual(87.5, self.v.fuel)

        self.v.refuel(7.5)
        self.assertEqual(95,self.v.fuel)

    def test_refuel_full_tank_raises_error(self):
        with self.assertRaises(Exception) as ex:
            self.v.refuel(1)
        self.assertEqual("Too much fuel",str(ex.exception))

    def test_string_representation(self):
        self.assertEqual(f"The vehicle has 100 " \
                         f"horse power with 100 fuel left and 1.25 fuel consumption",
                         self.v.__str__())


if __name__ == '__main__':
    main()