# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 10:09:08 2024

@author: user
"""

# %% Libraries

import os 
import mne
import pandas as pd
import numpy as np
import mne
%matplotlib qt
import matplotlib.pyplot as plt
import mne_connectivity
import random


path_on_the_computer = '' #!!! To write your path

# %% STEP 0 

# #!!! Manual input
# subject                  = '1400'
# table_with_bad_channels  = pd.read_excel('C:/Users/user/Desktop/bad_channels.xlsx')
# bad_channel_list         = ["EEG R'4", "EEG R'6", "EEG R'10", "EEG CR'8", "EEG CR'2", "EEG PM'3", "EEG PM'6", "EEG PM'7", "MKR1+", "EEG HC4", "EEG HC5", "EEG HC6", "EEG PM'8", "EEG PM'9"]

# annot_from_file_name     = '{}/{}_1.csv'.format(subject,subject)

# ###############################################################################
# def prepare_data(subject):
    
#     # DOWNLOADER
#     os.chdir('K:/EXP_DATA/iEEG_data')    
#     file     = 'K:/EXP_DATA/iEEG_data/' + subject + '/' + subject + '.edf'
#     folder   = 'K:/EXP_DATA/iEEG_data/' + subject 

#     os.chdir(folder)
#     stimulus_f                       = 'K:/EXP_DATA/iEEG_data/' + subject + '/' + subject + '_psychopy.csv'
#     stimulus_file                    = pd.read_csv(stimulus_f)
#     len(stimulus_file          )
#     len(stimulus_file[:-1])
#     stimulus_file                    = stimulus_file[:-1]

#     # LABELLING 
#     os.chdir('K:/EXP_DATA/iEEG_data')
#     from Step_0_Peak_finder_2 import find_events_eeg, label_define
#     table_with_time, raw_data        = find_events_eeg(file)
#     events                           = label_define(stimulus_file, table_with_time)

#     annot_from_file                  = mne.read_annotations(annot_from_file_name)
#     raw_data.set_annotations(annot_from_file)
#     raw_data.plot(events=events, scalings=dict(eeg=216.695e-6), duration=20)
#     raw_data.load_data()
#     raw_new                          = raw_data
        
#     return raw_new, events

# # ###############################################################################
# raw_new, events = prepare_data(subject)

# 
# # Channel dropping #!!! This part is individual, thus is should be out of a function
# # raw_new.info['bads']                = bad_channel_list
# info                                = raw_new.info
# chan_list                           = info['ch_names']
# print(chan_list)

# #!!! Based on doctors localization and Fieldtrip localization
# chan_list_to_drop                   = [
#                                        'EEG NA7', 'EEG NA8', 'EEG NA9', 'EEG NA10', 
                                     
#                                        'EEG HT7', 'EEG HT8', 'EEG HT9', 'EEG HT10', 
                                     
#                                        'EEG HC7', 'EEG HC8', 'EEG HC9', 'EEG HC10', 'EEG HC11', 'EEG HC12', 
#                                        'EEG GC1', 'EEG GC2', 'EEG GC3', 'EEG GC4', 'EEG GC5', 'EEG GC6', 
#                                        'EEG GC7', 'EEG GC8', 'EEG GC9', 'EEG GC10', 'EEG GC11', 'EEG GC12', 
#                                        'EEG PA1', 'EEG PA2', 'EEG PA3', 'EEG PA4', 'EEG PA5', 'EEG PA6', 
#                                        'EEG PA7', 'EEG PA8', 'EEG PA9', 'EEG PA10', 'EEG PA11', 'EEG PA12',
#                                        'EEG H1', 'EEG H2', 'EEG H3', 'EEG H4', 'EEG H5', 'EEG H6', 
#                                        'EEG H7', 'EEG H8', 'MKR1+', 
                                      
#                                        'EEG OP7', 'EEG OP8', 
                                     
#                                        'EEG OC7', 'EEG OC8', 
#                                        'EEG OF7', 'EEG OF8', 'EEG OF9', 'EEG OF10', 'EEG OF11', 'EEG OF12', 
                                      
#                                        "EEG HC'7", "EEG HC'8", "EEG HC'9", "EEG HC'10", 
#                                        "EEG OP'1", "EEG OP'2", "EEG OP'3", "EEG OP'4", "EEG OP'5", "EEG OP'6",
#                                        "EEG OP'7", "EEG OP'8",
                                   
#                                        "EEG OC'7", "EEG OC'8", 'thor+']


# raw_new.drop_channels(chan_list_to_drop, on_missing='raise')

# raw_new.plot(events=events, scalings=dict(eeg=216.695e-6), duration=20)

# ###############################################################################
# def create_bipolar(raw_new):
#     for i in range(len(raw_new.info['ch_names'])-2):
#         raw_new = mne.set_bipolar_reference(raw_new, anode = raw_new.info['ch_names'][i],  
#                                                      cathode = raw_new.info['ch_names'][i+1], 
#                                                      drop_refs=False)
#     return raw_new

# ###############################################################################  
# raw_new  = create_bipolar(raw_new)

# # Delete unipolar channels
# raw_new.info['ch_names']
# raw_new.info['ch_names'][47]
# ch_names = raw_new.info['ch_names'][:48] #!!! this will change
# raw_new.drop_channels(ch_names, on_missing='raise')

# # Visual data inspection
# raw_new.plot(events=events, scalings=dict(eeg=166.695e-6), duration=20)
# raw_new.annotations.save("{}_updated.csv".format(subject), overwrite=True)

# ###############################################################################  #??? should it be here or in the beginning
# def ch_name_shortening(raw_new): #MNE has issues to save names longer than 16 symbols
#     old    = raw_new.info['ch_names']
#     lising = old.copy()
    
#     for idx, ele in enumerate(lising):
#         lising[idx] = ele.replace('EEG', '')
#     for idx, ele in enumerate(lising):
#         lising[idx] = ele.replace(' ', '')
        
#     a              = old
#     b              = lising
#     mapname        = {}
#     for A, B in zip(a, b):
#         mapname[A] = B
#     print(mapname)
#     mne.rename_channels(raw_new.info, mapname, allow_duplicates=False, verbose=None)

#     return raw_new

# ###############################################################################  
# raw_new = ch_name_shortening(raw_new)
# raw_new.export('{}_upd2.edf'.format(subject), verbose=None, overwrite=True)

# %% STEP 1 - EPOCHING - start here (for all subjects except 18 and 20)

# This code works for all subjects, except 18 and 20.
# The code for subjects 18 and 20 is below in the next section. 

subject = '20'                    #[1,4,5,6,7,8,10,11,12,14,16,17,21,22,23,24,25,26]

#### DOWNLOADER ###############################################################
os.chdir(path_on_the_computer)
raw_new                         = mne.io.read_raw_edf('{}_upd2.edf'.format(subject))
annot_from_file                 = mne.read_annotations("{}_updated.csv".format(subject))

###############################################################################
# The function to upload file, find events based on MKR2+, upload annotations and set them the raw data
def prepare_data(subject): 
    
    # DOWNLOADER
    os.chdir(path_on_the_computer)    
    file     = path_on_the_computer + subject + '_upd2.edf'
    folder   = path_on_the_computer

    os.chdir(folder)
    stimulus_f                       = path_on_the_computer +  subject + '_psychopy.csv'
    stimulus_file                    = pd.read_csv(stimulus_f)
    len(stimulus_file          )
    len(stimulus_file[:-1])
    stimulus_file                    = stimulus_file[:-1]

    # LABELLING 
    os.chdir(path_on_the_computer)
    from Step_0_Peak_finder_2 import find_events_eeg, label_define
    table_with_time, raw_data        = find_events_eeg(file)
    events                           = label_define(stimulus_file, table_with_time)

    # annot_from_file                  = mne.read_annotations(annot_from_file_name)
    raw_data.set_annotations(annot_from_file)
    # raw_data.plot(events=events, scalings=dict(eeg=216.695e-6), duration=20)
    raw_data.load_data()
    raw_new                          = raw_data
        
    return raw_new, events


###############################################################################
################## FOR PLV ####################################################

# Dictionary with channels, which we take into consideration

eeg_channels1 = {'Left Amygdala'      : [],
                'Left Orbitofrontal' : ["OR'4-OR'5", "OR'5-OR'6", "OR'6-OR'7", "OR'7-OR'8", "OR'8-OR'9", "FP'1-FP'2", "FP'2-FP'3"],
                'Left Hippocampus'   : ["NA'1-NA'2", "NA'2-NA'3",  "NA'3-NA'4", "NA'4-NA'5", "HC'2-HC'3", "HC'3-HC'4", "HC'4-HC'5","HC'5-HC'6"],
                'Left Insula'        : [],
                'Right Amygdala'     : [],
                'Right Orbitofrontal': [],
                'Right Hippocampus'  : ['HC1-HC2', 'HC2-HC3'],
                'Right Insula'       : []   
                    }

eeg_channels4 = {'Left Amygdala'     : [],
                'Left Orbitofrontal' : [],
                'Left Hippocampus'   : [],
                'Left Insula'        : [],
                'Right Amygdala'     : [],
                'Right Orbitofrontal': [],
                'Right Hippocampus'  : ['HC2-HC3', 'HT1-HT2', 'HC3-HC4', 'HT2-HT3','HC4-HC5', 'HT5-HT6'],
                'Right Insula'       : ['OF1-OF2','OF2-OF3','OF3-OF4']   
                    }


eeg_channels5 = {'Left Amygdala'     : ["NA'1-NA'2", "NA'2-NA'3", "NA'3-NA'4"],
                'Left Orbitofrontal' : [ "R'2-R'3", "R'3-R'4", "R'4-R'5", "R'5-R'6", "R'6-R'7", "R'7-R'8", "R'8-R'9", "OR'1-OR'2", "OR'2-OR'3", "OR'3-OR'4","OR'4-OR'5", "OR'5-OR'6", "OR'6-OR'7", "OR'7-OR'8", "OR'8-OR'9", "OR'9-OR'10"],
                'Left Hippocampus'   : ["HT'1-HT'2", "HT'2-HT'3", "HT'3-HT'4"],
                'Left Insula'        : [],
                'Right Amygdala'     : [],
                'Right Orbitofrontal': ['OR1-OR2', 'OR2-OR3'],
                'Right Hippocampus'  : ['HC1-HC2', 'HC2-HC3', 'HC3-HC4', 'HC4-HC5'],
                'Right Insula'       : []   
                    }

eeg_channels6 = {'Left Amygdala'     : ["NA'1-NA'2", "NA'2-NA'3", "NA'3-NA'4", "NA'4-NA'5"],
                'Left Orbitofrontal' : ["R'1-R'2", "R'2-R'3", "R'3-R'4", "R'4-R'5", "R'5-R'6", "FP'1-FP'2", "FP'2-FP'3", "FP'3-FP'4", "FP'4-FP'5"],
                'Left Hippocampus'   : ["HP'1-HP'2", "HP'2-HP'3", "HP'3-HP'4",  "HP'4-HP'5",  "HP'5-HP'6",  "HP'6-HP'7",  "HP'7-HP'8"],
                'Left Insula'        : [],
                'Right Amygdala'     : [],
                'Right Orbitofrontal': [],
                'Right Hippocampus'  : ['HC1-HC2',  'HC2-HC3',  'HC3-HC4'],
                'Right Insula'       : []   
                    }

eeg_channels7 = {'Left Amygdala'     : [],
                'Left Orbitofrontal' : [],
                'Left Hippocampus'   : [],
                'Left Insula'        : ["T'2-T'3", "H'1-H'2", "H'2-H'3"],
                'Right Amygdala'     : [],
                'Right Orbitofrontal': [],
                'Right Hippocampus'  : [],
                'Right Insula'       : ['TT2-TT3', 'TT3-TT4', 'H2-H3', 'H3-H4']   
                    }

eeg_channels8 = {'Left Amygdala'     : [],
                'Left Orbitofrontal' : [],
                'Left Hippocampus'   : ["HT'1-HT'2","HT'4-HT'5"],
                'Left Insula'        : [ "OP'2-OP'3"],
                'Right Amygdala'     : [],
                'Right Orbitofrontal': [],
                'Right Hippocampus'  : ['HT4-HT5'],
                'Right Insula'       : ['H2-H3', 'H3-H4', 'OP1-OP2', 'OP2-OP3']   
                    }

eeg_channels10 = {'Left Amygdala'    : [],
                'Left Orbitofrontal' : ["OR'2-OR'3","OR'7-OR'8"],
                'Left Hippocampus'   : ["HC'1-HC'2", "HC'2-HC'3", "HC'3-HC'4",  "HC'4-HC'5"],
                'Left Insula'        : [],
                'Right Amygdala'     : [],
                'Right Orbitofrontal': ['R1-R2', 'R2-R3', 'R3-R4', 'R4-R5', 'R5-R6', 'R6-R7',  'R7-R8',  'R8-R9'],
                'Right Hippocampus'  : ['HC1-HC2', 'HC2-HC3', 'HC3-HC4', 'HC4-HC5'],
                'Right Insula'       : []   
                    }

eeg_channels11= {'Left Amygdala'     : [],
                'Left Orbitofrontal' : [],
                'Left Hippocampus'   : ["HC'1-HC'2", "HC'2-HC'3", "HC'3-HC'4", "HC'4-HC'5", "HC'5-HC'6"],
                'Left Insula'        : [],
                'Right Amygdala'     : ['NA1-NA2', 'NA2-NA3', 'NA3-NA4'],
                'Right Orbitofrontal': [],
                'Right Hippocampus'  : ['HT1-HT2',    'HT2-HT3',    'HT3-HT4',    'HT4-HT5', 'HP3-HP4', 'HP4-HP5', 'HP5-HP6'],
                'Right Insula'       : []   
                    }


eeg_channels12 = {'Left Amygdala'     : [],
                'Left Orbitofrontal' : ["OF'1-OF'2"],
                'Left Hippocampus'   : ["HC'3-HC'4"],
                'Left Insula'        : [],
                'Right Amygdala'     : [],
                'Right Orbitofrontal': [],
                'Right Hippocampus'  : [],
                'Right Insula'       : []   
                    }


eeg_channels14= {'Left Amygdala'     : ["NA'1-NA'2", "NA'2-NA'3", "NA'3-NA'4"],
                'Left Orbitofrontal' : [ "R'1-R'2", "R'2-R'3", "R'4-R'5", "R'5-R'6", "R'8-R'9", "R'9-R'10", "OR'1-OR'2", "OR'4-OR'5", "OR'5-OR'6", "OR'6-OR'7", "OR'7-OR'8"],
                'Left Hippocampus'   : [],
                'Left Insula'        : ["T'3-T'4","NA'5-NA'6"],
                'Right Amygdala'     : [],
                'Right Orbitofrontal': [],
                'Right Hippocampus'  : [],
                'Right Insula'       : []   
                    }

eeg_channels16= {'Left Amygdala'     : ["NA'2-NA'3","NA'3-NA'4","NA'4-NA'5"],
                'Left Orbitofrontal' : [],
                'Left Hippocampus'   : ["NA'1-NA'2", "HC'3-HC'4"],
                'Left Insula'        : [],
                'Right Amygdala'     : ['NA4-NA5'],
                'Right Orbitofrontal': [],
                'Right Hippocampus'  : ['NA1-NA2', 'NA2-NA3','NA3-NA4', 'HC1-HC2','HC2-HC3', 'HC3-HC4', 'HT1-HT2','HT2-HT3'],
                'Right Insula'       : ['OP2-OP3', 'OP3-OP4', 'OF1-OF2']   
                    }


eeg_channels17= {'Left Amygdala'     : [],
                'Left Orbitofrontal' : [],
                'Left Hippocampus'   : [ "HT'1-HT'2","HT'2-HT'3"],
                'Left Insula'        : [],
                'Right Amygdala'     : [],
                'Right Orbitofrontal': [],
                'Right Hippocampus'  : ['HT2-HT3'],
                'Right Insula'       : []   
                    }


eeg_channels18= {'Left Amygdala'     : [ "NA'2-NA'3", "NA'3-NA'4",],
                'Left Orbitofrontal' : [],
                'Left Hippocampus'   : [ "HC'3-HC'4"],
                'Left Insula'        : [],
                'Right Amygdala'     : [ 'NA3-NA4'],
                'Right Orbitofrontal': [],
                'Right Hippocampus'  : ['NA1-NA2', 'NA2-NA3', 'HT2-HT3','HT3-HT4', 'HT4-HT5'],
                'Right Insula'       : []   
                    }

eeg_channels20= {'Left Amygdala'     : [],
                'Left Orbitofrontal' : [],
                'Left Hippocampus'   : ["HC'1-HC'2",  "HC'2-HC'3", "HC'3-HC'4"],
                'Left Insula'        : ["T'2-T'3"],
                'Right Amygdala'     : [],
                'Right Orbitofrontal': [],
                'Right Hippocampus'  : ['HC1-HC2', 'HC2-HC3', 'HC3-HC4', 'HC4-HC5', 'HT1-HT2', 'HT2-HT3','HT3-HT4', 'HT4-HT5'],
                'Right Insula'       : ['OF1-OF2',  'H2-H3',  'O1-O2', 'O2-O3']   
                    }

eeg_channels21= {'Left Amygdala'     : [],
                'Left Orbitofrontal' : [],
                'Left Hippocampus'   : ["HT'1-HT'2","HT'2-HT'3","HT'3-HT'4","HT'4-HT'5"],
                'Left Insula'        : [],
                'Right Amygdala'     : [],
                'Right Orbitofrontal': [],
                'Right Hippocampus'  : ['HT1-HT2','HT2-HT3','HT3-HT4', 'HT4-HT5'],
                'Right Insula'       : []   
                    }


eeg_channels22= {'Left Amygdala'     : [],
                'Left Orbitofrontal' : [],
                'Left Hippocampus'   : [ "HT'1-HT'2", "HT'2-HT'3", "HT'3-HT'4","HT'4-HT'5"],
                'Left Insula'        : [],
                'Right Amygdala'     : [],
                'Right Orbitofrontal': ['OR2-OR3', 'OR3-OR4', 'OR4-OR5','OR5-OR6'],
                'Right Hippocampus'  : ['HT1-HT2'],
                'Right Insula'       : []   
                    }

eeg_channels23= {'Left Amygdala'     : [],
                'Left Orbitofrontal' : [],
                'Left Hippocampus'   : [],
                'Left Insula'        : [ "OF'1-OF'2", "OF'2-OF'3"],
                'Right Amygdala'     : [],
                'Right Orbitofrontal': ['OF1-OF2'],
                'Right Hippocampus'  : ["PFG'1-PFG'2"],
                'Right Insula'       : ['OF2-OF3','OF3-OF4','OF4-OF5','OF5-OF6','OC3-OC4']   
                    }

eeg_channels24= {'Left Amygdala'     : [],
                'Left Orbitofrontal' : [],
                'Left Hippocampus'   : [],
                'Left Insula'        : [],
                'Right Amygdala'     : [],
                'Right Orbitofrontal': ['OF3-OF4','OF5-OF6'],
                'Right Hippocampus'  : [],
                'Right Insula'       : [ 'CP3-CP4']   
                    }

eeg_channels25= {'Left Amygdala'     : [],
                'Left Orbitofrontal' : [],
                'Left Hippocampus'   : [],
                'Left Insula'        : [],
                'Right Amygdala'     : [],
                'Right Orbitofrontal': [],
                'Right Hippocampus'  : ['HT1-HT2'],
                'Right Insula'       : []   
                    }

eeg_channels26= {'Left Amygdala'     : [],
                'Left Orbitofrontal' : [],
                'Left Hippocampus'   : ["HC'2-HC'3","HC'3-HC'4"],
                'Left Insula'        : ["OC'2-OC'3"],
                'Right Amygdala'     : [],
                'Right Orbitofrontal': [],
                'Right Hippocampus'  : ['HT1-HT2'],
                'Right Insula'       : [ 'OC1-OC2','OC2-OC3','OC3-OC4','OF5-OF6','OP1-OP2','OP2-OP3','OP3-OP4', 'OP4-OP5',  'OP5-OP6']   
                    }

subject_ductionary = {
                        'sub1': eeg_channels1, 
                        'sub4': eeg_channels4, 
                        'sub5': eeg_channels5, 
                        'sub6': eeg_channels6, 
                        'sub7': eeg_channels7, 
                        'sub8': eeg_channels8, 
                        'sub10': eeg_channels10, 
                        'sub11': eeg_channels11, 
                        'sub12': eeg_channels12, 
                        'sub14': eeg_channels14, 
                        'sub16': eeg_channels16, 
                        'sub17': eeg_channels17, 
                        'sub18': eeg_channels18, 
                        'sub20': eeg_channels20, 
                        'sub21': eeg_channels21, 
                        'sub22': eeg_channels22, 
                        'sub23': eeg_channels23, 
                        'sub24': eeg_channels24, 
                        'sub25': eeg_channels25, 
                        'sub26': eeg_channels26 
                        }


###############################################################################
###############################################################################
###############################################################################

# This function takes all channels from the dictionary for particular subject and convert it to a string
# The string is later used to pick channels of interest only. 

def subj_analyzer(subject):
    what_dict_use = subject_ductionary['sub{}'.format(subject)]
    
    ch_names1 = what_dict_use['Left Amygdala']
    ch_names2 = what_dict_use['Left Orbitofrontal']
    ch_names3 = what_dict_use['Left Hippocampus']
    ch_names4 = what_dict_use['Left Insula']
    ch_names5 = what_dict_use['Right Amygdala']
    ch_names6 = what_dict_use['Right Orbitofrontal']
    ch_names7 = what_dict_use['Right Hippocampus']
    ch_names8 = what_dict_use['Right Insula']

    total_ch_names =  ch_names1 + ch_names2 + ch_names3 + ch_names4 + ch_names5 + ch_names6 + ch_names7 + ch_names8
    return total_ch_names

##############################################################################

raw_new, events = prepare_data(subject)
total_ch_names = subj_analyzer(subject)
raw_new.pick_channels(total_ch_names) 

#MKR2+ channel will be also droped. So, now we only navigate throught events object.

raw_new.plot(events=events, scalings=dict(eeg=216.695e-6), duration=20)


###############################################################################  
# This function creates epochs based on the found events. Epochs are created each 2 second interval. 
# Epochs are categorized based on condition and interval onset. 
# Thus, for each condition we have a list of 30 epochs, which consists of up to 6 repetitions (events) 

def epoching(raw_new, events):
    
    #### SEPERATE EPOCHS
    events_2              = events.astype(int)                             #events should be a NumPy array of integers, got <class 'numpy.ndarray'>
    
    condition             = [12,22,32,72] 
    step                  = [0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58]
    epochs                = [[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30],
                             [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30],
                             [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30],
                             [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]]
    
    #Loop for splitting the data for small bins
    for k in range(len(condition)):
        m                 = condition[k]
        
        for i in range(len(step)):
            j             = step[i]
            epochs[k][i]  = mne.Epochs(raw_new, events_2,  #raw_picked_data
                                       event_id=[m], 
                                       tmin=j, tmax=j+2, baseline=(j, j),
                                       reject_by_annotation=True,
                                       preload=True)
             
    # List of epochs
    epochs_watchpos       = epochs[0][:]
    epochs_suppress       = epochs[1][:]
    epochs_reassess       = epochs[2][:]
    epochs_watchneu       = epochs[3][:]
    
    # Epochs statistics
    i = 0
    wp = 0; wn = 0; r = 0; s = 0  
    for i in range(30):
        wp += len(epochs_watchpos[i].events)
        wn += len(epochs_watchneu[i].events)
        r  += len(epochs_reassess[i].events)
        s  += len(epochs_suppress[i].events)
        
    print('neu-watch',wn , '\npos-watch', wp, '\npos-reassess', r, '\npos-supress', s)    
    
    return epochs, epochs_watchpos, epochs_suppress, epochs_reassess, epochs_watchneu

###############################################################################  

epochs, epochs_watchpos, epochs_suppress, epochs_reassess, epochs_watchneu = epoching(raw_new, events)
epochs_list = [epochs_watchpos, epochs_suppress, epochs_reassess, epochs_watchneu ]



# %% STEP 1a - EPOCHING - start here (only for subjects 18 and 20)

# Subjects 18 and 19 have problems with initial number of triggers. 
# Thus I manually create for them events file and stored them in a particular place. 

subject = '20'                    # [18, 20]

#### DOWNLOADER ###############################################################
os.chdir(path_on_the_computer)
raw_new                         = mne.io.read_raw_edf('{}_upd2.edf'.format(subject))
annot_from_file                 = mne.read_annotations("{}_updated.csv".format(subject))

###############################################################################
################## FOR PLV ####################################################

# Dictionary with channels, which we take into consideration

eeg_channels1 = {'Left Amygdala'      : [],
                'Left Orbitofrontal' : ["OR'4-OR'5", "OR'5-OR'6", "OR'6-OR'7", "OR'7-OR'8", "OR'8-OR'9", "FP'1-FP'2", "FP'2-FP'3"],
                'Left Hippocampus'   : ["NA'1-NA'2", "NA'2-NA'3",  "NA'3-NA'4", "NA'4-NA'5", "HC'2-HC'3", "HC'3-HC'4", "HC'4-HC'5","HC'5-HC'6"],
                'Left Insula'        : [],
                'Right Amygdala'     : [],
                'Right Orbitofrontal': [],
                'Right Hippocampus'  : ['HC1-HC2', 'HC2-HC3'],
                'Right Insula'       : []   
                    }

eeg_channels4 = {'Left Amygdala'     : [],
                'Left Orbitofrontal' : [],
                'Left Hippocampus'   : [],
                'Left Insula'        : [],
                'Right Amygdala'     : [],
                'Right Orbitofrontal': [],
                'Right Hippocampus'  : ['HC2-HC3', 'HT1-HT2', 'HC3-HC4', 'HT2-HT3','HC4-HC5', 'HT5-HT6'],
                'Right Insula'       : ['OF1-OF2','OF2-OF3','OF3-OF4']   
                    }


eeg_channels5 = {'Left Amygdala'     : ["NA'1-NA'2", "NA'2-NA'3", "NA'3-NA'4"],
                'Left Orbitofrontal' : [ "R'2-R'3", "R'3-R'4", "R'4-R'5", "R'5-R'6", "R'6-R'7", "R'7-R'8", "R'8-R'9", "OR'1-OR'2", "OR'2-OR'3", "OR'3-OR'4","OR'4-OR'5", "OR'5-OR'6", "OR'6-OR'7", "OR'7-OR'8", "OR'8-OR'9", "OR'9-OR'10"],
                'Left Hippocampus'   : ["HT'1-HT'2", "HT'2-HT'3", "HT'3-HT'4"],
                'Left Insula'        : [],
                'Right Amygdala'     : [],
                'Right Orbitofrontal': ['OR1-OR2', 'OR2-OR3'],
                'Right Hippocampus'  : ['HC1-HC2', 'HC2-HC3', 'HC3-HC4', 'HC4-HC5'],
                'Right Insula'       : []   
                    }

eeg_channels6 = {'Left Amygdala'     : ["NA'1-NA'2", "NA'2-NA'3", "NA'3-NA'4", "NA'4-NA'5"],
                'Left Orbitofrontal' : ["R'1-R'2", "R'2-R'3", "R'3-R'4", "R'4-R'5", "R'5-R'6", "FP'1-FP'2", "FP'2-FP'3", "FP'3-FP'4", "FP'4-FP'5"],
                'Left Hippocampus'   : ["HP'1-HP'2", "HP'2-HP'3", "HP'3-HP'4",  "HP'4-HP'5",  "HP'5-HP'6",  "HP'6-HP'7",  "HP'7-HP'8"],
                'Left Insula'        : [],
                'Right Amygdala'     : [],
                'Right Orbitofrontal': [],
                'Right Hippocampus'  : ['HC1-HC2',  'HC2-HC3',  'HC3-HC4'],
                'Right Insula'       : []   
                    }

eeg_channels7 = {'Left Amygdala'     : [],
                'Left Orbitofrontal' : [],
                'Left Hippocampus'   : [],
                'Left Insula'        : ["T'2-T'3", "H'1-H'2", "H'2-H'3"],
                'Right Amygdala'     : [],
                'Right Orbitofrontal': [],
                'Right Hippocampus'  : [],
                'Right Insula'       : ['TT2-TT3', 'TT3-TT4', 'H2-H3', 'H3-H4']   
                    }

eeg_channels8 = {'Left Amygdala'     : [],
                'Left Orbitofrontal' : [],
                'Left Hippocampus'   : ["HT'1-HT'2","HT'4-HT'5"],
                'Left Insula'        : [ "OP'2-OP'3"],
                'Right Amygdala'     : [],
                'Right Orbitofrontal': [],
                'Right Hippocampus'  : ['HT4-HT5'],
                'Right Insula'       : ['H2-H3', 'H3-H4', 'OP1-OP2', 'OP2-OP3']   
                    }

eeg_channels10 = {'Left Amygdala'    : [],
                'Left Orbitofrontal' : ["OR'2-OR'3","OR'7-OR'8"],
                'Left Hippocampus'   : ["HC'1-HC'2", "HC'2-HC'3", "HC'3-HC'4",  "HC'4-HC'5"],
                'Left Insula'        : [],
                'Right Amygdala'     : [],
                'Right Orbitofrontal': ['R1-R2', 'R2-R3', 'R3-R4', 'R4-R5', 'R5-R6', 'R6-R7',  'R7-R8',  'R8-R9'],
                'Right Hippocampus'  : ['HC1-HC2', 'HC2-HC3', 'HC3-HC4', 'HC4-HC5'],
                'Right Insula'       : []   
                    }

eeg_channels11= {'Left Amygdala'     : [],
                'Left Orbitofrontal' : [],
                'Left Hippocampus'   : ["HC'1-HC'2", "HC'2-HC'3", "HC'3-HC'4", "HC'4-HC'5", "HC'5-HC'6"],
                'Left Insula'        : [],
                'Right Amygdala'     : ['NA1-NA2', 'NA2-NA3', 'NA3-NA4'],
                'Right Orbitofrontal': [],
                'Right Hippocampus'  : ['HT1-HT2',    'HT2-HT3',    'HT3-HT4',    'HT4-HT5', 'HP3-HP4', 'HP4-HP5', 'HP5-HP6'],
                'Right Insula'       : []   
                    }


eeg_channels12 = {'Left Amygdala'     : [],
                'Left Orbitofrontal' : ["OF'1-OF'2"],
                'Left Hippocampus'   : ["HC'3-HC'4"],
                'Left Insula'        : [],
                'Right Amygdala'     : [],
                'Right Orbitofrontal': [],
                'Right Hippocampus'  : [],
                'Right Insula'       : []   
                    }


eeg_channels14= {'Left Amygdala'     : ["NA'1-NA'2", "NA'2-NA'3", "NA'3-NA'4"],
                'Left Orbitofrontal' : [ "R'1-R'2", "R'2-R'3", "R'4-R'5", "R'5-R'6", "R'8-R'9", "R'9-R'10", "OR'1-OR'2", "OR'4-OR'5", "OR'5-OR'6", "OR'6-OR'7", "OR'7-OR'8"],
                'Left Hippocampus'   : [],
                'Left Insula'        : ["T'3-T'4","NA'5-NA'6"],
                'Right Amygdala'     : [],
                'Right Orbitofrontal': [],
                'Right Hippocampus'  : [],
                'Right Insula'       : []   
                    }

eeg_channels16= {'Left Amygdala'     : ["NA'2-NA'3","NA'3-NA'4","NA'4-NA'5"],
                'Left Orbitofrontal' : [],
                'Left Hippocampus'   : ["NA'1-NA'2", "HC'3-HC'4"],
                'Left Insula'        : [],
                'Right Amygdala'     : ['NA4-NA5'],
                'Right Orbitofrontal': [],
                'Right Hippocampus'  : ['NA1-NA2', 'NA2-NA3','NA3-NA4', 'HC1-HC2','HC2-HC3', 'HC3-HC4', 'HT1-HT2','HT2-HT3'],
                'Right Insula'       : ['OP2-OP3', 'OP3-OP4', 'OF1-OF2']   
                    }


eeg_channels17= {'Left Amygdala'     : [],
                'Left Orbitofrontal' : [],
                'Left Hippocampus'   : [ "HT'1-HT'2","HT'2-HT'3"],
                'Left Insula'        : [],
                'Right Amygdala'     : [],
                'Right Orbitofrontal': [],
                'Right Hippocampus'  : ['HT2-HT3'],
                'Right Insula'       : []   
                    }


eeg_channels18= {'Left Amygdala'     : [ "NA'2-NA'3", "NA'3-NA'4",],
                'Left Orbitofrontal' : [],
                'Left Hippocampus'   : [ "HC'3-HC'4"],
                'Left Insula'        : [],
                'Right Amygdala'     : [ 'NA3-NA4'],
                'Right Orbitofrontal': [],
                'Right Hippocampus'  : ['NA1-NA2', 'NA2-NA3', 'HT2-HT3','HT3-HT4', 'HT4-HT5'],
                'Right Insula'       : []   
                    }

eeg_channels20= {'Left Amygdala'     : [],
                'Left Orbitofrontal' : [],
                'Left Hippocampus'   : ["HC'1-HC'2",  "HC'2-HC'3", "HC'3-HC'4"],
                'Left Insula'        : ["T'2-T'3"],
                'Right Amygdala'     : [],
                'Right Orbitofrontal': [],
                'Right Hippocampus'  : ['HC1-HC2', 'HC2-HC3', 'HC3-HC4', 'HC4-HC5', 'HT1-HT2', 'HT2-HT3','HT3-HT4', 'HT4-HT5'],
                'Right Insula'       : ['OF1-OF2',  'H2-H3',  'O1-O2', 'O2-O3']   
                    }

eeg_channels21= {'Left Amygdala'     : [],
                'Left Orbitofrontal' : [],
                'Left Hippocampus'   : ["HT'1-HT'2","HT'2-HT'3","HT'3-HT'4","HT'4-HT'5"],
                'Left Insula'        : [],
                'Right Amygdala'     : [],
                'Right Orbitofrontal': [],
                'Right Hippocampus'  : ['HT1-HT2','HT2-HT3','HT3-HT4', 'HT4-HT5'],
                'Right Insula'       : []   
                    }


eeg_channels22= {'Left Amygdala'     : [],
                'Left Orbitofrontal' : [],
                'Left Hippocampus'   : [ "HT'1-HT'2", "HT'2-HT'3", "HT'3-HT'4","HT'4-HT'5"],
                'Left Insula'        : [],
                'Right Amygdala'     : [],
                'Right Orbitofrontal': ['OR2-OR3', 'OR3-OR4', 'OR4-OR5','OR5-OR6'],
                'Right Hippocampus'  : ['HT1-HT2'],
                'Right Insula'       : []   
                    }

eeg_channels23= {'Left Amygdala'     : [],
                'Left Orbitofrontal' : [],
                'Left Hippocampus'   : [],
                'Left Insula'        : [ "OF'1-OF'2", "OF'2-OF'3"],
                'Right Amygdala'     : [],
                'Right Orbitofrontal': ['OF1-OF2'],
                'Right Hippocampus'  : ["PFG'1-PFG'2"],
                'Right Insula'       : ['OF2-OF3','OF3-OF4','OF4-OF5','OF5-OF6','OC3-OC4']   
                    }

eeg_channels24= {'Left Amygdala'     : [],
                'Left Orbitofrontal' : [],
                'Left Hippocampus'   : [],
                'Left Insula'        : [],
                'Right Amygdala'     : [],
                'Right Orbitofrontal': ['OF3-OF4','OF5-OF6'],
                'Right Hippocampus'  : [],
                'Right Insula'       : [ 'CP3-CP4']   
                    }

eeg_channels25= {'Left Amygdala'     : [],
                'Left Orbitofrontal' : [],
                'Left Hippocampus'   : [],
                'Left Insula'        : [],
                'Right Amygdala'     : [],
                'Right Orbitofrontal': [],
                'Right Hippocampus'  : ['HT1-HT2'],
                'Right Insula'       : []   
                    }

eeg_channels26= {'Left Amygdala'     : [],
                'Left Orbitofrontal' : [],
                'Left Hippocampus'   : ["HC'2-HC'3","HC'3-HC'4"],
                'Left Insula'        : ["OC'2-OC'3"],
                'Right Amygdala'     : [],
                'Right Orbitofrontal': [],
                'Right Hippocampus'  : ['HT1-HT2'],
                'Right Insula'       : [ 'OC1-OC2','OC2-OC3','OC3-OC4','OF5-OF6','OP1-OP2','OP2-OP3','OP3-OP4', 'OP4-OP5',  'OP5-OP6']   
                    }

subject_ductionary = {
                        'sub1': eeg_channels1, 
                        'sub4': eeg_channels4, 
                        'sub5': eeg_channels5, 
                        'sub6': eeg_channels6, 
                        'sub7': eeg_channels7, 
                        'sub8': eeg_channels8, 
                        'sub10': eeg_channels10, 
                        'sub11': eeg_channels11, 
                        'sub12': eeg_channels12, 
                        'sub14': eeg_channels14, 
                        'sub16': eeg_channels16, 
                        'sub17': eeg_channels17, 
                        'sub18': eeg_channels18, 
                        'sub20': eeg_channels20, 
                        'sub21': eeg_channels21, 
                        'sub22': eeg_channels22, 
                        'sub23': eeg_channels23, 
                        'sub24': eeg_channels24, 
                        'sub25': eeg_channels25, 
                        'sub26': eeg_channels26 
                        }


###############################################################################
###############################################################################
###############################################################################

# This function takes all channels from the dictionary for particular subject and convert it to a string
# The string is later used to pick channels of interest only. 

def subj_analyzer(subject):
    what_dict_use = subject_ductionary['sub{}'.format(subject)]
    
    ch_names1 = what_dict_use['Left Amygdala']
    ch_names2 = what_dict_use['Left Orbitofrontal']
    ch_names3 = what_dict_use['Left Hippocampus']
    ch_names4 = what_dict_use['Left Insula']
    ch_names5 = what_dict_use['Right Amygdala']
    ch_names6 = what_dict_use['Right Orbitofrontal']
    ch_names7 = what_dict_use['Right Hippocampus']
    ch_names8 = what_dict_use['Right Insula']

    total_ch_names =  ch_names1 + ch_names2 + ch_names3 + ch_names4 + ch_names5 + ch_names6 + ch_names7 + ch_names8
    return total_ch_names

##############################################################################

total_ch_names = subj_analyzer(subject)
raw_new.pick_channels(total_ch_names) 

#MKR2+ channel will be also droped. So, now we only navigate throught events object.

raw_new.plot(events=events, scalings=dict(eeg=216.695e-6), duration=20)


###############################################################################  
# This function creates epochs based on the found events. Epochs are created each 2 second interval. 
# Epochs are categorized based on condition and interval onset. 
# Thus, for each condition we have a list of 30 epochs, which consists of up to 6 repetitions (events) 

def epoching(raw_new, events):
    
    #### SEPERATE EPOCHS
    events_2              = events.astype(int)                             #events should be a NumPy array of integers, got <class 'numpy.ndarray'>
    
    condition             = [12,22,32,72] 
    step                  = [0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58]
    epochs                = [[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30],
                             [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30],
                             [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30],
                             [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]]
    
    #Loop for splitting the data for small bins
    for k in range(len(condition)):
        m                 = condition[k]
        
        for i in range(len(step)):
            j             = step[i]
            epochs[k][i]  = mne.Epochs(raw_new, events_2,  #raw_picked_data
                                       event_id=[m], 
                                       tmin=j, tmax=j+2, baseline=(j, j),
                                       reject_by_annotation=True,
                                       preload=True)
             
    # List of epochs
    epochs_watchpos       = epochs[0][:]
    epochs_suppress       = epochs[1][:]
    epochs_reassess       = epochs[2][:]
    epochs_watchneu       = epochs[3][:]
    
    # Epochs statistics
    i = 0
    wp = 0; wn = 0; r = 0; s = 0  
    for i in range(30):
        wp += len(epochs_watchpos[i].events)
        wn += len(epochs_watchneu[i].events)
        r  += len(epochs_reassess[i].events)
        s  += len(epochs_suppress[i].events)
        
    print('neu-watch',wn , '\npos-watch', wp, '\npos-reassess', r, '\npos-supress', s)    
    
    return epochs, epochs_watchpos, epochs_suppress, epochs_reassess, epochs_watchneu

###############################################################################  

epochs, epochs_watchpos, epochs_suppress, epochs_reassess, epochs_watchneu = epoching(raw_new, events)
epochs_list = [epochs_watchpos, epochs_suppress, epochs_reassess, epochs_watchneu ]


# SPECIAL CASES - subj 18 and 20 
events               = mne.read_events('{}-events.eve'.format(subject))
raw_new.set_annotations(annot_from_file)
raw_new.plot(events=events, scalings=dict(eeg=216.695e-6), duration=20)

###############################################################################

# Important. Subjects 18 and 20 have one epoch where there is no repetition at all (no 2 second time segment). 
# I deleted this epochs from all conditions. 
# For Sub 18 - the 0th epoch. For sub 18 - the 17th 

del epochs_watchpos[0]
del epochs_watchneu[0]
del epochs_suppress[0]
del epochs_reassess[0]
# del epochs_watchpos[17]
# del epochs_watchneu[17]
# del epochs_suppress[17]
# del epochs_reassess[17]


# %% PSD

##### PSD PARAMETERS
n_jobs      = 4  
fmin        = 2 
fmax        = 80
method      = 'welch'

###############################################################################
###############################################################################   
###############################################################################
def psd_calculation(n_jobs, fmin, fmax, method, epochs_list):
    psd_wp_list = []
    i = 0
    epochs_watchpos = epochs_list[0]
    for i in range(len(epochs_watchpos)):
        epochs = epochs_watchpos[i]
        psd_wp = epochs.compute_psd(method=method, 
                                    fmin=fmin, fmax=fmax, 
                                    tmin=None, tmax=None, 
                                    # picks=ch_inc, 
                                    proj=False, 
                                    n_jobs=n_jobs, 
                                    verbose=None)
        psd_wp_list.append(psd_wp)
        
    
    psd_s_list = []
    i = 0
    epochs_suppress = epochs_list[1]
    for i in range(len(epochs_suppress)):
        epochs = epochs_suppress[i]
        psd_s = epochs.compute_psd(method=method, 
                                   fmin=fmin, fmax=fmax, 
                                   tmin=None, tmax=None, 
                                   # picks=ch_inc, 
                                   proj=False, 
                                   n_jobs=n_jobs, 
                                   verbose=None)
        psd_s_list.append(psd_s)
    
    
    psd_r_list = []
    i = 0
    epochs_reassess = epochs_list[2]
    for i in range(len(epochs_reassess)):
        epochs = epochs_reassess[i]
        if len(epochs.events) == 0:
            continue
        else: 
            psd_r = epochs.compute_psd(method=method, 
                                        fmin=fmin, fmax=fmax, 
                                        tmin=None, tmax=None, 
                                        # picks=ch_inc, 
                                        proj=False, 
                                        n_jobs=n_jobs, 
                                        verbose=None)
            psd_r_list.append(psd_r)
    
    psd_wn_list = []
    i = 0
    epochs_watchneu = epochs_list[3]
    for i in range(len(epochs_watchneu)):
        epochs = epochs_watchneu[i]
        if len(epochs.events) == 0:
            continue
        else: 
            psd_wn = epochs.compute_psd(method=method, 
                                        fmin=fmin, fmax=fmax, 
                                        tmin=None, tmax=None, 
                                        # picks=ch_inc, 
                                        proj=False, 
                                        n_jobs=n_jobs, 
                                        verbose=None)
            psd_wn_list.append(psd_wn)
        
    return psd_wp_list, psd_s_list, psd_r_list, psd_wn_list

###############################################################################
###############################################################################
###############################################################################

psd_wp_list, psd_s_list, psd_r_list, psd_wn_list = psd_calculation(n_jobs, fmin, fmax, method, epochs_list)
len(psd_wp_list)
len(psd_s_list)
len(psd_r_list)
len(psd_wn_list)
len(epochs_watchpos)
len(epochs_suppress)
len(epochs_reassess)
len(epochs_watchneu)    
###############################################################################
####### AVERAGE ACROSS EPOCHS #################################################

def psd_average_across_epochs(psd_wp_list, psd_s_list, psd_r_list, psd_wn_list):
    psd_wp_list_ave_30 = []
    i = 0 
    for i in range(len(psd_wp_list)):
        psd_to_work_with = psd_wp_list[i]
        
        #AVERAGE
        psd_ave = psd_to_work_with.average()
        psd_wp_list_ave_30.append(psd_ave)
        
        # #STD
        # psd_ave_std = psd_to_work_with.get_data()
        # psd_ave_std_np = psd_ave_std.std(axis=0)
        # psd_wp_list_ave_30_std.append(psd_ave_std_np)
    
    
    psd_s_list_ave_30 = []
    i = 0 
    for i in range(len(psd_s_list)):
        psd_to_work_with = psd_s_list[i]
        
        #AVERAGE
        psd_ave = psd_to_work_with.average()
        psd_s_list_ave_30.append(psd_ave)
        
        # #STD
        # psd_ave_std = psd_to_work_with.get_data()
        # psd_ave_std_np = psd_ave_std.std(axis=0)
        # psd_s_list_ave_30_std.append(psd_ave_std_np)
    
    psd_r_list_ave_30 = []
    i = 0 
    for i in range(len(psd_r_list)):
        psd_to_work_with = psd_r_list[i]
        psd_ave = psd_to_work_with.average()
        psd_r_list_ave_30.append(psd_ave)
       
        # #STD
        # psd_ave_std = psd_to_work_with.get_data()
        # psd_ave_std_np = psd_ave_std.std(axis=0)
        # psd_r_list_ave_30_std.append(psd_ave_std_np)
    
    psd_wn_list_ave_30 = []
    i = 0 
    for i in range(len(psd_wn_list)):
        psd_to_work_with = psd_wn_list[i]
        psd_ave = psd_to_work_with.average()
        psd_wn_list_ave_30.append(psd_ave)
         
        # #STD
        # psd_ave_std = psd_to_work_with.get_data()
        # psd_ave_std_np = psd_ave_std.std(axis=0)
        # psd_wn_list_ave_30_std.append(psd_ave_std_np)
    
    return psd_wn_list_ave_30, psd_r_list_ave_30, psd_s_list_ave_30, psd_wp_list_ave_30

###############################################################################
###############################################################################
###############################################################################

psd_wn_list_ave_30, psd_r_list_ave_30, psd_s_list_ave_30, psd_wp_list_ave_30 = psd_average_across_epochs(psd_wp_list, psd_s_list, psd_r_list, psd_wn_list )


###############################################################################
###############################################################################
def plot_psd(ch, what_to_use):
    one_ch_psd = []
  
    for i in range(len(what_to_use)):
        psd_particular = what_to_use[i]
        psd_ch = psd_particular.copy().pick(ch)
        one_ch_psd.append(psd_ch) #вот с этой штукой мы делаем магию СРЕДНЕГО И STD
        
    one_ch_psd_ave          = []
    i                       = 0 
    
    for i in range(len(one_ch_psd)):
        one_ch_psd_ave.append(one_ch_psd[i].get_data())
    np.shape(one_ch_psd_ave)
    
    ##### NUMPYING ##################
    one_ch_psd_ave_np     = np.array(one_ch_psd_ave)
    np.shape(one_ch_psd_ave_np)  
    
    ##### AVERAGE PSD ###############
    one_ch_psd_mean            = np.mean( one_ch_psd_ave_np, axis = 0 )
    np.shape(one_ch_psd_mean)  
    
    #####   STD PSD   ###############
    one_ch_psd_std            = np.std( one_ch_psd_ave_np, axis = 0 )
    np.shape(one_ch_psd_std)  
    
    ##### LOG SCALE   ###############
    one_ch_psd_mean_lg = np.log10(one_ch_psd_mean) 
    one_ch_psd_std_lg  = np.log10(one_ch_psd_std) 
    
    return one_ch_psd_mean_lg, one_ch_psd_std_lg, one_ch_psd_ave_np


##############################################################################
##############################################################################
##############################################################################

# Creating an average condition 

psd_ALL_list_ave_30 = psd_wn_list_ave_30 +  psd_r_list_ave_30 + psd_s_list_ave_30 + psd_wp_list_ave_30
np.shape(psd_ALL_list_ave_30)
np.shape(psd_wn_list_ave_30)

# %% PER SUBJECT PLOTTING 


###############################################################################
##### PICTURE #################################################################
###############################################################################

def plot_individual_spectrum(what_to_use, subject, condition_title, inc1, inc2): 

    ####### Y-limits
    one_psd_list = [] 
    for i in range(len(what_to_use)):
        one_psd = what_to_use[i].get_data()
        one_psd_list.append(one_psd)
    np.shape(one_psd_list)
    one_psd_list_np = np.array(one_psd_list)
    one_psd_list_np.shape
    one_psd_list_np = np.transpose(one_psd_list_np, (1,0,2))
    one_psd_list_np.shape
    one_psd_list_np_ch_mean = np.mean(one_psd_list_np, axis = 0 )
    one_psd_list_np_ch_mean.shape
    one_psd_list_np_ch_mean_epochs_mean = np.mean(one_psd_list_np_ch_mean, axis = 0 )
    one_psd_list_np_ch_mean_epochs_mean.shape
    np.min(one_psd_list_np_ch_mean_epochs_mean)
    ymin = np.min(one_psd_list_np_ch_mean_epochs_mean)
    ymax = np.max(one_psd_list_np_ch_mean_epochs_mean)
    ymin_lg = np.log10(ymin)-2.5
    ymax_lg = np.log10(ymax)+2.5
    
    # ax.set_ylim([ymin_lg, ymax_lg])
    
    ####### PLOTTER
    import random
    fig, ax = plt.subplots(4,2, layout='constrained')
    dict_name = 'sub' + subject
    dictionary_we_work_with = subject_ductionary[dict_name]
    
    ##### 
    ax[0,0].set_title('Left amygdala')
    ax[1,0].set_title('Left orbitofrontal')
    ax[2,0].set_title('Left hippocampus')
    ax[3,0].set_title('Left insula')
    ax[0,1].set_title('Right amygdala')
    ax[1,1].set_title('Right orbitofrontal')
    ax[2,1].set_title('Right hippocampus')
    ax[3,1].set_title('Right insula')
    
    #####
    # if key == 'Right Amygdala': 
    key='Right Amygdala'
    ch_list = dictionary_we_work_with[key]
    
    number_of_colors = len(ch_list)
    hexadecimal_alphabets = '0123456789ABCDEF'
      
    color = ["#" + ''.join([random.choice(hexadecimal_alphabets) for j in range(6)]) for i in range(number_of_colors)]
    j = 0
    for j in range(len(ch_list)):
        one_channel_to_plot = ch_list[j] 
        one_ch_psd_mean, one_ch_psd_std, one_ch_psd_ave_np = plot_psd(one_channel_to_plot,what_to_use)
        ax[0,1].plot(range(fmax-1), one_ch_psd_mean[0,:], color = color[j], label = one_channel_to_plot)
        # ax[0,1].fill_between(range(fmax-1), one_ch_psd_mean1[0,:]+one_ch_psd_std1[0,:], one_ch_psd_mean1[0,:]-one_ch_psd_std1[0,:],  alpha=0.2)
        ax[0,1].legend()
        ax[0,1].set_ylim([ymin_lg, ymax_lg])
    #####
    # if key == 'Right Orbitofrontal': 
    key='Right Orbitofrontal'
    ch_list = dictionary_we_work_with[key]
    
    number_of_colors = len(ch_list)
    hexadecimal_alphabets = '0123456789ABCDEF'
      
    color = ["#" + ''.join([random.choice(hexadecimal_alphabets) for j in range(6)]) for i in range(number_of_colors)]
    j = 0
    for j in range(len(ch_list)):
        one_channel_to_plot = ch_list[j] 
        one_ch_psd_mean, one_ch_psd_std, one_ch_psd_ave_np = plot_psd(one_channel_to_plot,what_to_use)
        ax[1,1].plot(range(fmax-1), one_ch_psd_mean[0,:], color = color[j], label = one_channel_to_plot)
        # ax[1,1].fill_between(range(fmax-1), one_ch_psd_mean1[0,:]+one_ch_psd_std1[0,:], one_ch_psd_mean1[0,:]-one_ch_psd_std1[0,:],  alpha=0.2)
        ax[1,1].legend()    
        ax[1,1].set_ylim([ymin_lg, ymax_lg])
    #####
    
    # if key == 'Right Hippocampus': 
    key='Right Hippocampus'
    ch_list = dictionary_we_work_with[key]
    
    number_of_colors = len(ch_list)
    hexadecimal_alphabets = '0123456789ABCDEF'
      
    color = ["#" + ''.join([random.choice(hexadecimal_alphabets) for j in range(6)]) for i in range(number_of_colors)]
    j = 0
    for j in range(len(ch_list)):
        one_channel_to_plot = ch_list[j] 
        one_ch_psd_mean, one_ch_psd_std, one_ch_psd_ave_np = plot_psd(one_channel_to_plot,what_to_use)
        ax[2,1].plot(range(fmax-1), one_ch_psd_mean[0,:], color = color[j], label = one_channel_to_plot)
        # ax[2,1].fill_between(range(fmax-1), one_ch_psd_mean1[0,:]+one_ch_psd_std1[0,:], one_ch_psd_mean1[0,:]-one_ch_psd_std1[0,:],  alpha=0.2)
        ax[2,1].legend()
        ax[2,1].set_ylim([ymin_lg, ymax_lg])
    #####
    
    # if key == 'Right Insula': 
    key='Right Insula'
    ch_list = dictionary_we_work_with[key]
    
    number_of_colors = len(ch_list)
    hexadecimal_alphabets = '0123456789ABCDEF'
      
    color = ["#" + ''.join([random.choice(hexadecimal_alphabets) for j in range(6)]) for i in range(number_of_colors)]
    j = 0
    for j in range(len(ch_list)):
        one_channel_to_plot = ch_list[j] 
        one_ch_psd_mean, one_ch_psd_std, one_ch_psd_ave_np = plot_psd(one_channel_to_plot,what_to_use)
        ax[3,1].plot(range(fmax-1), one_ch_psd_mean[0,:], color = color[j], label = one_channel_to_plot)
        # ax[3,1].fill_between(range(fmax-1), one_ch_psd_mean1[0,:]+one_ch_psd_std1[0,:], one_ch_psd_mean1[0,:]-one_ch_psd_std1[0,:],  alpha=0.2)
        ax[3,1].legend()
        ax[3,1].set_ylim([ymin_lg, ymax_lg])
    #####
    
    # if key == 'Left Amygdala': 
    key='Left Amygdala'
    ch_list = dictionary_we_work_with[key]
    
    number_of_colors = len(ch_list)
    hexadecimal_alphabets = '0123456789ABCDEF'
      
    color = ["#" + ''.join([random.choice(hexadecimal_alphabets) for j in range(6)]) for i in range(number_of_colors)]
    j = 0
    for j in range(len(ch_list)):
        one_channel_to_plot = ch_list[j] 
        one_ch_psd_mean, one_ch_psd_std, one_ch_psd_ave_np = plot_psd(one_channel_to_plot,what_to_use)
        ax[0,0].plot(range(fmax-1), one_ch_psd_mean[0,:], color = color[j], label = one_channel_to_plot)
        # ax[0,0].fill_between(range(fmax-1), one_ch_psd_mean1[0,:]+one_ch_psd_std1[0,:], one_ch_psd_mean1[0,:]-one_ch_psd_std1[0,:],  alpha=0.2)
        ax[0,0].legend()
        ax[0,0].set_ylim([ymin_lg, ymax_lg])
    #####
    
    # if key == 'Left Orbitofrontal': 
    key='Left Orbitofrontal'
    ch_list = dictionary_we_work_with[key]
    
    number_of_colors = len(ch_list)
    hexadecimal_alphabets = '0123456789ABCDEF'
      
    color = ["#" + ''.join([random.choice(hexadecimal_alphabets) for j in range(6)]) for i in range(number_of_colors)]
    j = 0
    for j in range(len(ch_list)):
        one_channel_to_plot = ch_list[j] 
        one_ch_psd_mean, one_ch_psd_std, one_ch_psd_ave_np = plot_psd(one_channel_to_plot,what_to_use)
        ax[1,0].plot(range(fmax-1), one_ch_psd_mean[0,:], color = color[j], label = one_channel_to_plot)
        # ax[1,0].fill_between(range(fmax-1), one_ch_psd_mean1[0,:]+one_ch_psd_std1[0,:], one_ch_psd_mean1[0,:]-one_ch_psd_std1[0,:],  alpha=0.2)
        ax[1,0].legend()
        ax[1,0].set_ylim([ymin_lg, ymax_lg])
    #####
    
    # if key == 'Left Hippocampus': 
    key='Left Hippocampus'
    ch_list = dictionary_we_work_with[key]
    
    number_of_colors = len(ch_list)
    hexadecimal_alphabets = '0123456789ABCDEF'
      
    color = ["#" + ''.join([random.choice(hexadecimal_alphabets) for j in range(6)]) for i in range(number_of_colors)]
    j = 0
    for j in range(len(ch_list)):
        one_channel_to_plot = ch_list[j] 
        one_ch_psd_mean, one_ch_psd_std, one_ch_psd_ave_np = plot_psd(one_channel_to_plot,what_to_use)
        ax[2,0].plot(range(fmax-1), one_ch_psd_mean[0,:], color = color[j], label = one_channel_to_plot)
        # ax[2,0].fill_between(range(fmax-1), one_ch_psd_mean1[0,:]+one_ch_psd_std1[0,:], one_ch_psd_mean1[0,:]-one_ch_psd_std1[0,:],  alpha=0.2)
        ax[2,0].legend()
        ax[2,0].set_ylim([ymin_lg, ymax_lg])
    #####
    
    # if key == 'Left Insula': 
    key='Left Insula'
    ch_list = dictionary_we_work_with[key]
    
    number_of_colors = len(ch_list)
    hexadecimal_alphabets = '0123456789ABCDEF'
      
    color = ["#" + ''.join([random.choice(hexadecimal_alphabets) for j in range(6)]) for i in range(number_of_colors)]
    j = 0
    for j in range(len(ch_list)):
        one_channel_to_plot = ch_list[j] 
        one_ch_psd_mean, one_ch_psd_std, one_ch_psd_ave_np = plot_psd(one_channel_to_plot,what_to_use)
        ax[3,0].plot(range(fmax-1), one_ch_psd_mean[0,:], color = color[j], label = one_channel_to_plot)
        # ax[3,0].fill_between(range(fmax-1), one_ch_psd_mean1[0,:]+one_ch_psd_std1[0,:], one_ch_psd_mean1[0,:]-one_ch_psd_std1[0,:],  alpha=0.2)
        ax[3,0].legend()
        ax[3,0].set_ylim([ymin_lg, ymax_lg])
        
    fig.set_size_inches(inc1, inc2) # set figure's size manually to your full screen (32x18)
    ##### FIG NAME
    # condition_title = condition_title.upper()
    plt.suptitle("Subject {} - condition {}".format(subject, condition_title))
   
    #### SAVER 
    plt.savefig("Subject {} - condition {}.png".format(subject, condition_title),  bbox_inches='tight')
    
    return fig

###############################################################################
##### ##### ###################################################################
###############################################################################

all_conditins = [psd_wn_list_ave_30, psd_r_list_ave_30, psd_s_list_ave_30, psd_wp_list_ave_30, psd_ALL_list_ave_30] 
all_conditional_titles = ['WN', 'R', 'S', 'WP', 'ALL']

inc1 = 32 #32
inc2 = 18 #18
for y in range(len(all_conditional_titles)):
    condition_title = all_conditional_titles[y]
    what_to_use     = all_conditins[y]
# what_to_use = psd_r_list_ave_30
    fig = plot_individual_spectrum(what_to_use, subject, condition_title, inc1, inc2)

# %% PLV CALCULATION

fmin   = 0
fmax   = 45
n_jobs = -1
what_to_take_from_the_dict = ['Left Orbitofrontal', 'Right Orbitofrontal', 'Left Hippocampus', 'Right Hippocampus',  
                              'Left Insula',  'Right Insula', 'Left Amygdala', 'Right Amygdala'] #In the end - I took all

###############################################################################
def define_ch_pairs(epochs_suppress, subject, what_to_take_from_the_dict):
    #### CHANNEL SELECTION
    example_epoch = epochs_suppress[0]  
    dict_name = 'sub' + subject
    dictionary_we_work_with_1 = subject_ductionary[dict_name]
  
    d = {}
     
    # iterating through the elements of list
    for i in what_to_take_from_the_dict:
        d[i] = dictionary_we_work_with_1[i]
        
    dictionary_we_work_with = d
    
    # all_channels    = example_epoch.ch_names
    # len(all_channels)
    all_channels = [value for key in what_to_take_from_the_dict for value in dictionary_we_work_with.get(key, [])]
    len(all_channels)
    
    # The list of the names of all channels
    # all_channels = epochs.ch_names
    # Dictionary with key as a channel and value as an index
    channel_to_index = {name: idx for idx, name in enumerate(all_channels)}
    # Opposite dictionary
    index_to_channel = {idx: name for idx, name in enumerate(all_channels)}

    # Iterating the combinations of the area pairs
    indices_pairs = []
    
    # Unique pairs list 
    unique_indices_pairs = set()
    # Unique pairs of channels names list 
    unique_names_pairs = set()

    # Functions to check the hemisphere
    def is_left_zone(zone_name):
        return 'Left' in zone_name
    
    def is_right_zone(zone_name):
        return 'Right' in zone_name
    
    for zone_1, channels_1 in dictionary_we_work_with.items():
        for zone_2, channels_2 in dictionary_we_work_with.items():
            # Checking whether the areas are related to one hemisphere 
            if ((is_left_zone(zone_1) and is_left_zone(zone_2)) or 
                (is_right_zone(zone_1) and is_right_zone(zone_2))) and channels_1 and channels_2:
                
                # Continue if the same brain area
                if zone_1 == zone_2:
                   continue  # We do not use the channels from the same brain area to connect with each other
                   
                # Iterating through channels from the first and the second area
                for ch1 in channels_1:
                    for ch2 in channels_2:
                        # Taking pairs of indices based on the channel names
                        if ch1 in all_channels and ch2 in all_channels:
                            ch1_idx = all_channels.index(ch1)
                            ch2_idx = all_channels.index(ch2)
                            
                            # Saving the indices pair if the channels are different
                            if ch1_idx != ch2_idx:
                                pair = tuple(sorted((ch1_idx, ch2_idx)))  # Sorting to always have (min,max)
                                unique_indices_pairs.add(pair)
                            
                                # Saving the names of indices in a pair
                                name_pair = tuple(sorted((ch1, ch2)))  # Soring in order to find unique pairs (0-1, but not 1-0)
                                unique_names_pairs.add(name_pair)
                                
    
    indices = ([pair[0] for pair in unique_indices_pairs], [pair[1] for pair in unique_indices_pairs])
    indices_names = ([pair[0] for pair in unique_names_pairs], [pair[1] for pair in unique_names_pairs])


    return unique_indices_pairs, indices,indices_names,  index_to_channel


###############################################################################
########################################## SELECT PARTICULAR CHANNELS #########
###############################################################################

unique_indices_pairs, indices, indices_names, index_to_channel = define_ch_pairs(epochs_suppress, subject, what_to_take_from_the_dict)


###############################################################################
########################################## PLV CALCULATION ##################**
###############################################################################
i = 0 
suppress_array = []
reassess_array = []
watchpos_array = []
watchneu_array = []

for i in range(len(epochs_watchpos)):

    #### CONDITION SELECTION
    datas   = epochs_suppress[i] #array_like, shape=(n_epochs, n_signals, n_times) 
    datar   = epochs_reassess[i] 
    datawp  = epochs_watchpos[i] 
    datawn  = epochs_watchneu[i] 

    #### PLV CALCULATION
    # PLV = |E[Sxy/|Sxy|]|
 
    outcome_wn = mne_connectivity.spectral_connectivity_epochs(datawn, 
                                                               names=None, 
                                                               method='plv', 
                                                               indices=indices, 
                                                               sfreq=raw_new.info['sfreq'], 
                                                               fmin=fmin, fmax=fmax, 
                                                               fskip=0, 
                                                               faverage=False, 
                                                               n_jobs=n_jobs, 
                                                               verbose=None)  #["HC'5-HC'6", 'HC1-HC2']

    
    outcome_wp = mne_connectivity.spectral_connectivity_epochs(datawp, 
                                                               names=None, 
                                                               method='plv', 
                                                               indices=indices, 
                                                               sfreq=raw_new.info['sfreq'], 
                                                               fmin=fmin, fmax=fmax, 
                                                               fskip=0, 
                                                               faverage=False, 
                                                               n_jobs=n_jobs, 
                                                               verbose=None)  #["HC'5-HC'6", 'HC1-HC2']

    outcome_r = mne_connectivity.spectral_connectivity_epochs(datar, 
                                                              names=None, 
                                                              method='plv', 
                                                              indices=indices, 
                                                              sfreq=raw_new.info['sfreq'], 
                                                              fmin=fmin, fmax=fmax, 
                                                              fskip=0, 
                                                              faverage=False, 
                                                              n_jobs=n_jobs, 
                                                              verbose=None)  #["HC'5-HC'6", 'HC1-HC2']
     
     
    outcome_s = mne_connectivity.spectral_connectivity_epochs(datas, 
                                                              names=None, 
                                                              method='plv', 
                                                              indices=indices, 
                                                              sfreq=raw_new.info['sfreq'], 
                                                              fmin=fmin, fmax=fmax, 
                                                              fskip=0, 
                                                              faverage=False, 
                                                              n_jobs=n_jobs, 
                                                              verbose=None)  #["HC'5-HC'6", 'HC1-HC2']
    
 
    
    suppress_array.append(outcome_s.get_data())
    reassess_array.append(outcome_r.get_data())
    watchpos_array.append(outcome_wp.get_data())
    watchneu_array.append(outcome_wn.get_data())


#### AVERAGING
suppress_array_np = np.array(suppress_array)
reassess_array_np = np.array(reassess_array)
watchpos_array_np = np.array(watchpos_array)
watchneu_array_np = np.array(watchneu_array)

np.shape(suppress_array_np)
mean_supr = np.mean(suppress_array_np, axis=0)
mean_reas = np.mean(reassess_array_np, axis=0)
mean_wpos = np.mean(watchpos_array_np, axis=0)
mean_wneu = np.mean(watchneu_array_np, axis=0)
np.shape(mean_wneu)

###############################################################################
###############################################################################
### All conditions - one-by-one channel visualization (iterating through the loop)
j = 0 
for j in range(len(outcome_s.indices[0])):
# for j in range(2):
# for i in range(10):
    # Visualize the data - OPTION 1
    fig, ax = plt.subplots(3,2)
    n1_l = outcome_s.indices[0]
    n2_l = outcome_s.indices[1]
    n1   = n1_l[j] 
    n2   = n2_l[j] 
    ch1_name  = index_to_channel[n1]
    ch2_name  = index_to_channel[n2]
  
    # Second title preparation
    current_dict = subject_ductionary['sub{}'.format(subject)]
    
    def get_key_for_channel(channel, current_dict):
        for key, channels in current_dict.items():
            if channel in channels:
                return key
        return None  # Return None if channel is not found
    
    # Get the keys corresponding to the channels
    key_ch1 = get_key_for_channel(ch1_name, current_dict)
    key_ch2 = get_key_for_channel(ch2_name, current_dict)
    
    ax[0,0].plot(np.array(outcome_s.freqs), mean_supr[j,:], label="Suppress", color = 'blue')
    ax[0,0].axhline(0, color='black', linestyle='--')
    ax[0,0].plot(np.array(outcome_s.freqs), mean_wneu[j,:], label="Watch Neutral", color = 'black') #, alpha = 0.5
    ax[0,0].plot(np.array(outcome_s.freqs), mean_wneu[j,:]  - mean_supr[j,:], label="Watch Neutral - Suppress difference", linewidth = 3, color ='red')
    ax[0,0].set_ylim([-0.5, 1])
    ax[0,0].legend()
    ax[0,0].margins(x=0) 
    fmin = outcome_s.freqs[0]
    fmax = outcome_s.freqs[-1]
    plt.xticks(np.arange(fmin, fmax, step=1))
 
    ax[1,0].plot(np.array(outcome_s.freqs), mean_reas[j,:], label="Reassess", color = 'green')
    ax[1,0].axhline(0, color='black', linestyle='--')
    ax[1,0].plot(np.array(outcome_s.freqs), mean_wneu[j,:], label="Watch Neutral", color = 'black') #, alpha = 0.5
    ax[1,0].plot(np.array(outcome_s.freqs), mean_wneu[j,:]  - mean_reas[j,:], label="Watch Neutral - Reassess difference", linewidth = 3, color ='red')
    ax[1,0].set_ylim([-0.5, 1])
    ax[1,0].legend()
    ax[1,0].margins(x=0) 
    fmin = outcome_s.freqs[0]
    fmax = outcome_s.freqs[-1]
    plt.xticks(np.arange(fmin, fmax, step=1))
 
    ax[2,0].plot(np.array(outcome_s.freqs), mean_wpos[j,:], label="Watch Positive", color = 'orange')
    ax[2,0].axhline(0, color='black', linestyle='--')
    ax[2,0].plot(np.array(outcome_s.freqs), mean_wneu[j,:], label="Watch Neutral", color = 'black') #, alpha = 0.5
    ax[2,0].plot(np.array(outcome_s.freqs), mean_wneu[j,:]  - mean_wpos[j,:], label="Watch Neutral - Watch Positive difference", linewidth = 3, color ='red')
    ax[2,0].set_ylim([-0.5, 1])
    ax[2,0].legend()
    ax[2,0].margins(x=0) 
    fmin = outcome_s.freqs[0]
    fmax = outcome_s.freqs[-1]
    plt.xticks(np.arange(fmin, fmax, step=1))
 
    ax[0,1].plot(np.array(outcome_s.freqs), mean_supr[j,:], label="Suppress", color = 'blue')
    ax[0,1].axhline(0, color='black', linestyle='--')
    ax[0,1].plot(np.array(outcome_s.freqs), mean_reas[j,:], label="Reassess", color = 'green') #, alpha = 0.5
    ax[0,1].plot(np.array(outcome_s.freqs), mean_supr[j,:]  - mean_reas[j,:], label="Suppress - Reassess difference", linewidth = 3, color ='red')
    ax[0,1].set_ylim([-0.5, 1])
    ax[0,1].legend()
    ax[0,1].margins(x=0) 
    fmin = outcome_s.freqs[0]
    fmax = outcome_s.freqs[-1]
    plt.xticks(np.arange(fmin, fmax, step=1))
 
    ax[1,1].plot(np.array(outcome_s.freqs), mean_supr[j,:], label="Suppress", color = 'blue')
    ax[1,1].axhline(0, color='black', linestyle='--')
    ax[1,1].plot(np.array(outcome_s.freqs), mean_wpos[j,:], label="Watch Positive", color = 'orange') #, alpha = 0.5
    ax[1,1].plot(np.array(outcome_s.freqs), mean_supr[j,:]  - mean_wpos[j,:], label="Suppress - Watch Positive difference", linewidth = 3, color ='red')
    ax[1,1].set_ylim([-0.5, 1])
    ax[1,1].legend()
    ax[1,1].margins(x=0) 
    fmin = outcome_s.freqs[0]
    fmax = outcome_s.freqs[-1]
    plt.xticks(np.arange(fmin, fmax, step=1))
 
    ax[2,1].plot(np.array(outcome_s.freqs), mean_reas[j,:], label="Reassess", color = 'green')
    ax[2,1].axhline(0, color='black', linestyle='--')
    ax[2,1].plot(np.array(outcome_s.freqs), mean_wpos[j,:], label="Watch Positive", color = 'orange') #, alpha = 0.5
    ax[2,1].plot(np.array(outcome_s.freqs), mean_reas[j,:]  - mean_wpos[j,:], label="Reassess - Watch Positive difference", linewidth = 3, color ='red')
    ax[2,1].set_ylim([-0.5, 1])
    ax[2,1].legend()
    ax[2,1].margins(x=0) 
    fmin = outcome_s.freqs[0]
    fmax = outcome_s.freqs[-1]
    plt.xticks(np.arange(fmin, fmax, step=1))
    
    plt.suptitle('{} - {}'.format(ch1_name , ch2_name))
    # fig.text(, x=0.5, y=1.00, fontsize=18, ha='center', va='center')
    fig.text(0.5, 0.95, '{} - {}'.format(key_ch1 , key_ch2), fontsize=12, ha='center', fontweight ='bold')
    
    os.chdir('E:/EXP_DATA/iEEG_data/PLVpicNEW/{}'.format(subject))    
    fig.set_size_inches(18, 12) # set figure's size manually to your full screen (32x18)
    plt.savefig("Subject {} - elec {} with elec {}.png".format(subject, ch1_name, ch2_name),  bbox_inches='tight')
    plt.close(fig)

###############################################################################
###############################################################################
###############################################################################

# MERGED CHANNELS VISUALIZATION
# Channels from one brain area are merged in one plot 
# The channels are in the same plot if their offset is the same 
# The channels are in the same plot if they belong to the same brain area

###############################################################################
def convert_channels_to_indices(dictionary_we_work_with, index_to_channel):
    # Reverse dictionary to find indices based on their value
    channel_to_index = {v: k for k, v in index_to_channel.items()}
    
    # Values change into indices
    updated_dict = {}
    for key, channels in dictionary_we_work_with.items():
        updated_channels = [channel_to_index[channel] for channel in channels if channel in channel_to_index]
        updated_dict[key] = updated_channels
    
    return updated_dict
###############################################################################

dict_name = 'sub' + subject
dictionary_we_work_with_1 = subject_ductionary[dict_name]
updated_dictionary = convert_channels_to_indices(dictionary_we_work_with_1, index_to_channel)

###############################################################################
def get_zone_indices(outcome_s, zone_name, updated_dictionary):
    # Taking indices for a particular brain area 
    zone_indices = updated_dictionary.get(zone_name, [])
    
    # Taking an order in outcome.indices[0] for indices oef the same brain area
    result = [i for i, idx in enumerate(outcome_s.indices[0]) if idx in zone_indices]
    
    return result
###############################################################################

### HERE THE AREA WE TAKE AS THE MAIN ONE (the number of channels)
zone_indices = get_zone_indices(outcome_s, 'Right Hippocampus', updated_dictionary) 
print(zone_indices)

###############################################################################
def find_common_electrodes_with_target(outcome, zone_indices, target_electrode):
    # Checking, which indicecs in zone_indices are connected with the target_electrode in outcome.indices[1]
    ch_to_plot = [idx for idx in zone_indices if outcome.indices[1][idx] == target_electrode]
    
    return ch_to_plot
###############################################################################


##### MANUAL PART
# I select the target electrde by hand in order to control the visualization 
# I used this for a help:   
#dict_name = 'sub' + subject
#dictionary_we_work_with_1 = subject_ductionary[dict_name]
#updated_dictionary

ch_to_plot = find_common_electrodes_with_target(outcome_s, zone_indices, target_electrode=15)
print("ch_to_plot:", ch_to_plot)


# VISUALIZATION 
u = ch_to_plot[0]
fig, ax = plt.subplots(3,2)
ax[0,0].axhline(0, color='black')# linestyle='--')
ax[0,1].axhline(0, color='black')#, linestyle='--')
ax[1,0].axhline(0, color='black')#, linestyle='--')
ax[1,1].axhline(0, color='black')#, linestyle='--')
ax[2,0].axhline(0, color='black')#, linestyle='--')
ax[2,1].axhline(0, color='black')#, linestyle='--')
number_of_colors = len(outcome_s.indices[0])
hexadecimal_alphabets = '0123456789ABCDEF'      
color = ["#" + ''.join([random.choice(hexadecimal_alphabets) for j in range(6)]) for i in range(number_of_colors)]

for u in ch_to_plot:
    name_list = outcome_s.indices[0]
    labeli = name_list[u]
    
    ax[0,0].title.set_text('Watch NEUTRAL - Supress')
    ax[0,0].plot(np.array(outcome_s.freqs), mean_supr[u,:], label=index_to_channel[labeli], color = color[u])
    ax[0,0].plot(np.array(outcome_s.freqs), mean_wneu[u,:], label=index_to_channel[labeli], color = color[u])#, alpha = 0.5) #, alpha = 0.5
    ax[0,0].plot(np.array(outcome_s.freqs), mean_wneu[u,:]  - mean_supr[u,:], label=index_to_channel[labeli], color = color[u])#, linewidth = 1, )
    ax[0,0].set_ylim([-0.5, 1])
    # ax[0,0].legend()
    ax[0,0].margins(x=0) 
   
    ax[1,0].title.set_text('Watch NEUTRAL - Reappraise')
    ax[1,0].plot(np.array(outcome_s.freqs), mean_reas[u,:], label=index_to_channel[labeli], color = color[u])
    ax[1,0].plot(np.array(outcome_s.freqs), mean_wneu[u,:], label=index_to_channel[labeli], color = color[u])#, alpha = 0.5)  
    ax[1,0].plot(np.array(outcome_s.freqs), mean_wneu[u,:]  - mean_reas[u,:], label=index_to_channel[labeli], color = color[u])#, linewidth = 1)
    ax[1,0].set_ylim([-0.5, 1])
    # ax[1,0].legend()
    ax[1,0].margins(x=0) 
   
    ax[2,0].title.set_text('Watch NEUTRAL- Watch POSITIVE')
    ax[2,0].plot(np.array(outcome_s.freqs), mean_wpos[u,:], label=index_to_channel[labeli], color = color[u])
    ax[2,0].plot(np.array(outcome_s.freqs), mean_wneu[u,:], label=index_to_channel[labeli], color = color[u])#, alpha = 0.5) #, alpha = 0.5
    ax[2,0].plot(np.array(outcome_s.freqs), mean_wneu[u,:]  - mean_wpos[u,:], label=index_to_channel[labeli], color = color[u])# linewidth = 1, color = color[u])
    ax[2,0].set_ylim([-0.5, 1])
    # ax[2,0].legend()
    ax[2,0].margins(x=0) 
  
    ax[0,1].title.set_text('Supress - Watch NEUTRAL')
    ax[0,1].plot(np.array(outcome_s.freqs), mean_supr[u,:], label=index_to_channel[labeli], color = color[u])
    ax[0,1].plot(np.array(outcome_s.freqs), mean_reas[u,:], label=index_to_channel[labeli], color = color[u])# alpha = 0.5) #, alpha = 0.5
    ax[0,1].plot(np.array(outcome_s.freqs), mean_supr[u,:]  - mean_reas[u,:], label=index_to_channel[labeli], color = color[u])# linewidth = 1, color = color[u])
    ax[0,1].set_ylim([-0.5, 1])
    # ax[0,1].legend()
    ax[0,1].margins(x=0) 

    ax[1,1].title.set_text('Supress - Watch POSITIVE')
    ax[1,1].plot(np.array(outcome_s.freqs), mean_supr[u,:], label=index_to_channel[labeli], color = color[u])
    ax[1,1].plot(np.array(outcome_s.freqs), mean_wpos[u,:], label=index_to_channel[labeli], color = color[u])# alpha = 0.5) #, alpha = 0.5
    ax[1,1].plot(np.array(outcome_s.freqs), mean_supr[u,:]  - mean_wpos[u,:], label=index_to_channel[labeli], color = color[u])# linewidth = 1, color =color[u])
    ax[1,1].set_ylim([-0.5, 1])
    # ax[1,1].legend()
    ax[1,1].margins(x=0) 
 
    ax[2,1].title.set_text('Reappraise - Watch POSITIVE')
    ax[2,1].plot(np.array(outcome_s.freqs), mean_reas[u,:], label=index_to_channel[labeli], color = color[u])
    ax[2,1].plot(np.array(outcome_s.freqs), mean_wpos[u,:], label=index_to_channel[labeli], color = color[u])# alpha = 0.5) #, alpha = 0.5
    ax[2,1].plot(np.array(outcome_s.freqs), mean_reas[u,:]  - mean_wpos[u,:], label=index_to_channel[labeli], color = color[u])# linewidth = 1, color = color[u])
    ax[2,1].set_ylim([-0.5, 1])
    # ax[2,1].legend()
    ax[2,1].margins(x=0) 
    
    
    handles, labels = ax[2,1].get_legend_handles_labels()
    fig.legend(handles, labels, loc='right')
    
    # Second title preparation
    name_list1 = outcome_s.indices[0]
    labeli1 = name_list1[u]
    name_list2 = outcome_s.indices[1]
    labeli2 = name_list2[u]
    
    def get_key_for_channel(channel, current_dict):
        for key, channels in current_dict.items():
            if channel in channels:
                return key
        return None  # Return None if channel is not found
    
    # Get the keys corresponding to the channels
    key_ch1 = get_key_for_channel(labeli1, updated_dictionary)
    key_ch2 = get_key_for_channel(labeli2, updated_dictionary)
    
    plt.suptitle('{} - {}'.format(key_ch1 , key_ch2))
    
    fig.set_size_inches(18, 12) # set figure's size manually to your the full screen 
 
    # plt.close(fig)

       
   