##
# This module defines the modified Question class
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
        correctResponse = correctResponse.lower()
        correctResponse = list(correctResponse)
        correctResponse = [i for i in correctResponse if i !=" "]
        self._answer = correctResponse

    ## Checks a given response for correctness.
    # @param response the response to check
    # @return True if the response was correct, False otherwise
    #
    def checkAnswer(self, response) :
        response = response.lower()
        response = list(response)
        response = [i for i in response if i !=" "]
        return response == self._answer

    ## Displays this question.
    #
    def display(self) :
        print(self._text)

