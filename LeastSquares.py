from numpy import transpose as t
from numpy import matrix as mat, matmul as mm
import math as m
import numpy as np
import pandas as pd

class LS():
    """
        Holds the universal values needed to integrate the different LS adjustments into one
    """
    def __init__(self):
        """
        Desc:
            
        Input:
        Output:
            sets up u_list (predefined in here)
            sets up number of unknowns (self.u)
            
                    self.u_list = ['SA10_E', "SA10_N", "SA10_H", 
                        'UCAL_E', "UCAL_N", "UCAL_H", 
                         'ASCM1_E', "ASCM1_N", "ASCM1_H",
                        'BASE_E', "BASE_N", "BASE_H",
                        'C1_E', "C1_N", "C1_H",
                        'C2_E', "C2_N", "C2_H",
                        'C3_E', "C3_N", "C3_H",
                      'N_E', "N_N", "N_H",
                      'S_E', "S_N", "S_H"]
        """
        
        #_______________________________________________________________
                #N, E, H linear
        self.u_list = ['SA10_E', "SA10_N", "SA10_H", 
                        'UCAL_E', "UCAL_N", "UCAL_H",
                       'ASCM1_E', "ASCM1_N","ASCM1_H",
                        'BASE_E', "BASE_N", "BASE_H",
                        'C1_H',
                        'C2_E', "C2_N", "C2_H",
                        'C3_E', "C3_N", "C3_H",
                      "N_H",
                      "S_H"]
        #N, E, H linear only
        self.x_0 = t(mat([-9292.095, 5660358.617, 1136.040,#SA10
                         -9378.481, 5660425.221, 1135.642,#UCAL
                          -9903.780, 5659098.252, 1099.627,#ASCM1
                         -9245.156, 5660419.921, 1111.683,#BASE
                         1111.207, #C1
                         -9492.719, 5660518.107, 1112.521, #C2
                         -9428.997, 5660514.752, 1114.125,#C3
                         1135.959, #N
                         1135.887 ]))#S
        
        #ASCM2_H, C1E, C1N
        self.c = t(mat([1110.234, -9000, 566000]))
        #_______________________________________________________________
        #_______________________________________________________________
                #H linear
        self.u_list = [
            "SA10_H", 
                        "UCAL_H",
                       "ASCM1_H",
                        "BASE_H",
                        'C1_H',
                        "C2_H",
                        "C3_H",
                      "N_H",
                      "S_H"]
        #N, E, H linear only
        self.x_0 = t(mat([ 
                            1136.040,#SA10
                          1135.642,#UCAL
                          1099.627,#ASCM1
                          1111.683,#BASE
                         1111.207, #C1
                          1112.521, #C2
                          1114.125,#C3
                         1135.959, #N
                         1135.887 ]))#S
        
        #ASCM2_H, C1E, C1N
        self.c = t(mat([1110.234, -9000, 566000]))
        #_______________________________________________________________
        #_______________________________________________________________
                #E N linear
        self.u_list = ['SA10_E', "SA10_N",  
                        'UCAL_E', "UCAL_N",
                       'ASCM1_E', "ASCM1_N",
                        'BASE_E', "BASE_N", 
                        'C2_E', "C2_N", 
                        'C3_E', "C3_N", 
                    ]
        #N, E, H linear only
        self.x_0 = t(mat([-9292.095, 5660358.617, #SA10
                         -9378.481, 5660425.221, #UCAL
                          -9903.780, 5659098.252,#ASCM1
                         -9245.156, 5660419.921, #BASE
                          #C1
                         -9492.719, 5660518.107,  #C2
                         -9428.997, 5660514.752, #C3
                         
                         ]))#S
        
        #ASCM2_H, C1E, C1N
        self.c = t(mat([1110.234, -9000, 566000]))
        
        self.datums = [
            "ASCM2_H",
            "C1_E",
            "C1_N",
            "1_solo"
        ]
        #_______________________________________________________________   
        #_______________________________________________________________
        #H linear (leveling only)
        self.u_list = [
                        'C1_H',
                        "C2_H",
                        "C3_H",]
        #N, E, H linear only
        self.x_0 = t(mat([
                         1111.207, #C1
                          1112.521, #C2
                          1114.125,#C3
        ]))#S
        
        #ASCM2_H, C1E, C1N
        self.c = t(mat([1110.234, -9000, 566000]))
        
        self.datums = [
            "ASCM2_H"]
        #_______________________________________________________________ 
        #_______________________________________________________________
        #H linear (leveling and static
        self.u_list = [
                        "SA10_H", 
                        "UCAL_H",
                       "ASCM1_H",
                        "BASE_H",
                        'C1_H',
                        "C2_H",
                        "C3_H",
                      "N_H",
                      "S_H"]
        #N, E, H linear only
        self.x_0 = t(mat([ 
                            1136.040,#SA10
                          1135.642,#UCAL
                          1099.627,#ASCM1
                          1111.683,#BASE
                         1111.207, #C1
                          1112.521, #C2
                          1114.125,#C3
                         1135.959, #N
                         1135.887 ]))#S
        
        #ASCM2_H, C1E, C1N
        self.c = t(mat([1110.234, -9000, 566000]))
        
        self.datums = [
            "ASCM2_H"]
        #_______________________________________________________________
                #_______________________________________________________________
                #N, E, H linear
        self.u_list = ['SA10_E', "SA10_N", "SA10_H", 
                        'UCAL_E', "UCAL_N", "UCAL_H",
                       'ASCM1_E', "ASCM1_N","ASCM1_H",
                        'BASE_E', "BASE_N", "BASE_H",
                        'C1_H',
                        'C2_E', "C2_N", "C2_H",
                        'C3_E', "C3_N", "C3_H",
                      "N_H",
                      "S_H"]
        #N, E, H linear only
        self.x_0 = t(mat([-9292.095, 5660358.617, 1136.040,#SA10
                         -9378.481, 5660425.221, 1135.642,#UCAL
                          -9903.780, 5659098.252, 1099.627,#ASCM1
                         -9245.156, 5660419.921, 1111.683,#BASE
                         1111.207, #C1
                         -9492.719, 5660518.107, 1112.521, #C2
                         -9428.997, 5660514.752, 1114.125,#C3
                         1135.959, #N
                         1135.887 ]))#S
        
        #ASCM2_H, C1E, C1N
        self.c = t(mat([1110.234, -9000, 566000]))
        #_______________________________________________________________
        self.u = len(self.u_list)
        
    def find_col(self, dimension, point_name, li = "u"):
        """
        Desc:
            returns the column index of the desired points
            **all values must be in caps**
        Input:
            u_list, list of strings of "pointname_dimension"
            dimension, string either "N", "E", "H"
        Output:
            integer value of the column to place the value 
            in the desired design matrix     
        """
        if li == "u" :
            li = self.u_list
        else:
            li = self.datums
            
        index = 0
        for key in li:
            #split the key into point name and dimension
            temp_name = key.split('_')[0]
            temp_dimension = key.split('_')[1]
            if (point_name == temp_name and dimension == temp_dimension):
                return index
            else:
                index = index + 1
        
        print(point_name + " Could not be found")
        return -1