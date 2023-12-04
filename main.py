class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_Lecturer(self, lecturer, course, grade):
        if isinstance((lecturer, Lecturer)
                      and course in self.courses_attached
                      and course in lecturer.courses_in_progress):
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        for value in Student.grades.values():
                countlen += len(value)
                for item in value:
                    count += item
                return round(count/countlen, 2)

        return (f"Имя: {self.name}\n"f"Фамилия: {self.surname}\n"
                f"Средняя оценка за домашние задания: {self.rate_Mentor()}\n"
                f"Курсы в процессе изучения: {', '.join(self.courses_in_progress)}\n"
                f"Завершенные курсы: {', '.join(self.courses_attached)}")


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):

    def __init__(self, name, surname, grades):
        super().__init__(name, surname)
        self.grades = {}

    def Lecturer(self):
        for value in Lecturer.grades.values():
            countlen += len(value)
            for item in value:
                count += item
            return round(count/countlen, 2)

    def __str__(self):
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за лекции: {self.Lecturer()}")


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance((student, Student)
                      and course in self.courses_attached
                      and course in student.courses_in_progress):
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f"Имя: {self.name} \nФамилия: {self.surname}"


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']

cool_mentor = Mentor('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']

cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
some_reviewer = Reviewer('Some', 'Buddy')
some_lecturer = Lecturer('Some', 'Buddy', grades=())
some_student = Student('Ruoy', 'Eman', 'your_gender')

print(best_student.grades)
print(some_student)
print(some_lecturer)
print(some_reviewer)
