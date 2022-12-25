#Question 

class Question:
    def __init__(self,text,choices,answer):
        self.text = text
        self.choices = choices
        self.answer = answer

    def checkAnswer(self,answer):
        return self.answer == answer


#Quiz 

class Quiz():
    def __init__(self,questions):
        self.questions = questions
        self.score = 0
        self.questionIndex = 0

    def getQuestion(self):
        return self.questions[self.questionIndex]

    def displayQuestion(self):
        question = self.getQuestion()
        print(f'Soru {self.questionIndex + 1}: {question.text}')

        for q in question.choices:
            print('-' + q)
        answer = input("Cevap girin:")
        self.guess(answer)
        self.loadQuestion()
    
    def guess(self,answer):
        question = self.getQuestion()

        if question.checkAnswer(answer):
            self.score += 1
        self.questionIndex += 1

    def loadQuestion(self):
        if len(self.questions) == self.questionIndex:
            self.showScore()
        else:
            self.displayProgress()
            self.displayQuestion()

    def showScore(self):
        print('score: ', self.score)

    def displayProgress(self):
        totalQuestion = len(self.questions)
        questionNumber = self.questionIndex + 1

        if questionNumber > totalQuestion:
            print("Quiz bitti.")
        else:
            print(f'Question {questionNumber} of {totalQuestion}'.center(100,'*'))



q1 = Question('En iyi programlama dili hangisidir ?',['C','Python','C++','Java'],'Python')
q2 = Question('En populer programlama dili hangisidir ?',['C#','Python','C++','Java'],'Python')
q3 = Question('En iyi programlama dili hangisidir ?',['PHP','Python','C++','Javascript'],'Python')

questions = [q1,q2,q3]

quiz = Quiz(questions)


quiz.loadQuestion()

#quiz.displayQuestion()

#question = quiz.getQuestion()
#print(question.text)



#print(q1.checkAnswer('Python'))
#print(q1.checkAnswer('C#'))
