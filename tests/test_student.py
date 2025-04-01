from school_schedule.student import Student

def test_class_student_instantion():
    # Arrange
    name = "Masha"
    grade = 11
    classes = ["Math", "Chemistry"]

    # Act

    student = Student(name, grade, classes)

    # Accert

    assert student.name == name
    assert student.grade == grade
    assert student.classes == classes


def test_add_single_class():

    # Arrange
    name = "Masha"
    grade = 11
    classes = ["Math", "Chemistry"]
    new_class = "Biology"
    student = Student(name, grade, classes)

    # Act
    new_classes = student.add_class(new_class)

    # Accert
    assert student.classes == new_classes
    assert student.classes == ["Math", "Chemistry", "Biology"]

def test_get_num_classes():
    # Arrange
    name = "Masha"
    grade = 11
    classes = ["Math", "Chemistry"]
    student = Student(name, grade, classes)

    # Act
    num_classes = student.get_num_classes()

    # Accert
    assert num_classes == len(classes)
    assert num_classes == 2

def test_display_classes():
    # Arrange
    name = "Masha"
    grade = 11
    classes = ["Math", "Chemistry"]
    student = Student(name, grade, classes)

    # Act
    string_classes = student.display_classes()

    # Accert
    assert string_classes == "Math, Chemistry"


def test_display_empty_classes():
    # Arrange
    name = "Masha"
    grade = 11
    classes = []
    student = Student(name, grade, classes)

    # Act
    string_classes = student.display_classes()

    # Accert
    assert string_classes == ""


def test_summary():
    # Arrange
    name = "Masha"
    grade = 11
    classes = ["Math", "Chemistry"]
    student = Student(name, grade, classes)

    # Act
    string_summary = student.summary()

    # Accert
    assert string_summary == "Masha is a 11 enrolled in 2 classes: Math, Chemistry"
