import pandas as pd
import random
import os

from faker import Faker
from datetime import timedelta


fake = Faker()


# =====================================
# SETTINGS
# =====================================

output_folder = "data/raw"

number_of_admissions = 50000


# =====================================
# Load reference data
# =====================================

patients = pd.read_csv(
    f"{output_folder}/patients.csv"
)

hospitals = pd.read_csv(
    f"{output_folder}/hospitals.csv"
)

doctors = pd.read_csv(
    f"{output_folder}/doctors.csv"
)

departments = pd.read_csv(
    f"{output_folder}/departments.csv"
)



# =====================================
# Reference values
# =====================================

diagnoses = [

    "Cardiovascular Disease",
    "Cancer Treatment",
    "Respiratory Infection",
    "Diabetes",
    "Stroke",
    "Fracture",
    "Pneumonia",
    "Kidney Disease",
    "Neurological Disorder",
    "Routine Checkup"

]


admission_types = [

    "Emergency",
    "Urgent",
    "Routine"

]


# =====================================
# Generate admissions
# =====================================


admissions = []


for i in range(1, number_of_admissions + 1):


    patient = patients.sample(1).iloc[0]

    hospital = hospitals.sample(1).iloc[0]

    doctor = doctors.sample(1).iloc[0]

    department = departments.sample(1).iloc[0]


    admission_date = fake.date_between(

        start_date="-3y",

        end_date="today"

    )


    length_of_stay = random.randint(1,14)


    discharge_date = (

        pd.to_datetime(admission_date)

        + timedelta(days=length_of_stay)

    ).date()



    treatment_cost = round(

        random.uniform(500,15000),

        2

    )


    admissions.append([

        f"ADM{i:07d}",

        patient["patient_id"],

        hospital["hospital_id"],

        doctor["doctor_id"],

        department["department_id"],

        admission_date,

        discharge_date,

        length_of_stay,

        random.choice(admission_types),

        random.choice(diagnoses),

        treatment_cost

    ])



# =====================================
# Create dataframe
# =====================================

admissions_df = pd.DataFrame(

    admissions,

    columns=[

        "admission_id",

        "patient_id",

        "hospital_id",

        "doctor_id",

        "department_id",

        "admission_date",

        "discharge_date",

        "length_of_stay",

        "admission_type",

        "diagnosis",

        "treatment_cost"

    ]

)



# =====================================
# Export
# =====================================

admissions_df.to_csv(

    f"{output_folder}/admissions.csv",

    index=False

)



print("Admissions dataset generated successfully!")