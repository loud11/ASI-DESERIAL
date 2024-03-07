import sys

import enum_specs
from enum_specs import *
from db_handler import *
import os
import blackboxprotobuf
import json


# echo db
def echo_db_handler(data_path):
    db_handle = db_handler(data_path)
    db_handle.execute_sql_commit("DROP TABLE IF EXISTS `echo_events_deserial`")
    db_handle.execute_sql_commit("CREATE TABLE IF NOT EXISTS `echo_events_deserial` (`event_id` INTEGER PRIMARY KEY "
                                 "AUTOINCREMENT NOT NULL, `entity_type` INTEGER NOT NULL, `entity_version` INTEGER "
                                 "NOT NULL, `trigger_time` INTEGER NOT NULL, `blob_deserial` BLOB NOT NULL, "
                                 "`entity_type_de` TEXT NOT NULL)")

    datas = db_handle.execute_sql("select * from echo_events;").fetchall()

    for i in datas:
        target_blob = blackboxprotobuf.protobuf_to_json(i[4])
        protobuf_dict = dict(json.loads(target_blob[0]))  # eval(target_blob[0])
        update_dict = dict()
        action_category_type = i[1]
        t2 = ""
        if action_category_type == enum_specs.echo_db.APP_TARGET.value:
            t2 = enum_specs.echo_db.APP_TARGET.name
            for key in protobuf_dict.keys():
                update_value = protobuf_dict[key]
                if key == echo_db_protobuf_APP_TARGET_protobuf.ACTION_TYPE.value:
                    update_value = echo_db_APP_TARGET_ACTION_TYPE(protobuf_dict[key]).name
                if key == echo_db_protobuf_APP_TARGET_protobuf.LAUNCH_LOCATION.value:
                    update_value = echo_db_APP_TARGET_LAUNCH_LOCATION(protobuf_dict[key]).name
                if key == echo_db_protobuf_APP_TARGET_protobuf.ECHO_TARGET.value:
                    update_dict_ECHO_TARGET = dict()

                    for key1 in protobuf_dict[key].keys():

                        update_key1 = key1
                        if int(echo_db_protobuf_APP_TARGET_ECHO_TARGET(key1).value) > 0:
                            update_key1 = echo_db_protobuf_APP_TARGET_ECHO_TARGET(key1).name
                        update_dict_ECHO_TARGET[update_key1] = protobuf_dict[key][key1]
                    update_value = update_dict_ECHO_TARGET
                update_key = echo_db_protobuf_APP_TARGET_protobuf(key).name
                update_dict[update_key] = update_value
        if action_category_type == enum_specs.echo_db.CONTEXT_AUDIO_DEVICE.value:
            t2 = enum_specs.echo_db.CONTEXT_AUDIO_DEVICE.name
            for key in protobuf_dict.keys():
                update_key = echo_db_protobuf_CONTEXT_AUDIO_DEVICE(key).name
                update_value = protobuf_dict[key]
                if key == echo_db_protobuf_CONTEXT_AUDIO_DEVICE.IS_PLUGGED_IN.value:
                    update_value = "UNPLUGGED"
                    if int(protobuf_dict[key]) == 1:
                        update_value = "PLUGGGED IN"
                update_dict[update_key] = update_value
        if action_category_type == enum_specs.echo_db.SHARE_SHEET.value:
            t2 = enum_specs.echo_db.SHARE_SHEET.name
            for key in protobuf_dict.keys():
                update_key = key
                update_value = protobuf_dict[key]
                if int(echo_db_protobuf_SHARE_SHEET(key).value) > 0:
                    update_key = echo_db_protobuf_SHARE_SHEET(key).name
                update_dict[update_key] = update_value
                if echo_db_protobuf_SHARE_SHEET(key).value == echo_db_protobuf_SHARE_SHEET.IMAGE_PATH.value:
                    image_path_dict = dict()
                    for key1 in protobuf_dict[key].keys():
                        update_key1 = key1
                        update_value1 = protobuf_dict[key][key1]
                        if int(echo_db_protobuf_SHARE_SHEET_IMAGE_PATH(key1).value) > 0:
                            update_key1 = echo_db_protobuf_SHARE_SHEET_IMAGE_PATH(key1).name
                        image_path_dict[update_key1] = update_value1
                    update_dict = image_path_dict
        if action_category_type == enum_specs.echo_db.SCREENSHOT.value:
            t2 = enum_specs.echo_db.SCREENSHOT.name
            for key in protobuf_dict.keys():
                update_key = key
                update_value = protobuf_dict[key]
                if int(echo_db_protobuf_SCREEN_SHOT(key).value) > 0:
                    update_key = echo_db_protobuf_SCREEN_SHOT(key).name
                update_dict[update_key] = update_value
        if action_category_type == enum_specs.echo_db.SEARCH.value:
            t2 = enum_specs.echo_db.SEARCH.name
            for key in protobuf_dict.keys():
                update_key = key
                update_value = protobuf_dict[key]
                if int(echo_db_protobuf_SEARCH(key).value) > 0:
                    update_key = echo_db_protobuf_SEARCH(key).name
                update_dict[update_key] = update_value
        if action_category_type == enum_specs.echo_db.SMARTSPACE.value:
            t2 = enum_specs.echo_db.SMARTSPACE.name
            for key in protobuf_dict.keys():
                update_key = key
                update_value = protobuf_dict[key]
                if int(echo_db_protobuf_SMART_SPACE(key).value) > 0:
                    update_key = echo_db_protobuf_SMART_SPACE(key).name
                update_dict[update_key] = update_value
        if action_category_type == enum_specs.echo_db.NOTIFICATION.value:
            t2 = enum_specs.echo_db.NOTIFICATION.name
            for key in protobuf_dict.keys():
                update_key = key
                update_value = protobuf_dict[key]
                if int(echo_db_protobuf_NOTIFICATION(key).value) > 0:
                    update_key = echo_db_protobuf_NOTIFICATION(key).name
                if key == echo_db_protobuf_NOTIFICATION.NOTIFI_TARGET.value:
                    new_value_dict = dict()
                    for key1 in protobuf_dict[key].keys():
                        update_key1 = key1
                        update_value1 = protobuf_dict[key][key1]

                        if int(echo_db_protobuf_NOTIFICATION_NOTIFI_TARGET(update_key1).value) > 0:
                            update_key1 = echo_db_protobuf_NOTIFICATION_NOTIFI_TARGET(update_key1).name

                        new_value_dict[update_key1] = update_value1

                    update_value = new_value_dict

                update_dict[update_key] = update_value

        t = "'" + json.dumps(update_dict) + "'"
        t2 = "'" + t2 + "'"
        ma_query = f"INSERT into echo_events_deserial values ({i[0]},{i[1]},{i[2]},{i[3]},{t},{t2})"

        db_handle.execute_sql(ma_query)

    db_handle.conn.commit()
    db_handle.conn.close()
    print(f"{data_path} deserial or decode done!")


# active users logger
def active_users_logger_handler(data_path):
    db_handle = db_handler(data_path)
    db_handle.execute_sql_commit("DROP TABLE IF EXISTS `active_users_logger_de`")
    db_handle.execute_sql_commit(
        "CREATE TABLE active_users_logger_de (id INTEGER PRIMARY KEY AUTOINCREMENT,feature_id INTEGER NOT NULL,feature_event_type TEXT,feature_date TEXT,timestamp INTEGER, actions TEXT)")
    datas = db_handle.execute_sql("select * from active_users_logger where feature_event_type = 'USED';").fetchall()
    for i in datas:
        ma_query = f"INSERT into active_users_logger_de values ({i[0]},{i[1]},'{i[2]}','{i[3]}',{i[4]},'{enum_specs.active_users_logger(i[1]).name}')"
        db_handle.execute_sql(ma_query)

    db_handle.conn.commit()
    db_handle.conn.close()
    print(f"{data_path} deserial or decode done!")


# a13~
def people_search_handler(data_path):
    db_handle = db_handler(data_path)

    check_people_version = "select sql from sqlite_master where name = 'search_index';"
    version_str = db_handle.execute_sql(check_people_version).fetchall()[0][0]

    version_flag = 12

    search_query = "select i.id, i.name, i.entity_id, i.entity_type, e.blob from search_index as i, search_entity " \
                       "as e where e.id = i.entity_id and e.type = 1 "

    if "store_id" in version_str:  # this means a13 version up
        search_query = "select * from search_index where entity_type == 1;"
        version_flag = 13

    db_handle.execute_sql_commit("DROP TABLE IF EXISTS `search_index_deserial`")
    db_handle.execute_sql_commit(
        "CREATE TABLE `search_index_deserial` (`id` INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, `name` TEXT NOT NULL, "
        "`entity_id` INTEGER, `entity_type` INTEGER NOT NULL, `store_id_de` BLOB)")

    datas = db_handle.execute_sql(search_query).fetchall()
    for i in datas:
        target_blob = blackboxprotobuf.protobuf_to_json(i[4])
        protobuf_dict = dict(json.loads(target_blob[0]))
        update_dict = dict()

        if version_flag == 12:
            #a12
            for key in protobuf_dict.keys():
                update_key = key
                update_value = protobuf_dict[key]
                if update_key == enum_specs.people_search_a12.PACKAGE_NAME.value:
                    update_key = enum_specs.people_search_a12.PACKAGE_NAME.name
                if update_key == enum_specs.people_search_a12.USER_IDENTIFIER.value:
                    update_key = enum_specs.people_search_a12.USER_IDENTIFIER.name
                if update_key == enum_specs.people_search_a12.USER_NICKNAME.value:
                    update_key = enum_specs.people_search_a12.USER_NICKNAME.name
                update_dict[update_key] = update_value

        if version_flag == 13:
            # a13
            for key in protobuf_dict.keys():
                update_key = key
                update_value = protobuf_dict[key]
                if key == enum_specs.people_search.SOURCES.value:
                    update_key = enum_specs.people_search.SOURCES.name
                    update_value1 = dict()
                    for key1 in protobuf_dict[key].keys():
                        update_key1 = key1
                        update_value2 = protobuf_dict[key][key1]
                        if update_key1 == enum_specs.people_search_SOURCES.PACKAGE_NAME.value:
                            update_key1 = enum_specs.people_search_SOURCES.PACKAGE_NAME.name
                        if update_key1 == enum_specs.people_search_SOURCES.USER_IDENTIFIER.value:
                            update_key1 = enum_specs.people_search_SOURCES.USER_IDENTIFIER.name
                        update_value1[update_key1] = update_value2
                    update_value = update_value1
                update_dict[update_key] = update_value

        t = "'" + json.dumps(update_dict) + "'"
        ma_query = f"INSERT into search_index_deserial values ({i[0]},'{i[1]}',{i[2]},{i[3]},{t})"
        if type(i[2]) == type(None):
            ma_query = f"INSERT into search_index_deserial values ({i[0]},'{i[1]}',Null,{i[3]},{t})"
        db_handle.execute_sql(ma_query)

    db_handle.conn.commit()
    db_handle.conn.close()
    print(f"{data_path} deserial or decode done!")


def simple_storage_now_playing_recognition_handler(data_path):
    db_handle = db_handler(data_path)
    datas = db_handle.execute_sql("select * from NowPlayingRecognitionEvents;").fetchall()

    db_handle.execute_sql_commit("DROP TABLE IF EXISTS `NowPlayingRecognitionEvents_dec`")
    db_handle.execute_sql_commit("CREATE TABLE `NowPlayingRecognitionEvents_dec` (`id` INTEGER PRIMARY KEY "
                                 "AUTOINCREMENT NOT NULL, `timestampMillis` INTEGER NOT NULL, `countryCode` TEXT NOT "
                                 "NULL, `shardVersion` INTEGER NOT NULL, `shardCountry` TEXT NOT NULL, `packageName` "
                                 "TEXT NOT NULL, `systemInfoId` INTEGER, `recognitionResult` INTEGER NOT NULL, "
                                 "`recognitionTrigger` INTEGER NOT NULL, `detectedMusicScore` REAL NOT NULL, "
                                 "`comparisonToLastMatch` INTEGER NOT NULL, `recognitionResult_dec` TEXT , `recognitionTrigger_dec` TEXT , FOREIGN KEY(`packageName`) REFERENCES "
                                 "`Packages`(`packageName`) ON UPDATE CASCADE ON DELETE CASCADE , FOREIGN KEY("
                                 "`systemInfoId`) REFERENCES `SystemInfo`(`id`) ON UPDATE CASCADE ON DELETE SET NULL)")

    for i in datas:
        ma_query = f"INSERT into NowPlayingRecognitionEvents_dec values ({i[0]},{i[1]},'{i[2]}',{i[3]},'{i[4]}','{i[5]}',{i[6]},{i[7]},{i[8]},{i[9]},{i[10]},'{simple_storage_nowplayingrecognition_recognition_result(i[7]).name}','{simple_storage_nowplayingrecognition_recognition_trigger(i[8]).name}')"
        db_handle.execute_sql(ma_query)

    db_handle.conn.commit()
    db_handle.conn.close()
    print(f"{data_path} deserial or decode done!")


def portable_geller_personalized_habits_handler(data_path):
    db_handle = db_handler(data_path)

    db_handle.execute_sql_commit("DROP TABLE IF EXISTS `geller_data_deserial`")
    db_handle.execute_sql_commit(
        "CREATE TABLE geller_data_deserial (data_type TEXT NOT NULL, key TEXT NOT NULL, timestamp_micro INTEGER NOT "
        "NULL, sync_status TEXT, delete_status TEXT, num_times_used INTEGER, deletion_sync_status TEXT, "
        "data_id INTEGER NOT NULL, data_deserial BLOB ,  FOREIGN KEY (data_id) REFERENCES geller_data_table (_id) ON "
        "DELETE CASCADE )")

    datas = db_handle.execute_sql(
        "select * from geller_key_table, geller_data_table where geller_key_table.data_id = geller_data_table._id and "
        "data_type = 'HABITS_AA_PROFILES';").fetchall()

    for i in datas:
        if not any(ss in i[1] for ss in ['MEDIA', 'SHOPPING', 'TRANSPORTATION']):
            continue
        target_blob = blackboxprotobuf.protobuf_to_json(i[9])
        protobuf_dict = dict(json.loads(target_blob[0]))  # eval(target_blob[0])
        update_val = "no data defined"
        try:
            if 'MEDIA' in i[1]:
                update_val = protobuf_dict['3']['2']['311287627']['4']
            if 'SHOPPING' in i[1]:
                update_val = protobuf_dict['3']['2']['338436589']['5']
            if 'TRANSPORTATION' in i[1]:
                update_val = protobuf_dict['3']['2']['479335935']['1']
        except:
            continue
        flag1 = i[4]
        flag2 = i[6]
        if type(i[4]) == type(None):
            flag1 = "Null"
        if type(i[6]) == type(None):
            flag2 = "Null"

        ma_query = f"INSERT into geller_data_deserial values ('{i[0]}','{i[1]}',{i[2]},'{i[3]}','{flag1}',{i[5]},'{flag2}',{i[7]},'{json.dumps(update_val)}')"
        db_handle.execute_sql(ma_query)
    db_handle.conn.commit()
    db_handle.conn.close()
    print(f"{data_path} deserial or decode done!")


if __name__ == '__main__':

    if len(sys.argv) < 2:
        print("usage : python asi_parser.py DATA_PATH")
        exit(-1)

    abs_path = os.path.abspath(sys.argv[1])
    for file_name in os.listdir(abs_path):
        if file_name in enum_specs.ASI_DATA_LIST:
            target_path = os.path.join(abs_path, file_name)
            print(f"{file_name} detected! trying to deserial or decode....")
            if file_name == enum_specs.ASI_DATA_LIST[0]:
                echo_db_handler(target_path)
                continue
            if file_name == enum_specs.ASI_DATA_LIST[1]:
                active_users_logger_handler(target_path)
                continue
            if file_name == enum_specs.ASI_DATA_LIST[2]:
                people_search_handler(target_path)
                continue
            if file_name == enum_specs.ASI_DATA_LIST[3]:
                simple_storage_now_playing_recognition_handler(target_path)
                continue
            if file_name == enum_specs.ASI_DATA_LIST[4]:
                portable_geller_personalized_habits_handler(target_path)
                continue

    print("-----ASI deserial or decoding done!-----")

# aiai matchmaker_fa_db --> already done no nothing to do
# autofill --> already done no nothing to do
# nasa_ps_db --> already done no nothing to do
# historyDB --> already done no nothing to do
# cell_db --> already done no nothing to do

# portable_geller_personalized.db v
# active_users_logger.db v
# people_search v
# simplestorage v