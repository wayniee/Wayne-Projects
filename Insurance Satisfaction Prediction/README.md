# Insurance Journey Analytics — Satisfaction & Conversion Prediction

Short project exploring **where applicants drop off** and how to **predict customer satisfaction & conversion** from journey data.

## Goals
- Identify **critical touchpoints** that drive drop-off.
- Build models to **predict satisfaction** and **propensity to convert**.
- Provide **actionable levers**: personalised nudges, simplified steps

## Contents
- `data.parquet` - original data file from Singlife
- `Insurance Satisfaction Prediction.ipynb` — end-to-end notebook (EDA → features → models → evaluation)

## Methods
- **EDA**: missing data, leakage checks, class balance
- **Feature Prep**: categorical encoding, numeric scaling, time features, step counts
- **Models**:
  - Decision Tree
  - k-Nearest Neighbours (Potential future development)
  - Support Vector Machine (Potential future development)
  - Multi-Layer Perceptron (Potential future development)
- **Evaluation**: ROC-AUC, PR-AUC, Precision/Recall/F1, calibration, confusion matrix


