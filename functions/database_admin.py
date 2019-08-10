import pandas as pd
import cx_Oracle


def _create_oracle_con():
    from oracle_conf import host, port, sid, user, passwd
    tns = cx_Oracle.makedsn(host, port, sid)
    conn = cx_Oracle.connect(user, passwd, tns)
    return conn


def create_df_by_query_data(sql, database_type):
    """
    args:
        sql: string
        database_type: "oracle"
        Other databases are not implemented yet
    return:
        pandas DataFrame
    """
    # Other databases are not implemented yet
    if database_type == "oracle":
        conn = _create_oracle_con()
    else:
        raise ValueError("指定のdatabase_typeが不正です")
    df = pd.read_sql_query(sql, conn)
    conn.close
    return df
