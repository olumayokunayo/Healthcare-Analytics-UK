import pandas as pd
import os


output_folder = "data/raw"

os.makedirs(output_folder, exist_ok=True)


medications = [

    ["Amlodipine", "Cardiovascular"],
    ["Ramipril", "Cardiovascular"],
    ["Atorvastatin", "Cholesterol Management"],

    ["Metformin", "Diabetes"],
    ["Insulin", "Diabetes"],

    ["Salbutamol", "Respiratory"],
    ["Budesonide", "Respiratory"],

    ["Paracetamol", "Pain Relief"],
    ["Ibuprofen", "Pain Relief"],

    ["Morphine", "Pain Management"],

    ["Warfarin", "Blood Thinner"],
    ["Aspirin", "Blood Thinner"],

    ["Amoxicillin", "Antibiotic"],
    ["Cefalexin", "Antibiotic"],

    ["Omeprazole", "Digestive System"],

    ["Levothyroxine", "Hormone Therapy"],

    ["Chemotherapy Drugs", "Cancer Treatment"],

    ["Radiotherapy Medication", "Cancer Treatment"]

]


medication_df = pd.DataFrame(

    medications,

    columns=[

        "medication_name",

        "medication_type"

    ]

)


medication_df.insert(

    0,

    "medication_id",

    range(1, len(medication_df)+1)

)


medication_df.to_csv(

    f"{output_folder}/medications.csv",

    index=False

)


print("Medications dataset generated successfully!")