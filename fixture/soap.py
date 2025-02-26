from zeep import Client
from zeep.exceptions import Fault

class SoapHelper:
    def __init__(self, app):
        self.app = app

    def can_login(self, username, password):
        client = Client("http://localhost/mantisbt-1.2.20/api/soap/mantisconnect.php?wsdl")
        try:
            client.service.mc_login(username, password)
            return True
        except Fault:
            return False

    project_cache = None

    def get_project_list_from_soap(self):
        client = Client("http://localhost/mantisbt-1.2.20/api/soap/mantisconnect.php?wsdl")
        try:
            get_projects = client.service.mc_projects_get_user_accessible(self.app.config["webadmin"]["username"],
                                                                  self.app.config["webadmin"]["password"])
            return get_projects

        except Fault:
            return False