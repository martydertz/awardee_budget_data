# -*- coding: utf-8 -*-
"""
Budget

@author: mdertz
"""

def computePercentages(dframe,totalColName):
    """takes budget df and column with total returns df with
    percentage of total column for each numeric column"""
    for column in dframe:
        if dframe[column].dtype == "int64" and column != totalColName:
            n = "perc_"+str(column)
            dframe[n] = dframe[column]/dframe[totalColName]
            
    return dframe


def costShareRiskPoints(row):
    if row["tot_cst_shar_dol"] == 0:
        return 0
    elif row["tot_cst_shar_dol"] <= 100000:
        return 1
    elif row["tot_cst_shar_dol"] > 100000 and row["tot_cst_shar_dol"] <= 500000:
        return 2
    elif row["tot_cst_shar_dol"] > 500000 and row["tot_cst_shar_dol"] <= 2000000:
        return 3
    elif row["tot_cst_shar_dol"] > 2000000 and row["tot_cst_shar_dol"] <= 5000000:
        return 4
    else:
        return 5  
        
def travelRiskPoints(row):
    if row["tot_travel_dol"] == 0:
        return 0
    elif row["tot_travel_dol"] <= 100000:
        return 1
    elif row["tot_travel_dol"] > 100000 and row["tot_travel_dol"] <= 500000:
        return 2
    elif row["tot_travel_dol"] > 500000 and row["tot_travel_dol"] <= 2000000:
        return 3
    elif row["tot_travel_dol"] > 2000000 and row["tot_travel_dol"] <= 5000000:
        return 4
    else:
        return 5
        
def cnslRiskPoints(row):
    if row["tot_cnsl_dol"] == 0:
        return 0
    elif row["tot_cnsl_dol"] <= 100000:
        return 1
    elif row["tot_cnsl_dol"] > 100000 and row["tot_cnsl_dol"] <= 500000:
        return 2
    elif row["tot_cnsl_dol"] > 500000 and row["tot_cnsl_dol"] <= 2000000:
        return 3
    elif row["tot_cnsl_dol"] > 2000000 and row["tot_cnsl_dol"] <= 5000000:
        return 4
    else:
        return 5
        
def subAwardRiskPoints(row):
    if row["tot_sub_ctr_dol"] == 0:
        return 0
    elif row["tot_sub_ctr_dol"] <= 100000:
        return 1
    elif row["tot_sub_ctr_dol"] > 100000 and row["tot_sub_ctr_dol"] <= 500000:
        return 2
    elif row["tot_sub_ctr_dol"] > 500000 and row["tot_sub_ctr_dol"] <= 2000000:
        return 3
    elif row["tot_sub_ctr_dol"] > 2000000 and row["tot_sub_ctr_dol"] <= 5000000:
        return 4
    else:
        return 5  

def partSupportRiskPoints(row):
    if row["tot_part_sup_cst_dol"] == 0:
        return 0
    elif row["tot_part_sup_cst_dol"] <= 50000:
        return 1
    elif row["tot_part_sup_cst_dol"] > 50000 and row["tot_part_sup_cst_dol"] <= 200000:
        return 2
    elif row["tot_part_sup_cst_dol"] > 200000 and row["tot_part_sup_cst_dol"] <= 300000:
        return 3
    elif row["tot_part_sup_cst_dol"] > 300000 and row["tot_part_sup_cst_dol"] <= 500000:
        return 4
    else:
        return 5
        
def equipRiskPoints(row):
    if row["tot_equp_cst_dol"] <= 20000:
        return 0
    elif row["tot_equp_cst_dol"] > 20000 and row["tot_equp_cst_dol"] <= 100000:
        return 1
    elif row["tot_equp_cst_dol"] > 100000 and row["tot_equp_cst_dol"] <= 500000:
        return 2
    elif row["tot_equp_cst_dol"] > 500000 and row["tot_equp_cst_dol"] <= 2000000:
        return 3
    elif row["tot_equp_cst_dol"] > 2000000 and row["tot_equp_cst_dol"] <= 10000000:
        return 4
    else:
        return 5

def timeAwdRisk(row):
    if row["awd_eff_date"].year == 2015 and row["awd_eff_date"].month in [8,9]:
        return 5
    else:
        return 0
    
