from Obj import Obj


class Volume(Obj):

    def __init__(self, id, name, state, region, attached_instance_id=''):
        """
        function initiates attributes of provided class instance
        """
        super().__init__(id, region, name)
        self.state = state
        self.attached_instance_id = attached_instance_id  # ID of Instance to which the volume is attached

    def print(self):
        """
        function prints all instance attributes
        """
        super().print()
        print("state: {0} ,attached_instance_id: {1}".format(self.state, self.attached_instance_id))
        print("_____________________________________________________________________")

