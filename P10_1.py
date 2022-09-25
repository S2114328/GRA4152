##
# This module defines the Question class and the NumericQuestion subclass
##
import numpy as np
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


class NumericQuestion(Question):
    def __init__(self):
        super().__init__()
    
    def checkAnswer(self, response) :
        if np.abs(self._answer - response)<0.01:
            return True
        else:
            return False

