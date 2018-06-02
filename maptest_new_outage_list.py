# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 15:27:21 2017

@author: saqibhasan
"""
def maptest14bus_test_system(comp_filename, start_range, contingency_range, max_load_loss_contingency):
    from compiler.ast import flatten    
    
# Method Variables Initialization
    CMB = [];
    CMB_new = [];
    temp_valueset = [];
    new_valueset = []
    valueset_new = []
    valueset = comp_filename;
    valueset_new = list(flatten(valueset))
    iter_max_load_loss_outage = max_load_loss_contingency
    max_load_loss_outage = iter_max_load_loss_outage
    max_load_loss_outage = list(flatten(max_load_loss_outage))
    
    # Remove the identified transmission lines 
    for elem in range(0, len(max_load_loss_outage)):
        valueset_new.remove(max_load_loss_outage[elem])
    new_valueset = [valueset_new[i:i+1] for i in range(0, len(valueset_new), 1)]
    
    # Creating a new contingency list
    for i in range(0, len(new_valueset)):
        temp_valueset = new_valueset[i];
        temp_iter_max_load_loss_outage = iter_max_load_loss_outage[0];
        iter_temp_comb = temp_valueset + temp_iter_max_load_loss_outage;
        CMB.append(iter_temp_comb)
    CMB_new.append(CMB)
    return CMB_new
    

#maptest14bus_test_system("G:\saqib\open DSS\OpenDSS_Python_Interface\ieee_14_bus_data\component_data.txt",0,1);
