import pandas as pd
import os


output_folder = "data/raw"

os.makedirs(output_folder, exist_ok=True)


diagnoses = [

    ["Hypertension", "Cardiovascular"],
    ["Heart Failure", "Cardiovascular"],
    ["Stroke", "Neurological"],
    ["Epilepsy", "Neurological"],
    ["Brain Tumour", "Neurological"],

    ["Breast Cancer", "Oncology"],
    ["Lung Cancer", "Oncology"],
    ["Prostate Cancer", "Oncology"],

    ["Type 2 Diabetes", "Endocrinology"],
    ["Thyroid Disorder", "Endocrinology"],

    ["Pneumonia", "Respiratory"],
    ["Asthma", "Respiratory"],
    ["COPD", "Respiratory"],

    ["Kidney Disease", "Renal"],
    ["Kidney Failure", "Renal"],

    ["Hip Fracture", "Orthopaedics"],
    ["Bone Injury", "Orthopaedics"],

    ["Appendicitis", "General Surgery"],
    ["Gallstones", "General Surgery"],

    ["Routine Health Check", "Preventive Care"]

]


diagnosis_df = pd.DataFrame(

    diagnoses,

    columns=[

        "diagnosis_name",
        "category"

    ]

)


diagnosis_df.insert(

    0,

    "diagnosis_id",

    range(1, len(diagnosis_df)+1)

)


diagnosis_df.to_csv(

    f"{output_folder}/diagnoses.csv",

    index=False

)


print("Diagnoses dataset generated successfully!")