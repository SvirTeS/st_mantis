from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
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
        wd.find_element_by_xpath("//input[@value='Create New Project']").click()

    def change_project_fill_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def change_project_status(self, status):
        wd = self.app.wd
        if status is not None:
            wd.find_element_by_name('status').click
            Select(wd.find_element_by_name('status')).select_by_value(status)

    def change_project_viewstatus(self, viewstatus):
        wd = self.app.wd
        if viewstatus is not None:
            wd.find_element_by_name('viewstatus').click
            Select(wd.find_element_by_name('viewstatus')).select_by_value(viewstatus)

    def fill_project_data(self, project):
        wd = self.app.wd
        self.change_project_fill_value(field_name='name', text=project.projectname)
        self.change_project_status(project.status)
        self.change_project_viewstatus(project.viewstatus)
        self.change_project_fill_value(field_name='description', text=project.description)

    def save_new_project(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//input[@value='Add Project']").click()

    def create(self, project):
        self.open_manage_page()
        self.open_manage_project_page()
        self.open_create_project_page()
        self.fill_project_data(project)
        self.save_new_project()
        self.project_cache = None

    def open_project_by_id(self, id):
        wd = self.app.wd
        self.open_manage_project_page()
        wd.find_element_by_xpath(f".//a[@href='manage_proj_edit_page.php?project_id={id}']").click()

    def del_project(self, id):
        wd = self.app.wd
        self.open_project_by_id(id)
        wd.find_element_by_xpath("//input[@value='Delete Project']").click()
        wd.find_element_by_xpath("//input[@value='Delete Project']").click()
        self.project_cache = None

    def get_project_list_from_ui(self):
        if self.project_cache is None:
            wd = self.app.wd
            self.open_manage_project_page()
            self.project_cache = []
            wait = WebDriverWait(self.app.wd, 10)
            wait.until(EC.visibility_of_element_located((By.XPATH, "//table[@class='width100' and @cellspacing=1]")))
            rows = wd.find_elements_by_xpath("//table[@class='width100' and @cellspacing=1]//tr[.//a[contains(@href, 'id')]]")
            for row in rows:
                cells = row.find_elements_by_tag_name("td")
                id = cells[0].find_element_by_xpath('.//a').get_attribute('href').split('project_id=')[1]
                projectname = cells[0].text.strip()
                status = cells[1].text.strip()
                igc = cells[2].text.strip()
                viewstatus = cells[3].text.strip()
                description = cells[4].text.strip()
                self.project_cache.append(Project(id=id, projectname=projectname, status=status,
                                                  igc=igc, description=description, viewstatus=viewstatus))
        return list(self.project_cache)
