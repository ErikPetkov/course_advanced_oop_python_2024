from project.restaurant import Restaurant
from unittest import TestCase,main

class TestRestaurant(TestCase):
    def setUp(self):
        self.gusto = Restaurant('Gusto',1)
        self.gusto2 = Restaurant('Gusto2',2)

    def test_init(self):
        self.assertEqual('Gusto',self.gusto.name)
        self.assertEqual(1,self.gusto.capacity)
        self.assertEqual([],self.gusto.waiters)

    def test_name_setter_error(self):
        with self.assertRaises(ValueError) as ex:
            Restaurant('',5)
        self.assertEqual("Invalid name!",str(ex.exception))

    def test_capacity_setter_error(self):
        with self.assertRaises(ValueError) as ex:
            Restaurant('test',-1)
        self.assertEqual("Invalid capacity!",str(ex.exception))

    def test_get_waiter_none(self):
        result = self.gusto.get_waiters()
        self.assertEqual([],result)

    def test_get_waiter(self):
        self.gusto.add_waiter('Ivo')
        result = self.gusto.get_waiters()
        self.assertEqual([{'name':'Ivo'}],result)

    def test_add_waiter(self):
        self.assertEqual([],self.gusto.waiters)
        self.gusto.add_waiter('Ivo')
        self.assertEqual([{'name':'Ivo'}],self.gusto.waiters)

    def test_add_waiter_reaturn_there_is_to_many(self):
        self.assertEqual([], self.gusto.waiters)
        self.gusto.add_waiter('Ivo')
        result = self.gusto.add_waiter('Ivon')
        self.assertEqual("No more places!",result)

    def test_add_waiter_that_elready_is_there(self):
        self.assertEqual([], self.gusto2.waiters)
        self.gusto2.add_waiter('Ivo')
        result = self.gusto2.add_waiter('Ivo')
        self.assertEqual("The waiter Ivo already exists!", result)

    def test_remove_waiter_found(self):
        self.gusto.add_waiter('Ivo')
        result = self.gusto.remove_waiter('Ivo')
        self.assertEqual("The waiter Ivo has been removed.",result)

    def test_remove_waiter_not_found(self):
        result = self.gusto.remove_waiter('Ivo')
        self.assertEqual("No waiter found with the name Ivo.",result)

    def test_get_total_earnings(self):
        self.gusto2.add_waiter('Ivo')
        self.gusto2.add_waiter('Ivon')
        self.gusto2.get_waiters(5,5)
        result = self.gusto2.get_total_earnings()
        self.assertEqual(0,result)





if __name__ == '__main__':
    main()