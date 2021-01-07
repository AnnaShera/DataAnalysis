from Obj import Obj


class Snapshot(Obj):

    def __init__(self, id, name, region, source_volume_id):
        """
        function initiates attributes of provided class instance
        """
        super().__init__(id, region, name)
        self.source_volume_id = source_volume_id  # ID of the Volume to which this snapshot belongs

    def print(self):
        """
        function prints all instance attributes
        """
        super().print()
        print("source_volume_id: {0}".format(self.source_volume_id))
        print("_____________________________________________________________________")
