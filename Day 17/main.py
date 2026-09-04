# class User:
#     def __init__(self,user_id,username):
#         self.id = user_id
#         self.username = username
#         self.following = 0
#         self.followers = 0
#
#     def follow(self,user):
#         user.followers += 1
#         self.following += 1
#
#
#
# user_1 = User("001","Awais")
# user_2 = User("002","Alyan")
#
# user_1.follow(user_2)
#
# print(user_1.following)
# print(user_1.followers)
# print(user_2.following)
# print(user_2.followers)
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


question_bank = []

for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]

    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)


while quiz.still_has_question():
    quiz.next_question()


print("You've completed the quiz.")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")