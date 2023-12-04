

class StudentManager:
    def __init__(self):
        self.students = {}

    def validate_add_student(self, student_id, name, grade):
        self.validate_student_id(student_id)
        if student_id in self.students:
            raise ValueError("Student ID must be unique")
        self.validate_name(name)
        self.validate_grade(grade)

    def validate_update_grade(self, student_id, new_grade):
        self.validate_student_id(student_id)
        self.validate_grade(new_grade)

    def validate_student_id(self, student_id):
        if not isinstance(student_id, int):
            raise ValueError("Student ID must be an integer")

    def validate_name(self, name):
        if not isinstance(name, str):
            raise ValueError("Name must be a string")

    def validate_grade(self, grade):
        if not isinstance(grade, (int, float)):
            raise ValueError("Grade must be a number")
        if not (0 <= grade <= 100):
            raise ValueError("Grade must be between 0 and 100")

    def add_student(self, student_id, name, grade):
        self.validate_add_student(student_id, name, grade)
        self.add_student_to_database(student_id)
        self.students[student_id] = {'name': name, 'grade': grade}

    def remove_student(self, student_id):
        self.validate_student_id(student_id)
        self.remove_student_from_database(student_id)
        self.students.pop(student_id, None)

    def remove_student_from_database(self, student_id):
        pass

    def add_student_to_database(self, student_id):
        pass

    def get_student_info(self, student_id):
        self.validate_student_id(student_id)
        return self.students.get(student_id, None)

    def get_all_students(self):
        return self.students.copy()

    def update_grade(self, student_id, new_grade):
        self.validate_update_grade(student_id, new_grade)
        if student_id in self.students:
            self.students[student_id]['grade'] = new_grade


# Пример использования
if __name__ == "__main__":
    student_manager = StudentManager()

    # Добавление студентов
    student_manager.add_student(1, 'Alexander', 90)
    student_manager.add_student(2, 'Nikita', 85)
    student_manager.add_student(3, 'Eugene', 78)

    # Получение информации о студентах
    print("Student №1:", student_manager.get_student_info(1))
    print("All students:", student_manager.get_all_students())

    # Обновление оценки
    student_manager.update_grade(2, 88)
    print("Updated grade for student №2:", student_manager.get_student_info(2))

    # Удаление студента
    student_manager.remove_student(3)
    print("All students after removing student №3:", student_manager.get_all_students())
