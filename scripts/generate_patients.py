import pandas as pd
import random
import os

from faker import Faker


fake = Faker()


# ===================================
# Settings
# ===================================

output_folder = "data/raw"

os.makedirs(output_folder, exist_ok=True)


number_of_patients = 10000


# ===================================
# Reference data
# ===================================

insurance = pd.read_csv(
    f"{output_folder}/insurance_providers.csv"
)


# ===================================
# Generate patients
# ===================================

patients = []


blood_types = [
    "A+",
    "A-",
    "B+",
    "B-",
    "AB+",
    "AB-",
    "O+",
    "O-"
]


genders = [
    "Male",
    "Female"
]


cities = [
    "Coventry",
    "Birmingham",
    "London",
    "Manchester",
    "Leeds",
    "Bristol",
    "Nottingham",
    "Sheffield",
    "Oxford",
    "Cambridge"
]


for i in range(1, number_of_patients + 1):

    first_name = fake.first_name()
    last_name = fake.last_name()


    insurance_provider = insurance.sample(1).iloc[0]


    patients.append([

        f"PAT{i:06d}",

        first_name,

        last_name,

        f"{first_name} {last_name}",

        random.choice(genders),

        random.randint(0,95),

        random.choice(blood_types),

        random.choice(cities),

        random.choice(
            ["UK", "UK"]
        ),

        insurance_provider["insurance_id"],

        insurance_provider["provider_name"]

    ])



# ===================================
# Create dataframe
# ===================================

patient_df = pd.DataFrame(

    patients,

    columns=[

        "patient_id",

        "first_name",

        "last_name",

        "full_name",

        "gender",

        "age",

        "blood_type",

        "city",

        "country",

        "insurance_id",

        "insurance_provider"

    ]

)



# ===================================
# Export
# ===================================

patient_df.to_csv(

    f"{output_folder}/patients.csv",

    index=False

)


print("Patients dataset generated successfully!")