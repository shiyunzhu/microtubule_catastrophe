import numpy as np
import pandas as pd

def ecdf_vals(vals):
        '''This function takes in a one-dimensional numpy array or pandas series
           and calculates the ECDF of each value.
           ---------------------------------------------------------------------
           Parameters:
           vals - 1-D numpy array or pandas series
           ---------------------------------------------------------------------
           Output:
           two arrays - sorted_vals, ECDFs'''
        
        sorted_vals = np.sort(vals)
        result = np.arange(1, vals.size + 1) / vals.size       
            
        return sorted_vals, result
