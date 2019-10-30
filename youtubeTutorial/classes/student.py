

class Student:
    def __init__(self, name, major, grade_average, is_on_probation):
        self.name = name
        self.major = major
        self.grade_average = grade_average
        self.is_on_probation = is_on_probation
        #print( "In student init self method" )

    def on_honor_roll( self ):
        if self.grade_average >= 3.5:
            return True
        else:
            return False

