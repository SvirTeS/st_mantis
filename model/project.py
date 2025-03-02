from sys import maxsize


class Project:

    def __init__(self, name=None, status=None, description=None, view_status=None, id=None, igc=None):
        self.name = name
        self.status = status
        self.description = description
        self.view_status = view_status
        self.id = id
        self.igc = igc

    def __repr__(self):
        return "%s" % self.name

    def __eq__(self, other):
        return self.name == other.name

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize

    def name(self):
        return self.name