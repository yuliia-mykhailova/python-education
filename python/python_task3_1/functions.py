"""Creating functions exercise"""


def list_benefits():
    """Returns the following list"""

    return "More organized code", "More readable code", "Easier code reuse", \
           "Allowing programmers to share and connect code together"


def build_sentence(benefit):
    """Returns benefit + 'is a benefit of function!' """

    return benefit + " is a benefit of functions!"


def name_the_benefits_of_functions():
    """Adds to every el in list a string"""

    list_of_benefits = list_benefits()
    for benefit in list_of_benefits:
        print(build_sentence(benefit))


name_the_benefits_of_functions()
