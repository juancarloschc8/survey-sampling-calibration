# Complex Survey Sampling & Calibration Engine (Raking)

*Project Status:* Completed  
*Tools:* Python, Samplics, Pandas, Numpy  
*Type:* Statistical Inference / Market Research

## Executive Summary
In Market Research, simple random sampling is rarely feasible. We often deal with *Complex Survey Designs* (Stratification & Clustering) and non-response bias. 

This project simulates a full demographic study workflow:
1.  *Population Simulation:* Creating a synthetic census of 100k individuals.
2.  *Complex Sampling:* Implementing a multi-stage design (Stratified by Region, Clustered by Municipality).
3.  *Bias Injection:* Simulating realistic non-response patterns (e.g., young males responding less).
4.  *Calibration (Raking):* Using Iterative Proportional Fitting (IPF) to adjust sampling weights, ensuring the sample marginals match known census totals.

## Key Results
By applying Raking calibration, we reduced the estimation error significantly compared to the raw sample data.

| Methodology | Estimated Income | Error vs Census |
|Summay|---|---|
| *Census (Ground Truth)* | *$19,842* | *$0* |
| Sample (Unweighted/Biased) | $20,510 | +$668 (Overestimation) |
| *Sample (Calibrated)* | *$19,890* | *+$48 (92% Error Reduction)* |

## Methodology Detail

### 1. Sampling Design
We utilized a *Two-Stage Cluster Sampling* design:
* *PSU (Primary Sampling Unit):* Municipality (Clusters).
* *Strata:* Geographic Regions (North/South).
* *SSU (Secondary Sampling Unit):* Individuals within selected municipalities.

### 2. Weighting & Calibration
Initial weights ($w_i$) were calculated based on selection probabilities. However, due to differential non-response, the raw sample was unrepresentative.

We used *Raking (Iterative Proportional Fitting)* to adjust weights so that:
$$\sum w_i^{cal} \cdot I(x \in AgeGroup) = N_{AgeGroup}$$
$$\sum w_i^{cal} \cdot I(x \in Gender) = N_{Gender}$$

This ensures the sample structure perfectly mirrors the known population demographics.

## How to Run

1. Install requirements:
   ```bash
   pip install -r requirements.txt
