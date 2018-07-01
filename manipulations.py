  #!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  4 16:48:37 2017

filename: manipulations.py

description: All data manipulations that are not part of the cleaning process

author: Timo Klingler
"""

import cleaner
import credentials

import pandas as pd
import datetime

df = cleaner.df

update = pd.read_csv(credentials.update)
update ["Last Name"] = update ["Last Name"].apply(lambda x: hash(x))
update ["First Name"] = update["First Name"].apply(lambda x: hash(x))

"""
Functions
"""

def simple_counter(df, column, cumsum = False):
    counter = df[[column]].groupby(df[column]).count()
    counter.rename(columns = {column : "Count"}, inplace = True)
    counter = counter.reset_index()

    if cumsum == True:
        counter["Cumulative Sum"] = pd.Series(counter["Count"].cumsum(),
                                          index = counter.index,
                                          name = "Cumulative Sum")
        return counter

    else:
        return counter

def describer(df):
    stats = df.describe()
    stats.drop("Count", axis = 1, inplace = True)

    cols = ["Additional Nodule", "Nodule 1", "Nodule 2", "Nodule 3", "Nodule 4", "Nodule 5"]
    stats.columns = cols

    index = ["count", "mean", "std", "min", "25%", "50%", "75%", "max"]
    stats.index = index

    stats = stats.set_index(stats.index).T
    stats = stats.reset_index()

    ncols = ["Nodule", "Count", "Mean", "Std", "Min", "25%", "50%", "75%", "Max"]
    stats.columns = ncols

    return stats.reindex(index = [1, 2, 3, 4, 5, 0])

"""
Baseline
"""

baseline_df = df[df["Type of Exam"] == "Baseline"]

# Date of Baseline CT

date_of_baseline_ct = simple_counter(baseline_df, "Date of Baseline CT", cumsum = True)

# Total Number of Nodules

bl_nod_non_calc_tot = simple_counter(baseline_df, "Total Number of Non-Calcified Nodules")
bl_nod_tot = simple_counter(baseline_df, "Total Number of Nodules")

bl_total_number_of_nodules = pd.concat([bl_nod_non_calc_tot, bl_nod_tot], axis = 0)

# Is it new?

bl_new_1 = simple_counter(baseline_df, "Is it new? (Nodule 1)")
bl_new_2 = simple_counter(baseline_df, "Is it new? (Nodule 2)")
bl_new_3 = simple_counter(baseline_df, "Is it new? (Nodule 3)")
bl_new_4 = simple_counter(baseline_df, "Is it new? (Nodule 4)")
bl_new_5 = simple_counter(baseline_df, "Is it new? (Nodule 5)")
bl_new_add = simple_counter(baseline_df, "Is it new? (Additional Nodule)")

bl_new_all = pd.concat([bl_new_1, bl_new_2, bl_new_3, bl_new_4, bl_new_5, bl_new_add], axis = 0)

# Endobronchial

bl_endo_1 = simple_counter(baseline_df, "Endobronchial? (Nodule 1)")
bl_endo_2 = simple_counter(baseline_df, "Endobronchial? (Nodule 2)")
bl_endo_3 = simple_counter(baseline_df, "Endobronchial? (Nodule 3)")
bl_endo_4 = simple_counter(baseline_df, "Endobronchial? (Nodule 4)")
bl_endo_5 = simple_counter(baseline_df, "Endobronchial? (Nodule 5)")
bl_endo_add = simple_counter(baseline_df, "Endobronchial? (Additional Nodule)")

bl_endo_all = pd.concat([bl_endo_1, bl_endo_2, bl_endo_3, bl_endo_4, bl_endo_5, bl_endo_add], axis = 0)

# Most Likely Location

bl_mll_1 = simple_counter(baseline_df, "Most Likely Location (Nodule 1)")
bl_mll_2 = simple_counter(baseline_df, "Most Likely Location (Nodule 2)")
bl_mll_3 = simple_counter(baseline_df, "Most Likely Location (Nodule 3)")
bl_mll_4 = simple_counter(baseline_df, "Most Likely Location (Nodule 4)")
bl_mll_5 = simple_counter(baseline_df, "Most Likely Location (Nodule 5)")
bl_mll_add = simple_counter(baseline_df, "Most Likely Location (Additional Nodule)")

bl_mll_all = pd.concat([bl_mll_1, bl_mll_2, bl_mll_3, bl_mll_4, bl_mll_5, bl_mll_add], axis = 0)

# Distance from the Costal Pleura

bl_dist_1 = simple_counter(baseline_df, "Distance from the costal pleura in mm (Nodule 1)")
bl_dist_2 = simple_counter(baseline_df, "Distance from the costal pleura in mm (Nodule 2)")
bl_dist_3 = simple_counter(baseline_df, "Distance from the costal pleura in mm (Nodule 3)")
bl_dist_4 = simple_counter(baseline_df, "Distance from the costal pleura in mm (Nodule 4)")
bl_dist_5 = simple_counter(baseline_df, "Distance from the costal pleura in mm (Nodule 5)")
bl_dist_add = simple_counter(baseline_df, "Distance from the costal pleura in mm (Additional Nodule)")

bl_dist_all = pd.concat([bl_dist_1, bl_dist_2, bl_dist_3, bl_dist_4, bl_dist_5, bl_dist_add], axis = 0)

# Nodule Length

bl_nodl_1 = simple_counter(baseline_df, "Length in mm (Nodule 1)")
bl_nodl_2 = simple_counter(baseline_df, "Length in mm (Nodule 2)")
bl_nodl_3 = simple_counter(baseline_df, "Length in mm (Nodule 3)")
bl_nodl_4 = simple_counter(baseline_df, "Length in mm (Nodule 4)")
bl_nodl_5 = simple_counter(baseline_df, "Length in mm (Nodule 5)")
bl_nodl_add = simple_counter(baseline_df, "Length in mm (Additional Nodule)")

bl_nodl_all = pd.concat([bl_nodl_1, bl_nodl_2, bl_nodl_3, bl_nodl_4, bl_nodl_5, bl_nodl_add], axis = 0)

# Maximum Width

bl_nodw_1 = simple_counter(baseline_df, "Maximum Width in mm (Nodule 1)")
bl_nodw_2 = simple_counter(baseline_df, "Maximum Width in mm (Nodule 2)")
bl_nodw_3 = simple_counter(baseline_df, "Maximum Width in mm (Nodule 3)")
bl_nodw_4 = simple_counter(baseline_df, "Maximum Width in mm (Nodule 4)")
bl_nodw_5 = simple_counter(baseline_df, "Maximum Width in mm (Nodule 5)")
bl_nodw_add = simple_counter(baseline_df, "Maximum Width in mm (Additional Nodule)")

bl_nodw_all = pd.concat([bl_nodw_1, bl_nodw_2, bl_nodw_3, bl_nodw_4, bl_nodw_5, bl_nodw_add], axis = 0)

# Nodule Consistency

bl_nc_1 = simple_counter(baseline_df, "Nodule Consistency (Nodule 1)")
bl_nc_2 = simple_counter(baseline_df, "Nodule Consistency (Nodule 2)")
bl_nc_3 = simple_counter(baseline_df, "Nodule Consistency (Nodule 3)")
bl_nc_4 = simple_counter(baseline_df, "Nodule Consistency (Nodule 4)")
bl_nc_5 = simple_counter(baseline_df, "Nodule Consistency (Nodule 5)")
bl_nc_add = simple_counter(baseline_df, "Nodule Consistency (Additional Nodule)")

bl_nc_all = pd.concat([bl_nc_1, bl_nc_2, bl_nc_3, bl_nc_4, bl_nc_5, bl_nc_add], axis = 0)

# Smooth Edges

bl_sme_1 = simple_counter(baseline_df, "Smooth Edges (Nodule 1)")
bl_sme_2 = simple_counter(baseline_df, "Smooth Edges (Nodule 2)")
bl_sme_3 = simple_counter(baseline_df, "Smooth Edges (Nodule 3)")
bl_sme_4 = simple_counter(baseline_df, "Smooth Edges (Nodule 4)")
bl_sme_5 = simple_counter(baseline_df, "Smooth Edges (Nodule 5)")
bl_sme_add = simple_counter(baseline_df, "Smooth Edges (Additional Nodule)")

bl_sme_all = pd.concat([bl_sme_1, bl_sme_2, bl_sme_3, bl_sme_4, bl_sme_5, bl_sme_add], axis = 0)

# Calcifications c/w Benignity

bl_cab_1 = simple_counter(baseline_df, "Calcifications c/w Benignity (Nodule 1)")
bl_cab_2 = simple_counter(baseline_df, "Calcifications c/w Benignity (Nodule 2)")
bl_cab_3 = simple_counter(baseline_df, "Calcifications c/w Benignity (Nodule 3)")
bl_cab_4 = simple_counter(baseline_df, "Calcifications c/w Benignity (Nodule 4)")
bl_cab_5 = simple_counter(baseline_df, "Calcifications c/w Benignity (Nodule 5)")
bl_cab_add = simple_counter(baseline_df, "Calcifications c/w Benignity (Additional Nodule)")

bl_cab_all = pd.concat([bl_cab_1, bl_cab_2, bl_cab_3, bl_cab_4, bl_cab_5, bl_cab_add], axis = 0)

# Spiculations/ Pleural Tags

bl_spic_1 = simple_counter(baseline_df, "Spiculations /Pleural Tags (Nodule 1)")
bl_spic_2 = simple_counter(baseline_df, "Spiculations /Pleural Tags (Nodule 2)")
bl_spic_3 = simple_counter(baseline_df, "Spiculations /Pleural Tags (Nodule 3)")
bl_spic_4 = simple_counter(baseline_df, "Spiculations /Pleural Tags (Nodule 4)")
bl_spic_5 = simple_counter(baseline_df, "Spiculations /Pleural Tags (Nodule 5)")
bl_spic_add = simple_counter(baseline_df, "Spiculations /Pleural Tags (Additional Nodule)")

bl_spic_all = pd.concat([bl_spic_1, bl_spic_2, bl_spic_3, bl_spic_4, bl_spic_5, bl_spic_add], axis = 0)

# Parenchymal Abnormality

bl_para_1 = simple_counter(baseline_df,"Parenchymal Abnormality within 1 cm (Nodule 1)")
bl_para_2 = simple_counter(baseline_df,"Parenchymal Abnormality within 1 cm (Nodule 2)")
bl_para_3 = simple_counter(baseline_df,"Parenchymal Abnormality within 1 cm (Nodule 3)")
bl_para_4 = simple_counter(baseline_df,"Parenchymal Abnormality within 1 cm (Nodule 4)")
bl_para_5 = simple_counter(baseline_df,"Parenchymal Abnormality within 1 cm (Nodule 5)")
bl_para_add = simple_counter(baseline_df,"Parenchymal Abnormality within 1 cm (Additional Nodule)")

bl_para_all = pd.concat([bl_para_1, bl_para_2, bl_para_3, bl_para_4, bl_para_5, bl_para_add], axis = 0)

# Nodule Status

bl_nods_1 = simple_counter(baseline_df, "Nodule Status (Nodule 1)")
bl_nods_2 = simple_counter(baseline_df, "Nodule Status (Nodule 2)")
bl_nods_3 = simple_counter(baseline_df, "Nodule Status (Nodule 3)")
bl_nods_4 = simple_counter(baseline_df, "Nodule Status (Nodule 4)")
bl_nods_5 = simple_counter(baseline_df, "Nodule Status (Nodule 5)")
bl_nods_add = simple_counter(baseline_df, "Nodule Status (Additional Nodule)")

bl_nods_all = pd.concat([bl_nods_1, bl_nods_2, bl_nods_3, bl_nods_4, bl_nods_5, bl_nods_add], axis = 0)

# Action

bl_act_1 = simple_counter(baseline_df, "Action (Nodule 1)")
bl_act_2 = simple_counter(baseline_df, "Action (Nodule 2)")
bl_act_3 = simple_counter(baseline_df, "Action (Nodule 3)")
bl_act_4 = simple_counter(baseline_df, "Action (Nodule 4)")
bl_act_5 = simple_counter(baseline_df, "Action (Nodule 5)")
bl_act_add = simple_counter(baseline_df, "Action (Additional Nodule)")

bl_act_all = pd.concat([bl_act_1, bl_act_2, bl_act_3, bl_act_4, bl_act_5, bl_act_add], axis = 0)

# Cysts/Blebs/Bullae

bl_cbb_1 = simple_counter(baseline_df, "Cysts/Blebs/Bullae RUL")
bl_cbb_2 = simple_counter(baseline_df, "Cysts/Blebs/Bullae RML")
bl_cbb_3 = simple_counter(baseline_df, "Cysts/Blebs/Bullae RLL")
bl_cbb_4 = simple_counter(baseline_df, "Cysts/Blebs/Bullae LUL")
bl_cbb_5 = simple_counter(baseline_df, "Cysts/Blebs/Bullae LLL")

bl_cbb_all = pd.concat([bl_cbb_1, bl_cbb_2, bl_cbb_3, bl_cbb_4, bl_cbb_5], axis = 0)

# Small Airways Disease/ Bronchiolectasis

bl_sadb_1 = simple_counter(baseline_df, "Small Airways Disease/Bronchiolectasis RUL")
bl_sadb_2 = simple_counter(baseline_df, "Small Airways Disease/Bronchiolectasis RML")
bl_sadb_3 = simple_counter(baseline_df, "Small Airways Disease/Bronchiolectasis RLL")
bl_sadb_4 = simple_counter(baseline_df, "Small Airways Disease/Bronchiolectasis LUL")
bl_sadb_5 = simple_counter(baseline_df, "Small Airways Disease/Bronchiolectasis LLL")

bl_sadb_all = pd.concat([bl_sadb_1, bl_sadb_2, bl_sadb_3, bl_sadb_4, bl_sadb_5], axis = 0)

# Bronchiectasis

bl_bron_1 = simple_counter(baseline_df, "Bronchiectasis RUL")
bl_bron_2 = simple_counter(baseline_df, "Bronchiectasis RML")
bl_bron_3 = simple_counter(baseline_df, "Bronchiectasis RLL")
bl_bron_4 = simple_counter(baseline_df, "Bronchiectasis LUL")
bl_bron_5 = simple_counter(baseline_df, "Bronchiectasis LLL")

bl_bron_all = pd.concat([bl_bron_1, bl_bron_2, bl_bron_3, bl_bron_4, bl_bron_5], axis = 0)

# Interstitial Lung Disease

bl_ild_1 = simple_counter(baseline_df, "Interstitial lung disease RUL")
bl_ild_2 = simple_counter(baseline_df, "Interstitial lung disease RML")
bl_ild_3 = simple_counter(baseline_df, "Interstitial lung disease RLL")
bl_ild_4 = simple_counter(baseline_df, "Interstitial lung disease LUL")
bl_ild_5 = simple_counter(baseline_df, "Interstitial lung disease LLL")

bl_ild_all = pd.concat([bl_ild_1, bl_ild_2, bl_ild_3, bl_ild_4, bl_ild_5], axis = 0)

# Honeycombing

bl_hon_1 = simple_counter(baseline_df, "Honeycombing RUL")
bl_hon_2 = simple_counter(baseline_df, "Honeycombing RML")
bl_hon_3 = simple_counter(baseline_df, "Honeycombing RLL")
bl_hon_4 = simple_counter(baseline_df, "Honeycombing LUL")
bl_hon_5 = simple_counter(baseline_df, "Honeycombing LLL")

bl_hon_all = pd.concat([bl_hon_1, bl_hon_2, bl_hon_3, bl_hon_4, bl_hon_5], axis = 0)

# Regional or Diffuse Consolidation

bl_rdc_1 = simple_counter(baseline_df, "Regional or Diffuse Consolidation RUL")
bl_rdc_2 = simple_counter(baseline_df, "Regional or Diffuse Consolidation RML")
bl_rdc_3 = simple_counter(baseline_df, "Regional or Diffuse Consolidation RLL")
bl_rdc_4 = simple_counter(baseline_df, "Regional or Diffuse Consolidation LUL")
bl_rdc_5 = simple_counter(baseline_df, "Regional or Diffuse Consolidation LLL")

bl_rdc_all = pd.concat([bl_rdc_1, bl_rdc_2, bl_rdc_3, bl_rdc_4, bl_rdc_5], axis = 0)

# Scarring

bl_scar_1 = simple_counter(baseline_df, "Scarring RUL")
bl_scar_2 = simple_counter(baseline_df, "Scarring RML")
bl_scar_3 = simple_counter(baseline_df, "Scarring RLL")
bl_scar_4 = simple_counter(baseline_df, "Scarring LUL")
bl_scar_5 = simple_counter(baseline_df, "Scarring LLL")

bl_scar_all = pd.concat([bl_scar_1, bl_scar_2, bl_scar_3, bl_scar_4, bl_scar_5], axis = 0)

# Rounded Atelectasis

bl_rat_1 = simple_counter(baseline_df, "Rounded Atelectasis RUL")
bl_rat_2 = simple_counter(baseline_df, "Rounded Atelectasis RML")
bl_rat_3 = simple_counter(baseline_df, "Rounded Atelectasis RLL")
bl_rat_4 = simple_counter(baseline_df, "Rounded Atelectasis LUL")
bl_rat_5 = simple_counter(baseline_df, "Rounded Atelectasis LLL")

bl_rat_all = pd.concat([bl_rat_1, bl_rat_2, bl_rat_3, bl_rat_4, bl_rat_5], axis = 0)

# Other Atelectasis

bl_oat_1 = simple_counter(baseline_df, "Other Atelectasis RUL")
bl_oat_2 = simple_counter(baseline_df, "Other Atelectasis RML")
bl_oat_3 = simple_counter(baseline_df, "Other Atelectasis RLL")
bl_oat_4 = simple_counter(baseline_df, "Other Atelectasis LUL")
bl_oat_5 = simple_counter(baseline_df, "Other Atelectasis LLL")

bl_oat_all = pd.concat([bl_oat_1, bl_oat_2, bl_oat_3, bl_oat_4, bl_oat_5])

# Bronchial Resection Margin

bl_brm_1 = simple_counter(baseline_df, "Bronchial Resection Margin")
bl_brm_2 = simple_counter(baseline_df, "Bronchial Resection Margin Right")
bl_brm_3 = simple_counter(baseline_df, "Bronchial Resection Margin Left")

bl_brm_all = pd.concat([bl_brm_1, bl_brm_2, bl_brm_3], axis = 0)

# Pleural Thickening/ Fissural Plaques

bl_ptf_1 = simple_counter(baseline_df, "Pleural Thickening/Fissural Plaques Right")
bl_ptf_2 = simple_counter(baseline_df, "Pleural Thickening/Fissural Plaques Left")
bl_ptf_3 = simple_counter(baseline_df, "Pleural Thickening/Fissural Plaques Calcification")

bl_ptf_all = pd.concat([bl_ptf_1, bl_ptf_2, bl_ptf_3], axis = 0)

# Coronary Calcification

bl_cca_1 = simple_counter(baseline_df, "Coronary Calcification Left Main")
bl_cca_2 = simple_counter(baseline_df, "Coronary Calcification LAD")
bl_cca_3 = simple_counter(baseline_df, "Coronary Calcification Circumflex")
bl_cca_4 = simple_counter(baseline_df, "Coronary Calcification RCA")

bl_cca_all = pd.concat([bl_cca_1, bl_cca_2, bl_cca_3, bl_cca_4], axis = 0)

# Visual CAC Score

bl_vcac_all = simple_counter(baseline_df, "Visual CAC Score")

# Thyroid Abnormalities

bl_thyr_1 = simple_counter(baseline_df, "Thyroid Calcification")
bl_thyr_2 = simple_counter(baseline_df, "Thyroid Cyst")
bl_thyr_3 = simple_counter(baseline_df, "Thyroid Mass")
bl_thyr_4 = simple_counter(baseline_df, "Thyroid Other")

bl_thyr_all = pd.concat([bl_thyr_1, bl_thyr_2, bl_thyr_3, bl_thyr_4], axis = 0)

# Lymph Nodes Enlarged

bl_lnod_1 = simple_counter(baseline_df, "Lymph Nodes Enlarged N1")
bl_lnod_2 = simple_counter(baseline_df, "Lymph Nodes Enlarged N2R")
bl_lnod_3 = simple_counter(baseline_df, "Lymph Nodes Enlarged N2L")
bl_lnod_4 = simple_counter(baseline_df, "Lymph Nodes Enlarged N3")
bl_lnod_5 = simple_counter(baseline_df, "Lymph Nodes Enlarged N4R")
bl_lnod_6 = simple_counter(baseline_df, "Lymph Nodes Enlarged N4L")
bl_lnod_7 = simple_counter(baseline_df, "Lymph Nodes Enlarged N5")
bl_lnod_8 = simple_counter(baseline_df, "Lymph Nodes Enlarged N6")
bl_lnod_9 = simple_counter(baseline_df, "Lymph Nodes Enlarged N7")
bl_lnod_10 = simple_counter(baseline_df, "Lymph Nodes Enlarged N8")
bl_lnod_11 = simple_counter(baseline_df, "Lymph Nodes Enlarged N9")
bl_lnod_12 = simple_counter(baseline_df, "Lymph Nodes Enlarged N10R")
bl_lnod_13 = simple_counter(baseline_df, "Lymph Nodes Enlarged N10L")

bl_lnod_all = pd.concat([bl_lnod_1, bl_lnod_2, bl_lnod_3, bl_lnod_4,
                         bl_lnod_5, bl_lnod_6, bl_lnod_7,
                         bl_lnod_8, bl_lnod_9, bl_lnod_10,
                         bl_lnod_11, bl_lnod_12, bl_lnod_13], axis = 0)

# Right Breast Abnormalities

bl_rba_1 = simple_counter(baseline_df, "Right Breast Calcification")
bl_rba_2 = simple_counter(baseline_df, "Right Breast Cyst")
bl_rba_3 = simple_counter(baseline_df, "Right Breast Mass")
bl_rba_4 = simple_counter(baseline_df, "Right Breast Other")

bl_rba_all = pd.concat([bl_rba_1, bl_rba_2, bl_rba_3, bl_rba_4], axis = 0)

# Left Breast Abnormalities

bl_lba_1 = simple_counter(baseline_df, "Left Breast Calcification")
bl_lba_2 = simple_counter(baseline_df, "Left Breast Cyst")
bl_lba_3 = simple_counter(baseline_df, "Left Breast Mass")
bl_lba_4 = simple_counter(baseline_df, "Left Breast Other")

bl_lba_all = pd.concat([bl_lba_1, bl_lba_2, bl_lba_3, bl_lba_4], axis = 0)

# Gall Bladder Abnormalities

bl_gba_1 = simple_counter(baseline_df, "Gall Bladder Cholecystectomy")
bl_gba_2 = simple_counter(baseline_df, "Gall Bladder Stones")
bl_gba_3 = simple_counter(baseline_df, "Gall Bladder Sludge")
bl_gba_4 = simple_counter(baseline_df, "Gall Bladder Other")

bl_gba_all = pd.concat([bl_gba_1, bl_gba_2, bl_gba_3, bl_gba_4], axis = 0)

# Spleen Abnormalities

bl_spa_1 = simple_counter(baseline_df, "Spleen Calcification")
bl_spa_2 = simple_counter(baseline_df, "Spleen Cyst")
bl_spa_3 = simple_counter(baseline_df, "Spleen Mass")
bl_spa_4 = simple_counter(baseline_df, "Spleen Other")

bl_spa_all = pd.concat([bl_spa_1, bl_spa_2, bl_spa_3, bl_spa_4], axis = 0)

# Liver Abnormalities

bl_lia_1 = simple_counter(baseline_df, "Liver Calcification")
bl_lia_2 = simple_counter(baseline_df, "Liver Cyst")
bl_lia_3 = simple_counter(baseline_df, "Liver Mass")
bl_lia_4 = simple_counter(baseline_df, "Liver Other")

bl_lia_all = pd.concat([bl_lia_1, bl_lia_2, bl_lia_3, bl_lia_4], axis = 0)

# Pancreas Abnormalities

bl_paa_1 = simple_counter(baseline_df, "Pancreas Calcification")
bl_paa_2 = simple_counter(baseline_df, "Pancreas Cyst")
bl_paa_3 = simple_counter(baseline_df, "Pancreas Mass")
bl_paa_4 = simple_counter(baseline_df, "Pancreas Other")

bl_paa_all = pd.concat([bl_paa_1, bl_paa_2, bl_paa_3, bl_paa_4], axis = 0)

# Adrenals Abnormalities

bl_ada_1 = simple_counter(baseline_df, "Adrenals Calcification")
bl_ada_2 = simple_counter(baseline_df, "Adrenals Cyst")
bl_ada_3 = simple_counter(baseline_df, "Adrenals Mass")
bl_ada_4 = simple_counter(baseline_df, "Adrenals Other")

bl_ada_all = pd.concat([bl_ada_1, bl_ada_2, bl_ada_3, bl_ada_4], axis = 0)

# Kidneys Abnormalities

bl_kia_1 = simple_counter(baseline_df, "Kidneys Calcification")
bl_kia_2 = simple_counter(baseline_df, "Kidneys Cyst")
bl_kia_3 = simple_counter(baseline_df, "Kidneys Mass")
bl_kia_4 = simple_counter(baseline_df, "Kidneys Other")

bl_kia_all = pd.concat([bl_kia_1, bl_kia_2, bl_kia_3, bl_kia_4], axis = 0)

# Follow-up

bl_fou_all = simple_counter(baseline_df, "Follow-up")

# When

bl_when_all = simple_counter(baseline_df, "When")

# Follow-up Date

bl_fod_all = df[["Study ID", "Last Name", "First Name", "Follow-up Date"]]
bl_fod_all = bl_fod_all[bl_fod_all["Follow-up Date"] > datetime.datetime.now()]
bl_fod_all = bl_fod_all.sort_values("Follow-up Date")

# Impression Nodule

bl_inod_all = simple_counter(baseline_df, "Impression Nodules")

# CT Evaluations

bl_cte_all = update
bl_cte_all = bl_cte_all.drop(["Unnamed: 0"], axis = 1)
bl_cte_all = bl_cte_all.sort_values(["CT Evaluation"], ascending = False)

"""
Panels
"""

pan_ct = bl_cte_all[["Study ID", "Last Name", "First Name", "CT Evaluation"]]
pan_fod = bl_fod_all

"""
Statistics
"""

# Distance from the Costal Pleura

bl_stat_dist = describer(bl_dist_all)

# Nodule Length

bl_stat_nodl = describer(bl_nodl_all)

# Maximum Width

bl_stat_nodw = describer(bl_nodw_all)
