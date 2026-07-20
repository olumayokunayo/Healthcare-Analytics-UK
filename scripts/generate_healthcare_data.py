import pandas as pd
import os


# Create output folder if it does not exist
output_folder = "data/raw"

os.makedirs(output_folder, exist_ok=True)


# =====================================================
# HOSPITALS
# =====================================================

hospitals = [
    ["University Hospital Coventry", "University Hospitals Coventry and Warwickshire NHS Trust", "Coventry", "West Midlands", "CV2 2DX", "NHS Trust", 1250, 1976],
    ["Queen Elizabeth Hospital Birmingham", "University Hospitals Birmingham NHS Foundation Trust", "Birmingham", "West Midlands", "B15 2GW", "NHS Trust", 1213, 2010],
    ["St Thomas' Hospital", "Guy's and St Thomas' NHS Foundation Trust", "London", "London", "SE1 7EH", "NHS Trust", 840, 1843],
    ["Guy's Hospital", "Guy's and St Thomas' NHS Foundation Trust", "London", "London", "SE1 9RT", "NHS Trust", 600, 1721],
    ["Addenbrooke's Hospital", "Cambridge University Hospitals NHS Foundation Trust", "Cambridge", "East England", "CB2 0QQ", "NHS Trust", 1100, 1766],
    ["Royal Free Hospital", "Royal Free London NHS Foundation Trust", "London", "London", "NW3 2QG", "NHS Trust", 839, 1828],
    ["Manchester Royal Infirmary", "Manchester University NHS Foundation Trust", "Manchester", "North West", "M13 9WL", "NHS Trust", 800, 1752],
    ["Leeds General Infirmary", "Leeds Teaching Hospitals NHS Trust", "Leeds", "Yorkshire", "LS1 3EX", "NHS Trust", 900, 1771],
    ["Nottingham City Hospital", "Nottingham University Hospitals NHS Trust", "Nottingham", "East Midlands", "NG5 1PB", "NHS Trust", 1300, 1903],
    ["John Radcliffe Hospital", "Oxford University Hospitals NHS Foundation Trust", "Oxford", "South East", "OX3 9DU", "NHS Trust", 1000, 1979],
    ["Royal Stoke University Hospital", "University Hospitals of North Midlands NHS Trust", "Stoke-on-Trent", "West Midlands", "ST4 6QG", "NHS Trust", 1200, 2015],
    ["Leicester Royal Infirmary", "University Hospitals of Leicester NHS Trust", "Leicester", "East Midlands", "LE1 5WW", "NHS Trust", 850, 1771],
    ["Southmead Hospital", "North Bristol NHS Trust", "Bristol", "South West", "BS10 5NB", "NHS Trust", 800, 2014],
    ["University Hospital Southampton", "University Hospital Southampton NHS Foundation Trust", "Southampton", "South East", "SO16 6YD", "NHS Trust", 1200, 2012],
    ["King's College Hospital", "King's College Hospital NHS Foundation Trust", "London", "London", "SE5 9RS", "NHS Trust", 950, 1840],
    ["University College Hospital", "University College London Hospitals NHS Foundation Trust", "London", "London", "NW1 2BU", "NHS Trust", 800, 2005],
    ["Royal Victoria Infirmary", "The Newcastle upon Tyne Hospitals NHS Foundation Trust", "Newcastle", "North East", "NE1 4LP", "NHS Trust", 900, 1906],
    ["Royal Hallamshire Hospital", "Sheffield Teaching Hospitals NHS Foundation Trust", "Sheffield", "Yorkshire", "S10 2JF", "NHS Trust", 750, 1979]
]


hospital_df = pd.DataFrame(
    hospitals,
    columns=[
        "hospital_name",
        "nhs_trust",
        "city",
        "region",
        "postcode",
        "hospital_type",
        "bed_capacity",
        "established_year"
    ]
)

hospital_df.insert(0, "hospital_id", range(1, len(hospital_df)+1))


hospital_df.to_csv(
    f"{output_folder}/hospitals.csv",
    index=False
)



# =====================================================
# DEPARTMENTS
# =====================================================

departments = [
    ["Cardiology","CARD","Cardiovascular"],
    ["Oncology","ONCO","Cancer Care"],
    ["Emergency Medicine","EMER","Emergency Care"],
    ["Neurology","NEUR","Neurological Care"],
    ["Orthopaedics","ORTH","Musculoskeletal"],
    ["General Surgery","SURG","Surgery"],
    ["Paediatrics","PAED","Children"],
    ["Obstetrics and Gynaecology","OBGY","Women's Health"],
    ["Respiratory Medicine","RESP","Respiratory"],
    ["Gastroenterology","GAST","Digestive Health"],
    ["Endocrinology","ENDO","Hormonal Disorders"],
    ["Nephrology","NEPH","Kidney Care"]
]


department_df = pd.DataFrame(
    departments,
    columns=[
        "department_name",
        "department_code",
        "clinical_specialty"
    ]
)

department_df.insert(0,"department_id",range(1,len(department_df)+1))


department_df.to_csv(
    f"{output_folder}/departments.csv",
    index=False
)



# =====================================================
# INSURANCE PROVIDERS
# =====================================================

insurance = [
    ["NHS","Public","UK"],
    ["Bupa","Private","UK"],
    ["AXA Health","Private","UK"],
    ["Aviva Health","Private","UK"],
    ["Vitality Health","Private","UK"],
    ["WPA","Private","UK"],
    ["Self Pay","Private","UK"]
]


insurance_df = pd.DataFrame(
    insurance,
    columns=[
        "provider_name",
        "provider_type",
        "contact_region"
    ]
)

insurance_df.insert(0,"insurance_id",range(1,len(insurance_df)+1))


insurance_df.to_csv(
    f"{output_folder}/insurance_providers.csv",
    index=False
)



print("Reference data generated successfully!")