# Part 1: Discussion What are the three main design advantages that object
# orientation can provide?

""" Abstraction: Implements the methods at a higher level, without including a
lot of detail.

Encapsulation: It's grouping all the data and methods within a class.

Polymorphism: The object can take any kind of form.

Inheritance: The subclass inherits the methods and attributes of the superclass.
"""

# Explain each concept.

# 1. What is a class?

""" Class is a way of grouping data and methods. Thus, it creates instances
(objects) """

# 2. What is an instance attribute?

"""  Instance attribute is different from a class attribute. Instance attribute
is an attribute that is specific to a specific instance. On the other hand,
class attribute is applicable to all instances. All instances will inherit the
class attribute.  """

# 3. What is a method?

""" A method is a function that has been defined on a class. """

# 4. What is an instance in object orientation?

""" An instance (object) is an individual instance of a class. """

# 5. How is a class attribute different than an instance attribute? Give an
# example of when you might use each.

"""  See question 2

For example:  Class Dog, has aclass attribute : age = 9.  Morfy, an instance of
Class Dog has an instance attribute age = 3, which takes presedence over age =
9.  """


# Parts 2 through 5: Create your classes and class methods


class Student(object):
    """Student"""

    def __init__(self, first_name, last_name, address):

        self.first_name = first_name
        self.last_name = last_name
        self.address = address


class Question(object):
    """Question"""

    def __init__(self, question, correct_answer):

        self.question = question
        self.correct_answer = correct_answer

    def ask_and_evaluate(self):

        print self.question

        answer = raw_input("> ")

        if self.correct_answer == answer:

            return True


class Exam(object):
    """Exam"""

    def __init__(self, name, questions):

        self.name = name
        self.questions = questions

    def add_question(self, question, correct_answer):

        question_object = Question(question, correct_answer)
        self.questions.append(question_object)
