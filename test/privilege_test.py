from ..privilege import check_privilege as cp


def test_level1():
    """
    ユーザに実行権限がある場合
    """
    user_id = "test_id"
    privilege_level = 0
    assert cp.has_privilege(user_id, privilege_level) is True


def test_level2():
    """
    ユーザに実行権限がない場合
    """
    user_id = "test_id"
    privilege_level = 2
    assert cp.has_privilege(user_id, privilege_level) is False


def test_level3():
    """
    ユーザの登録データがない場合
    """
    user_id = "No Data"
    privilege_level = 0
    assert cp.has_privilege(user_id, privilege_level) is False
