import pandas as pd
import requests

# Load Excel
df = pd.read_excel(r"C:\Users\satya\Downloads\Test Message.xlsx")

print("Columns:", df.columns)

url = "http://127.0.0.1:8000/chat"

results = []

for _, row in df.iterrows():
    message = row["Whatsapp Message"]   # ✅ FIXED

    try:
        res = requests.post(url, json={"message": message})
        output = res.json()
        status = "PASS"
    except Exception as e:
        output = str(e)
        status = "FAIL"

    results.append({
        "message": message,
        "response": output,
        "status": status
    })

pd.DataFrame(results).to_excel("output_results.xlsx", index=False)

print("✅ Testing Completed")