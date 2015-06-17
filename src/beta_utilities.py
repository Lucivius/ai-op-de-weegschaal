# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 10:55:42 2015

@author: Tom
"""

from __future__ import division
import numpy as np
from scipy.stats import beta
import os
import csv

headers = [5, 15, 35]
adtypes = ['skyscraper', 'square', 'banner']
colors = ['green', 'blue', 'red', 'black', 'white']
productids = np.arange(10, 26, 1)
prices = [25,35,45]



def create_possible_pages(headers, adtypes, colors, productids, prices):
    possible_pages=[]
    for header in headers:
        for adtype in adtypes:
            for color in colors:
                for productid in productids:
                    for price in prices:
                        possible_pages.append({'header': header, 'adtype' : adtype, 'color' : color, 'productid' : productid, 'price' : price})

    return possible_pages



def draw_from_beta_distributions(alphas, betas):

    max_id = 0
    max_=0
    
    for i in range(0, (alphas.size-1)):
        beta_outcome = beta.rvs(alphas[i], betas[i])
        
        if  beta_outcome > max_:
            max_ = beta_outcome
            max_id = i
        
    return max_id
    
def update_alphas_betas(index, success, alphas, betas, price):
    
    if success==1:
        alphas[index] = float(alphas[index]+1*(price/50))# pas alpha aan naar de prijs van het product
        
    else:
        betas[index] = float(betas[index]+1*(price/50))# niet zeker of het bij de failures ook moet
        
    return alphas, betas
    
def save_ab(runid, i, alphas, betas, file_path = '../data/alpha_beta/'):
        print 'write alphas and betas to file'        
        
        if not os.path.exists(file_path):
            os.makedirs(file_path)

        filename = file_path + str(runid)        
        index = np.array(i)
        np.savez(filename, alphas=alphas, betas=betas, index=index)
#        if os.path.isfile(filename):
#            f = open(filename, 'a')
#        else:
#            f= open(filename, 'w')
#        
#        writer = csv.writer(f)
#        writer.writerow([i, alphas, betas])
#        
#        f.close()

def load_ab(runid, i, file_path = '../data/alpha_beta/'):
    filename = file_path + str(runid) + ".npz"
    
    data = np.load(filename)
    a = data['alphas']
    b = data['betas']
    index = data['index']
    data.close()
    return a,b, index
    
#    f = open(filename, 'r')
#    
#    reader = csv.reader(f)
#    for row in reader:
#        if int(row[0]) == i:
#            f.close()
#            return row[1], row[2]
#        
    
if __name__ == '__main__':
    
    runid = 0
    i = 0
    a1 = np.arange(10)
    b1 = np.arange(10,20)
    save_ab(runid, i, a1, b1)
    print load_ab(runid, i)

    
    
    
    
    
        