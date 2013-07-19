import numpy as np
import os


def projectPaths(projectName):
    '''
    This function returns the paths necesary to work on several
    projects. The paths change according to the machine this function
    is called from.
    '''
    A=os.environ.get('COMPUTERNAME')
    if projectName == 'problematic_use':
        if A=='JULIAN':
            print 'working on JULIAN@CMU'
            main_path='K:/research_data_sets/kettle/problematic_use_data/problematic_use_data'
            data_path='K:/research_data_sets/kettle/problematic_use_data/problematic_use_data/SOFDataSet'
            results_path='K:/research_data_sets/kettle/problematic_use_data/problematic_use_data/Results'
            transitions_path='K:/research_data_sets/kettle/problematic_use_data/problematic_use_data/transitionsData'
            os.chdir(data_path);
        else :
            print 'working on Julian@laptop'
            main_path='E:/research_data_sets/kettle/problematic_use_data/problematic_use_data'
            data_path='E:/research_data_sets/kettle/problematic_use_data/problematic_use_data/SOFDataSet'
            results_path='E:/research_data_sets/kettle/problematic_use_data/problematic_use_data/Results'
            transitions_path='E:/research_data_sets/kettle/problematic_use_data/problematic_use_data/transitionsData'
            os.chdir(data_path);
        return {'main_path':main_path,'data_path':data_path,'results_path':results_path,'transitions_path':transitions_path}
            
    if projectName == 'Activity_RS':
        if A=='JULIAN':
            print 'working on JULIAN@CMU'
            main_path='F:/Activity_RS/Dataset'
            data_path='F:/Activity_RS/Dataset'
            results_path='F:/Activity_RS/Results'
            print 'Moved to the data path '+data_path
            os.chdir(data_path);
        else :
            print 'working on Julian@laptop'
            print 'This paths have not being defined yet'
            main_path='F:Activity_RS/Dataset'
            data_path='F:Activity_RS/Dataset'
            results_path='F:Activity_RS/Results'
            print 'Moved to the data path '+data_path
            os.chdir(data_path);
        return {'main_path':main_path,'data_path':data_path,'results_path':results_path}
            
    
    
def transitionsExtractor(data,timeData):
    last=data[0]
    dataOut=[]
    timeOut=[]
    dataOut.append(data[0])
    timeOut.append(timeData[0])
    for i in range(len(data)):
        if last!=data[i]:
            dataOut.append(data[i])
            timeOut.append(timeData[i])
            last=data[i]
    return {'dataOut':dataOut,'timeOut':timeOut}
        
    
    
