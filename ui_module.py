from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import pandas as pd
from openpyxl import load_workbook
import module as md
DEBUG_ON = 1
DEBUG_OFF = 0

debug = DEBUG_OFF
D_set_df_table_3_arr = DEBUG_OFF
D_set_df_table_2_arr = DEBUG_OFF
D_set_df_table = DEBUG_OFF

try:
    
# FUNCTION CODE : 
# 
# 3 array 타입 
# comment :  PLAN 에 통합시트시간, 업무시간, 학습 및 나머지 시간을 읽어와서 TABLE 에 뿌려준다. 
###############################################################################################    
    def set_df_table_3_arr(self, jobs):
        try :
            for k in range(0,len(self.tbw)):
                for i in range(0,len(jobs[k])):
                    self.tbw[k].setRowCount(len(jobs[k]))
                    self.tbw[k].setColumnCount(len(jobs[k][i].columns))
                    self.tbw[k].setHorizontalHeaderLabels(jobs[k][i].columns)
                    
            for i in range(0,len(jobs)):
                    # print(f'START {l}')
                    for j in range(0,len(jobs[i])):
                        # print(f'I V {i}')
                        for k in range(0,len(jobs[i][j].columns)):
                            # print(f'J {j}')
                            # print(jobs[i][j].iloc[0,k])
                            self.tbw[i].setItem(j,k,QTableWidgetItem(str(jobs[i][j].iloc[0, k]))) 
                            # 가운데 정렬    
                            self.tbw[i].item(j, k).setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)
            if debug or D_set_df_table_3_arr: 
                SUCCESS = f'set_df_table_3_arr : SUCCESS'
                print(f"CODE : {SUCCESS} ")
                print(f"\tREAD JOBS FRAME : {jobs}")     
            
            for k in range(0,len(self.tbw)):
                # 폭 자동조절 
                self.tbw[k].resizeColumnsToContents()
                # 날짜 폭 고정조절 
                self.tbw[k].setColumnWidth(0, 85)
            
            return self.tbw        
        except :
            if debug or D_set_df_table_3_arr: 
                ERROR = f'set_df_table_3_arr : ERROR'
                print(f"CODE : {ERROR} ")        
    
    
# FUNCTION CODE : 
# 
# 2 array 타입 
# comment :  PLAN 에 통합시트시간, 업무시간, 학습 및 나머지 시간을 읽어와서 TABLE 에 뿌려준다. 
###############################################################################################    
    def set_df_table_2_arr(self, jobs):
        try :
            for k in range(0,len(self.tbw)):
                self.tbw[k].setRowCount(len(jobs[k].index))
                self.tbw[k].setColumnCount(len(jobs[k].columns))
                self.tbw[k].setHorizontalHeaderLabels(jobs[k].columns)
                
        
                for i in range(len(jobs[k].index)):
                        for j in range(len(jobs[k].columns)):
                            self.tbw[k].setItem(i,j,QTableWidgetItem(str(jobs[k].iloc[i, j])))
                            # 가운데 정렬 
                            self.tbw[k].item(i, j).setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)
                
            for k in range(0,len(self.tbw)):
                # 폭 자동조절 
                self.tbw[k].resizeColumnsToContents()
                # 날짜 폭 고정조절 
                self.tbw[k].setColumnWidth(0, 85)

            if debug or D_set_df_table_2_arr: 
                SUCCESS = f'set_df_table_2_arr : SUCCESS'
                print(f"CODE : {SUCCESS} ")
                print(f"\tREAD JOBS FRAME : {jobs}")     
            
            return self.tbw        
        except :
            if debug or D_set_df_table_2_arr: 
                ERROR = f'set_df_table_2_arr : ERROR'
                print(f"CODE : {ERROR} ")
    
# FUNCTION CODE : 
# 
# 타입 
# comment :  계층이 없는 데이터 프레임 읽기
###############################################################################################    
    def set_df_table(self, job):
        try :
            self.tbw1.setRowCount(len(job.index))
            self.tbw1.setColumnCount(len(job.columns))
            self.tbw1.setHorizontalHeaderLabels(job.columns)
            
    
            for i in range(len(job.index)):
                    for j in range(len(job.columns)):
                        self.tbw1.setItem(i,j,QTableWidgetItem(str(job.iloc[i, j])))
                        # 가운데 정렬 
                        self.tbw1.item(i, j).setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)

            if debug or D_set_df_table: 
                SUCCESS = f'set_df_table : SUCCESS'
                print(f"CODE : {SUCCESS} ")
                print(f"\tREAD JOBS FRAME : {job}")     
            
            # 폭 자동조절 
            self.tbw1.resizeColumnsToContents()
            # 날짜 폭 고정조절 
            self.tbw1.setColumnWidth(2, 85)
            # 가운데 정렬 
            for j in range(len(job.index)):
                self.tbw1.item(j,8).setTextAlignment(Qt.AlignLeft | Qt.AlignVCenter)


            return self.tbw        
        except :
            if debug or D_set_df_table: 
                ERROR = f'set_df_table : ERROR'
                print(f"CODE : {ERROR} ")
                print(f"CODE : {len(job.index)} ")
                print(f"CODE : {len(job.columns)} ")
                print(f"CODE : {job} ")

    
                    
except Exception as ex:
    print('error' + str(ex))



