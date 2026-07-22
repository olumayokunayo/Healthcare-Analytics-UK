# Healthcare Analytics Insights

## Exploratory Data Analysis (EDA)

## Dataset Overview

The healthcare dataset contains:

| Metric | Count |

| Total Patients | 1,0000 |
| Total Admissions | 50,000 |
| Total Doctors | 500 |
| Total Hospitals | 18 |
| Total Billing Records | 50,000 |

### Observations

- The dataset contains 50,000 patient admission records.
- Each admission has an associated billing record.
- The dataset covers interactions between 1,0000 patients, 500 doctors, and 18 hospitals.

## Date Range Analysis

| Metric | Date |

| First Admission | 2021-07-19 |
| Last Admission | 2026-07-19 |
| First Payment | 2023-07-25 |
| Last Payment | 2026-10-16 |

### Observations

- The admissions dataset covers approximately 5 years of healthcare activity (July 2021 - July 2026).
- Billing records begin later than admission records, starting in July 2023.
- The dataset is suitable for analysing admission trends, hospital performance, and financial metrics over time.

## Data Quality Checks

### Missing Values - Admissions

| Column | Missing Records |

| Patient ID | 0 |
| Doctor ID | 0 |
| Hospital ID | 0 |
| Admission Date | 0 |
| Discharge Date | 0 |

### Missing Values - Billing

| Column | Missing Records |

| Admission Reference | 0 |
| Treatment Cost | 0 |
| Claim Amount | 0 |
| Payment Status | 0 |

### Observation

- No missing values were identified.
- The dataset is complete enough for further analysis.

## Duplicate Record Checks

### Billing Data

- Original billing records: 50,000
- Duplicate invoice numbers identified: 17
- Extra duplicate rows identified: 130
- Duplicate invoices were removed using invoice number as the business key.
- Clean billing records available for analysis: 49,870

### Observation

- Duplicate billing events were identified and removed before financial analysis.
- Cleaning prevents inflated revenue and claim calculations.

## Data Integrity Checks

### Admissions → Patients

Result:

- Invalid patient references: 0

Findings:

- Every admission is linked to a valid patient.

### Admissions → Doctors

Result:

- Invalid doctor references: 0

Finding:

- Every admission is linked to a valid doctor.

### Admissions → Hospitals

Result:

- Invalid hospital references: 0

Findings:

- Every admission is linked to a valid hospital.

### Billing → Admissions

Findings:

- Admissions table uses numeric `admission_id` values (1,2,3...)
- Billing table uses `admission_reference` values (ADMxxxxx)
- No mapping table exists to connect these identifiers.

Impact:

- Billing cannot be linked to individual admissions, hospitals, doctors, or departments.
- Billing analysis will be performed independently unless a valid mapping source is provided.

## Distribution Analysis

## Patient Demographics

### Age Analysis

Patient age was calculated from date of birth.

Findings:

- Youngest patient: 18 years
- Oldest patient: 90 years
- Average patient age: 53.8 years

Observation:

- The dataset represents an adult patient population.
- The average age of 53.8 years suggests healthcare activity is concentrated among middle-aged and older adults.

### Gender Distribution

Findings:

- Male: 5077 | 50.77%
- Female: 4923 | 49.23%

Observation:

- The patient population is almost evenly distributed between males and females.
- The balanced gender distribution provides a representative sample for demographic analysis.

### Age Distribution

Findings:

18-35: 2,520
36-50: 2,057
51-65: 2,012
65+: 3,411

Observation:

- Patients aged 65 years and above represent the largest age group.
- This suggests greater healthcare utilisation among older adults.

### Blood Type Distribution

Findings:

A+: 1,330 | 13.30%
B+: 1,283 | 12.83%
O-: 1,276 | 12.76%
AB-: 1,252 | 12.52%
O+: 1,250 | 12.50%
A-: 1,235 | 12.35%
AB+: 1,235 | 12.35%
B-: 1,139 | 11.39%

Observation:

- Blood groups are evenly distributed across the patient population.
- No blood type appears significantly overrepresented or underrepresented.

### Admission Analysis

Findings:

- Total admissions analysed: 50,000
- Admission period: July 2021 - July 2026
- Monthly admissions generally range between 760 and 905 admissions.

Observation:

- Admission volumes remain relatively stable throughout the five-year period.
- No significant seasonal spikes or prolonged declines were observed.

### Admission Type Distribution

Findings:

Elective: 16,808
Emergency: 16,770
Urgent: 16,422

Observation:

- Admission types are almost equally distributed.
- Hospitals appear to manage a balanced combination of planned procedures and emergency care.
- No single admission type dominates the dataset.

### Admission Status Distribution

Findings:

Under Treatment: 16,772
Transferred: 16,641
Discharged: 16,587

Observation:

- Admission outcomes are evenly distributed across all three status categories.
- Similar volumes suggest consistent patient flow through the healthcare system.
- No abnormal concentration exists within any admission outcome.

#### Exploratory Data Analysis Summary

The exploratory data analysis shows that the healthcare dataset is clean, comprehensive, and suitable for advanced analytics.

Key findings include:

The dataset contains 50,000 admissions linked to 10,000 patients, 500 doctors, and 18 hospitals.
No missing values were found in critical admission or billing fields.
Duplicate billing records were identified and removed by creating a cleaned billing table (billing_clean) containing 49,870 unique records.
All admission records successfully reference valid patients, doctors, and hospitals.
Financial data cannot currently be joined to admissions because the billing table stores formatted admission references (ADMxxxxx) while the admissions table stores numeric admission IDs.
The patient population is well balanced by gender, with an average age of 53.8 years.
Patients aged 65 years and above form the largest age group, indicating higher healthcare utilisation among older adults.
Admission volumes remain stable over the five-year period, with a balanced distribution of Elective, Emergency, and Urgent admissions.
Overall, the dataset demonstrates strong data quality and provides a reliable foundation for business intelligence, SQL analysis, KPI reporting, and interactive dashboard development.
