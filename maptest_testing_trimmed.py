# -*- coding: utf-8 -*-
"""
Created on Fri Jun 16 11:11:22 2017

@author: saqibhasan
"""
def maptest14bus_test_system(comp_filename, start_range, contingency_range, selected_item):
    
# --------------------- Importing supporting libraries and method variable initialization ----------------------
    from  more_itertools import unique_everseen
    valueset = [];
    sub_items = {};
    temp_valueset = {};

# -------------- Open and read the text file ----------------    
    data_file = open(comp_filename, 'r'); 
    line_data = data_file.readline();
    valueset = eval(line_data);
    data_file.close()

# -------------- Removing selected substation from the system model ----------------
    if selected_item in valueset:
        sub_items[selected_item] = valueset[selected_item];
        del valueset[selected_item]
# ------------- Creating a new selection space for the attack strategy -------------------
    for item in valueset:
        temp_valueset[item, selected_item] = valueset[item];
        valueset_key_values = valueset[item];
        sub_items_values = sub_items[selected_item];
        temp_valueset[item,  selected_item] = list(unique_everseen(valueset_key_values + sub_items_values));
    print temp_valueset
    return temp_valueset

    
# maptest14bus_test_system("G:\saqib\open DSS\OpenDSS_Python_Interface\ieee_14_bus_data\component_data_subs.txt",1,2,'S7');
