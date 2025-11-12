import pandas as pd
import matplotlib.pyplot as plt
import os

# ✅ Helper function: auto-rename if file exists
def get_unique_filename(filename):
    base, ext = os.path.splitext(filename)
    counter = 1
    new_filename = filename
    while os.path.exists(new_filename):
        new_filename = f"{base}_{counter}{ext}"
        counter += 1
    return new_filename

# ✅ Read CSV with tab separator
df = pd.read_csv("sales.csv", sep="\t")

# ✅ Clean data
df['amount'] = pd.to_numeric(df['amount'], errors='coerce')
df = df.dropna(subset=['amount'])
df['amount'] = df['amount'].astype(int)

# ✅ Save cleaned data (auto-rename if existing)
cleaned_file = get_unique_filename("sales_cleaned.csv")
df.to_csv(cleaned_file, index=False)

# ✅ Summary per product
summary = df.groupby('product')['amount'].sum().reset_index()

# ✅ Save summary text (auto-rename)
summary_file = get_unique_filename("summary.txt")
with open(summary_file, "w") as f:
    for _, row in summary.iterrows():
        f.write(f"{row['product']}: {row['amount']}\n")

# ✅ Generate bar chart
plt.figure(figsize=(6, 4))
plt.bar(summary['product'], summary['amount'], color='skyblue')
plt.title("Total Sales per Product")
plt.xlabel("Product")
plt.ylabel("Total Amount")

# ✅ Save chart (auto-rename)
chart_file = get_unique_filename("sales_chart.png")
plt.savefig(chart_file)
plt.close()

print(f"\n✅ Done! Files generated:")
print(f"- {cleaned_file}")
print(f"- {summary_file}")
print(f"- {chart_file}")
