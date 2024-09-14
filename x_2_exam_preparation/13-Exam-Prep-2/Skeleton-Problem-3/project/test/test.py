from project.robot import Robot
from unittest import TestCase,main

class TestRobot(TestCase):
    def setUp(self):
        self.military_robot = Robot('s888','Military',50,100)
        self.education_robot = Robot('s883','Education',40,70)
        self.educations_robot = Robot('s882','Education',30,70)

    def test_init(self):
        self.assertEqual('s888',self.military_robot.robot_id)
        self.assertEqual('Military',self.military_robot.category)
        self.assertEqual(50,self.military_robot.available_capacity)
        self.assertEqual(100,self.military_robot.price)
        self.assertEqual([],self.military_robot.hardware_upgrades)
        self.assertEqual([],self.military_robot.software_updates)

    def test_catecory_setter_raises(self):
        with self.assertRaises(ValueError) as ex:
            Robot('b856','Baker',20,80)
        self.assertEqual("Category should be one of '['Military', 'Education', 'Entertainment', 'Humanoids']'",str(ex.exception))

    def test_price_setter_raises(self):
        with self.assertRaises(ValueError) as ex:
            Robot('b856', 'Education', 20, -1)
        self.assertEqual("Price cannot be negative!",str(ex.exception))


    def test_upgrade_was_upgraded(self):
        result = self.education_robot.upgrade('bolt',5)
        self.assertEqual(f'Robot s883 was upgraded with bolt.',result)

    def test_upgrade_was_not_upgraded(self):
        self.education_robot.upgrade('bolt', 5)
        result = self.education_robot.upgrade('bolt', 5)
        self.assertEqual(f"Robot s883 was not upgraded.", result)

    def test_update_was_upgraded(self):
        result = self.military_robot.update(8.5,5)
        self.assertEqual('Robot s888 was updated to version 8.5.',result)

    def test_update_was_not_updated(self):
        self.military_robot.update(8.5, 5)
        result = self.military_robot.update(8.5, 5)
        self.assertEqual("Robot s888 was not updated.", result)

    def test_military_robot_greater_than_education_robot(self):
        result = self.military_robot.__gt__(self.education_robot)
        self.assertEqual(f'Robot with ID s888 is more expensive than Robot with ID s883.',result)

    def test_education_robot_is_not_greater_than_military_robot(self):
        result = self.education_robot.__gt__(self.military_robot)
        self.assertEqual('Robot with ID s883 is cheaper than Robot with ID s888.', result)

    def test_education_robot_is_equal_to_educations_robot(self):
        result = self.education_robot.__gt__(self.educations_robot)
        self.assertEqual('Robot with ID s883 costs equal to Robot with ID s882.', result)


if __name__ == '__main__':
    main()