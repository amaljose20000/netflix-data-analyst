import pandas as pd
import sqlite3
df = pd.read_csv("netflix_titles.csv", encoding="latin1")
cols = ["show_id","type","title","director","cast","country","date_added","release_year","rating","duration","listed_in","description"]
df = df[cols]
df["director"] = df["director"].fillna("Unknown")
df["country"] = df["country"].fillna("Unknown")
df["rating"] = df["rating"].fillna("Not Rated")
conn = sqlite3.connect("netflix.db")
df.to_sql("netflix", conn, if_exists="replace", index=False)
conn.commit()
conn.close()
print("Done! netflix.db created. Total rows:", len(df))
