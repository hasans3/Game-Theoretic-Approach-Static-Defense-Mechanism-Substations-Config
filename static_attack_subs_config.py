# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 12:50:11 2017

@author: saqibhasan

This code is used to identify the transmission lines and its associated protection assembly that cause the worst load loss.

"""

def greedy_hueristics(filepath, comp_filename, load_file_name, start_range, contingency_range, blackout_criterion, system_name, budget, PA_name_file):
    
    # Importing supporting methods and initializing method variables
    import cascade_algorithm
    import maptest_new_outage_list
    import cascade_algorithm_reduced_outages
    import protection_assembly_info
    import time
    tot_exe_time_start = time.time()
    temp_max_loadloss = 0;
    worst_case_outage = [];
    PA_names = [];
    max_load_loss_outage, max_loadloss = cascade_algorithm.DSS_Python_Interface1(filepath, comp_filename, load_file_name, start_range, contingency_range, blackout_criterion, system_name);
#    print max_load_loss_outage
    temp_max_loadloss = max_loadloss;
    worst_case_outage = max_load_loss_outage;  
    for k in range(0, (budget-1)):
        new_outage_list = maptest_new_outage_list.maptest14bus_test_system(comp_filename, start_range, contingency_range, max_load_loss_outage);
#        print new_outage_list
        max_load_loss_outage, max_loadloss = cascade_algorithm_reduced_outages.DSS_Python_Interface1(filepath, comp_filename, load_file_name, start_range, contingency_range, blackout_criterion, system_name, new_outage_list);
        if (max_loadloss > temp_max_loadloss):
            temp_max_loadloss = max_loadloss;
            worst_case_outage = max_load_loss_outage;
    PA_names = protection_assembly_info.protection_assembly_info(PA_name_file, worst_case_outage)
    tot_exe_time_end = time.time()
    tot_exe_time = (tot_exe_time_end - tot_exe_time_start)
    print '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@'
    print 'Worst Case Outage: %s' %worst_case_outage
    print 'Worst Case Loadloss: %s' %temp_max_loadloss
    print 'Critical Protection Assemblies: %s' %PA_names
    print 'Total Execution Time In Seconds: %s' %tot_exe_time
    print '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@'

#greedy_hueristics("'G:\saqib\open DSS\opendss_matlab_interface\ieee9bus_system.dss'", "G:\saqib\open DSS\OpenDSS_Python_Interface\ieee_9_bus_data\component_data_heuristics.txt", "G:\saqib\open DSS\OpenDSS_Python_Interface\ieee_9_bus_data\Load_data_with_reactive_load.txt", 0, 1, 40, 'wscc9bus_system_test_N-1.xml', 2, "G:\saqib\open DSS\OpenDSS_Python_Interface\ieee_9_bus_data\\transmissionlines_PA_names.txt");
greedy_hueristics("'G:\saqib\open DSS\OpenDSS_Python_Interface\ieee_14_bus_data\ieee14bus_system_with_txr.dss'", "G:\saqib\open DSS\OpenDSS_Python_Interface\ieee_14_bus_data\component_data.txt", "G:\saqib\open DSS\OpenDSS_Python_Interface\Load_data_with_reactive_power.txt", 0, 1, 40, 'ieee14bus_system_N-1.xml', 3, "G:\saqib\open DSS\OpenDSS_Python_Interface\ieee_14_bus_data\\transmissionlines_PA_names.txt");
#greedy_hueristics("'G:\saqib\open DSS\OpenDSS_Python_Interface\ieee39bus_system\ieee39bus_system_with_1kv_base.dss'", "G:\saqib\open DSS\OpenDSS_Python_Interface\ieee39bus_system\component_data.txt", "G:\saqib\open DSS\OpenDSS_Python_Interface\ieee39bus_system\Load_data1.txt", 0, 1, 40, 'ieee39bus_system_test_N-3.xml', 2);
#greedy_hueristics("'G:\saqib\open DSS\OpenDSS_Python_Interface\ieee_57_bus_system\ieee57bussystem1.dss'", "G:\saqib\open DSS\OpenDSS_Python_Interface\ieee_57_bus_system\component_data.txt", "G:\saqib\open DSS\OpenDSS_Python_Interface\ieee_57_bus_system\Load_data.txt", 0, 1, 40, 'ieee57bus_system_N-1.xml', 4);    
