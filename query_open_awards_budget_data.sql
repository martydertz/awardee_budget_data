SELECT   DISTINCT(awd.awd_id), awd.inst_id, awd.awd_istr_code, awd.awd_eff_date, prop.dd_rcom_date,
inst.trbl_col_flag, inst.inst_name, inst.duns_id, inst.perf_org_type_code, inst.perf_org_code, 

SUM(bd.budg_splt_tot_dol) AS tot_budg_dol, SUM(bd.sr_tot_grnt_dol) AS tot_sr_dol,
SUM(bd.pdoc_grnt_dol) AS tot_pdoc_dol,SUM(bd.oth_prof_grnt_dol) AS tot_oth_prof_dol, 
SUM(bd.grad_grnt_dol) AS tot_grad_dols, SUM(bd.un_grad_grnt_dol) AS tot_un_grad_dol, 
SUM(bd.sec_pers_grnt_dol) AS tot_sec_pers_dol, SUM(bd.oth_pers_grnt_dol) AS tot_oth_pers_dol, 
SUM(bd.frin_bnft_dol) AS tot_frin_bnft_dol, SUM(bd.equp_cst_dol) AS tot_equp_cst_dol, 
SUM(bd.dom_trav_dol) AS tot_dom_trav_dols, SUM(bd.frgn_trav_dol) AS tot_frgn_trav_dol,
SUM(bd.part_dol) AS tot_part_dol, SUM(bd.matl_dol) tot_matl_dol, 
SUM(bd.pub_dol) AS tot_pub_dol, SUM(bd.cnsl_dol) AS tot_cnsl_dol, 
SUM(bd.cptr_serv_dol) AS tot_cptr_serv_dol, SUM(bd.sub_ctr_dol) AS tot_sub_ctr_dol,
SUM(bd.oth_drct_cst_dol) AS tot_oth_drct_cst_dol, SUM(bd.idir_cst_dol) AS tot_idir_cst_dol, 
SUM(bd.rsid_dol) AS tot_rsid_dol, SUM(bd.smal_bus_fee_dol) AS tot_smal_bus_fee_dol, 
SUM(bd.cst_shar_dol) AS tot_cst_shar_dol, SUM(bd.part_supp_cst_stip_dol) AS tot_part_sup_cst_stip_dol, 
SUM(bd.part_supp_cst_trav_dol) AS tot_part_supp_cst_trav_dol,SUM(bd.part_supp_cst_subs_dol) AS tot_part_sup_cst_subs_dol, 
SUM(bd.part_supp_cst_oth_dol) AS tot_part_sup_cst_oth_dol

FROM (((csd.budg_splt bd JOIN csd.awd awd ON bd.awd_id = awd.awd_id) 
       JOIN csd.inst inst ON inst.inst_id = awd.inst_id) 
      JOIN csd.prop prop ON prop.prop_id = awd.last_prop_id)

WHERE awd.awd_stts_code = '80' OR awd.awd_stts_code = '82'

GROUP BY awd.awd_id , awd.inst_id, awd.awd_istr_code, awd.awd_eff_date, prop.dd_rcom_date, 
inst.trbl_col_flag, inst.inst_name, inst.duns_id, inst.perf_org_type_code, inst.perf_org_code

ORDER BY tot_budg_dol DESC
