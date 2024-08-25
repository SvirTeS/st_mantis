from model.project import Project
from selenium.webdriver.support.ui import Select


class ProjectHelper:

    def __init__(self, app):
        self.app = app

    project_cache = None

    def open_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("My View").click()

    def open_manage_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Manage").click()

    def open_manage_project_page(self):
        wd = self.app.wd
        self.open_manage_page()
        wd.find_element_by_link_text("Manage Projects").click()

    def open_create_project_page(self):
        wd = self.app.wd
        self.open_manage_page()
        self.open_manage_project_page()
        wd.find_element_by_value("Create New Project").click()

    def change_project_fill_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def change_project_status(self, status):
        wd = self.app.wd
        wd.find_element_by_name('status').click
        Select(wd.find_element_by_name('status')).select_by_value(status)

    def change_project_viewstatus(self, viewstatus):
        wd = self.app.wd
        wd.find_element_by_name('status').click
        Select(wd.find_element_by_name('status')).select_by_value(viewstatus)

    def fill_project_data(self, project):
        wd = self.app.wd
        self.change_project_fill_value(field_name='projectname', text=project.projectname)
        self.change_project_status(project.status)
        self.change_project_viewstatus(project.viewstatus)
        self.change_project_fill_value(field_name='description', text=project.description)

    def save_new_project(self):
        wd = self.app.wd
        self.find_element_by_value('Add Project').click()

    def create(self, project):
        wd = self.app.wd
        self.open_manage_page()
        self.open_manage_project_page()
        self.open_create_project_page()
        self.fill_project_data(project)
        self.save_new_project()

    def select_project_by_id(self, id):
        pass

    def del_project_by_id(self, id):
        pass

    def get_id_from_link(self):
        wd = self.app.wd
        elems = []
        elems.append(wd.find_elements_by_partial_link_text('project_id='))
        id_list = elems.split('=')

    def get_project_list_from_ui(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_manage_page()
            self.open_manage_project_page()


