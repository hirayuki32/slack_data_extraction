import pandas as pd
import cx_Oracle


def _create_oracle_con():
    from oracle_conf import host, port, sid, user, passwd
    tns = cx_Oracle.makedsn(host, port, sid)
    conn = cx_Oracle.connect(user, passwd, tns)
    return conn


def create_df_by_query_data(sql):
    """
    args:
        oracle_cur: oracle cursol created by cx_Oracle
        SQL: string
    return:
        pandas DataFrame
    """
    conn = _create_oracle_con()
    df = pd.read_sql_query(sql, conn)
    conn.close
    return df
