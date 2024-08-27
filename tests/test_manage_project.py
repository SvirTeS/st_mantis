from model.project import Project
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + ' '*10
    result = prefix + ''.join([random.choice(symbols) for i in range(random.randrange(maxlen))])
    return " ".join(result.split())


project_data = Project(projectname=random_string('name', 10), description=random_string('header', 20))


def test_add_project(app):
    app.session.ensure_login('administrator', 'root')
    old_list_project = app.project.get_project_list_from_ui()
    app.project.create(project_data)
    new_list_project = app.project.get_project_list_from_ui()
    old_list_project.append(project_data)
    assert sorted(old_list_project, key=Project.projectname) == sorted(new_list_project, key=Project.projectname)


def test_del_random_project_by_id(app):
    app.session.ensure_login('administrator', 'root')
    if len(app.project.get_project_list_from_ui()) == 0:
        app.project.create(project_data)
    old_list_project = app.project.get_project_list_from_ui()
    project_choice = random.choice(old_list_project)
    app.project.del_project(project_choice.id)
    new_list_project = app.project.get_project_list_from_ui()
    old_list_project.remove(project_choice)
    assert sorted(old_list_project, key=Project.projectname) == sorted(new_list_project, key=Project.projectname)
