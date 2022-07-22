from enum import Enum

class Cmd(Enum):
    INIT = 1
    SCREEN_CLR = 2
    LOAD_SERVER = 3
    SAVE_SERVER = 4
    LOG_CLR = 5
    INPUT_CLR = 6
    
    LOAD_SPR_INFO = 20
    SAVE_F_SPR_INFO_EXCEL = 21
    # BTN = 22
    # BTN = 23
    LOAD_SPR_SUM = 24
    SAVE_F_SPR_SUM_EXCEL = 25
    
    # FILE_JOB_1 = 22
    # CONVERT = 23
    # CONVERT_ALL = 24

    CONVERT_ERAW_SPR = 40
    SAVE_SUM_SPR_EXCLE = 41
    # BTN = 22
    # BTN = 23
    LOAD_SUM_SPR_LLP = 44
    SAVE_LLP_EXCEL = 45
    
    # RESULT_LOAD = 40
    # LOAD_SPR_FILE = 41
    # SAVE_SPR_EXCEL = 42
    # LOAD_ALL = 43
    # SAVE_ALL = 44

class Filter(Enum):
    NONE = 0
    PATHNER = 1
    OEM = 2
    SPR_NO = 3
    PROJECT = 4
    DATE = 5
    





    
        