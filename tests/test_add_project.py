from model.project import Project


def test_add_project(app):
    project = 'pass'
    app.session.login('administrator', 'root')
    old_list_project = app.project.get_project_list_from_ui()
    app.project.create(project)
    new_list_project = app.project.get_project_list_from_ui()
    old_list_project.append(project)
    assert sorted(old_list_project, key=Project.id_or_max) == sorted(new_list_project, key=Project.id_or_max)
