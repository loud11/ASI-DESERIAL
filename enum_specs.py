from enum import Enum


ASI_DATA_LIST = ['echo_db','active_users_logger.db', 'people_search', 'SimpleStorage', 'portable_geller_personalized.db', 'aiai_matchmaker_fa_db']

# a11
class aiai_matchmaker_fa_db(Enum):
    NOT_DEFINED = -1
    OVERVIEW_SCREEN_STARTED = 11  # enter recent task list
    OVERVIEW_APP_CLOSED = 16  # quit applications in recent task list
    OVERVIEW_EXIT_APP_ENTERED = 71  # enter application from recent task list
    OVERVIEW_EXIT_BACK_BUTTON = 72  # close recent task list with back button
    OVERVIEW_EXIT_HOME_BUTTON = 73  # close recent task list with home button
    OVERVIEW_EXIT_POWER_BUTTON = 74  # close recent task list with power button
    OVERVIEW_ENTER_ALL_APPS = 75  # enter all apps from recent tasks list
    TASK_SNAPSHOT_CREATED = 31  # screen captured
    TASK_SNAPSHOT_DISMISSED = 36  # dismiss screen capture result

    @classmethod
    def _missing_(cls, value):
        return cls.NOT_DEFINED


# a11,a12,a13,a14
# echo db deserializer done!
class echo_db(Enum):
    NOT_DEFINED = -1
    APP_TARGET = 0  # application execution history
    NOTIFICATION = 1  # application notification history
    CONTEXT_AUDIO_DEVICE = 4  # audio equipment connection history
    SHARE_SHEET = 5  # share history
    SCREENSHOT = 6  # screenshot history
    SEARCH = 7  # history of use of search function in Android
    SMARTSPACE = 10  # smart space interaction history

    @classmethod
    def _missing_(cls, value):
        return cls.NOT_DEFINED


class echo_db_APP_TARGET_LAUNCH_LOCATION(Enum):
    NOT_DEFINED = -1
    WORKSPACE = "1"  # execution of application of top of the main screen
    HOTSEAT_PINNED = "2"  # execution of application of bottom of the main screen
    FOLDER = "3"  # execution of application in folder
    ALLAPPS = "4"  # execution of application in all apps
    WIDGETS = "5"  # execution of application of widgets of the main screen
    OVERVIEW = "6"  # execution of application of the recent task list
    PREDICTION = "7"
    SEARCHRESULT = "8"  # execution of application of search function in all apps
    PINITEM = "10"  # execution of application of pinned item of the recent task list
    TASKSWITCHER = "12"
    HOTSEAT_PREDICTED = "17"  # execution of application of prediction icon of the main screen
    NOTIFICATION = "1000"

    @classmethod
    def _missing_(cls, value):
        return cls.NOT_DEFINED


class echo_db_APP_TARGET_ACTION_TYPE(Enum):
    NOT_DEFINED = -1
    ACTION_LAUNCH = "1"
    ACTION_DISMISS = "2"
    ACTION_PIN = "3"
    ACTION_UNPIN = "4"
    ACTION_UNDISMISS = "5"

    @classmethod
    def _missing_(cls, value):
        return cls.NOT_DEFINED


class echo_db_SMARTSPACE(Enum):
    NOT_DEFINED = -1
    DATE_CARD = "date_card"
    WEATHER_UPDATED = "WEATHER"
    AMBIENT_LIGHT = "ambient_light"
    PAIRED_DEVICE_STATS = "paired_device"

    @classmethod
    def _missing_(cls, value):
        return cls.NOT_DEFINED


class echo_db_protobuf_SMART_SPACE(Enum):
    NOT_DEFINED = -1
    EVENT_DEFINITION = "1"
    UPDATED_TIME = "4"
    EXPIRE_TIME = "5"
    PACKAGE_NAME = "7"
    CLASS_NAME = "8"
    TRIGGER_TIME = "10"

    @classmethod
    def _missing_(cls, value):
        return cls.NOT_DEFINED


class echo_db_protobuf_SEARCH(Enum):
    NOT_DEFINED = -1
    QUERY = "1"
    TRIGGER_TIME = "3"
    SEARCH_RESULT = "4"
    INTERACTION_TARGET = "5"
    RESULT_CONNECTED_APP_PACKAGE = "6"

    @classmethod
    def _missing_(cls, value):
        return cls.NOT_DEFINED


class echo_db_protobuf_NOTIFICATION(Enum):
    NOT_DEFINED = -1
    NOTIFI_TARGET = "1"  # "1" : package , "2": activity name
    TRIGGER_TIME = "2"

    @classmethod
    def _missing_(cls, value):
        return cls.NOT_DEFINED


class echo_db_protobuf_NOTIFICATION_NOTIFI_TARGET(Enum):
    NOT_DEFINED = -1
    PACKAGE_NAME = "1"
    ACTIVITY_NAME = "2"

    @classmethod
    def _missing_(cls, value):
        return cls.NOT_DEFINED


class echo_db_protobuf_SHARE_SHEET(Enum):
    NOT_DEFINED = -1
    IMAGE_PATH = "1"
    TRIGGER_TIME = "3"
    SHARE_TYPE = "4"
    SHARE_OBJECT_PATH = "5"
    SHOWN_SHARE_TARGETS = "6"

    @classmethod
    def _missing_(cls, value):
        return cls.NOT_DEFINED


class echo_db_protobuf_SHARE_SHEET_IMAGE_PATH(Enum):
    NOT_DEFINED = -1
    IMAGE_PATH = "1"
    ACTIVITY_NAME = "2"

    @classmethod
    def _missing_(cls, value):
        return cls.NOT_DEFINED


class echo_db_protobuf_SCREEN_SHOT(Enum):
    NOT_DEFINED = -1
    IMAGE_PATH = "1"
    PACKAGE_NAME = "2"
    TRIGGER_TIME = "4"

    @classmethod
    def _missing_(cls, value):
        return cls.NOT_DEFINED


class echo_db_protobuf_CONTEXT_AUDIO_DEVICE(Enum):
    NOT_DEFINED = -1
    IS_PLUGGED_IN = "1"
    DEVICE_MAC = "2"
    TRIGGER_TIME = "3"

    @classmethod
    def _missing_(cls, value):
        return cls.NOT_DEFINED


class echo_db_protobuf_APP_TARGET_protobuf(Enum):
    NOT_DEFINED = -1
    ACTION_TYPE = '1'
    ECHO_TARGET = '2'  # '1' : package_name , '2' : activity_name
    LAUNCH_LOCATION = '3'
    TRIGGER_TIME = '4'
    POSTURE = '5'

    @classmethod
    def _missing_(cls, value):
        return cls.NOT_DEFINED


class echo_db_protobuf_APP_TARGET_ECHO_TARGET(Enum):
    NOT_DEFINED = -1
    PACKAGE_NAME = '1'
    ACTIVITY_NAME = '2'

    @classmethod
    def _missing_(cls, value):
        return cls.NOT_DEFINED


# a12, a13, a14
class active_users_logger(Enum):
    NOT_DEFINED = -1
    LIVE_CAPTION = 1  # use real time voice subtitle generation function
    SCREENSHOT = 3  # use screen shot
    ATTENTION = 4  # screen gaze detection from user
    NOW_PLAYING = 5  # setting the function to detect music heard nearby
    TEXT_CLASSIFIER = 7  # text category detection
    LENS_OVERVIEW_SEARCH = 8
    HYBRID_HOTSEAT = 9  # run application at the bottom of the desktop
    ECHO_ALL_APPS = 10  # execution prediction score update
    AUTOFILL_REQUEST = 11   #autofill request
    VISUAL_CORTEX = 12  # call artificial intelligence function for screen output image
    ADAPTIVE_AUDIO = 14  # set appropriate sound level after analyzing surrounding noise
    LENS_SCREENSHOTS_TRANSLATE = 17  # translation through Google Lens for screenshots
    AUTO_ROTATE = 22  # automatic screen rotation
    LIVE_TRANSLATE_CHIP_TRIGGER = 35  # real-time text translation triggered

    @classmethod
    def _missing_(cls, value):
        return cls.NOT_DEFINED


# (12754, 'jennifer', 854269542, 1, b'\n\x13com.groupme.android\x10\x00\x1a\x0897776964"\x08Jennifer(\x000\x008\x01') {'1': 'com.groupme.android', '2': '0', '3': '97776964', '4': 'Jennifer', '5': '0', '6': '0', '7': '1'}
# (12755, 'GroupMe', 854269542, 1, b'\n\x13com.groupme.android\x10\x00\x1a\x0897776964"\x08Jennifer(\x000\x008\x01') {'1': 'com.groupme.android', '2': '0', '3': '97776964', '4': 'Jennifer', '5': '0', '6': '0', '7': '1'}
class people_search_a12(Enum):
    NOT_DEFINED = -1
    PACKAGE_NAME = "1"
    USER_IDENTIFIER = "3"
    USER_NICKNAME = "4"
    @classmethod
    def _missing_(cls, value):
        return cls.NOT_DEFINED





class people_search(Enum):
    NOT_DEFINED = -1
    SOURCES = "2"
    @classmethod
    def _missing_(cls, value):
        return cls.NOT_DEFINED


class people_search_SOURCES(Enum):
    NOT_DEFINED = -1
    PACKAGE_NAME = "2"
    USER_IDENTIFIER = "3"

    @classmethod
    def _missing_(cls, value):
        return cls.NOT_DEFINED


# a13, a14
class simple_storage_nowplayingrecognition_recognition_result(Enum):
    NOT_DEFINED = -1
    RECOGNIZED = 1  # music detection in DB
    NOT_RECOGNNIZED = 2  # detection of music not found in DB
    NOT_MUSIC = 3  # simple noise detection, not music
    SUPRESSED_AUDIO_PLAYING = 5  # audio play by device
    SUPRESSED_AUDIO_RECORDING = 6  # audio recording by device
    SUPRESSED_PHONE_CALL = 7  # call comes into your device

    @classmethod
    def _missing_(cls, value):
        return cls.NOT_DEFINED


class simple_storage_nowplayingrecognition_recognition_trigger(Enum):
    NOT_DEFINED = -1
    DSP_MODEL = 1  # by user
    GET_MODEL_STATE_SCREEN_ON = 2  # by automatic detection

    @classmethod
    def _missing_(cls, value):
        return cls.NOT_DEFINED


class portable_geller_personalized_habits_profile(Enum):
    NOT_DEFINED = -1
    MEDIA = "MEDIA"
    SHOPPING_LOCATION = "SHOPPINGLOCATION"
    TRANSPORTATION = "TRANSPORTATION"

    @classmethod
    def _missing_(cls, value):
        return cls.NOT_DEFINED


# should not be implement --> todo : just make another parser for it not by enum
class nasa_ps_db(Enum):
    NOT_DEFINED = -1
    LIVE_CAPTION = 1  # use real time voice subtitle generation function
    SCREENSHOT = 3  # use screen shot
    ATTENTION = 4  # screen gaze detection from user
    NOW_PLAYING = 5  # setting the function to detect music heard nearby
    TEXT_CLASSIFIER = 7  # text category detection
    HYBRID_HOTSEAT = 9  # run application at the bottom of the desktop
    ECHO_ALL_APPS = 10  # execution prediction score update
    VISUAL_CORTEX = 12  # call artificial intelligence function for screen output image
    ADAPTIVE_AUDIO = 14  # set appropriate sound level after analyzing surrounding noise
    LENS_SCREENSHOTS_TRANSLATE = 17  # translation through Google Lens for screenshots
    AUTO_ROTATE = 22  # automatic screen rotation
    LIVE_TRANSLATE_CHIP_TRIGGER = 35  # real-time text translation triggered

    @classmethod
    def _missing_(cls, value):
        return cls.NOT_DEFINED


# should not be implement --> todo : just make another parser for it not by enum
class cell_db(Enum):
    NOT_DEFINED = -1
    LIVE_CAPTION = 1  # use real time voice subtitle generation function
    SCREENSHOT = 3  # use screen shot
    ATTENTION = 4  # screen gaze detection from user
    NOW_PLAYING = 5  # setting the function to detect music heard nearby
    TEXT_CLASSIFIER = 7  # text category detection
    HYBRID_HOTSEAT = 9  # run application at the bottom of the desktop
    ECHO_ALL_APPS = 10  # execution prediction score update
    VISUAL_CORTEX = 12  # call artificial intelligence function for screen output image
    ADAPTIVE_AUDIO = 14  # set appropriate sound level after analyzing surrounding noise
    LENS_SCREENSHOTS_TRANSLATE = 17  # translation through Google Lens for screenshots
    AUTO_ROTATE = 22  # automatic screen rotation
    LIVE_TRANSLATE_CHIP_TRIGGER = 35  # real-time text translation triggered

    @classmethod
    def _missing_(cls, value):
        return cls.NOT_DEFINED


if __name__ == '__main__':
    print("unit test?")
