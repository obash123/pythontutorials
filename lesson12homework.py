student_answers = {
    1: ['A', 'B'],
    2: ['C'],
    3: ['A', 'C', 'D']
}

correct_answers = {
    1: ['A', 'B'],
    2: ['C', 'D'],
    3: ['A', 'C', 'D']
}

def grade_test(student_answers, correct_answers):

    score = 0

    for question_num in student_answers:
        student_choices = student_answers[question_num]
        correct_choices = correct_answers.get(question_num, [])
 
        if student_choices == correct_choices:
            score += 1
            
    return score


score = grade_test(student_answers, correct_answers)
print("Student's score:", score)


class TestGrader:
    def __init__(self, student_answers, correct_answers):
        self.student_answers = student_answers
        self.correct_answers = correct_answers

    def grade_test(self):
        score = 0
        for question_num in self.student_answers:
            student_choices = self.student_answers[question_num]
            correct_choices = self.correct_answers.get(question_num, [])

            if student_choices == correct_choices:
                score += 1
        return score



student_answers = {
    1: ['A', 'B'],
    2: ['C'],
    3: ['A', 'C', 'D']
}

correct_answers = {
    1: ['A', 'B'],
    2: ['C', 'D'],
    3: ['A', 'C', 'D']
}

test_grader = TestGrader(student_answers, correct_answers)
score = test_grader.grade_test()
print("Student's score:", score)