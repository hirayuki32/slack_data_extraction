import glob
import sys
import os
from importlib import import_module
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

project_list = glob.glob("project/*.py")
project_list.remove("project/__init__.py")


def test_project_data_types():
    """
    privilege_levelに入っているデータ型の確認
    """
    for project in project_list:
        module_name = project.replace(".py", "").replace("/", ".")
        project_module = import_module(module_name)
        assert type(project_module.privilege_level) == int
        assert type(project_module.database_type) == str
        assert type(project_module.data_type) == str
        assert type(project_module.sql) == str
        assert type(project_module.document_link) == str
