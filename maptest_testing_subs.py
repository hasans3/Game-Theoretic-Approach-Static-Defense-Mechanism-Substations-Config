# -*- coding: utf-8 -*-
"""
Created on Tue Jun 06 15:45:48 2017

@author: saqibhasan
"""
def maptest14bus_test_system(comp_filename, start_range, contingency_range):
    
# To generate all possible combinations itertools is needed
    import itertools
    cmb = [];
    valueset =[];
    valueset = comp_filename;
#    print valueset
# ------------- Generate all the possible combinations from the list ------------- 
    for i in range(start_range, contingency_range):
        comb=[];
        for j in itertools.combinations(valueset, i+1):
            comb.append(list(j));
            #print comb
        cmb.append(comb);
#    print cmb
    return cmb;
    
#maptest14bus_test_system("G:\saqib\open DSS\OpenDSS_Python_Interface\ieee_14_bus_data\component_data_subs.txt",1,2);