import pandas as pd
import random
import os

from faker import Faker


fake = Faker("en_GB")


output_folder = "data/raw"


# ================================
# Load reference tables
# ================================

patients = pd.read_csv(
    f"{output_folder}/patients.csv"
)

doctors = pd.read_csv(
    f"{output_folder}/doctors.csv"
)

diagnoses = pd.read_csv(
    f"{output_folder}/diagnoses.csv"
)

medications = pd.read_csv(
    f"{output_folder}/medications.csv"
)

hospitals = pd.read_csv(
    f"{output_folder}/hospitals.csv"
)

departments = pd.read_csv(
    f"{output_folder}/departments.csv"
)


# ================================
# Settings
# ================================

number_of_admissions = 50000


admission_types = [
    "Emergency",
    "Elective",
    "Urgent"
]


sources = [
    "GP Referral",
    "Emergency Department",
    "Transfer"
]


referrals = [
    "GP",
    "Consultant",
    "Self Referral"
]


statuses = [
    "Discharged",
    "Transferred",
    "Under Treatment"
]


wards = [
    "Ward A",
    "Ward B",
    "Ward C",
    "ICU",
    "Surgical Ward"
]


destinations = [
    "Home",
    "Care Home",
    "Another Hospital"
]


# ================================
# Generate admissions
# ================================

admissions = []


for i in range(1, number_of_admissions + 1):

    patient = patients.sample(1).iloc[0]

    doctor = doctors.sample(1).iloc[0]

    diagnosis = diagnoses.sample(1).iloc[0]

    medication = medications.sample(1).iloc[0]

    hospital = hospitals.sample(1).iloc[0]

    department = departments.sample(1).iloc[0]


    admission_date = fake.date_between(
        start_date="-5y",
        end_date="today"
    )


    length_of_stay = random.randint(1,20)


    discharge_date = (
        pd.to_datetime(admission_date)
        +
        pd.Timedelta(days=length_of_stay)
    ).date()



    admissions.append([

        i,

        patient["patient_id"],

        doctor["doctor_id"],

        diagnosis["diagnosis_id"],

        medication["medication_id"],

        hospital["hospital_id"],

        department["department_id"],

        admission_date,

        discharge_date,

        random.choice(admission_types),

        random.choice(sources),

        random.choice(referrals),

        random.choice([0,1]),

        random.choice([0,1]),

        random.choice(wards),

        f"BED-{random.randint(1,300)}",

        length_of_stay,

        random.choice(statuses),

        random.choice(destinations)

    ])



# ================================
# Dataframe
# ================================

df = pd.DataFrame(

    admissions,

    columns=[

        "admission_id",

        "patient_id",

        "doctor_id",

        "diagnosis_id",

        "medication_id",

        "hospital_id",

        "department_id",

        "admission_date",

        "discharge_date",

        "admission_type",

        "admission_source",

        "referral_type",

        "emergency_flag",

        "readmission_flag",

        "ward",

        "bed_number",

        "length_of_stay",

        "admission_status",

        "discharge_destination"

    ]

)


df.to_csv(
    f"{output_folder}/admissions.csv",
    index=False
)


print("Admissions dataset generated successfully!")
print(f"Generated {number_of_admissions} admissions")