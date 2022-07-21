import pandas as pd

DEBUG_ON = 1
DEBUG_OFF = 0

debug = DEBUG_OFF
D_get_mlfb = DEBUG_OFF
D_get_bu = DEBUG_OFF
D_get_factor = DEBUG_OFF

# FUNCTION CODE : load_spr_info_excel
# 
# comment : 
###############################################################################################    
def get_mlfb(mlfb):
    v_str_mlfb = mlfb[:5]
    r_str_mlfb = ""
    try :
        if v_str_mlfb == "6GK75":
            r_str_mlfb = "PA CM"
            
        if v_str_mlfb == "1FN31" or v_str_mlfb == "L1M21":
            r_str_mlfb ="MC 리니어"
        
        if v_str_mlfb == "1FW32":
            r_str_mlfb ="MC 토크모터"
        
        
        if debug or D_get_mlfb: 
            SUCCESS = f'get_mlfb : SUCCESS'
            print(f"CODE : {SUCCESS} ") 
            print(f"CODE : {v_str_mlfb} ") 
            print(f"CODE : {r_str_mlfb} ") 
        
        return r_str_mlfb 
        
    except :
        if debug or D_get_mlfb: 
            ERROR = f'get_mlfb : ERROR '
            print(f"CODE : {ERROR} ")
# FUNCTION CODE : get_bu
# 
# comment : 
###############################################################################################    
def get_bu(pg):
    v_pg = pg
    r_pg = ""
    FA_L = ["Z1", "JG", "9J", "95", "1)", "2Z7"	]
    MC_L = ["1!", "(1", "1%", "16", "51", "71", "4E", "5T", "IM", "IP", "5!", "14", "18", "52", "4G", "5B", "5C", "5N", "5Q", "5S", "5Y", "5Z", "D5", "D6", "JA"]
    MC_G = "1?"
    PA_L = ["6T", "6)", "6(", "6R", "6S", "Z0", "Z2", "Z3", "Z4", "ZJ", "Z5"]
    try :
        for item in FA_L:
            if v_pg == item:
                r_pg = "FA"
                return r_pg 

        for item in MC_L:
            if v_pg == item:
                r_pg = "MC"
                return r_pg 

        for item in PA_L:
            if v_pg == item:
                r_pg = "PA"
                return r_pg 
        if v_pg == MC_G:
            r_pg = "MC_G"
            return r_pg  
        
        else :
            r_pg = "BU 확인"
        
        if debug or D_get_bu: 
            SUCCESS = f'get_bu : SUCCESS'
            print(f"CODE : {SUCCESS} ") 
            print(f"CODE : {v_pg} ") 
            print(f"CODE : {r_pg} ") 
        
        return r_pg 
        
    except :
        if debug or D_get_bu: 
            ERROR = f'get_bu : ERROR '
            print(f"CODE : {ERROR} ")
# FUNCTION CODE : get_bu
# 
# comment : 
###############################################################################################    
def get_factor(discount):
    v_dis = float(discount)
    r_dis = 0.0
    
    try :
        r_dis = (100.0 - v_dis) / 100.0
        
        
        if debug or D_get_factor: 
            SUCCESS = f'get_factor : SUCCESS'
            print(f"CODE : {SUCCESS} ") 
            print(f"CODE : {r_dis} ") 
            
        
        return r_dis 
        
    except :
        if debug or D_get_factor: 
            ERROR = f'get_factor : ERROR '
            print(f"CODE : {ERROR} ")