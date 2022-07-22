
from PyQt5.QtCore import QCoreApplication, QBasicTimer, Qt, QTimer, QTime,QSize

from Class_Data.Command import Cmd, Filter
import pandas as pd
from datetime import datetime

import module as md
import ui_module as uimd



DEBUG_ON = 1
DEBUG_OFF = 0

debug = DEBUG_OFF
D_main_process = DEBUG_OFF


def ui_process1(self, cmd, date= '220701', sht_num_cnt = 0):
        v_str_command = cmd
        v_int_date = date
        v_int_sht_num_cnt = int(sht_num_cnt)

        if v_str_command == Cmd.INIT:
            message =f"{Cmd.INIT.name}  SPR_DATA.xlsx 파일을 만들었습니다."
            log(self, message)
            md.create_new_excel()    
            bar_timer_on(self, "start",10)
        
        if v_str_command == Cmd.SCREEN_CLR:
            bar_timer_on("start",5)
            message =f"{Cmd.SCREEN_CLR.name}  테이블 스크린을 지웠습니다."
            log(self, message)
            self.tbw1.clear()

        
        if v_str_command == Cmd.LOAD_SERVER:
            message = Cmd.LOAD_SERVER.name
            log(self, message)    
        
        if v_str_command == Cmd.SAVE_SERVER:
            message = Cmd.SAVE_SERVER.name
            log(self, message)

        if v_str_command == Cmd.LOG_CLR:
            message = Cmd.LOG_CLR.name
            log(self, message, clear = True) 
        
        if v_str_command == Cmd.INPUT_CLR:
            message = Cmd.INPUT_CLR.name
            log(self, message, clear = True) 
            self.ed1_1.setText("")
            self.ed1_2.setText("")
            self.ed1_3.setText("")
            self.ed2_1.setText("")
            self.ed2_2.setText("")
            self.ed2_3.setText("")
            self.ed2_4.setText("")
            self.ed3_1.setText("")


def ui_process2(self, cmd, date= '220701', sht_num_cnt = 0):
        v_str_command = cmd
        v_int_date = date
        v_int_sht_num_cnt = int(sht_num_cnt)

        if v_str_command == Cmd.LOAD_SPR_INFO:
            bar_timer_on(self, "start",10)
            message = Cmd.LOAD_SPR_INFO.name
            log(self, message)

            df = md.load_spr_info_excel()
            message = 'LOAD SPR INFO EXCEL'
            log(self, message)

            
            if self.rbt1.isChecked():
                message = Filter.PATHNER.name
                log(self, message)
                df = md.make_df_spr_info(self, df, Filter.PATHNER)
                message = 'MAKE DF SPR INFO'
                log(self, message)


            elif self.rbt2.isChecked():
                message = Filter.OEM.name
                log(self, message)
                df = md.make_df_spr_info(self, df, Filter.OEM)
                message = 'MAKE DF SPR INFO'
                log(self, message)

            elif self.rbt3.isChecked():
                message = Filter.SPR_NO.name
                log(self, message)
                df = md.make_df_spr_info(self, df, Filter.SPR_NO)
                message = 'MAKE DF SPR INFO'
                log(self, message)

            elif self.rbt4.isChecked():
                message = Filter.PROJECT.name
                log(self, message)
                df = md.make_df_spr_info(self, df, Filter.PROJECT)
                message = 'MAKE DF SPR INFO'
                log(self, message)
            
            elif self.rbt5.isChecked():
                message = Filter.DATE.name
                log(self, message)
                df = md.make_df_spr_info(self, df, Filter.DATE)
                message = 'MAKE DF SPR INFO'
                log(self, message)
            
            else :
                df = md.make_df_spr_info(self, df, Filter.NONE)
                message = 'MAKE DF SPR INFO'
                log(self, message)
            
            uimd.set_df_table(self,df)
            message = 'call set table'
            log(self, message)
        
        if v_str_command == Cmd.SAVE_F_SPR_INFO_EXCEL:
            bar_timer_on(self, "start",10)
            message = Cmd.SAVE_F_SPR_INFO_EXCEL.name
            log(self, message) 

            md.save_filtered_spr_info_excel(self)
            message = 'save_filtered_spr_info_excel()'
            log(self, message) 


        if v_str_command == Cmd.LOAD_SPR_SUM:
            message = Cmd.LOAD_SPR_SUM.name
            log(self, message)    
            
        
        if v_str_command == Cmd.SAVE_F_SPR_SUM_EXCEL:
            message = Cmd.SAVE_F_SPR_SUM_EXCEL.name
            log(self, message)    
        

def ui_process3(self, cmd, date= '220701', sht_num_cnt = 0):
        v_str_command = cmd
        v_int_date = date
        v_int_sht_num_cnt = int(sht_num_cnt)
        
        if v_str_command == Cmd.CONVERT_ERAW_SPR:
            bar_timer_on(self, "start",10)
            message = Cmd.CONVERT_ERAW_SPR.name
            log(self, message)

            frame = md.load_spr_in_folds()
            message = 'md.load_spr_in_folds()'
            log(self, message)

            df = md.make_df_from_arr(frame)
            message = 'md.make_df_from_arr(frame)'
            log(self, message)

            uimd.set_df_table(self,df, 11)
            message = 'uimd.set_df_table(self,df, 11)'
            log(self, message)

        if v_str_command == Cmd.SAVE_SUM_SPR_EXCLE:
            message = Cmd.SAVE_SUM_SPR_EXCLE.name
            log(self, message)    
            bar_timer_on(self, "start",10)
        
        if v_str_command == Cmd.LOAD_SUM_SPR_LLP:
            message = Cmd.LOAD_SUM_SPR_LLP.name
            log(self, message)    

        if v_str_command == Cmd.SAVE_LLP_EXCEL:
            message = Cmd.SAVE_LLP_EXCEL.name
            log(self, message)        

def log(self, message , clear = False):
        TODAY = datetime.today().strftime("%y-%m-%d-%H:%M:%S")
        print('LOG : ' + TODAY + ": " + message)
        self.tb1.append('LOG : ' + TODAY + " :  " + message)
        if clear:
            self.tb1.clear()


def bar_timer_on(self, commend, base_time = 10):
        if commend == "init": 
            self.bar1_timer.timeout.connect(lambda : timerEvent(self,1))  
            self.bar1.setValue(0)
            self.bar1_time = QTime(0,0,0) 

        elif commend == "start":
            self.bar1_timer.timeout.connect(lambda : timerEvent(self,1))  
            self.bar1.setValue(0)
            self.bar1_time = QTime(0,0,0) 
            self.bar1_timer.start(base_time)

        elif commend == "end": 
            self.bar1_timer.stop()
        else :
            print("timer 동작안함")


def timerEvent(self, time_interval = 1):
    self.bar1_time = self.bar1_time.addSecs(time_interval)
    v_int_time = int(self.bar1_time.toString("ss"))
    self.bar1.setValue(v_int_time)
    
    if v_int_time >= self.bar1.maximum():
        self.bar1_timer.stop()
        return 