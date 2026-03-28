import pandas as pd
from database import engine, SessionLocal
from models import Base, Item

Base.metadata.create_all(bind=engine)

# Load CSV
df = pd.read_csv(r"C:\Users\satya\Downloads\test_item.csv")

db = SessionLocal()

# Optional: clear old data
db.query(Item).delete()

for _, row in df.iterrows():

    # Handle NaN safely
    stock_value = row["Stock On Hand"]

    if pd.isna(stock_value):
        stock_value = 0   # default value

    item = Item(
        item_code=int(row["Item ID"]),
        name=str(row["Item ID2"]),
        stock=int(stock_value)
    )

    db.add(item)

db.commit()
db.close()

print("✅ Data Loaded Successfully into MySQL")