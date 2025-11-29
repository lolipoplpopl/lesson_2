from models import Student


class TestCRUDOperations:
    def test_create_student(self, db_session):
        new_student = Student(name="Иван Тестовый", age=20)
        db_session.add(new_student)
        db_session.commit()

        student_from_db = db_session.query(Student).filter_by(
            name="Иван Тестовый"
        ).first()
        assert student_from_db is not None
        assert student_from_db.name == "Иван Тестовый"
        assert student_from_db.age == 20

    def test_update_student(self, db_session):
        student = Student(name="Петр Обновляемый", age=25)
        db_session.add(student)
        db_session.commit()

        student_to_update = db_session.query(Student).filter_by(
            name="Петр Обновляемый"
        ).first()
        student_to_update.age = 26
        db_session.commit()

        updated_student = db_session.query(Student).filter_by(
            name="Петр Обновляемый"
        ).first()
        assert updated_student.age == 26

    def test_delete_student(self, db_session):
        student = Student(name="Сергей Удаляемый", age=30)
        db_session.add(student)
        db_session.commit()

        student_to_delete = db_session.query(Student).filter_by(
            name="Сергей Удаляемый"
        ).first()
        db_session.delete(student_to_delete)
        db_session.commit()

        deleted_student = db_session.query(Student).filter_by(
            name="Сергей Удаляемый"
        ).first()
        assert deleted_student is None
