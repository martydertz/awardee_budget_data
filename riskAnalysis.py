"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

os.chdir("...budget_data\\python")
print os.getcwd()
from budget_fns import *

budg = pd.read_csv("12-29-2015_Open_Awds_Budg_Data2.csv")
budg.columns =["awd_id","inst_id","awd_istr_code", "awd_eff_date","duns_id",
                 "perf_org_type_code", 
                 "tot_budg_dol", "tot_sr_dol",
                 "tot_pdoc_dol", "tot_oth_prof_dol", "tot_grad_dols", "tot_un_grad_dol",
                 "tot_sec_pers_dol", "tot_oth_pers_dol", "tot_frin_bnft_dol", "tot_equp_cst_dol",
                 "tot_dom_trav_dol", "tot_frgn_trav_dol", "tot_part_dol", "tot_matl_dol", "tot_pub_dol",
                 "tot_cnsl_dol", "tot_cptr_serv_dol", "tot_sub_ctr_dol", "tot_oth_drct_cst_dol",
                 "tot_idir_cst_dol", "tot_rsid_dol", "tot_smal_bus_fee_dol", "tot_cst_shar_dol",
                 "tot_part_sup_cst_stip_dol", "tot_part_supp_cst_trav_dol", "tot_part_sup_cst_subs_dol",
                 "tot_part_sup_cst_oth_dol"]
                 
budg["awd_eff_date"] = pd.to_datetime(budg["awd_eff_date"])
travel = ["tot_dom_trav_dol","tot_frgn_trav_dol"]
budg["tot_travel_dol"] = budg[travel].sum(axis=1)
# add column for sum of part_sup_cst
part_sup_cst =  ["tot_part_sup_cst_stip_dol", "tot_part_supp_cst_trav_dol", "tot_part_sup_cst_subs_dol",
                 "tot_part_sup_cst_oth_dol"]
budg["tot_part_sup_cst_dol"] = budg[part_sup_cst].sum(axis=1)
                  
budg = computePercentages(budg, "tot_budg_dol") 
risk_categories = ["cnsl_rsk_pts","travel_rsk_pts", "sub_awd_rsk_pts",
                   "part_sup_rsk_pts","equp_rsk_pts"]
                    
budg["cost_shr_rsk_pts"] = budg.apply(costShareRiskPoints, axis=1)  
budg["travel_rsk_pts"] = budg.apply(travelRiskPoints, axis=1)  
budg["sub_awd_rsk_pts"] = budg.apply(subAwardRiskPoints, axis=1)  
budg["part_sup_rsk_pts"] = budg.apply(partSupportRiskPoints, axis=1)  
budg["equp_rsk_pts"] = budg.apply(equipRiskPoints, axis=1)  
budg["tot_rsk_pts"] = budg[risk_categories].sum(axis=1)
budg["time_of_awd_rsk_pts"] = budg.apply(timeAwdRisk, axis=1)

fig = plt.figure(figsize=(5, 4))
ax = fig.add_subplot(1,1,1)
ax.set_title("Equipment Costs: Total (log) vs Percent of Budget")
ax.scatter(budg["perc_tot_equp_cst_dol"],budg["tot_equp_cst_dol"])
ax.set_yticks([2000.0,100000.0,500000.0,2000000.0,10000000.0])
#y_formatter = matplotlib.ticker.ScalarFormatter(useOffset=False)
#ax.yaxis.set_major_formatter(y_formatter)
ax.set_yscale("log")
ax.hlines([2000,100000,500000,2000000,10000000],xmin=0, xmax=1,
       colors=["black","green","palegreen","yellow","red"],
       linestyles='solid')
fig.canvas.draw()
from sklearn.cluster import KMeans
