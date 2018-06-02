# -*- coding: utf-8 -*-
"""
Created on Thu Jun 22 15:50:54 2017

@author: saqibhasan
"""
def maptest14bus_test_system(comp_filename, start_range, contingency_range):
    
    valueset = [];
# -------------- Open and read the text file and convert the content into a dictionary and returning it ----------------    
    data_file = open(comp_filename, 'r'); 
    line_data = data_file.readline();
    valueset = eval(line_data);
    data_file.close()

    return valueset;
    
#maptest14bus_test_system("G:\saqib\open DSS\OpenDSS_Python_Interface\ieee_14_bus_data\component_data_subs.txt",1,2, tuple(['S1']));
