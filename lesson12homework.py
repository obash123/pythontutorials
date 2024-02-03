# student_answers = {
#     1: ['A', 'B'],
#     2: ['C'],
#     3: ['A', 'C', 'D']
# }

# correct_answers = {
#     1: ['A', 'B'],
#     2: ['C', 'D'],
#     3: ['A', 'C', 'D']
# }

# def grade_test(student_answers, correct_answers):

#     score = 0

#     for question_num in student_answers:
#         student_choices = student_answers[question_num]
#         correct_choices = correct_answers.get(question_num, [])
 
#         if student_choices == correct_choices:
#             score += 1
            
#     return score


# score = grade_test(student_answers, correct_answers)
# print("Student's score:", score)


class TestGrader:
    def __init__(self):
        self.score = 0


    def grade_test(self,student_answers,correct_answers):
        for question_num in student_answers:
            student_choices = student_answers[question_num]
            correct_choices = correct_answers.get(question_num, [])

            if student_choices == correct_choices:
                self.score += 1
        return self.score
    




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

test_grader = TestGrader()
score = test_grader.grade_test(student_answers,correct_answers)

get_score = test_grader.score
print(get_score)
print("Student's score:", score)