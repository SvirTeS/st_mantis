from sys import maxsize


class Project:

    def __init__(self, projectname, status=None, description=None, viewstatus=None, id=None, igc=None):
        self.projectname = projectname
        self.status = status
        self.description = description
        self.viewstatus = viewstatus
        self.id = id
        self.igc = igc

    def __repr__(self):
        return "%s" % self.projectname

    def __eq__(self, other):
        return self.projectname == other.projectname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize

    def projectname(self):
        return self.projectname