import pandas as pd
import random
import os
from faker import Faker
from datetime import timedelta


# =====================================================
# INITIAL SETUP
# =====================================================

fake = Faker("en_GB")

output_folder = "data/raw"

os.makedirs(output_folder, exist_ok=True)


NUMBER_OF_BILLS = 50000



# =====================================================
# LOAD ADMISSIONS DATA
# =====================================================

admissions = pd.read_csv(
    "data/raw/admissions.csv"
)


print(
    f"Loaded {len(admissions)} admissions records"
)



# =====================================================
# INSURANCE PROVIDERS
# Matches insurance_providers table IDs
# =====================================================

insurance_ids = [
    1,  # NHS
    2,  # Bupa
    3,  # AXA Health
    4,  # Aviva Health
    5,  # Vitality Health
    6,  # WPA
    7   # Self Pay
]



# =====================================================
# GENERATE BILLING DATA
# =====================================================

billing_data = []


for i in range(1, NUMBER_OF_BILLS + 1):


    # Select existing admission
    admission = admissions.sample(1).iloc[0]


    admission_date = pd.to_datetime(
        admission["admission_date"]
    )


    # Treatment cost
    treatment_cost = round(
        random.uniform(500, 20000),
        2
    )


    # Insurance covers 70-100%
    claim_percentage = random.uniform(
        0.70,
        1.00
    )


    claim_amount = round(
        treatment_cost * claim_percentage,
        2
    )


    payment_status = random.choice(
        [
            "Paid",
            "Pending",
            "Rejected"
        ]
    )


    payment_method = random.choice(
        [
            "Insurance",
            "NHS Funding",
            "Self Pay"
        ]
    )


    payment_date = (
        admission_date +
        timedelta(
            days=random.randint(5,90)
        )
    )


    billing_data.append(
        [
            i,
            admission["admission_id"],
            random.choice(insurance_ids),
            fake.bothify(
                text="INV-#######"
            ),
            treatment_cost,
            claim_amount,
            payment_status,
            payment_method,
            payment_date.date()
        ]
    )



# =====================================================
# CREATE DATAFRAME
# =====================================================

billing_df = pd.DataFrame(
    billing_data,
    columns=[
        "billing_id",
        "admission_id",
        "insurance_id",
        "invoice_number",
        "treatment_cost",
        "claim_amount",
        "payment_status",
        "payment_method",
        "payment_date"
    ]
)



# =====================================================
# EXPORT CSV
# =====================================================

billing_df.to_csv(
    f"{output_folder}/billing.csv",
    index=False
)



print(
    "Billing dataset generated successfully!"
)

print(
    f"Created {len(billing_df)} billing records"
)