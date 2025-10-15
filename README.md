# 🌟 Data Science & Analytics Projects Repository 🌟

Welcome! This repository is a curated collection of applied analytics and machine-learning projects spanning e-commerce optimisation, financial risk modelling, healthcare AI, and environmental analytics. The common theme is **end-to-end analysis**: turning messy, real-world data into deployable insights through thorough cleaning, feature engineering, modelling, evaluation, and clear communication

These projects emphasises on:
- **Reproducibility** – versioned code/notebooks, environment files, and consistent data handling
- **Responsible modelling** – attention to leakage, class imbalance, calibration, and explainability
- **Business alignment** – metrics and model choices tied to real decision costs
- **Practicality** – lightweight scripts/notebooks that produce usable figures, metrics, and artefacts

Each project is organised in its own folder, each of them containing the necessary files such as datasets, analytics notebooks, and reports. Click on folder to explore a specific project in detail.

If you’re exploring the repo for the first time, start with any project’s README and find out about the overview of the project. Some larger assets (e.g., model weights, chemistry files, big CSVs) are stored via **Git LFS** which is written in greater detail near the end.

---

## 1. E-Commerce Optimisation
This project analyses the end-to-end purchase funnel to identify where users drop off and which levers (channels, pricing etc.) drive conversion. It pairs exploratory analysis with predictive models for conversion and churn, plus simple A/B testing workflows. The aim is to prioritise high-impact optimisations and quantify expected lift for e-commerce stakeholders.  

**Open:** [`E-Commerce Optimisation`](E-Commerce%20Optimisation/)

---

## 2. Credit Risk Prediction

This project models credit card approval outcomes by combining application features with repayment status and addressing class imbalance carefully. Multiple models (e.g., LR, Tree/Forest, KNN, SVM, MLP) are evaluated with cost-aware metrics (PR-AUC, ROC-AUC, F1) and calibration checks. The focus is on transparent, auditable decisions with thresholds tuned to minimise costly false approvals.  

**Open:** [`Credit Risk Prediction`](Credit%20Risk%20Prediction/)

---

## 3. Deforestation in Brazil

This data visualisation project explores global forest change and zooms into Brazil to understand which activities (e.g., pasture, crops) drive loss over time. Visual analyses (diverging bars, stacked areas, maps + time series) connect data trends to policy and commodity dynamics. The goal is to communicate why and where change occurs in a way non-technical audiences can act on.  

**Open:** [`Deforestation in Brazil`](Deforestation%20in%20Brazil/)

---

## 4. Predicting Drug–Drug Interaction (PDDI)

This project focuses on using machine learning to predict how drugs will interact with each other. This project also compares classical feature-based models with deep learning approaches (SSI-DDI, SSF-DDI) to predict whether drugs interact and the interaction type. The dataset is curated from multiple sources and tailored for clinical relevance, with Top-k accuracy and AUC metrics reported. Trade-offs between accuracy, interpretability, and compute are discussed for practical deployment.  

> **Large files note:** Some data/models use **Git LFS**. If you see small pointer files, run `git lfs install && git pull` before opening. Heavy files may be excluded or provided via scripts.

**Open:** [`Predicting Drug Drug Interaction`](Predicting%20Drug%20Drug%20Interaction/)

---

## 5. Insurance Satisfaction Prediction (Notebook)

This project features compact notebook that demonstrates end-to-end prediction of customer satisfaction in an insurance journey. It includes preprocessing, baseline models, and core evaluation plots for quick experimentation. Intended as a simple, adaptable starting point.  

**Open:** [`Insurance Satisfaction Prediction`](Insurance%20Satisfaction%20Prediction/)

---

### Only needed if you plan to pull large data/models
git lfs install
git pull