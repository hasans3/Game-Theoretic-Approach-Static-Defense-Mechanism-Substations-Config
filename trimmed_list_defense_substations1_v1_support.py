# -*- coding: utf-8 -*-
"""
Created on Thu Jun 22 17:09:46 2017

@author: saqibhasan
"""
def maptest14bus_test_system(comp_filename, start_range, contingency_range, selected_item, substation_names):
    
    from  more_itertools import unique_everseen
    valueset = [];
    sub_items = {};
    temp_valueset = {};
    temp_sub_item_values = [];
# -------------- Open and read the text file and convert the content into a list ----------------    
    data_file = open(comp_filename, 'r'); 
    line_data = data_file.readline();
    valueset = eval(line_data);
    data_file.close()
#    for item in range(0, len(pro_subs_name)):
#        if pro_subs_name[item] in valueset:
#            del valueset[pro_subs_name[item]];
    for item in range(0, len(substation_names)):
        if substation_names[item] in valueset:
            del valueset[substation_names[item]];
    for t in range(0, len(selected_item)):
        if selected_item[t] in valueset:
            temp_sub_item_values = temp_sub_item_values + valueset[selected_item[t]];
            sub_items[selected_item] = temp_sub_item_values;
            del valueset[selected_item[t]];
    for item in valueset:
        valueset_key_values = valueset[item];
        sub_items_values = sub_items[selected_item];
        temp_valueset[tuple([item]) + tuple(selected_item)] = list(unique_everseen(valueset_key_values + sub_items_values));
    print temp_valueset
    return temp_valueset
    
#maptest14bus_test_system("G:\saqib\open DSS\OpenDSS_Python_Interface\ieee_14_bus_data\component_data_subs.txt", 1, 2, ('S4','S7'), tuple(['S1']));