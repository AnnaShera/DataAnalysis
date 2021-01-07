from Obj import Obj

from enum import Enum


class States(Enum):
    Running = 1
    Stopped = 2
    Terminated = 3


class Instance(Obj):

    def __init__(self, id, type, state, region, name=''):
        """
       function initiates attributes of provided class instance
        """
        super().__init__(id, region, name)
        self.type = type
        self.state = state

    def print(self):
        """
        function prints all instance attributes
         """
        super().print()
        print("type: {0} ,state: {1}".format(self.type, self.state))
        print("_____________________________________________________________________")

