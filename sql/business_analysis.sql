-- Healthcare Analytics Project
-- Business Analysis

-- Hospital Performance 

-- Highest number of admissions

SELECT 
    h.hospital_name,
    COUNT(a.admission_date) AS admission_count
FROM hospitals h
JOIN admissions a
ON h.hospital_id = a.hospital_id
GROUP BY h.hospital_name
ORDER BY admission_count DESC;

-- Highest treatment cost

SELECT h.hospital_name, SUM(bc.treatment_cost) AS total_treatment_cost
FROM billing_clean bc
JOIN billing_admission_mapping bam
ON bc.admission_reference = bam.admission_reference
JOIN admissions a
ON bam.admission_id = a.admission_id
JOIN hospitals h
ON a.hospital_id = h.hospital_id 
GROUP BY h.hospital_name
ORDER BY total_treatment_cost DESC
LIMIT 1;

