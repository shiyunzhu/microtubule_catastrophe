import numpy as np
import scipy.special

import pandas as pd

import panel as pn
pn.extension()

import colorcet

import bokeh_catplot
import bokeh.io
import holoviews as hv

import bebi103

import microtubule_catastrophe.general_utils as utils

bokeh.io.output_notebook()
hv.extension('bokeh')

def make_ecdf(df, x_vals, groupby, groupby_vals):
    '''Creates a holoviews points graph of the ECDFs grouped into groupby values
       -------------------------------------------------------------------------
       Parameters:
       df - Dataframe that contains a column called x_vals and a column called 
       groupby with those values
       x_vals - a String that is the column name of the x values wanted for 
       the ECDF
       groupby - a String that is the column name of the values we want to 
       group by
       groupby_vals - an array of values we want to compare (in the column 
       named groupby)
       --------------------------------------------------------------------------
       Return:
       A holoviews graph
       '''
    
    for val in groupby_vals:
        df_val = df.loc[df[groupby] == val]
        sorted_x, ecdfs = utils.ecdf_vals(df_val[x_vals])
        df.loc[df[groupby] == val, x_vals] = sorted_x
        df.loc[df[groupby] == val, 'ECDF val'] = ecdfs

    p = hv.Points(
        data=df,
        kdims=[x_vals, 'ECDF val'],
        vdims=[groupby]
    ).groupby(
        groupby
    ).overlay()
    
    return p
    
    