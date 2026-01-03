import uuid


class myclass:
    def __init__(self):
        self.my= str(uuid.uuid4())

    def one(self):
        data = {'id': self.my }
        return data['id']

    def two(self):
        yourid = self.one()
        print(yourid)


myc = myclass()
myc.two()