import os
import subprocess
import datetime


def getStartDate():
    today = datetime.datetime.now()
    # definition of 3 years:
    # 1. same month and day 3 years ago, problematic if today is 29th Feb.
    # 2. 3 * 365 days ago
    # definition 2 is used.
    startDate = today - datetime.timedelta(days=3*365)
    return startDate


def getNumCommit(module):
    date = getStartDate()
    command = "git log  --oneline --after={y}-{m}-{d} {module}".format(y=date.year, m=date.month, d=date.day, module=module)
    process = subprocess.run(command.split(), capture_output=True, text=True)
    commits = process.stdout.splitlines()
    return len(commits)


def getModules():
    command = "ls -d -w1 */"
    process = subprocess.run(command, capture_output=True, text=True, shell=True)
    modules = process.stdout.splitlines()

    # remove '/' at the end of module names
    for i in range(len(modules)):
        modules[i] = modules[i][:-1]

    return modules


def getNumCommitsForModules():
    modules = getModules()
    moduleCommitMap = []
    for module in modules:
        moduleCommitMap.append((module, getNumCommit(module)))
    moduleCommitMap.sort(key=lambda x: x[1], reverse=True)
    return moduleCommitMap

def main():
    os.chdir("./neutron")
    moduleCommitMap = getNumCommitsForModules()
    numModulesToPrint = min(5, len(moduleCommitMap))
    
    print("The five most actively changed modules are:")
    print("module, commits")
    for i in range(numModulesToPrint):
        module = moduleCommitMap[i][0]
        numCommits = moduleCommitMap[i][1]
        print("{m}, {n}".format(m=module, n=numCommits))


main()
