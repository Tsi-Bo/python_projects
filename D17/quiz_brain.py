class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list


    def next_question(self):
        curr_question = self.question_list[self.question_number]
        self.question_number += 1
        input(f"Q.{self.question_number}: {curr_question.text} (True/False)?: ")