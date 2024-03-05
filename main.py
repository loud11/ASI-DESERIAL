import os
import blackboxprotobuf
from db_handler import *
import json

def call_sql_blobs():
    db_handle = db_handler('./target/echo_db_notification')
    db_handle.execute_sql_commit("DROP TABLE IF EXISTS `echo_events_deserial`")
    db_handle.execute_sql_commit("CREATE TABLE IF NOT EXISTS `echo_events_deserial` (`event_id` INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, `entity_type` INTEGER NOT NULL, `entity_version` INTEGER NOT NULL, `trigger_time` INTEGER NOT NULL, `blob_deserial` BLOB NOT NULL)")

    datas = db_handle.execute_sql("select * from echo_events;").fetchall()
    for i in datas:
        target_blob = blackboxprotobuf.protobuf_to_json(i[4])
        t = "'"+json.dumps(json.loads(target_blob[0]))+"'"
        #parsed deserialed data => eval(target_blob[0])
        ma_query = f"INSERT into echo_events_deserial values ({i[0]},{i[1]},{i[2]},{i[3]},{t})"
        db_handle.execute_sql(ma_query)
    db_handle.conn.commit()
    db_handle.conn.close()

if __name__ == '__main__':
    print("echo deseeializer")
    call_sql_blobs()

