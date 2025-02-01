from typing import List, Optional

class QADocument:
    """
    Class representing a document with questions and answers.
    """
    def __init__(self, text: str, questions: List[str], answers: List[str], doc_id: Optional[str]):
        """
        Constructor
        """
        self.__text = text
        self.__questions = questions
        self.__answers = answers
        self.__doc_id = doc_id

    @property
    def doc_id(self):
        """
        Returns the ID of the document.
        """
        return self.__doc_id

    @property
    def text(self):
        """
        Returns the text of the document.
        """
        return self.__text

    @property
    def questions(self):
        """
        Returns the list of questions.
        """
        return self.__questions
    
    @property
    def answers(self):
        """
        Returns the list of answers.
        """
        return self.__answers
