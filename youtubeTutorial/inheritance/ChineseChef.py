
from chef import Chef

#This is how a child class inherits from parent class.
class ChineseChef(Chef):
    def make_fried_rice( self ):
        print("The chef makes fried rice")
    def make_special_dish( self):
        print("The chef makes orange chicken")
