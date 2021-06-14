import pandas


class Definition:

    DATA = pandas.read_csv("data.csv")

    def __init__(self, term):
        self.term = term

    def get(self):
        definition = self.DATA.loc[self.DATA["word"] == self.term]['definition'].values
        return definition