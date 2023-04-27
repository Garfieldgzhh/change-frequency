# Change Frequency Detector

## Overview
The script "change_frequency" is used to extract the change frequencies of modules in the Neuron projects.

## Environment
The script is tested on Ubuntu with Python 3.8.10

## Execution
Step 1: clone the Neuron project: 

```
git clone https://github.com/openstack/neutron.git
```

Step 2:
Place the change_frequency under the Neuron project root directory

Step 3:
run the command from the project root directory 
```
python3 change_frequency.py
```

The output should look like this:

```
The five most actively changed modules are:
module, commits
tests, 1811
plugins, 808
agent, 550
db, 390
services, 266
```
