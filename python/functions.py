import pandas as pd
import numpy as np
import pickle, random


def result_table(name):
    """present the table for the selected restuarant"""
    
    with open('get_the_foodies_demo/static/result_table/'+name+'.pickle', 'rb') as f:
        table = pickle.load(f)
    
    return table

def result_f1scr(name):

    """present the f1 score for the model"""
    
    with open('get_the_foodies_demo/static/f1_scr/'+name+'.pickle', 'rb') as f:
        f1scr = pickle.load(f)
    
    return f1scr