# Predictive Analysis of Credit Risk

A reproducible ML pipeline to predict **credit card approval** outcomes, surface **feature importance**, and balance **risk vs. inclusion** for financial decision-making

---

## Objectives
- **Predict** approve/reject outcomes for credit applications
- **Explain** which applicant features drive decisions (global & local)
- **Optimise thresholds** to minimise costly false approvals while preserving access to credit
- **Evaluate fairness** and calibration to support responsible use

---

## Data

We use the **Credit Card Approval Prediction** dataset (Kaggle), which has **two linked tables**:  
- **Application Record** — 438,557 rows × 18 features (demographics & finances)
- **Credit Record** — 1,048,575 rows × 3 features (monthly status/overdue)

**Label (target):**  
- **Reject (bad client)** if predicted loan status is **≥ 90 days past due**.  
- **Approve (good client)** if **< 90 days past due**.  
This mirrors common lender practice where 90+ DPD signifies **serious delinquency**. 

**Why this matters:** the work balances lender risk, customer access, and transparency in approvals

---

## Methodology

### 1) EDA & Data Quality
- Explore distributions, outliers, missingness, and potential **leakage**
- Sanity-check joins by unique client IDs and time spans
- Visualise correlations and category cardinalities (group rare levels)

### 2) Preprocessing
- **Join** on client ID; **deduplicate** records
- **Impute** missing values (median for numeric, most-frequent/“Unknown” for categorical)
- **Encode** categoricals (one-hot; target encoding tried under CV safeguards)
- **Scale** numeric features (Standard/Robust scaler where models need it)
- **Split** data **80/20** (stratified)

> **Class imbalance:** Fit re-sampling (e.g., **SMOTE/SMOTE-NC**) **inside CV on the training folds only** to prevent leakage

### 3) Models
1. **Logistic Regression (L1/L2)** — interpretable, calibrated probabilities; check multicollinearity
2. **Decision Tree / Random Forest (Bagging)** — non-linear interactions; permutation importance
3. **k-Nearest Neighbours (KNN)** — non-parametric baseline; sensitive to scaling/`k`
4. **Support Vector Machine (SVM)** — linear/RBF kernels; `C`, `gamma`, `class_weight`
5. **Neural Network (MLP)** — `(128, 64)` style hidden layers, ReLU, early stopping

**Training:** K-Fold Cross-Validation (e.g., `cv=5`) for hyperparameters & threshold selection

### 4) Decision Thresholding
Tune the probability cutoff per business cost curve: maximise F1, or fix **Recall** at target level and maximise **Precision** to reduce false approvals for risk-averse policies. 

---

## Evaluation

Because the label is **imbalanced** and costs are **asymmetric**, report:

- **Precision / Recall / F1** (macro, micro, weighted)
- **ROC-AUC** and **PR-AUC** (PR-AUC emphasises minority class)
- **Confusion Matrix** (flag **False Positives** as most costly)

---
