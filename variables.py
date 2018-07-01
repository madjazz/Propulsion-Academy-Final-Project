#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  6 16:26:51 2017

@author: Timo
"""

import numpy as np

var_dict = {
                      "Date of Baseline CT" : None,

                      "Research Protocol" : {
                              "y" : "Yes",
                              "n" : "No"
                              }, 

                      "Cancellation" : {
                              'y' : 'Yes',
                              'n' : 'No'
                              },
                             
                      "Special Attention" : {
                              'y' : 'Yes'
                              },
                            
                      "How did you hear about our program?" : {
                              'br' : 'Brochure',
                              'md' : 'Doctor Referral',
                              'fp' : 'Friend in program',
                              'in' : 'Internet',
                              'np' : 'Newspaper',
                              'ra' : 'Radio',
                              'at' : 'Television',
                              'wm' : 'Word of Mouth',
                              'ot' : 'Other',
                              'NA' : np.nan
                              },
                      
                      "Date of Birth" : None,
                      
                      "Patient Status" : {
                              'ac' : 'Active',
                              'tr' : 'Transferred to Another Institution (specify)',
                              'mr' : 'Unable Due to Medical Reason (specify)',
                              'pr' : 'Unwilling Due to Personal Reason (specify)',
                              'rf' : 'Refused to Continue',
                              'pa' : 'Physician Advised Against',
                              'ra' : 'Concern About Radiation',
                              'mv' : 'Moved and Unable to Return',
                              'in' : 'No Insurance, can\'t have Dx CT',
                              'bc' : 'Burden of Cost',
                              'os' : 'Other (specify)',
                              'es' : 'Excluded (specify)',
                              'sc' : 'Study Complete',
                              'nr' : 'No Response to 3 Calls + 3 Letters',
                              'fe' : 'Being Followed Elsewhere (Get Results)',
                              'ex' : 'Expired (Record Date / Cause)',
                              'NA' : np.nan
                              },
                               
                      "Date of Exit" : None,
                      
                      "Correspondence Date" : None,
                      
                      "Date of Exam" : None,
                      
                      "Recipient" : {
                              's' : 'Patient',
                              'm' : 'Physician',
                              'NA' : np.nan,
                              }, 
                              
                     "Nature" : {
                             'fr' : 'faxed report',
                             'mr' : 'mailed report',
                             'pr' : 'called to give results',
                             'ab' : 'Abx discussed with physician', 
                             'bx' : 'Bx discussed with physician',
                             'os' : 'other (specify)'
                             }, 
                     
                     "Study Date" : None,
                     
                     "Final Reading" : {
                             'y' : 'Yes'
                             }, 
                     
                     "CT Scan Performed at Outside Institution" : {
                             'y' : 'Yes'
                             },
                     
                     "Type of Exam" : {
                             'b' : 'Baseline',
                             'a' : 'Annual Repeat',
                             'd' : 'Follow-up (Not Annual Repeat)'
                             },
                     
                     "CT Protocol" : {
                             'l' : 'Low-Dose CT',
                             'd' : 'Standard CT',
                             'i' : 'Limited CT'
                             },
                     
                     "Date of Most Recent Comparative Study" : None,
                     
                     "Normal Shortcut" : {
                             'y' : 'Yes',
                             }, 
                             
                     "Is it new? (Nodule 1)" : {
                             'n' : 'Newly Seen',
                             'pn' : 'Prev Seen, No Change', 
                             'pd' : 'Slight Decr',
                             'pe' : 'Prev Seen, Marked Decr',
                             'pi' : 'Prev Seen, Slight Incr',
                             'pj' : 'Prev Seen, Marked Incr',
                             'po' : 'Prev Seen, Obscured',
                             'pw' : 'Prev Seen, Resolved',
                             'px' : 'Prev Seen, Not a Nodule',
                             'pr' : 'Prev Seen, Resected',
                             'rn' : 'Retrospect, No Chg',
                             'rd' : 'Retrospect, Decrease',
                             'ri' : 'Retrospect, Slight Incr',
                             'rj' : 'Retrospect, Marked Incr',
                             'pk' : 'Not in Outside Report',
                             'pv' : 'Not Included in Scan',
                             'NA' : np.nan
                             },

                    "Is it new? (Nodule 2)" : {
                             'n' : 'Newly Seen',
                             'pn' : 'Prev Seen, No Change', 
                             'pd' : 'Slight Decr',
                             'pe' : 'Prev Seen, Marked Decr',
                             'pi' : 'Prev Seen, Slight Incr',
                             'pj' : 'Prev Seen, Marked Incr',
                             'po' : 'Prev Seen, Obscured',
                             'pw' : 'Prev Seen, Resolved',
                             'px' : 'Prev Seen, Not a Nodule',
                             'pr' : 'Prev Seen, Resected',
                             'rn' : 'Retrospect, No Chg',
                             'rd' : 'Retrospect, Decrease',
                             'ri' : 'Retrospect, Slight Incr',
                             'rj' : 'Retrospect, Marked Incr',
                             'pk' : 'Not in Outside Report',
                             'pv' : 'Not Included in Scan',
                             'NA' : np.nan
                             },
                    
                    "Is it new? (Nodule 3)" : {
                             'n' : 'Newly Seen',
                             'pn' : 'Prev Seen, No Change', 
                             'pd' : 'Slight Decr',
                             'pe' : 'Prev Seen, Marked Decr',
                             'pi' : 'Prev Seen, Slight Incr',
                             'pj' : 'Prev Seen, Marked Incr',
                             'po' : 'Prev Seen, Obscured',
                             'pw' : 'Prev Seen, Resolved',
                             'px' : 'Prev Seen, Not a Nodule',
                             'pr' : 'Prev Seen, Resected',
                             'rn' : 'Retrospect, No Chg',
                             'rd' : 'Retrospect, Decrease',
                             'ri' : 'Retrospect, Slight Incr',
                             'rj' : 'Retrospect, Marked Incr',
                             'pk' : 'Not in Outside Report',
                             'pv' : 'Not Included in Scan',
                             'NA' : np.nan
                             },

                    "Is it new? (Nodule 4)" : {
                             'n' : 'Newly Seen',
                             'pn' : 'Prev Seen, No Change', 
                             'pd' : 'Slight Decr',
                             'pe' : 'Prev Seen, Marked Decr',
                             'pi' : 'Prev Seen, Slight Incr',
                             'pj' : 'Prev Seen, Marked Incr',
                             'po' : 'Prev Seen, Obscured',
                             'pw' : 'Prev Seen, Resolved',
                             'px' : 'Prev Seen, Not a Nodule',
                             'pr' : 'Prev Seen, Resected',
                             'rn' : 'Retrospect, No Chg',
                             'rd' : 'Retrospect, Decrease',
                             'ri' : 'Retrospect, Slight Incr',
                             'rj' : 'Retrospect, Marked Incr',
                             'pk' : 'Not in Outside Report',
                             'pv' : 'Not Included in Scan',
                             'NA' : np.nan
                             },

                    "Is it new? (Nodule 5)" : {
                             'n' : 'Newly Seen',
                             'pn' : 'Prev Seen, No Change', 
                             'pd' : 'Slight Decr',
                             'pe' : 'Prev Seen, Marked Decr',
                             'pi' : 'Prev Seen, Slight Incr',
                             'pj' : 'Prev Seen, Marked Incr',
                             'po' : 'Prev Seen, Obscured',
                             'pw' : 'Prev Seen, Resolved',
                             'px' : 'Prev Seen, Not a Nodule',
                             'pr' : 'Prev Seen, Resected',
                             'rn' : 'Retrospect, No Chg',
                             'rd' : 'Retrospect, Decrease',
                             'ri' : 'Retrospect, Slight Incr',
                             'rj' : 'Retrospect, Marked Incr',
                             'pk' : 'Not in Outside Report',
                             'pv' : 'Not Included in Scan',
                             'NA' : np.nan
                             },

                    "Is it new? (Additional Nodule)" : {
                            'n' : 'Newly Seen',
                            'pn' : 'Prev Seen, No Change', 
                            'pd' : 'Slight Decr',
                            'pe' : 'Prev Seen, Marked Decr',
                            'pi' : 'Prev Seen, Slight Incr',
                            'pj' : 'Prev Seen, Marked Incr',
                            'po' : 'Prev Seen, Obscured',
                            'pw' : 'Prev Seen, Resolved',
                            'px' : 'Prev Seen, Not a Nodule',
                            'pr' : 'Prev Seen, Resected',
                            'rn' : 'Retrospect, No Chg',
                            'rd' : 'Retrospect, Decrease',
                            'ri' : 'Retrospect, Slight Incr',
                            'rj' : 'Retrospect, Marked Incr',
                            'pk' : 'Not in Outside Report',
                            'pv' : 'Not Included in Scan',
                            'NA' : np.nan
                            },

                    "Endobronchial? (Nodule 1)" : {
                            'no' : 'No',
                            'tr' : 'Trachea',
                            'rm' : 'Rt. Main',
                            'lm' : 'Lt. Main',
                            'bi' : 'BI',
                            'rul' : 'RUL',
                            'rml' : 'RML',
                            'rll' : 'RLL',
                            'lul' : 'LUL',
                            'lll' : 'LLL',
                            'NA' : np.nan
                            }, 
                    "Endobronchial? (Nodule 2)" : {
                            'no' : 'No',
                            'tr' : 'Trachea',
                            'rm' : 'Rt. Main',
                            'lm' : 'Lt. Main',
                            'bi' : 'BI',
                            'rul' : 'RUL',
                            'rml' : 'RML',
                            'rll' : 'RLL',
                            'lul' : 'LUL',
                            'lll' : 'LLL',
                            'NA' : np.nan
                            },
                    
                    "Endobronchial? (Nodule 3)" : {
                            'no' : 'No',
                            'tr' : 'Trachea',
                            'rm' : 'Rt. Main',
                            'lm' : 'Lt. Main',
                            'bi' : 'BI',
                            'rul' : 'RUL',
                            'rml' : 'RML',
                            'rll' : 'RLL',
                            'lul' : 'LUL',
                            'lll' : 'LLL',
                            'NA' : np.nan
                            },
                    
                    "Endobronchial? (Nodule 4)" : {
                            'no' : 'No',
                            'tr' : 'Trachea',
                            'rm' : 'Rt. Main',
                            'lm' : 'Lt. Main',
                            'bi' : 'BI',
                            'rul' : 'RUL',
                            'rml' : 'RML',
                            'rll' : 'RLL',
                            'lul' : 'LUL',
                            'lll' : 'LLL',
                            'NA' : np.nan
                            },
                    
                    "Endobronchial? (Nodule 5)" : {
                            'no' : 'No',
                            'tr' : 'Trachea',
                            'rm' : 'Rt. Main',
                            'lm' : 'Lt. Main',
                            'bi' : 'BI',
                            'rul' : 'RUL',
                            'rml' : 'RML',
                            'rll' : 'RLL',
                            'lul' : 'LUL',
                            'lll' : 'LLL',
                            'NA' : np.nan
                            },
                    
                    "Endobronchial? (Additional Nodule)" : {
                            'no' : 'No',
                            'tr' : 'Trachea',
                            'rm' : 'Rt. Main',
                            'lm' : 'Lt. Main',
                            'bi' : 'BI',
                            'rul' : 'RUL',
                            'rml' : 'RML',
                            'rll' : 'RLL',
                            'lul' : 'LUL',
                            'lll' : 'LLL',
                            'NA' : np.nan
                            },
                    
                    "Most Likely Location (Nodule 1)" : {
                            'end' : 'Endobr',
                            'lul' : 'LUL',
                            'lll' : 'LLL',
                            'rul' : 'RUL',
                            'rml' : 'RML',
                            'rll' : 'RLL',
                            'NA' : np.nan
                            },
                    
                    "Most Likely Location (Nodule 2)" : {
                            'end' : 'Endobr',
                            'lul' : 'LUL',
                            'lll' : 'LLL',
                            'rul' : 'RUL',
                            'rml' : 'RML',
                            'rll' : 'RLL',
                            'NA' : np.nan
                            },
                    
                    "Most Likely Location (Nodule 3)" : {
                            'end' : 'Endobr',
                            'lul' : 'LUL',
                            'lll' : 'LLL',
                            'rul' : 'RUL',
                            'rml' : 'RML',
                            'rll' : 'RLL',
                            'NA' : np.nan
                            },
                    
                    "Most Likely Location (Nodule 4)" : {
                            'end' : 'Endobr',
                            'lul' : 'LUL',
                            'lll' : 'LLL',
                            'rul' : 'RUL',
                            'rml' : 'RML',
                            'rll' : 'RLL',
                            'NA' : np.nan
                            },
                            
                    "Most Likely Location (Nodule 5)" : {
                            'end' : 'Endobr',
                            'lul' : 'LUL',
                            'lll' : 'LLL',
                            'rul' : 'RUL',
                            'rml' : 'RML',
                            'rll' : 'RLL',
                            'NA' : np.nan
                            },
                    
                    "Most Likely Location (Additional Nodule)" : {
                            'end' : 'Endobr',
                            'lul' : 'LUL',
                            'lll' : 'LLL',
                            'rul' : 'RUL',
                            'rml' : 'RML',
                            'rll' : 'RLL',
                            'NA' : np.nan
                            },
                    
                    "Nodule Consistency (Nodule 1)" : {
                            's' : 'Solid',
                            'm' : 'Part-solid',
                            'g' : 'Non-solid',
                            'o' : 'Other (See Comment)',
                            'NA' : np.nan
                            },
                    
                    "Nodule Consistency (Nodule 2)" : {
                            's' : 'Solid',
                            'm' : 'Part-solid',
                            'g' : 'Non-solid',
                            'o' : 'Other (See Comment)',
                            'NA' : np.nan
                            },
                    
                    "Nodule Consistency (Nodule 3)" : {
                            's' : 'Solid',
                            'm' : 'Part-solid',
                            'g' : 'Non-solid',
                            'o' : 'Other (See Comment)',
                            'NA' : np.nan
                            },
                    
                    "Nodule Consistency (Nodule 4)" : {
                            's' : 'Solid',
                            'm' : 'Part-solid',
                            'g' : 'Non-solid',
                            'o' : 'Other (See Comment)',
                            'NA' : np.nan
                            },
                    
                    "Nodule Consistency (Nodule 5)" : {
                            's' : 'Solid',
                            'm' : 'Part-solid',
                            'g' : 'Non-solid',
                            'o' : 'Other (See Comment)',
                            'NA' : np.nan
                            },
                    
                    "Nodule Consistency (Additional Nodule)" : {
                            's' : 'Solid',
                            'm' : 'Part-solid',
                            'g' : 'Non-solid',
                            'o' : 'Other (See Comment)',
                            'NA' : np.nan
                            },
                    
                    "Smooth Edges (Nodule 1)" : {
                            'n' : 'No',
                            'y' : 'Yes',
                            'q' : 'Question'
                            },
                    
                    "Smooth Edges (Nodule 2)" : {
                            'n' : 'No',
                            'y' : 'Yes',
                            'q' : 'Question'
                            },
                    
                    "Smooth Edges (Nodule 3)" : {
                            'n' : 'No',
                            'y' : 'Yes',
                            'q' : 'Question'
                            },
                    
                    "Smooth Edges (Nodule 4)" : {
                            'n' : 'No',
                            'y' : 'Yes',
                            'q' : 'Question'
                            },
                    
                    "Smooth Edges (Nodule 5)" : {
                            'n' : 'No',
                            'y' : 'Yes',
                            'q' : 'Question'
                            },
                    
                    "Smooth Edges (Additional Nodule)" : {
                            'n' : 'No',
                            'y' : 'Yes',
                            'q' : 'Question'
                            },
                    
                    "Calcifications c/w Benignity (Nodule 1)" : {
                            'n' : 'No',
                            'y' : 'Yes',
                            'q' : 'Question'
                            },
                    
                    "Calcifications c/w Benignity (Nodule 2)" : {
                            'n' : 'No',
                            'y' : 'Yes',
                            'q' : 'Question'
                            },
                    
                    "Calcifications c/w Benignity (Nodule 3)" : {
                            'n' : 'No',
                            'y' : 'Yes',
                            'q' : 'Question'
                            },
                    
                    "Calcifications c/w Benignity (Nodule 4)" : {
                            'n' : 'No',
                            'y' : 'Yes',
                            'q' : 'Question'
                            },
                    
                    "Calcifications c/w Benignity (Nodule 5)" : {
                            'n' : 'No',
                            'y' : 'Yes',
                            'q' : 'Question'
                            },
                    
                    "Calcifications c/w Benignity (Additional Nodule)" : {
                            'n' : 'No',
                            'y' : 'Yes',
                            'q' : 'Question'
                            },
                    
                    "Spiculations /Pleural Tags (Nodule 1)" : {
                            'n' : 'Absent',
                            'y' : 'Present'
                            },
                    
                    "Spiculations /Pleural Tags (Nodule 2)" : {
                            'n' : 'Absent',
                            'y' : 'Present'
                            },
                    
                    "Spiculations /Pleural Tags (Nodule 3)" : {
                            'n' : 'Absent',
                            'y' : 'Present'
                            },
                    
                    "Spiculations /Pleural Tags (Nodule 4)" : {
                            'n' : 'Absent',
                            'y' : 'Present'
                            },
                    
                    "Spiculations /Pleural Tags (Nodule 5)" : {
                            'n' : 'Absent',
                            'y' : 'Present'
                            },
                    
                    "Spiculations /Pleural Tags (Additional Nodule)" : {
                            'n' : 'Absent',
                            'y' : 'Present'
                            },
                    
                    "Parenchymal Abnormality within 1 cm (Nodule 1)" : {
                            'n' : 'No',
                            'y' : 'Yes',
                            'q' : 'Question'
                            },
                    
                    "Parenchymal Abnormality within 1 cm (Nodule 2)" : {
                            'n' : 'No',
                            'y' : 'Yes',
                            'q' : 'Question'
                            },
                    
                    "Parenchymal Abnormality within 1 cm (Nodule 3)" : {
                            'n' : 'No',
                            'y' : 'Yes',
                            'q' : 'Question'
                            },
                    
                    "Parenchymal Abnormality within 1 cm (Nodule 4)" : {
                            'n' : 'No',
                            'y' : 'Yes',
                            'q' : 'Question'
                            },
                    
                    "Parenchymal Abnormality within 1 cm (Nodule 5)" : {
                            'n' : 'No',
                            'y' : 'Yes',
                            'q' : 'Question'
                            },
                    
                    "Parenchymal Abnormality within 1 cm (Additional Nodule)" : {
                            'n' : 'No',
                            'y' : 'Yes',
                            'q' : 'Question'
                            },
                    
                    "Nodule Status (Nodule 1)" : {
                            'un' : 'Unknown',
                            'bc' : 'Benign (Ca++)',
                            'pc' : 'Prob Benign, prob Ca++',
                            're' : 'Resolved',
                            'rg' : 'Resolving',
                            'tn' : 'No Change, 2 yrs',
                            'pp' : 'PET - Positive',
                            'pn' : 'PET - Negative',
                            'pi' : 'PET - Indeterminate',
                            'ub' : 'Biopsy - Unknown',  
                            'bb' : 'Biopsy - Benign',
                            'mb' : 'Biopsy - Malignant',
                            'ab' : 'Biopsy - Atyp Bronch Prolif',
                            'om' : 'Biopsy - Metastatic',
                            'mr' : 'Resected - Malignant',
                            'br' : 'Resected - Benign',
                            'NA' : np.nan
                            },
                    
                    "Nodule Status (Nodule 2)" : {
                            'un' : 'Unknown',
                            'bc' : 'Benign (Ca++)',
                            'pc' : 'Prob Benign, prob Ca++',
                            're' : 'Resolved',
                            'rg' : 'Resolving',
                            'tn' : 'No Change, 2 yrs',
                            'pp' : 'PET - Positive',
                            'pn' : 'PET - Negative',
                            'pi' : 'PET - Indeterminate',
                            'ub' : 'Biopsy - Unknown',  
                            'bb' : 'Biopsy - Benign',
                            'mb' : 'Biopsy - Malignant',
                            'ab' : 'Biopsy - Atyp Bronch Prolif',
                            'om' : 'Biopsy - Metastatic',
                            'mr' : 'Resected - Malignant',
                            'br' : 'Resected - Benign',
                            'NA' : np.nan
                            },
                    
                    "Nodule Status (Nodule 3)" : {
                            'un' : 'Unknown',
                            'bc' : 'Benign (Ca++)',
                            'pc' : 'Prob Benign, prob Ca++',
                            're' : 'Resolved',
                            'rg' : 'Resolving',
                            'tn' : 'No Change, 2 yrs',
                            'pp' : 'PET - Positive',
                            'pn' : 'PET - Negative',
                            'pi' : 'PET - Indeterminate',
                            'ub' : 'Biopsy - Unknown',  
                            'bb' : 'Biopsy - Benign',
                            'mb' : 'Biopsy - Malignant',
                            'ab' : 'Biopsy - Atyp Bronch Prolif',
                            'om' : 'Biopsy - Metastatic',
                            'mr' : 'Resected - Malignant',
                            'br' : 'Resected - Benign',
                            'NA' : np.nan
                            },
                    
                    "Nodule Status (Nodule 4)" : {
                            'un' : 'Unknown',
                            'bc' : 'Benign (Ca++)',
                            'pc' : 'Prob Benign, prob Ca++',
                            're' : 'Resolved',
                            'rg' : 'Resolving',
                            'tn' : 'No Change, 2 yrs',
                            'pp' : 'PET - Positive',
                            'pn' : 'PET - Negative',
                            'pi' : 'PET - Indeterminate',
                            'ub' : 'Biopsy - Unknown',  
                            'bb' : 'Biopsy - Benign',
                            'mb' : 'Biopsy - Malignant',
                            'ab' : 'Biopsy - Atyp Bronch Prolif',
                            'om' : 'Biopsy - Metastatic',
                            'mr' : 'Resected - Malignant',
                            'br' : 'Resected - Benign',
                            'NA' : np.nan
                            },
                    
                    "Nodule Status (Nodule 5)" : {
                            'un' : 'Unknown',
                            'bc' : 'Benign (Ca++)',
                            'pc' : 'Prob Benign, prob Ca++',
                            're' : 'Resolved',
                            'rg' : 'Resolving',
                            'tn' : 'No Change, 2 yrs',
                            'pp' : 'PET - Positive',
                            'pn' : 'PET - Negative',
                            'pi' : 'PET - Indeterminate',
                            'ub' : 'Biopsy - Unknown',  
                            'bb' : 'Biopsy - Benign',
                            'mb' : 'Biopsy - Malignant',
                            'ab' : 'Biopsy - Atyp Bronch Prolif',
                            'om' : 'Biopsy - Metastatic',
                            'mr' : 'Resected - Malignant',
                            'br' : 'Resected - Benign',
                            'NA' : np.nan
                            },
                    
                    "Nodule Status (Additional Nodule)" : {
                            'un' : 'Unknown',
                            'bc' : 'Benign (Ca++)',
                            'pc' : 'Prob Benign, prob Ca++',
                            're' : 'Resolved',
                            'rg' : 'Resolving',
                            'tn' : 'No Change, 2 yrs',
                            'pp' : 'PET - Positive',
                            'pn' : 'PET - Negative',
                            'pi' : 'PET - Indeterminate',
                            'ub' : 'Biopsy - Unknown',  
                            'bb' : 'Biopsy - Benign',
                            'mb' : 'Biopsy - Malignant',
                            'ab' : 'Biopsy - Atyp Bronch Prolif',
                            'om' : 'Biopsy - Metastatic',
                            'mr' : 'Resected - Malignant',
                            'br' : 'Resected - Benign',
                            'NA' : np.nan
                            },
                    
                    "Action (Nodule 1)" : {
                            's' : 'Annual Repeat CT',
                            'f' : 'f/u CT',
                            'a' : 'Abx + f/u CT',
                            'e' : 'PET',
                            'c' : 'CT w Contrast',
                            'b' : 'CT-Guided Biopsy',
                            'p' : 'Bronchoscopy',
                            'v' : 'VAT',
                            'r' : 'Resection',
                            'NA' : np.nan
                            },
                    
                    "Action (Nodule 2)" : {
                            's' : 'Annual Repeat CT',
                            'f' : 'f/u CT',
                            'a' : 'Abx + f/u CT',
                            'e' : 'PET',
                            'c' : 'CT w Contrast',
                            'b' : 'CT-Guided Biopsy',
                            'p' : 'Bronchoscopy',
                            'v' : 'VAT',
                            'r' : 'Resection',
                            'NA' : np.nan
                            },
                    
                    "Action (Nodule 3)" : {
                            's' : 'Annual Repeat CT',
                            'f' : 'f/u CT',
                            'a' : 'Abx + f/u CT',
                            'e' : 'PET',
                            'c' : 'CT w Contrast',
                            'b' : 'CT-Guided Biopsy',
                            'p' : 'Bronchoscopy',
                            'v' : 'VAT',
                            'r' : 'Resection',
                            'NA' : np.nan
                            },
                    
                    "Action (Nodule 4)" : {
                            's' : 'Annual Repeat CT',
                            'f' : 'f/u CT',
                            'a' : 'Abx + f/u CT',
                            'e' : 'PET',
                            'c' : 'CT w Contrast',
                            'b' : 'CT-Guided Biopsy',
                            'p' : 'Bronchoscopy',
                            'v' : 'VAT',
                            'r' : 'Resection',
                            'NA' : np.nan
                            },
                    
                    "Action (Nodule 5)" : {
                            's' : 'Annual Repeat CT',
                            'f' : 'f/u CT',
                            'a' : 'Abx + f/u CT',
                            'e' : 'PET',
                            'c' : 'CT w Contrast',
                            'b' : 'CT-Guided Biopsy',
                            'p' : 'Bronchoscopy',
                            'v' : 'VAT',
                            'r' : 'Resection',
                            'NA' : np.nan
                            },
                    
                    "Action (Additional Nodule)" : {
                            's' : 'Annual Repeat CT',
                            'f' : 'f/u CT',
                            'a' : 'Abx + f/u CT',
                            'e' : 'PET',
                            'c' : 'CT w Contrast',
                            'b' : 'CT-Guided Biopsy',
                            'p' : 'Bronchoscopy',
                            'v' : 'VAT',
                            'r' : 'Resection',
                            'NA' : np.nan
                            },
                    
                    "Other Parenchymal Abnormalities" : {
                            'n' : 'No',
                            'y' : 'Yes',
                            'e' : np.nan
                            },
                    
                    "Emphysema n/v" : {
                            'e' : np.nan,
                            'NA' : np.nan
                            },
                    
                    "Emphysema" : {
                            'no' : 'None',
                            'mi' : 'Mild',
                            'mo' : 'Moderate',
                            'se' : 'Severe'
                            },
                    
                    "Cysts/Blebs/Bullae" : {
                            'n' : 'No',
                            'y' : 'Yes',
                            'e' : np.nan
                            },
                    
                    "Cysts/Blebs/Bullae RUL" : {
                            'rul' : 'RUL',
                            'NA' : np.nan
                            },
                    
                    "Cysts/Blebs/Bullae RML" : {
                            'rml' : 'RML',
                            'NA' : np.nan
                            },
                    
                    "Cysts/Blebs/Bullae RLL" : {
                            'rll' : 'RLL',
                            'NA' : np.nan
                            },
                    
                    "Cysts/Blebs/Bullae LUL" : {
                            'lul' : 'LUL',
                            'NA' : np.nan
                            },
                    
                    "Cysts/Blebs/Bullae LLL" : {
                            'lll' : 'LLL',
                            'NA' : np.nan
                            },
                    
                    "Small Airways Disease/Bronchiolectasis" : {
                            'n' : 'No',
                            'y' : 'Yes',
                            'e' : np.nan
                            },
                    
                    "Small Airways Disease/Bronchiolectasis RUL" : {
                            'rul' : 'RUL',
                            'NA' : np.nan
                            },
                    
                    "Small Airways Disease/Bronchiolectasis RML" : {
                            'rml' : 'RML',
                            'NA' : np.nan
                            },
                    
                    "Small Airways Disease/Bronchiolectasis RLL" : {
                            'rll' : 'RLL',
                            'NA' : np.nan
                            },
                    
                    "Small Airways Disease/Bronchiolectasis LUL" : {
                            'lul' : 'LUL',
                            'NA' : np.nan
                            },
                    
                    "Small Airways Disease/Bronchiolectasis LLL" : {
                            'lll' : 'LLL',
                            'NA' : np.nan
                            },
                    
                    "Bronchiectasis" : {
                            'n' : 'No',
                            'y' : 'Yes',
                            'e' : np.nan
                            },
                    
                    "Bronchiectasis RUL" : {
                            'rul' : 'RUL',
                            'NA' : np.nan
                            },
                    
                    "Bronchiectasis RML" : {
                            'rml' : 'RML',
                            'NA' : np.nan
                            },
                    
                    "Bronchiectasis RLL" : {
                            'rll' : 'RLL',
                            'NA' : np.nan
                            },
                    
                    "Bronchiectasis LUL" : {
                            'lul' : 'LUL',
                            'NA' : np.nan
                            },
                    
                    "Bronchiectasis LLL" : {
                            'lll' : 'LLL',
                            'NA' : np.nan
                            },
                    
                    "Interstitial lung disease" : {
                            'n' : 'No',
                            'y' : 'Yes',
                            'e' : np.nan
                            },
                    
                    "Interstitial lung disease RUL" : {
                            'rul' : 'RUL',
                            'NA' : np.nan
                            },
                    
                    "Interstitial lung disease RML" : {
                            'rml' : 'RML',
                            'NA' : np.nan
                            },
                    
                    "Interstitial lung disease RLL" : {
                            'rll' : 'RLL',
                            'NA' : np.nan
                            },
                    
                    "Interstitial lung disease LUL" : {
                            'lul' : 'LUL',
                            'NA' : np.nan
                            },
                    
                    "Interstitial lung disease LLL" : {
                            'lll' : 'LLL',
                            'NA' : np.nan
                            },
                    
                    "Honeycombing" : {
                            'n' : 'No',
                            'y' : 'Yes',
                            'e' : np.nan
                            },
                    
                    "Honeycombing RUL" : {
                            'rul' : 'RUL',
                            'NA' : np.nan
                            },
                    
                    "Honeycombing RML" : {
                            'rml' : 'RML',
                            'NA' : np.nan
                            },
                    
                    "Honeycombing RLL" : {
                            'rll' : 'RLL',
                            'NA' : np.nan
                            },
                    
                    "Honeycombing LUL" : {
                            'lul' : 'LUL',
                            'NA' : np.nan
                            },
                    
                    "Honeycombing LLL" : {
                            'lll' : 'LLL',
                            'NA' : np.nan
                            },
                    
                    "Regional or Diffuse Consolidation" : {
                            'n' : 'No',
                            'y' : 'Yes',
                            'e' : np.nan
                            },
                    
                    "Regional or Diffuse Consolidation RUL" : {
                            'rul' : 'RUL',
                            'NA' : np.nan
                            },
                    
                    "Regional or Diffuse Consolidation RML" : {
                            'rml' : 'RML',
                            'NA' : np.nan
                            },
                    
                    "Regional or Diffuse Consolidation RLL" : {
                            'rll' : 'RLL',
                            'NA' : np.nan
                            },
                    
                    "Regional or Diffuse Consolidation LUL" : {
                            'lul' : 'LUL',
                            'NA' : np.nan
                            },
                    
                    "Regional or Diffuse Consolidation LLL" : {
                            'lll' : 'LLL',
                            'NA' : np.nan
                            },
                    
                    "Scarring" : {
                            'n' : 'No',
                            'y' : 'Yes',
                            'e' : np.nan
                            },
                    
                    "Scarring RUL" : {
                            'rul' : 'RUL',
                            'NA' : np.nan
                            },
                    
                    "Scarring RML" : {
                            'rml' : 'RML',
                            'NA' : np.nan
                            },
                    
                    "Scarring RLL" : {
                            'rll' : 'RLL',
                            'NA' : np.nan
                            },
                    
                    "Scarring LUL" : {
                            'lul' : 'LUL',
                            'NA' : np.nan
                            },
                    
                    "Scarring LLL" : {
                            'lll' : 'LLL',
                            'NA' : np.nan
                            },
                    
                    "Rounded Atelectasis" : {
                            'n' : 'No',
                            'y' : 'Yes',
                            'e' : np.nan
                            },
                    
                    "Rounded Atelectasis RUL" : {
                            'rul' : 'RUL',
                            'NA' : np.nan
                            },
                    
                    "Rounded Atelectasis RML" : {
                            'rml' : 'RML',
                            'NA' : np.nan
                            },
                    
                    "Rounded Atelectasis RLL" : {
                            'rll' : 'RLL',
                            'NA' : np.nan
                            },
                    
                    "Rounded Atelectasis LUL" : {
                            'lul' : 'LUL',
                            'NA' : np.nan
                            },
                    
                    "Rounded Atelectasis LLL" : {
                            'lll' : 'LLL',
                            'NA' : np.nan
                            },
                    
                    "Other Atelectasis" : {
                            'n' : 'No',
                            'y' : 'Yes',
                            'e' : np.nan
                            },
                    
                    "Other Atelectasis RUL" : {
                            'rul' : 'RUL',
                            'NA' : np.nan
                            },
                    
                    "Other Atelectasis RML" : {
                            'rml' : 'RML',
                            'NA' : np.nan
                            },
                    
                    "Other Atelectasis RLL" : {
                            'rll' : 'RLL',
                            'NA' : np.nan
                            },
                    
                    "Other Atelectasis LUL" : {
                            'lul' : 'LUL',
                            'NA' : np.nan
                            },
                    
                    "Other Atelectasis LLL" : {
                            'lll' : 'LLL',
                            'NA' : np.nan
                            },
                    
                    "Bronchial Resection Margin" : {
                            'n' : 'NA',
                            'o' : 'Normal',
                            'y' : 'Abnormal',
                            'e' : np.nan
                            },
                    
                    "Bronchial Resection Margin Right" : {
                            'r' : 'Right'
                            },
                    
                    "Bronchial Resection Margin Left" : {
                            'l' : 'Left'
                            },
                    
                    "Pleural Effusion" : {
                            'e' : np.nan
                            },
                    
                    "Pleural Effusion Right" : {
                            'no' : 'None',
                            'sm' : 'Small',
                            'mo' : 'Moderate',
                            'lg' : 'Large',
                            'NA' : np.nan
                            },
                    
                    "Pleural Effusion Left" : {
                            'no' : 'None',
                            'sm' : 'Small',
                            'mo' : 'Moderate',
                            'lg' : 'Large',
                            'NA' : np.nan
                            },
                    
                    "Pleural Thickening/Fissural Plaques" : {
                            'n' : 'No',
                            'y' : 'Yes',
                            'e' : np.nan
                            },
                    
                    "Pleural Thickening/Fissural Plaques Right" : {
                            'r' : 'Right',
                            'NA' : np.nan
                            },
                    
                    "Pleural Thickening/Fissural Plaques Left" : {
                            'l' : 'Left',
                            'NA' : np.nan
                            },
                    
                    "Pleural Thickening/Fissural Plaques Calcification" : {
                            'c' : 'Calcification',
                            'NA' : np.nan
                            },
                    
                    "Pleural Tumor" : {
                            'n' : 'No',
                            'y' : 'Yes',
                            'e' : np.nan
                            },
                    
                    "Cardiac Abnormalities" : {
                            'e' : np.nan,
                            'NA' : np.nan
                            },
                    
                    "Coronary Calcification" : {
                            'no' : 'None',
                            'mi' : 'Minimal',
                            'mo' : 'Moderate',
                            'ex' : 'Extensive',
                            'NA' : np.nan
                            },
                    
                    "Coronary Calcification Left Main" : {
                            'no' : 'None',
                            'mi' : 'Minimal',
                            'mo' : 'Moderate',
                            'ex' : 'Extensive',
                            'NA' : np.nan
                            },
                    
                    "Coronary Calcification LAD" : {
                            'no' : 'None',
                            'mi' : 'Minimal',
                            'mo' : 'Moderate',
                            'ex' : 'Extensive',
                            'NA' : np.nan
                            },
                    
                    "Coronary Calcification Circumflex" : {
                            'no' : 'None',
                            'mi' : 'Minimal',
                            'mo' : 'Moderate',
                            'ex' : 'Extensive',
                            'NA' : np.nan
                            },
                    
                    "Coronary Calcification RCA" : {
                            'no' : 'None',
                            'mi' : 'Minimal',
                            'mo' : 'Moderate',
                            'ex' : 'Extensive',
                            'NA' : np.nan
                            },
                    
                    "Pericardial Effusion" : {
                            'e' : np.nan,
                            'NA' : np.nan
                            },
                    
                    "Pericardial Effusion Severity" : {
                            'no' : 'None',
                            'mi' : 'Minimal',
                            'mo' : 'Moderate',
                            'ex' : 'Extensive',
                            'NA' : np.nan
                            },
                    
                    "Thyroid" : {
                            'n' : 'No',
                            'y' : 'Yes',
                            'e' : np.nan
                            },
                    
                    "Thyroid Calcification" : {
                            'c' : 'Calcification',
                            'NA' : np.nan
                            },
                    
                    "Thyroid Cyst" : {
                            'y' : 'Cyst',
                            'NA' : np.nan
                            },
                    
                    "Thyroid Mass" : {
                            'm' : 'Mass',
                            'NA' : np.nan
                            },
                    
                    "Thyroid Other" : {
                            'o' : 'Other',
                            'NA' : np.nan
                            },
                    
                    "Thymus" : {
                            'n' : 'No',
                            'y' : 'Yes',
                            'e' : np.nan
                            },
                    
                    "Thymus Calcification" : {
                            'c' : 'Calcification',
                            'NA' : np.nan
                            },
                    
                    "Thymus Cyst" : {
                            'y' : 'Cyst',
                            'NA' : np.nan
                            },
                    
                    "Thymus Mass" : {
                            'm' : 'Mass',
                            'NA' : np.nan
                            },
                    
                    "Thymus Other" : {
                            'o' : 'Other',
                            'NA' : np.nan
                            },
                    
                    "Lymph Nodes Enlarged" : {
                            'n' : 'No',
                            'y' : 'Yes',
                            'e' : np.nan
                            }, 
                    
                    "Lymph Nodes Enlarged N1" : {
                            'NA' : np.nan
                            },
                    
                    "Lymph Nodes Enlarged N2R" : {
                            'NA' : np.nan
                            },
                    
                    "Lymph Nodes Enlarged N2L" : {
                            'N2L' : 'N2L (upper paratracheal)',
                            'NA' : np.nan
                            },
                    
                    "Lymph Nodes Enlarged N3" : {
                            'N3' : 'N3 (prevascular, retrotracheal)',
                            'NA' : np.nan
                            },
                    
                    "Lymph Nodes Enlarged N4R" : {
                            'NA' : np.nan
                            },
                    
                    "Lymph Nodes Enlarged N4L" : {
                            'N4L' : 'N4L (lower paratracheal)',
                            'NA' : np.nan
                            },
                    
                    "Lymph Nodes Enlarged N5" : {
                            'N5' : 'N5 (subaortic (A-P window))',
                            'NA' : np.nan
                            },
                    
                    "Lymph Nodes Enlarged N6" : {
                            'N6' : 'N6 (para-aortic)',
                            'NA' : np.nan
                            },
                    
                    "Lymph Nodes Enlarged N7" : {
                            'N7' : 'N7 (subcarinal)',
                            'NA' : np.nan
                            },
                    
                    "Lymph Nodes Enlarged N8" : {
                            'N8' : 'N8 (para-esophageal) (any size)',
                            'NA' : np.nan
                            },
                    
                    "Lymph Nodes Enlarged N9" : {
                            'N9' : 'N9 (pulmonary ligament)',
                            'NA' : np.nan
                            },
                    
                    "Lymph Nodes Enlarged N10R" : {
                            'NA' : np.nan
                            },
                    
                    "Lymph Nodes Enlarged N10L" : {
                            'N10L' : 'N10L (hilar)',
                            'NA' : np.nan
                            },
                    
                    "Lymph Nodes Calcified" : {
                            'n' : 'No',
                            'y' : 'Yes',
                            'e' : np.nan
                            },
                    
                    "Axillary lymph nodes" : {
                            'n' : 'No',
                            'y' : 'Yes',
                            'e' : np.nan
                            },
                    
                    "Axillary lymph nodes Right" : {
                            'r' : 'Right',
                            'NA' : np.nan
                            },
                    
                    "Axillary lymph nodes Left" : {
                            'l' : 'Left',
                            'NA' : np.nan
                            },
                    
                    "Other Vascular Abnormalities" : {
                            'n' : 'No',
                            'y' : 'Yes',
                            'e' : np.nan
                            },
                    
                    "Other Vascular Abnormalities Aorta" : {
                            'a' : 'Aorta',
                            'NA' : np.nan
                            },
                    
                    "Other Vascular Abnormalities Pulmonary Arteries" : {
                            'w' : 'Pulmonary Arteries',
                            'NA' : np.nan
                            },
                    
                    "Other Vascular Abnormalities Other" : {
                            'o' : 'Other',
                            'NA' : np.nan
                            },
                    
                    "Esophageal" : {
                            'n' : 'No',
                            'y' : 'Yes',
                            'e' : np.nan
                            },
                    
                    "Esophageal Air-fluid level" : {
                            'a' : 'Air-fluid level',
                            'NA' : np.nan
                            },
                    
                    "Esophageal Wall thickening" : {
                            'w' : 'Wall thickening',
                            'NA' : np.nan
                            },
                    
                    "Esophageal Mass" : {
                            'm' : 'Mass',
                            'NA' : np.nan
                            },
                    
                    "Esophageal Other" : {
                            'o' : 'Other',
                            'NA' : np.nan
                            },
                    
                    "Hiatal Hernia" : {
                            'n' : 'No',
                            'y' : 'Yes',
                            'e' : np.nan
                            },
                    
                    "Other Mediastinal Masses" : {
                            'n' : 'No',
                            'y' : 'Yes',
                            'e' : np.nan
                            },
                    
                    "Other Mediastinal Masses Calcification" : {
                            'c' : 'Calcification',
                            'NA' : np.nan
                            },
                    
                    "Other Mediastinal Masses Cyst" : {
                            'y' : 'Cyst',
                            'NA' : np.nan
                            },
                    
                    "Other Mediastinal Masses Mass" : {
                            'm' : 'Mass',
                            'NA' : np.nan
                            },
                    
                    "Other Mediastinal Masses Other" : {
                            'm' : 'Mass',
                            'NA' : np.nan
                            },
                    
                    "Breast Abnormalities" : {
                            'n' : 'No',
                            'y' : 'Yes',
                            'e' : np.nan
                            },
                    
                    "Right Breast Abnormalities" : {
                            'n' : 'No',
                            'y' : 'Yes',
                            'e' : np.nan
                            },
                    
                    "Right Breast Calcification" : {
                            'c' : 'Calcification',
                            'NA' : np.nan
                            },
                    
                    "Right Breast Cyst" : {
                            'y' : 'Cyst',
                            'NA' : np.nan
                            },
                    
                    "Right Breast Mass" : {
                            'm' : 'Mass',
                            'NA' : np.nan
                            },
                    
                    "Right Breast Other" : {
                            'o' : 'Other',
                            'NA' : np.nan
                            },
                    
                    "Left Breast Abnormalities" : {
                            'n' : 'No',
                            'y' : 'Yes',
                            'e' : np.nan
                            },
                    
                    "Left Breast Calcification" : {
                            'c' : 'Calcification',
                            'NA' : np.nan
                            },
                    
                    "Left Breast Cyst" : {
                            'y' : 'Cyst',
                            'NA' : np.nan
                            },
                    
                    "Left Breast Mass" : {
                            'm' : 'Mass',
                            'NA' : np.nan
                            },
                    
                    "Left Breast Other" : {
                            'o' : 'Other',
                            'NA' : np.nan
                            },
                    
                    "Gall Bladder Abnormalities" : {
                            'n' : 'No',
                            'y' : 'Yes',
                            'e' : np.nan
                            },
                    
                    "Gall Bladder Cholecystectomy" : {
                            'h' : 'Cholecystectomy',
                            'NA' : np.nan
                            },
                    
                    "Gall Bladder Stones" : {
                            's' : 'Stones',
                            'NA' : np.nan
                            },
                    
                    "Gall Bladder Sludge" : {
                            'l' : 'Sludge',
                            'NA' : np.nan
                            },
                    
                    "Gall Bladder Other" : {
                            'y' : 'Other',
                            'NA' : np.nan
                            },
                    
                    "Spleen Abnormalities" : {
                            'n' : 'No',
                            'y' : 'Yes',
                            'e' : np.nan
                            },
                    
                    "Spleen Calcification" : {
                            'y' : 'Calcification',
                            'NA' : np.nan
                            },
                    
                    "Spleen Cyst" : {
                            'y' : 'Cyst',
                            'NA' : np.nan
                            },
                    
                    "Spleen Mass" : {
                            'm' : 'Mass',
                            'NA' : np.nan
                            },
                    
                    "Spleen Other" : {
                            'y' : 'Other',
                            'NA' : np.nan
                            },
                    
                    "Liver Abnormalities" : {
                            'n' : 'No',
                            'y' : 'Yes',
                            'e' : np.nan
                            },
                    
                    "Liver Calcification" : {
                            'y' : 'Calcification',
                            'NA' : np.nan
                            },
                    
                    "Liver Cyst" : {
                            'y' : 'Cyst',
                            'NA' : np.nan
                            },
                    
                    "Liver Mass" : {
                            'm' : 'Mass',
                            'NA' : np.nan
                            },
                    
                    "Liver Other" : {
                            'y' : 'Other',
                            'NA' : np.nan
                            },
                    
                    "Pancreas Abnormalities" : {
                            'n' : 'No',
                            'y' : 'Yes',
                            'e' : np.nan
                            },
                    
                    "Pancreas Calcification": {
                            'y' : 'Calcification',
                            'NA' : np.nan
                            },
                    
                    "Pancreas Cyst" : {
                            'y' : 'Cyst',
                            'NA' : np.nan
                            },
                    
                    "Pancreas Mass" : {
                            'm' : 'Mass',
                            'NA' : np.nan
                            },
                    
                    "Pancreas Other" : {
                            'y' : 'Other',
                            'NA' : np.nan
                            },
                    
                    "Adrenals Abnormalities" : {
                            'n' : 'No',
                            'y' : 'Yes',
                            'e' : np.nan
                            },
                    
                    "Adrenals Calcification" : {
                            'y' : 'Calcification',
                            'NA' : np.nan
                            },
                    
                     "Adrenals Cyst" : {
                            'y' : 'Cyst',
                            'NA' : np.nan
                            },
                    
                    "Adrenals Mass" : {
                            'm' : 'Mass',
                            'NA' : np.nan
                            },
                    
                    "Adrenals Other" : {
                            'y' : 'Other',
                            'NA' : np.nan
                            },
                    
                    "Kidneys Abnormalities" : {
                            'n' : 'No',
                            'y' : 'Yes',
                            'e' : np.nan
                            },
                    
                    "Kidneys Calcification" : {
                            'y' : 'Calcification',
                            'NA' : np.nan
                            },
                    
                     "Kidneys Cyst" : {
                            'y' : 'Cyst',
                            'NA' : np.nan
                            },
                    
                    "Kidneys Mass" : {
                            'm' : 'Mass',
                            'NA' : np.nan
                            },
                    
                    "Kidneys Other" : {
                            'y' : 'Other',
                            'NA' : np.nan
                            },
                    
                    "Bone Abnormalities" : {
                            'n' : 'No',
                            'y' : 'Yes',
                            'e' : np.nan
                            },
                    
                    "Follow-up" : {
                            'rs' : 'Annual Repeat CT',
                            'dx' : 'f/u CT',
                            'af' : 'Abx + f/u CT',
                            'pe' : 'PET',
                            'cc' : 'CT w Contrast',
                            'fn' : 'CT-Guided Biopsy',
                            'br' : 'Bronchoscopy',
                            'va' : 'VAT',
                            'su' : 'Resection',
                            'NA' : np.nan
                            },
                    
                    "When" : {
                            "nw" : "Now",
                            "1m" : "1 Month",
                            "3m" : "3 Months",
                            "6m" : "6 Months",
                            "1y" : "1 Year",
                            "os" : "Other"
                            },
                    
                    "Follow-up Date" : None,
                    
                    "Special Attention CT" : {
                            'y' : 'Yes',
                            'NA' : np.nan
                            },
                    
                    "Impression Nodules" : {
                            'rs' : 'No evidence of nodules. Follow-up as recommended above.',
                            'ro' : 'Nodule(s) as described above. Consistent with old granulomatous disease. Follow-up as recommended above.',
                            'ru' : 'Nodule(s) unchanged, as described above. Follow-up as recommended above.',
                            'nf' : 'Nodule(s) as described above. Follow-up as recommended above.'
                            },
                    
                    "Other Findings" : {
                            'no' : 'No other abnormalities.', 
                            'oa' : 'Other abnormalities and suggested follow-up as described above.'
                            },                                                      
                       }   
        