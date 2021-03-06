from input_data import *

class TestClassroom:
    
    student = Classroom()
    teacher = Classroom()

    def test_create_table(self):
        """
        :return: checks table name exist or not
        """
        table_name = "student_data"
        table_dict = self.student.create_table()
        assert table_name in table_dict, "Table not created"

    def test_insert_student_data(self):
        """
        :return: check if rows inserted or not
        """
        row_count = self.student.insert_student_data("santosh", 26, "B-tech")
        assert row_count == 1, "Data not inserted"

    def test_update_student_name(self):
        """return: the updated value
        """
        value = "soumya"
        update_value = self.student.update_row_student(value)
        assert value in update_value, "Data not updated"

    def test_delete_student_data(self):
        """return: count if data deleted or not.
        """
        count_deleted_data = self.student.delete_row_student()
        assert count_deleted_data == 0, "Data not deleted"

    def test_create_table_teacher(self):
        """
        :return: checks table name exist or not
        """
        table_name = "teacher_data"
        table_dict = self.teacher.create_table()
        assert table_name in table_dict, "Table not created"

    def test_insert_teacher_data(self):
        """
        :return: check if rows inserted or not
        """
        row_count = self.teacher.insert_teacher_data("Ashis",1)
        assert row_count == 1, "Data not inserted"

    def test_update_teacher_name(self):
        """return: the updated value
        """
        value = "Ashis Ogale"
        update_value = self.teacher.update_row_teacher(value)
        assert value in update_value, "Data not updated"

    def test_delete_teacher_data(self):
        """return: count if data deleted or not.
        """
        count_deleted_data = self.teacher.delete_row_teacher()
        assert count_deleted_data == 0, "Data not deleted"