import pandas as pd
import random
import os

from faker import Faker


fake = Faker()


# ================================
# File locations
# ================================

output_folder = "data/raw"

os.makedirs(output_folder, exist_ok=True)


# ================================
# Load reference tables
# ================================

hospitals = pd.read_csv(
    f"{output_folder}/hospitals.csv"
)

departments = pd.read_csv(
    f"{output_folder}/departments.csv"
)


# ================================
# Doctor settings
# ================================

number_of_doctors = 500


employment_types = [
    "Consultant",
    "Specialist",
    "Registrar",
    "Junior Doctor"
]


salary_bands = [
    "NHS Band 6",
    "NHS Band 7",
    "NHS Band 8A",
    "NHS Band 8B",
    "NHS Band 8C",
    "NHS Band 9"
]


# ================================
# Generate doctors
# ================================

doctors = []


for i in range(1, number_of_doctors + 1):

    first_name = fake.first_name()
    last_name = fake.last_name()

    hospital = hospitals.sample(1).iloc[0]
    department = departments.sample(1).iloc[0]


    doctors.append([
        f"DOC{i:04d}",
        first_name,
        last_name,
        f"Dr {first_name} {last_name}",
        random.choice(
            ["Male", "Female"]
        ),
        department["department_id"],
        department["department_name"],
        hospital["hospital_id"],
        hospital["hospital_name"],
        random.choice(employment_types),
        random.randint(2,35),
        random.choice(salary_bands)
    ])



# ================================
# Create dataframe
# ================================

doctor_df = pd.DataFrame(
    doctors,
    columns=[
        "doctor_id",
        "first_name",
        "last_name",
        "full_name",
        "gender",
        "department_id",
        "department_name",
        "hospital_id",
        "hospital_name",
        "employment_type",
        "years_experience",
        "salary_band"
    ]
)


# ================================
# Export CSV
# ================================

doctor_df.to_csv(
    f"{output_folder}/doctors.csv",
    index=False
)


print("Doctors dataset generated successfully!")