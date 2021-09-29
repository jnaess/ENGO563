from numpy import transpose as t
from numpy import matrix as mat, matmul as mm
import matplotlib as plt

from numpy import linalg as lin
from numpy.linalg import inv
import math as m
import numpy as np
import pandas as pd
from LeastSquares import LS
from Level import Delta
from Tables import Tables

from scipy import stats
from scipy.stats import t as stu



class PostAdjustmentTester(Tables):
    """
    Desc:
        Assumes that the LSA has been conducted and outputs results for post adjustment tests
    """
    def __init__(self):
        """
        Desc:
            Figuring out if we need to take in matrices or if we'll just inherit the class and assume that they're build
        """
        Tables.__init__(self)
        
    def global_a_posteriori(self, alpha = .05):
        """
        Desc:
            Tests the statistical sifnigicance of the aposteriori to a priori variance factor
        Input:
            alpha: to generate the two confidence intervals. Be sure to make sure that these values are generated in the respective dataframe of values, otherwise they won't be found :-)
            self.u: # of unknowns
            self.n: # of knowns
            self.a_post: final computed a posteriori variance factor
            self.apriori: initial apriori variance factor
        Output:
            Prints the output and respective indication
        """
        #set up DOF (r)
        self.r = self.n - self.u
        
        #retrieves dataframe of chi values for our respective DOF
        ch_df = self.x_2()
        
        low = ch_df[alpha][0]
        high = ch_df[1-alpha][0]
        
        y = (self.r * self.a_post**2)/self.apriori**2
        
        #if fails this check then there is an indication that the residuals or math model may be off
        
        
        print("{} tested with chi_square boundries of {} and {}".format(y, low, high))
        if y > low and y < high:
            print("Global A-Posteriori Variance Factor Test passes at a {} confidence level".format((1 - alpha)*100))
            print("There is no indication for errors within residual or the math models")
        else:
            print("Global A-Posteriori Variance Factor Test **failed** at a {}% confidence level".format((1 - alpha)*100))
            print("There is indication that errors exsist within residual or the math models")
            
    def significance_estimated_param(self, alpha = .05):
        """
        Desc:
            Determines whether there is statistical signifiance to beleive the final estimated value of parameters
        Input:
            alpha: to generate the two confidence intervals. Be sure to make sure that these values are generated in the respective dataframe of values, otherwise they won't be found :-)
        Output:
        """
        #set up DOF (r)
        self.r = self.n - self.u
        
        high = stu.ppf(1.0 - alpha, self.r)
        low = stu.ppf(alpha, self.r)
        
        #final paramter values
        self.x_hat
        xs = []
        
        #unknown names in string format
        self.u_list
        us = []
        
        #list to store their signifiance as Signifiance or Not Significant
        sig = []
        
        #list to store the value that was checked
        sig_value = []
        
        #list of standard deviation values
        std = []
        
        #test values
        y = []
        
        #confidence levels
        conf = []
        
        #confidence levels
        alphs = []
        
        #test bounds
        bounds = []
        
        
        for i in range(0,self.u):
            std.append(m.sqrt(self.Cx[0,0]))
            
            y.append((self.x_hat[i]/std[i])[0,0])
            
            if y[i] > low and y[i] < high:
                #if fails then there IS statistical significance
                sig.append("No")
            else:
                sig.append("Yes")
                
            xs.append(self.x_hat[i][0,0])
            us.append(self.u_list[i])
            conf.append((1-alpha)*100)
            alphs.append(alpha)
            bounds.append(str([low, high]))
        #to store values in a dictionary before conversion to dataframe
        dict_list = {
                "Unknown": xs,
                "Final Value": us,
                "Value Standard Deviation": std,
                "Test Value": y,
                "Indicated Significance": sig,
                "Alpha Tested": alphs,
                "Confidence Level": conf,
                "Test Bounds": bounds
            }
        #return dict_list
        return pd.DataFrame.from_dict(dict_list)