# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 16:21:26 2017

@author: saqibhasan
"""
def maptest14bus_test_system(comp_filename, start_range, contingency_range, substation_name, pro_subs):
    
    valueset = [];
# -------------- Open and read the text file and convert the content into a list ----------------    
    data_file = open(comp_filename, 'r'); 
    line_data = data_file.readline();
    valueset = eval(line_data);
    data_file.close()
    print valueset
    print len(valueset)
    print len(substation_name)
    for item in range(0, len(pro_subs)):
        if pro_subs[item] in valueset:
            del valueset[pro_subs[item]];
    for item in range(0, len(substation_name)):
        if substation_name[item] in valueset:
            del valueset[substation_name[item]];
    print valueset
    print len(valueset)
    return valueset;
    
#maptest14bus_test_system("G:\saqib\open DSS\OpenDSS_Python_Interface\ieee_14_bus_data\component_data_subs.txt",1,2, tuple(['S1']), ['S2', 'S3']);