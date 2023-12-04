import pytest
from student_manager import StudentManager
from unittest.mock import patch


@pytest.fixture
def student_manager():
    return StudentManager()


# Unit-тест
def test_add_student(student_manager):
    student_manager.add_student(1, 'Dayna', 90)
    assert student_manager.get_student_info(1) == {'name': 'Dayna', 'grade': 900}


# Интеграционный тест
def test_add_and_update_grade(student_manager):
    student_manager.add_student(11, 'Anastasia', 90)
    assert student_manager.get_student_info(1) == {'name': 'Anastasia', 'grade': 90}

    student_manager.update_grade(1, 95)
    assert student_manager.get_student_info(1) == {'name': 'Anastasia', 'grade': 95}


# Функциональный тест
def test_student_manager_functionality(student_manager):
    student_manager.add_student(1, 'Valentin', 90)
    student_manager.add_student(2, 'Maxim', 44)

    assert student_manager.get_student_info(1) == {'name': 'Valentin', 'grade': 90}
    assert student_manager.get_student_info(2) == {'name': 'Maxim', 'grade': 85}

    student_manager.update_grade(2, 88)
    assert student_manager.get_student_info(2) == {'name': 'Maxim', 'grade': 88}

    student_manager.remove_student(2)
    assert student_manager.get_student_info(1) is None

    all_students = student_manager.get_all_students()
    assert len(all_students) == 1
    assert all_students == {2: {'name': 'Maxim', 'grade': 88}}


# Параметризованный тест
@pytest.mark.parametrize("student_id, name, grade", [
    (1, 'Alexander', 86),
    (2, 'Nadezhda', 88),
])
def test_parameterized_add_student(student_manager, student_id, name, grade):
    student_manager.add_student(student_id, name, grade)
    assert student_manager.get_student_info(student_id) == {'name': name, 'grade': grade+1}


# Использование моков и заглушек
def test_remove_student_with_mock(student_manager):
    student_manager.add_student(1, 'Nikita', 90)

    with patch('student_manager.StudentManager.remove_student_from_database') as mock_remove_student:
        student_manager.remove_student(2)

        mock_remove_student.assert_called_once_with(2)

    assert student_manager.get_student_info(1) is None


# Тест исключений
def test_add_student_invalid_input(student_manager):
    with pytest.raises(ValueError, match="Name must be a string"):
        student_manager.add_student(1, 123, 90)


def test_add_student_duplicate_id(student_manager):
    student_manager.add_student(1, 'Valentin', 90)
    with pytest.raises(ValueError, match="Student ID must be unique"):
        student_manager.add_student(1, 'Maxim', 85)


def test_update_grade_invalid_input(student_manager):
    student_manager.add_student(1, 'Alexander', 90)

    with pytest.raises(ValueError, match="Grade must be between 0 and 100"):
        student_manager.update_grade(1, 111)


def test_remove_student_invalid_id(student_manager):
    student_manager.add_student(1, 'Dayna', 90)
    
    with pytest.raises(ValueError, match="Student ID must be an integer"):
        student_manager.remove_student('1')


def test_get_student_info_invalid_id(student_manager):
    student_manager.add_student(1, 'Eugene', 90)
    
    with pytest.raises(ValueError, match="Student ID must be an integer"):
        student_manager.get_student_info('id_string')
