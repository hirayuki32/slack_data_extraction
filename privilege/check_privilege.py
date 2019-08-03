import os
import pandas as pd

user_privileges = pd.read_csv("privilege/user_privileges.csv", index_col=[0])


def has_privilege(user_id, project_privilege_level):
    """
    ユーザにprojectの実行権限があるか確認する
    Args:
    user_id (str): ユーザID
    project_privilege_level (int): 
        そのprojectの実行権限レベル

    Returns:
        bool: ユーザにprojectの実行権限があるか
    """
    try:
        user_privilege_level = user_privileges.loc[user_id]["privilege_level"]
    except:
        return False
    if project_privilege_level == user_privileges.loc[user_id]["privilege_level"]:
        return True
    return False
