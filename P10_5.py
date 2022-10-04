##
# This module defines the Question class and the NumericQuestion subclass
##

class Question :
    ## Constructs a question with empty question and answer strings.
    #
    def __init__(self) :
        self._text = ""
        self._answer = ""

    ## Sets the question text.
    # @param questionText the text of this question
    #
    def setText(self, questionText) :
        self._text = questionText

    ## Sets the answer for this question.
    # @param correctResponse the answer
    #
    def setAnswer(self, correctResponse) :
        self._answer = correctResponse

    ## Checks a given response for correctness.
    # @param response the response to check
    # @return True if the response was correct, False otherwise
    #
    def checkAnswer(self, response) :
        return response == self._answer

    ## Displays this question.
    #
    def display(self) :
        print(self._text)


class MultiChoiceQuestion(Question):
    ## Constructs a class with multiple correct answers
    #
    def __init__(self):
        super().__init__()
        self._answer = []
    ## Multiple correct answers
    #    
    def setAnswer(self, *correctResponse) :
        self._answer = [str(i).lower() for i in correctResponse]
     
    ## provide response and check whether correct
    #
    def checkAnswer(self, response) :
        response = response.lower()
        response = response.split(" ")
        if set(response) == set(self._answer):
            return True
        else:
            return False

