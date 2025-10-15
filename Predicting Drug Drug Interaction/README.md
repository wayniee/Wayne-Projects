Drug–Drug Interaction (DDI) Prediction
*A comparative study of data-driven ML and graph/deep learning models (SSI-DDI, SSF-DDI) for predicting drug-drug interaction types and risks*

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue)]()
[![scikit-learn](https://img.shields.io/badge/ML-scikit--learn-black)]()
[![PyTorch](https://img.shields.io/badge/DL-PyTorch-red)]()

---

## Overview
This project predicts **drug–drug interactions** (DDIs) and analyzes trade-offs between **accuracy, interpretability, and computational cost** across three approaches:

1) **Data-Driven Models** (engineered features → classical ML)  
2) **SSI-DDI** — *Substructure–Substructure Interaction* (GNN + co-attention)  
3) **SSF-DDI** — sequence + structure features (CNN on SMILES + D-MPNN + GAT/SAGPooling)

We also tailor the dataset for **Singapore** (filter to locally approved drugs and chronic-disease classes), and evaluate models with **Top-k accuracy, AUC-ROC, AU-PRC**, and qualitative explainability

---

## Key Contributions
- Curated a **Singapore-relevant** DDI dataset (DrugBank + DDInter + NDF/HSA + ATC), yielding **33,067** high-relevance pairs
- Built a **data-driven baseline** with PCA features and six classic learners (XGBoost, CatBoost, RF, GBM, SVM, LR) 
- Reproduced and adapted **SSI-DDI** (binary interaction check) and **SSF-DDI** (multiclass interaction type)
- Benchmarked on **Top-1/Top-5** accuracy (multiclass) and **AUC-ROC/AU-PRC** (binary), plus run-time/compute considerations

---

## Data Sources (curated)
- **DrugBank 6.0** — DDI pairs, SMILES, structures  
- **DDInter 2.0** — severity labels  
- **Singapore NDF & HSA** — locally approved drugs  
- **WHO ATC Index** — therapeutic classes (CKD, hypertension, lipid disorder)  
Merging, de-duping, consistency checks, and filtering produce the final training/eval set used across models

---

## Methods

### 1) Data-Driven Models
- **Features:** molecular descriptors (MolWt, LogP, TPSA, HBD/HBA, rings, etc.) + functional groups → **PCA (13 PCs, >95% var)**
- **Models:** XGBoost, CatBoost, Random Forest, Gradient Boosting, SVM, Logistic Regression
- **Evaluation:** Top-1/Top-5 accuracy + precision/recall/F1; emphasis on **interpretability** (feature importance/SHAP)

### 2) SSI-DDI (Substructure–Substructure Interaction)
- **Representation:** SMILES → molecular graphs; atoms as nodes, bonds as edges
- **Backbone:** stacked **GAT** layers to extract substructures; **co-attention** to score substructure pairs; **binary** prediction per interaction type.  
- **Optimisation:** BCE loss with positive/negative pairs

### 3) SSF-DDI (Sequence + Structure Features)
- **Sequence arm:** SMILES → embedding → **1D CNN** layers
- **Structure arm:** **D-MPNN → GAT → SAGPooling** to keep salient substructures
- **Fusion:** concat sequence/structure features → **multiclass** classifier (interaction type)
- **Training:** Adam + scheduler, **early stopping**

---

## Results (from the report)

**Data-Driven (Random Forest best among classical):**  
- **Top-1:** 0.86 **Top-5:** 0.99  
Good for shortlist-style decision support where several interaction types may be clinically relevant. :contentReference[oaicite:6]{index=6}

**SSI-DDI (binary):**  
- **AUC-ROC ~0.94, AUPRC ~0.92**, val loss ≈ 0.34; strong discriminative power and generalisation for validating a proposed interaction

**SSF-DDI (multiclass):**  
- Early stopped ~epoch 26; train loss ↓ to ~0.18, val loss ~0.41; **AUC-ROC ~0.87, AUPRC ~0.78**, accuracy ~0.89 (multiclass is harder; compute-intensive)

> **Takeaway:** Classical ensembles (with engineered features) are strong baselines and very interpretable; **SSI-DDI** excels at *is this interaction valid?*; **SSF-DDI** integrates sequence+structure for multiclass typing but needs more compute/tuning

---
