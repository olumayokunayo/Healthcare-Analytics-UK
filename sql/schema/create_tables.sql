-- =====================================================
-- UK Healthcare Analytics Database
-- Database Schema Creation
-- =====================================================


-- Create database
CREATE DATABASE IF NOT EXISTS healthcare_analytics;

USE healthcare_analytics;


-- =====================================================
-- 1. HOSPITALS TABLE
-- =====================================================

CREATE TABLE hospitals (

    hospital_id INT AUTO_INCREMENT PRIMARY KEY,

    hospital_name VARCHAR(150) NOT NULL,

    nhs_trust VARCHAR(150),

    city VARCHAR(50),

    region VARCHAR(50),

    postcode VARCHAR(10),

    hospital_type VARCHAR(50),

    bed_capacity INT,

    established_year YEAR

);



-- =====================================================
-- 2. DEPARTMENTS TABLE
-- =====================================================

CREATE TABLE departments (

    department_id INT AUTO_INCREMENT PRIMARY KEY,

    department_name VARCHAR(100) NOT NULL,

    department_code VARCHAR(20),

    clinical_specialty VARCHAR(100)

);



-- =====================================================
-- 3. INSURANCE PROVIDERS TABLE
-- =====================================================

CREATE TABLE insurance_providers (

    insurance_id INT AUTO_INCREMENT PRIMARY KEY,

    provider_name VARCHAR(100) NOT NULL,

    provider_type VARCHAR(50),

    contact_region VARCHAR(50)

);



-- =====================================================
-- 4. DIAGNOSES TABLE
-- =====================================================

CREATE TABLE diagnoses (

    diagnosis_id INT AUTO_INCREMENT PRIMARY KEY,

    diagnosis_name VARCHAR(100),

    category VARCHAR(100)

);



-- =====================================================
-- 5. MEDICATIONS TABLE
-- =====================================================

CREATE TABLE medications (

    medication_id INT AUTO_INCREMENT PRIMARY KEY,

    medication_name VARCHAR(100),

    medication_type VARCHAR(100)

);



-- =====================================================
-- 6. DOCTORS TABLE
-- =====================================================

CREATE TABLE doctors (

    doctor_id INT AUTO_INCREMENT PRIMARY KEY,

    first_name VARCHAR(50),

    last_name VARCHAR(50),

    gender VARCHAR(20),

    specialty VARCHAR(100),

    years_experience INT,

    consultant_level VARCHAR(50),

    gmc_number VARCHAR(20),

    employment_type VARCHAR(50),

    hire_date DATE,


    hospital_id INT,

    department_id INT,


    CONSTRAINT fk_doctor_hospital

    FOREIGN KEY (hospital_id)

    REFERENCES hospitals(hospital_id),


    CONSTRAINT fk_doctor_department

    FOREIGN KEY (department_id)

    REFERENCES departments(department_id)

);



-- =====================================================
-- 7. PATIENTS TABLE
-- =====================================================

CREATE TABLE patients (

    patient_id INT AUTO_INCREMENT PRIMARY KEY,

    first_name VARCHAR(50),

    last_name VARCHAR(50),

    gender VARCHAR(20),

    date_of_birth DATE,

    nhs_number VARCHAR(10),

    postcode VARCHAR(10),

    blood_group VARCHAR(5),

    ethnicity VARCHAR(50),

    marital_status VARCHAR(30),

    registration_date DATE

);



-- =====================================================
-- 8. ADMISSIONS TABLE
-- =====================================================

CREATE TABLE admissions (

    admission_id INT AUTO_INCREMENT PRIMARY KEY,


    patient_id INT,

    doctor_id INT,

    diagnosis_id INT,

    medication_id INT,


    admission_date DATE,

    discharge_date DATE,


    admission_type VARCHAR(50),

    admission_source VARCHAR(50),

    referral_type VARCHAR(50),

    emergency_flag BOOLEAN,

    readmission_flag BOOLEAN,


    ward VARCHAR(50),

    length_of_stay INT,

    admission_status VARCHAR(50),



    CONSTRAINT fk_admission_patient

    FOREIGN KEY(patient_id)

    REFERENCES patients(patient_id),



    CONSTRAINT fk_admission_doctor

    FOREIGN KEY(doctor_id)

    REFERENCES doctors(doctor_id),



    CONSTRAINT fk_admission_diagnosis

    FOREIGN KEY(diagnosis_id)

    REFERENCES diagnoses(diagnosis_id),



    CONSTRAINT fk_admission_medication

    FOREIGN KEY(medication_id)

    REFERENCES medications(medication_id)

);



-- =====================================================
-- 9. BILLING TABLE
-- =====================================================

CREATE TABLE billing (

    billing_id INT AUTO_INCREMENT PRIMARY KEY,


    admission_id INT,

    insurance_id INT,


    invoice_number VARCHAR(50),

    treatment_cost DECIMAL(10,2),

    claim_amount DECIMAL(10,2),

    payment_status VARCHAR(50),

    payment_method VARCHAR(50),

    payment_date DATE,


    CONSTRAINT fk_billing_admission

    FOREIGN KEY(admission_id)

    REFERENCES admissions(admission_id),



    CONSTRAINT fk_billing_insurance

    FOREIGN KEY(insurance_id)

    REFERENCES insurance_providers(insurance_id)

);



-- =====================================================
-- CHECK TABLES
-- =====================================================

SHOW TABLES;