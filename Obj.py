class Obj:

    def __init__(self, id, region, name=''):
        """
        function initiates attributes of provided class instance
        """
        self.id = id
        self.name = name
        self.region = region

    def print(self):
        """
        function prints all instance attributes
        """
        print("id: {0} ,name: {1} ,region: {2}".format(self.id, self.name, self.region))
