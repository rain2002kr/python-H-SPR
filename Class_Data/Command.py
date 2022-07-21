from enum import Enum

class Cmd(Enum):
    INIT = 1
    SCREEN_CLR = 2
    LOAD_SERVER = 3
    SAVE_SERVER = 4
    LOG_CLR = 5
    INPUT_CLR = 6
    
    SPR_INFO_1 = 20
    FILE_JOB_0 = 21
    FILE_JOB_1 = 22
    CONVERT = 23
    CONVERT_ALL = 24

    RESULT_LOAD = 40
    LOAD_SPR_FILE = 41
    SAVE_SPR_EXCEL = 42
    LOAD_ALL = 43
    SAVE_ALL = 44

class Filter(Enum):
    NONE = 0
    PATHNER = 1
    OEM = 2
    SPR_NO = 3
    PROJECT = 4
    





    
        