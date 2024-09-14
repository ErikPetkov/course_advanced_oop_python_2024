from project.climbing_robot import ClimbingRobot
from unittest import TestCase,main

class TestClimbingRobot(TestCase):
    def setUp(self):
        self.cr1 = ClimbingRobot('Mountain','82',8,10)

    def test_init(self):
        self.assertEqual('Mountain',self.cr1.category)
        self.assertEqual('82',self.cr1.part_type)
        self.assertEqual(8,self.cr1.capacity)
        self.assertEqual(10,self.cr1.memory)
        self.assertEqual([],self.cr1.installed_software)

    def test_category_setter_raises(self):
        with self.assertRaises(ValueError) as ex:
            cr2 = ClimbingRobot('Mount','82',8,10)
        self.assertEqual("Category should be one of "
                         "['Mountain', 'Alpine', 'Indoor', 'Bouldering']",str(ex.exception))

    def test_get_used_capacity(self):
        result = self.cr1.get_used_capacity()
        self.assertEqual(0,result)

    def test_get_available_capacity(self):
        result = self.cr1.get_available_capacity()
        self.assertEqual(8, result)

    def test_get_used_memory(self):
        result = self.cr1.get_used_memory()
        self.assertEqual(0, result)

    def test_get_available_memory(self):
        result = self.cr1.get_available_memory()
        self.assertEqual(10, result)

    def test_install_software(self):
        result = self.cr1.installed_software({'name':'updat5','capacity_consumption':2,'memory_consumption':2})
        self.assertEqual("Software 'updat5' successfully installed on 4 part.")






if __name__ == '__main__':
    main()
