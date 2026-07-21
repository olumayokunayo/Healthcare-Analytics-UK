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
# Load insurance providers
# ==================================

insurance = pd.read_csv(
    f"{output_folder}/insurance_providers.csv"
)


# ==================================
# Settings
# ==================================

number_of_patients = 10000


blood_groups = [
    "A+",
    "A-",
    "B+",
    "B-",
    "AB+",
    "AB-",
    "O+",
    "O-"
]


ethnicities = [
    "White British",
    "Black British",
    "Asian British",
    "Mixed",
    "Other"
]


marital_status = [
    "Single",
    "Married",
    "Divorced",
    "Widowed"
]


# ==================================
# Generate patients
# ==================================

patients = []


for i in range(1, number_of_patients + 1):

    insurance_provider = insurance.sample(1).iloc[0]


    patients.append([

        # patient_id
        i,

        # names
        fake.first_name(),
        fake.last_name(),

        # gender
        random.choice([
            "Male",
            "Female"
        ]),


        # DOB
        fake.date_of_birth(
            minimum_age=18,
            maximum_age=90
        ),


        # NHS number
        str(random.randint(
            1000000000,
            9999999999
        )),


        # postcode
        fake.postcode(),


        # blood group
        random.choice(
            blood_groups
        ),


        # ethnicity
        random.choice(
            ethnicities
        ),


        # marital status
        random.choice(
            marital_status
        ),


        # registration date
        fake.date_between(
            start_date="-10y",
            end_date="today"
        ),


        # insurance FK
        insurance_provider["insurance_id"]

    ])



# ==================================
# Dataframe
# ==================================

patient_df = pd.DataFrame(

    patients,

    columns=[

        "patient_id",
        "first_name",
        "last_name",
        "gender",
        "date_of_birth",
        "nhs_number",
        "postcode",
        "blood_group",
        "ethnicity",
        "marital_status",
        "registration_date",
        "insurance_id"

    ]

)



# ==================================
# Export
# ==================================

patient_df.to_csv(
    f"{output_folder}/patients.csv",
    index=False
)


print("Patients dataset generated successfully!")
print(f"Generated {number_of_patients} patients")