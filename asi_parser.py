import enum_specs
from enum_specs import *
from db_handler import *
import os
import blackboxprotobuf
import json


# echo db
def echo_db_handler():
    db_handle = db_handler('./target/echo_db_24-02-20')
    datas = db_handle.execute_sql("select * from echo_events;").fetchall()
    for i in datas:
        target_blob = blackboxprotobuf.protobuf_to_json(i[4])
        protobuf_dict = dict(json.loads(target_blob[0]))  # eval(target_blob[0])
        update_dict = dict()

        if i[1] == enum_specs.echo_db.APP_TARGET.value:
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
        if i[1] == enum_specs.echo_db.CONTEXT_AUDIO_DEVICE.value:
            for key in protobuf_dict.keys():
                update_key = echo_db_protobuf_CONTEXT_AUDIO_DEVICE(key).name
                update_value = protobuf_dict[key]
                if key == echo_db_protobuf_CONTEXT_AUDIO_DEVICE.IS_PLUGGED_IN.value:
                    update_value = "UNPLUGGED"
                    if int(protobuf_dict[key]) == 1:
                        update_value = "PLUGGGED IN"
                update_dict[update_key] = update_value
        if i[1] == enum_specs.echo_db.SHARE_SHEET.value:
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
        if i[1] == enum_specs.echo_db.SCREENSHOT.value:
            for key in protobuf_dict.keys():
                update_key = key
                update_value = protobuf_dict[key]
                if int(echo_db_protobuf_SCREEN_SHOT(key).value) > 0:
                    update_key = echo_db_protobuf_SCREEN_SHOT(key).name
                update_dict[update_key] = update_value
        if i[1] == enum_specs.echo_db.SEARCH.value:
            for key in protobuf_dict.keys():
                update_key = key
                update_value = protobuf_dict[key]
                if int(echo_db_protobuf_SEARCH(key).value) > 0:
                    update_key = echo_db_protobuf_SEARCH(key).name
                update_dict[update_key] = update_value
            print(update_dict)
        if i[1] == enum_specs.echo_db.SMARTSPACE.value:
            for key in protobuf_dict.keys():
                update_key = key
                update_value = protobuf_dict[key]
                if int(echo_db_protobuf_SMART_SPACE(key).value) > 0:
                    update_key = echo_db_protobuf_SMART_SPACE(key).name
                update_dict[update_key] = update_value
        if i[1] == enum_specs.echo_db.NOTIFICATION.value:
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
        print(update_dict)
    db_handle.conn.close()


# active users logger
def active_users_logger_handler():
    db_handle = db_handler('./target/active_users_logger.db')
    datas = db_handle.execute_sql("select * from active_users_logger where feature_event_type = 'USED';").fetchall()
    for i in datas:
        print(i[0], enum_specs.active_users_logger(i[1]).name, i[2], i[3], i[4])
    db_handle.conn.close()


# a13~
def people_search_handler():
    db_handle = db_handler('./target/people_search')
    datas = db_handle.execute_sql("select * from search_index where entity_type == 1;").fetchall()
    for i in datas:
        target_blob = blackboxprotobuf.protobuf_to_json(i[4])
        protobuf_dict = dict(json.loads(target_blob[0]))  # eval(target_blob[0])
        update_dict = dict()

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
        print(update_dict)
        print(protobuf_dict)

    db_handle.conn.close()


def simple_storage_now_playing_recognition_handler():
    db_handle = db_handler('./target/SimpleStorage')
    datas = db_handle.execute_sql("select * from NowPlayingRecognitionEvents;").fetchall()
    for i in datas:
        print(simple_storage_nowplayingrecognition_recognition_result(i[7]).name,
              simple_storage_nowplayingrecognition_recognition_trigger(i[8]).name)
    db_handle.conn.close()


def portable_geller_personalized_habits_handler():
    db_handle = db_handler('./target/portable_geller_personalized.db')
    datas = db_handle.execute_sql(
        "select * from geller_key_table, geller_data_table where geller_key_table.data_id = geller_data_table._id and "
        "data_type = 'HABITS_AA_PROFILES' and key like '%PROFILE%';").fetchall()
    for i in datas:
        if not any(ss in i[1] for ss in ['MEDIA', 'SHOPPING', 'TRANSPORTATION']):
            continue
        target_blob = blackboxprotobuf.protobuf_to_json(i[9])
        protobuf_dict = dict(json.loads(target_blob[0]))  # eval(target_blob[0])
        try:
            if 'MEDIA' in i[1]:
                print(protobuf_dict['3']['2']['311287627']['4'])
            if 'SHOPPING' in i[1]:
                print(protobuf_dict['3']['2']['338436589']['5'])
        except:
            print("no data defined")

    db_handle.conn.close()


if __name__ == '__main__':
    # echo_db_handler()
    # active_users_logger_handler()
    # people_search_handler()
    # simple_storage_now_playing_recognition_handler()
    portable_geller_personalized_habits_handler()

# aiai matchmaker_fa_db

# autofill

# active_users_logger.db

# people_search

# nasa_ps_db

# cell_db

# portable_geller_personalized.db

# simplestorage

# historyDB
