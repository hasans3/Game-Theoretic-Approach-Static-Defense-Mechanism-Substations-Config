## Game-Theoretic-Approach-Static-Defense-Mechanism

This folder contains the respective methods and supporting files needed for identifying static defense strategies with substation configuration.

## Background: 
Static attacks are those attacks that takes place simultaneously. Here, we consider a power system model representing a cyber-physical
energy system. This system consists of both physical and cyber components. Physical components represent transmission lines, loads, generators, transformers, buses, etc. However, cyber components represents the protection assemblies such as distance relay, over-current relay and circuit breakers. A power system consists of a large number of substations. Each substation consists of several protection assemblies. These protection assemblies can be remotely monitored and controlled using the remote terminal units located in every substations. If an attacker gain access to a substation then he can manipulate these protection assemblies to disconnect transmission lines from the power system network and cause system damage. However, considering the scale of the power system network it is impossible to exhaustively identify the substations and protection assemblies to attack in order to maximize system damage. Similarly, with a limited defense budget, it is impossible to protect all the necessary substations of the power system network. Hence, we use our game-theoretic approach to model this as an optimization problem and use our "static_defense_substations_v1_test.py" method to obtain an efficient and resonable solution that provides the details on which substations to protect that will minimize the system damage when the system is under attack. 

Note: For more details about the problem, system model, etc., please refer to the paper titled "Vulnerability Analysis of Power Systems Based on Cyber-Attack and Defense Models". 
The document will be available on Vanderbilt Universities, Institute for software integrated systems under "Publications".

## How to run the main method `static_defense_substations_v1_test.py`?
  
To run the attack method, the following steps are needed:
1. `Install the OpenDSS` from  [Download Link](https://sourceforge.net/projects/electricdss/#Link) on the Windows machine as OpenDSS is not mac compatible.
2. `Download and save` the system models from the "System Models" folder to the local drive. 
3. `Install` Python 2.7.
4. `Install` Spyder, PyCharm or any other Python IDE.
5. `Install` all the necessary inbuilt python packages using `pip install package name`. Example `pip install numpy`.
6. `Open` the `static_defense_substations_v1_test.py` method and set the paths for the `filepath, comp_filename, load_file_name` as per the 
directory where the downloaded files are stored from the "System Models" folder. 

`filepath` is the path where `.dss` file is stored on the local drive.

`comp_filename` is the local drive path where `component_data_subs.txt` file is stored.

`load_file_name` is the path for the `load_data.txt` file stored on the local drive. For certain models the file name can be `load_data1.txt` or `load_data_testing1.txt`, etc.

7. Run `static_defense_substations_v1_test.py`.

## Supporting Methods 
1. `static_attack_subs_v2.py`
2. `static_defense_substations_v1_support.py`
3. `maptest_testing_defense_substations1_v1_support.py`
4. `trimmed_list_defense_substations1_v1_support.py`
5. `maptest_testing.py`
6. `trimmed_list.py`
7. `static_defense_substations1_v1_support.py`
8. `post_defense_static_attack_subs.py`

Each of these method have their own supporting methods that are not listed here.

## Dependencies
more-itertools 

pywin32

pypiwin32

numpy

To install dependencies: `pip install <dependencyname>`; ex: `pip install numpy`.
