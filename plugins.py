from slackbot.bot import respond_to
from importlib import import_module
from privilege.check_privilege import has_privilege
#from functions.send_data import get_channel_id_from_name
from slacker import Slacker
import re
import slackbot_settings


slacker = Slacker(slackbot_settings.API_TOKEN)


def read_project(project_name):
    """
    データ抽出の定義が書かれたprojectファイルを読み込む
    Args:
    user_id (str): projectのファイル名
    Returns:
        module: 以下の4つの属性を持つprojectの定義
        privilege_level(int): default 0
        database_type(str): ex.oracle, mysql
        data_type(str): csv, excel not
        sql(str)
        document_link(str): ドキュメントのリンク
    """
    project = import_module("project."+project_name)
    return project


@respond_to(r'.*')
def data_exetraction_master(message):
    project_name = message.body["text"]
    project = read_project(project_name)

    user_id = message.body["user"]
    if not has_privilege(user_id, project.privilege_level):
        message.reply("You have no privilege")
        return

    data_file_path = "temp_data/{}.{}".format(project_name, project.data_type)
    # create_data(project.sql, project.database_type, data_file_path)

    channel_id = message.body["channel"]
    slacker.files.upload(file_=data_file_path, channels=channel_id)
    message.reply("データを抽出しました。csv形式で納品します。")


class Message():
    """for test"""
    body = {}

    def __init__(self):
        pass

message = Message()
