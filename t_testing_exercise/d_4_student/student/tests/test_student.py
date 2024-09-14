from unittest import TestCase,main
from project.student import Student

class TestStudent(TestCase):

    def setUp(self):
        self.s1 = Student('Ivo')
        self.s2 = Student('Emo',{'OOP advanced':[]})

    def test_init(self):
        self.assertEqual('Ivo',self.s1.name)
        self.assertEqual({},self.s1.courses)
        # s2
        self.assertEqual('Emo', self.s2.name)
        self.assertEqual({'OOP advanced':[]}, self.s2.courses)

    def test_enroll_create_and_add_notes(self):
        cours = self.s1.enroll('basic', '')
        self.assertEqual("Course and course notes have been added.",cours)

    def test_enroll_update_notes_course(self):
        cours = self.s1.enroll('basic','')
        cours = self.s1.enroll('basic','')
        self.assertEqual("Course already added. Notes have been updated.",cours)

    def test_enroll_create_course(self):
        cours = self.s1.enroll('basic', 'njjh','N')
        self.assertEqual("Course has been added.", cours)

    def test_add_notes_cucsesful(self):
        res = self.s2.add_notes('OOP advanced','note')
        self.assertEqual("Notes have been updated",res)

    def test_add_notes_course_not_in_courses_raises(self):
        with self.assertRaises(Exception) as ex:
            self.s1.add_notes('bass','hi')
        self.assertEqual("Cannot add notes. Course not found.",str(ex.exception))

    def test_leave_course_sucsessfuly(self):
        res = self.s2.leave_course('OOP advanced')
        self.assertEqual("Course has been removed",res)

    def test_leave_course_course_not_in_courses_raises(self):
        with self.assertRaises(Exception) as ex:
            self.s1.leave_course('music')
        self.assertEqual("Cannot remove course. Course not found.",str(ex.exception))




if __name__ == '__main__':
    main()