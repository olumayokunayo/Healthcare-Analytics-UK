import pandas as pd
import random
import os

from faker import Faker


fake = Faker("en_GB")


# ==================================
# File locations
# ==================================

output_folder = "data/raw"

os.makedirs(output_folder, exist_ok=True)


# ==================================
# Load reference tables
# ==================================

hospitals = pd.read_csv(
    f"{output_folder}/hospitals.csv"
)

departments = pd.read_csv(
    f"{output_folder}/departments.csv"
)


# ==================================
# Doctor settings
# ==================================

number_of_doctors = 500


specialties = [
    "Cardiology",
    "Neurology",
    "Emergency Medicine",
    "Oncology",
    "General Surgery",
    "Paediatrics",
    "Orthopaedics",
    "Radiology",
    "Psychiatry",
    "Gastroenterology"
]


consultant_levels = [
    "Consultant",
    "Senior Consultant",
    "Clinical Lead",
    "Specialist",
    "Registrar"
]


employment_types = [
    "Permanent",
    "Full Time",
    "Part Time",
    "Locum"
]


# ==================================
# Generate doctors
# ==================================

doctors = []


for i in range(1, number_of_doctors + 1):

    hospital = hospitals.sample(1).iloc[0]

    department = departments.sample(1).iloc[0]


    doctors.append([

        # doctor_id
        i,

        # names
        fake.first_name(),
        fake.last_name(),

        # gender
        random.choice([
            "Male",
            "Female"
        ]),

        # specialty
        random.choice(specialties),

        # experience
        random.randint(1,35),

        # consultant level
        random.choice(consultant_levels),

        # GMC number
        f"GMC{random.randint(1000000,9999999)}",

        # employment
        random.choice(employment_types),

        # hire date
        fake.date_between(
            start_date="-25y",
            end_date="-1y"
        ),

        # hospital FK
        hospital["hospital_id"],

        # department FK
        department["department_id"]

    ])



# ==================================
# Create dataframe
# ==================================

doctor_df = pd.DataFrame(
    doctors,
    columns=[

        "doctor_id",
        "first_name",
        "last_name",
        "gender",
        "specialty",
        "years_experience",
        "consultant_level",
        "gmc_number",
        "employment_type",
        "hire_date",
        "hospital_id",
        "department_id"

    ]
)



# ==================================
# Export
# ==================================

doctor_df.to_csv(
    f"{output_folder}/doctors.csv",
    index=False
)


print("Doctors dataset generated successfully!")
print(f"Generated {number_of_doctors} doctors")