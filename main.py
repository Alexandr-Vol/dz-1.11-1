class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def __lt__(self, other_student):
        if not isinstance(other_student, Student):

            return self._get_avg_grades() < other_student._get_avg_grades()

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance((lecturer, Lecturer)
                      and course in self.courses_attached
                      and course in lecturer.courses_in_progress
                      and grade in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]):
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        best_student = [list_grades for all_grades in self.grades.values()
                        for list_grades in all_grades]
        return (f"Имя: {self.name}\n"f"Фамилия: {self.surname}\n"
                f"Средняя оценка за домашние задания: {self.rate_Mentor()}\n"
                f"Курсы в процессе изучения: {', '.join(self.courses_in_progress)}\n"
                f"Завершенные курсы: {', '.join(self.courses_attached)}")


def total_hw_grade(students, course):
    hw_grades = []
    for student in students:
        if course in student.grades:
            hw_grades.extend(student.grades[course])
    return sum(hw_grades)/len(hw_grades)


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grades = {}
        self.rate_hw = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = []

    def av_gr(self):
        sum_gr = 0
        len_gr = 0
        for course in self.grades.values():
            sum_gr += sum(course)
            len_gr += len(course)
            average_grade = round(sum_gr / len_gr)

    def __str__(self):
        list_grades = [list_grades for all_grades in self.grades.values()
                       for list_grades in all_grades]
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за лекции: {self.av_gr()}")


def total_lect_grade(lecturers, course):
    lect_grades = []
    for lecturer in lecturers:
        if course in lecturer.grades:
            lect_grades.extend(lecturer.grades[course])
    return sum(lect_grades)/len(lect_grades)


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance((student, Student)
                      and course in self.courses_attached
                      and course in student.courses_in_progress
                      and grade in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]):
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']

print(best_student.grades)

cool_mentor = Mentor('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']

cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
some_reviewer = Reviewer('Some', 'Buddy')
some_lecturer = Lecturer('Some', 'Buddy', grades=())
some_student = Student('Ruoy', 'Eman', 'your_gender')

print(some_lecturer)
print(some_reviewer)
print(some_student)
