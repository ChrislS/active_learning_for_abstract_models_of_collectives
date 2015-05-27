# active_learning_for_abstract_models_of_collectives
This repository contains the code reproducing the results
in the papers "Active Learning for Abstract Models of Collectives" [1] and 
"Active Learning for Efficient Sampling of Control Models of Collectives" [2], by Alexander Schiendorfer, Christoph Lassner, Gerrit Anders, Wolfgang Reif and Rainer Lienhart.

a) comparison_GPs_DFs.ipynb presents the results of two different active learning strategies using Gaussian Processes (GPs) 
   and Decision Forests (DFs) on a single AVPP dataset (costs50.csv) shown in [1] and [2]
b) integrated_active_learning_eval.ipynb presents the analysis of the effectiveness of DF-AL integrated into 
   a full simulation environment [2]
   
   
The full source code of the simulation environment used to produce the results in b) is found at 
https://github.com/Alexander-Schiendorfer/active-learning-collectives .
