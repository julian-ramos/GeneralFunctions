import time
import numpy as np
import os
import winsound


def experimentVariables(projectName):
    '''
    This function returns all the variables necessary to start a experiment including:
    name of the experiment
    datasets locations
    variables to report from the experiment
    what to report from the experiment
    '''
    computerName=os.environ.get('COMPUTERNAME')
    if projectName== 'unlabeledModelS':
        if computerName=='JULIAN':
            from sklearn.datasets import  load_boston, load_iris, load_diabetes, load_digits, load_linnerud
            
            datasets={'boston':load_boston(),'iris':load_iris(),'diabetes':load_diabetes(),'digits':load_digits(),'linnerud':load_linnerud()}
            print('working at JULIAN@CMU')
            dataset='digits'
            numTests=20
            experimentName='One'
            agmntlvl=0
            description='here the description of this experiment'
            data=datasets[dataset]['data']
            labels=datasets[dataset]['target']
            verbose=0
            
            #The next are variables that store the outcomes from the
            #experiment
            variables=\
            'spear=[]\n'

            return {'dataset':dataset,'numTests':numTests,'experimentName':experimentName,\
                    'description':description,'agmntlvl':agmntlvl,'variables':variables,'data':data,'labels':labels,'verbose':verbose}
        else:
            print('Variables not defined for Julian@Laptop')
    


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
            main_path='G:/Activity_RS/Dataset'
            data_path='G:/Activity_RS/Dataset'
            results_path='G:/Activity_RS/Results'
            print 'Moved to the data path '+data_path
            os.chdir(data_path);
        return {'main_path':main_path,'data_path':data_path,'results_path':results_path}
    
    
    if projectName == 'Discovering_APPC':
        if A=='JULIAN':
            print 'working on JULIAN@CMU'
            print 'This paths have not being defined yet'
            main_path='F:/Activity_RS/Dataset'
            data_path='F:/Activity_RS/Dataset'
            results_path='F:/Activity_RS/Results'
            print 'Moved to the data path '+data_path
            os.chdir(data_path);
        else :
            print 'working on Julian@laptop'
            main_path='E:/research_data_sets/neill/upmc'
            data_path='E:/research_data_sets/neill/upmc/DeIDOutput/copd_pat_10'
            results_path='E:/research_data_sets/neill/upmc/unifiedFiles/'
            print 'Moved to the data path '+data_path
            os.chdir(data_path);
        return {'main_path':main_path,'data_path':data_path,'results_path':results_path}
            
            
    if projectName == 'EigenRoutines':
        if A=='JULIAN':
            print 'working on JULIAN@CMU'
            main_path='K:/research_data_sets/kettle/problematic_use_data/problematic_use_data'
            data_path='K:/research_data_sets/kettle/problematic_use_data/problematic_use_data/ScreenOff-DataSet'
            results_path='K:/research_data_sets/kettle/problematic_use_data/problematic_use_data/Results'
            transitions_path='K:/research_data_sets/kettle/problematic_use_data/problematic_use_data/transitionsData'
            os.chdir(data_path);
        else :
            print 'working on Julian@laptop'
            main_path='E:/research_data_sets/kettle/problematic_use_data/problematic_use_data'
            data_path='E:/research_data_sets/kettle/problematic_use_data/problematic_use_data/ScreenOff-DataSet'
            results_path='E:/research_data_sets/kettle/problematic_use_data/problematic_use_data/Results'
            transitions_path='E:/research_data_sets/kettle/problematic_use_data/problematic_use_data/transitionsData'
            os.chdir(data_path);
        return {'main_path':main_path,'data_path':data_path,'results_path':results_path,'transitions_path':transitions_path}
    
    if projectName == 'topicModels':
        if A=='JULIAN':
            print 'working on JULIAN@CMU'
            main_path='K:/research_folders/topicModels/'
            data_path='--not provided yet--'
            results_path='K:/research_folders/topicModels/results/'
            corpus_path='K:/research_folders/topicModels/corpus/'
#             os.chdir(data_path);
        else :
            print 'working on Julian@laptop'
            main_path='E:/research_data_sets/kettle/problematic_use_data/problematic_use_data'
            data_path='E:/research_data_sets/kettle/problematic_use_data/problematic_use_data/ScreenOff-DataSet'
            results_path='E:/research_data_sets/kettle/problematic_use_data/problematic_use_data/Results'
            transitions_path='E:/research_data_sets/kettle/problematic_use_data/problematic_use_data/transitionsData'
#             os.chdir(data_path);
        return {'main_path':main_path,'data_path':data_path,'results_path':results_path,'corpus_path':corpus_path}
    
    if projectName== 'unlabelebeledModelS':
        if A=='JULIAN':
            print('working at JULIAN@CMU')
            
        else:
            print('Variables not defined for Julian@Laptop') 
    
    
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

## Miscellaneous functions
def tic(vars=0):
    '''
    This function works similarly to tic in matlab. When called tic(0) internally stores the current time
    when called as tic(1) returns the time elapsed between the last tic(0) and tic(1)
    Calling tic(0) always overwrites the starting time
    '''
    if vars==1:
        t=time.time()-tic.start
    else:
        tic.start=time.time()
        t=tic.start
    return t 
        
    
    import winsound

def beep():
    Freq = 3000 # Set Frequency To 2500 Hertz
    Dur = 1000 # Set Duration To 1000 ms == 1 second
    winsound.Beep(Freq,Dur)
    
    