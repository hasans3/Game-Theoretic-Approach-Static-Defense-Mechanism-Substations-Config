# -*- coding: utf-8 -*-
"""
Created on Wed Jun 21 16:12:11 2017

@author: saqibhasan

This code provides the defense mechanism for the worst case static attack and this is the updated version of the implementation so far. THis can be named as version1, any updates on this code can be 
named as version1.x
"""

def static_defense_subs(filepath, comp_filename, load_file_name, start_range, contingency_range, blackout_criterion, system_name, p_budget, s_budget, d_budget):

    # Importing the supporting methods 
    import time
    import static_attack_subs_v2
    import static_defense_substations_v1_support
    import maptest_testing_defense_substations1_v1_support
    import trimmed_list_defense_substations1_v1_support
    import maptest_testing
    import trimmed_list
    import static_defense_substations1_v1_support
    import post_defense_static_attack_subs
    
    # Method variables initialization
    tot_exe_time_start = time.time()
    temp_sub_protected = [];
    sub_protected = [];
    sub_protected1 = [];
    temp_max_loadloss = 100;
    prev_post_defese_loadloss = 100;
    
    # Identifying the worst case static attack and storing the details
    temp_worst_case_outage, temp_worst_case_loadloss, temp_worst_case_sub = static_attack_subs_v2.greedy_hueristics(filepath, comp_filename, load_file_name, start_range, contingency_range, blackout_criterion, system_name, p_budget, s_budget);
    pre_defense_worst_case_outage = temp_worst_case_outage;
    pre_defense_worst_case_loadloss = temp_worst_case_loadloss;
    pre_defense_worst_case_subs = temp_worst_case_sub;
    
    # Running the loop until the defense budget expires
    for i in range(0, d_budget):
        temp_max_loadloss = 100;
        flag = 0
        # This check runns the if substations are protected to identify the new static attack
        if (len(sub_protected) != 0):
            temp_worst_case_sub, prev_post_defese_loadloss = static_defense_substations1_v1_support.greedy_hueristics(filepath, comp_filename, load_file_name, start_range, contingency_range, blackout_criterion, system_name, p_budget, s_budget, sub_protected);
            temp_worst_case_sub = temp_worst_case_sub;
        # Removes each substation and its components from the attackable set and obtain the system damage
        for item in range(0, len(temp_worst_case_sub)):
            temp_worst_case_outage, temp_worst_case_loadloss, temp_worst_case_substation = static_defense_substations_v1_support.greedy_hueristics(filepath, comp_filename, load_file_name, start_range, contingency_range, blackout_criterion, system_name, p_budget, s_budget, tuple([temp_worst_case_sub[item]]), sub_protected);
            # Updates the solution for the substation that minimizes the damage if protected
            if (temp_worst_case_loadloss < temp_max_loadloss):
                temp_max_loadloss = temp_worst_case_loadloss
#                prev_post_defese_loadloss = temp_worst_case_loadloss
                temp_sub_protected = temp_worst_case_sub[item];
                flag = 1
        sub_protected.append(temp_sub_protected); 
        sub_protected1.append(temp_sub_protected);
        # Keeps a temporary solution in order to obtain an optimal solution
        if (temp_max_loadloss > prev_post_defese_loadloss and flag == 1):
            sub_protected1.remove(temp_sub_protected);
        else:
            sub_protected1 = []
            for item in sub_protected:
                sub_protected1.append(item)
#        post_defense_worst_case_outage, post_defense_worst_case_sub, post_defense_worst_case_loadloss = post_defense_static_attack_subs.greedy_hueristics(filepath, comp_filename, load_file_name, start_range, contingency_range, blackout_criterion, system_name, p_budget, s_budget, sub_protected);
#        if post_defense_worst_case_loadloss > prev_post_defese_loadloss: 
#            sub_protected1.remove(temp_sub_protected);
#        else:
#            sub_protected1 = []
#            for item in sub_protected:
#                sub_protected1.append(item)
#    print sub_protected1
#    print sub_protected
#        prev_post_defese_loadloss = post_defense_worst_case_loadloss
#        print sub_protected 

    # Obtain the worst case static attack after protecting the substations based on the defense budget
    post_defense_worst_case_outage, post_defense_worst_case_sub, post_defense_worst_case_loadloss = post_defense_static_attack_subs.greedy_hueristics(filepath, comp_filename, load_file_name, start_range, contingency_range, blackout_criterion, system_name, p_budget, s_budget, sub_protected1);
    tot_exe_time_end = time.time()
    tot_exe_time = (tot_exe_time_end - tot_exe_time_start)    
    
    # Outputs the details on the console
    print '**************************************************************************************************************************'
    print 'Pre defense worst case static-attack outages: %s' %pre_defense_worst_case_outage
    print 'Pre defense worst case static-attack on substations: {0}'.format(pre_defense_worst_case_subs)
    print 'Pre defense worst case static-attack load loss: %f' %pre_defense_worst_case_loadloss
    print 'Substations to be proteceted: %s' %sub_protected1
    print 'Post defense worst case static-attack outages: %s' %post_defense_worst_case_outage
    print 'Post defense worst case static-attack on substations: {0}'.format(post_defense_worst_case_sub)
    print 'Post defense worst case static-attack load loss: %f' %post_defense_worst_case_loadloss
    print 'Post defense percentage reduction in load loss: {0}%'.format(((pre_defense_worst_case_loadloss - post_defense_worst_case_loadloss)/pre_defense_worst_case_loadloss)*100)
    print 'Total execution time in seconds: %s' %tot_exe_time
    print '**************************************************************************************************************************'

# Method call with different system models
static_defense_subs("'G:\saqib\open DSS\OpenDSS_Python_Interface\ieee_14_bus_data\ieee14bus_system_with_txr.dss'", "G:\saqib\open DSS\OpenDSS_Python_Interface\ieee_14_bus_data\component_data_subs.txt", "G:\saqib\open DSS\OpenDSS_Python_Interface\Load_data_with_reactive_power.txt", 0, 1, 40, 'ieee14bus_system_N-1.xml', 3, 3, 5);
#static_defense_subs("'G:\saqib\open DSS\OpenDSS_Python_Interface\ieee39bus_system\ieee39bus_system_with_1kv_base.dss'", "G:\saqib\open DSS\OpenDSS_Python_Interface\ieee39bus_system\component_data_subs.txt", "G:\saqib\open DSS\OpenDSS_Python_Interface\ieee39bus_system\Load_data1.txt", 0, 1, 40, 'ieee39bus_system_test_N-3.xml', 2, 2, 14);
#static_defense_subs("'G:\saqib\open DSS\OpenDSS_Python_Interface\ieee_57_bus_system\ieee57bussystem1.dss'", "G:\saqib\open DSS\OpenDSS_Python_Interface\ieee_57_bus_system\component_data_subs.txt", "G:\saqib\open DSS\OpenDSS_Python_Interface\ieee_57_bus_system\Load_data.txt", 0, 1, 40, 'ieee57bus_system_N-1.xml', 2, 2, 4);    
