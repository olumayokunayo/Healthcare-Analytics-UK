-- Healthcare Analytics Project
-- Exploratory Data Analysis (EDA)


-- Total Patients

SELECT COUNT(*) AS total_patients
FROM patients

-- Total Admissions

SELECT COUNT(*) AS total_admissions
FROM admissions

-- Total Doctors

SELECT COUNT(*) AS total_doctors
FROM doctors

-- Total Hospitals

SELECT COUNT(*) AS total_hospitals
FROM hospitals

-- Total Billing Records

SELECT COUNT(*) AS total_billing_records
FROM billing


-- DATE RANGE ANALYSIS

-- Admission Period

SELECT 
MIN(admission_date) AS first_admission,
MAX(admission_date) AS last_admission
FROM admissions

-- Billing Period

SELECT 
MIN(payment_date) AS first_payment,
MAX(payment_date) AS last_payment
FROM billing


-- DATA QUALITY CHECKS
-- Missing Values

--  Missing values - Admissions
SELECT
    COUNT(*) AS total_records,
    SUM(patient_id IS NULL) AS missing_patient_id,
    SUM(doctor_id IS NULL) AS missing_doctor_id,
    SUM(hospital_id IS NULL) AS missing_hospital_id,
    SUM(admission_date IS NULL) AS missing_admission_date,
    SUM(discharge_date IS NULL) AS missing_discharge_date
FROM admissions;

-- Missing values - Billing
SELECT
    COUNT(*) AS total_records,
    SUM(admission_reference IS NULL) AS missing_admission_reference,
    SUM(treatment_cost IS NULL) AS missing_treatment_cost,
    SUM(claim_amount IS NULL) AS missing_claim_amount,
    SUM(payment_status IS NULL) AS missing_payment_status
FROM billing;

-- Duplicates

SELECT 
    COUNT(*) AS duplicate_rows
FROM billing
WHERE invoice_number IN (
    SELECT invoice_number
    FROM billing
    GROUP BY invoice_number
    HAVING COUNT(*) > 1
);

CREATE TABLE billing_clean AS
SELECT *
FROM (
    SELECT 
        b.*,
        ROW_NUMBER() OVER(
            PARTITION BY invoice_number
            ORDER BY billing_id
        ) AS rn
    FROM billing b
) x
WHERE rn = 1;


-- DATA INTEGRITY CHECKS


-- Admissions without valid patients

SELECT 
    COUNT(*) AS invalid_patient_records
FROM admissions a
LEFT JOIN patients p
ON a.patient_id = p.patient_id
WHERE p.patient_id IS NULL;

-- Admissions without valid doctors

SELECT 
    COUNT(*) AS invalid_doctor_records
FROM admissions a
LEFT JOIN doctors d
ON a.doctor_id = d.doctor_id
WHERE d.doctor_id IS NULL;

-- Admissions without valid hospitals

SELECT 
    COUNT(*) AS invalid_hospital_records
FROM admissions a
LEFT JOIN hospitals h
ON a.hospital_id = h.hospital_id
WHERE h.hospital_id IS NULL;

-- Age summary

SELECT
    MIN(TIMESTAMPDIFF(YEAR, date_of_birth, CURDATE())) AS youngest_patient,
    MAX(TIMESTAMPDIFF(YEAR, date_of_birth, CURDATE())) AS oldest_patient,
    ROUND(AVG(TIMESTAMPDIFF(YEAR, date_of_birth, CURDATE())),1) AS average_age
FROM patients;

-- Gender Distribution

SELECT
    gender,
    COUNT(*) AS patient_count,
    ROUND(
        COUNT(*) * 100.0 / (SELECT COUNT(*) FROM patients),
        2
    ) AS percentage
FROM patients
GROUP BY gender;

-- Patient Blood Group Distribution

SELECT
    blood_group,
    COUNT(*) AS patient_count,
    ROUND(
        COUNT(*) * 100.0 / (SELECT COUNT(*) FROM patients),
        2
    ) AS percentage
FROM patients
GROUP BY blood_group
ORDER BY patient_count DESC;

-- Age Groups

SELECT
CASE
    WHEN TIMESTAMPDIFF(YEAR,date_of_birth,CURDATE()) BETWEEN 18 AND 35 THEN '18-35'
    WHEN TIMESTAMPDIFF(YEAR,date_of_birth,CURDATE()) BETWEEN 36 AND 50 THEN '36-50'
    WHEN TIMESTAMPDIFF(YEAR,date_of_birth,CURDATE()) BETWEEN 51 AND 65 THEN '51-65'
    ELSE '65+'
END AS age_group,

COUNT(*) AS patients

FROM patients

GROUP BY age_group

ORDER BY patients DESC;

-- Total Admissions

SELECT
COUNT(*) AS total_admissions
FROM admissions;

-- Admissions Per Year

SELECT
YEAR(admission_date) AS admission_year,
COUNT(*) AS admissions
FROM admissions
GROUP BY admission_year
ORDER BY admission_year;

-- Admissions Per Month

SELECT
DATE_FORMAT(admission_date, '%Y-%m') AS admission_month,
COUNT(*) AS admissions
FROM admissions
GROUP BY admission_month
ORDER BY admission_month;

-- Admission Type

SELECT
admission_type,
COUNT(*) AS admissions
FROM admissions
GROUP BY admission_type
ORDER BY admissions DESC;

-- Admission Status

SELECT
admission_status,
COUNT(*) AS total
FROM admissions
GROUP BY admission_status;
