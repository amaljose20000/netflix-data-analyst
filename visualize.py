import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

conn = sqlite3.connect("netflix.db")

# Chart 1: Movies vs TV Shows
q1 = pd.read_sql_query("SELECT type, COUNT(*) AS total FROM netflix GROUP BY type", conn)
plt.figure(figsize=(6,4))
plt.bar(q1["type"], q1["total"], color=["#E50914","#221F1F"])
plt.title("Netflix: Movies vs TV Shows")
plt.ylabel("Count")
plt.savefig("chart1_type.png", bbox_inches="tight")
plt.close()
print("Chart 1 saved")

# Chart 2: Top 10 countries
q2 = pd.read_sql_query("SELECT country, COUNT(*) AS total FROM netflix WHERE country != \"Unknown\" GROUP BY country ORDER BY total DESC LIMIT 10", conn)
plt.figure(figsize=(10,5))
plt.barh(q2["country"][::-1], q2["total"][::-1], color="#E50914")
plt.title("Top 10 Countries by Netflix Content")
plt.xlabel("Total Titles")
plt.savefig("chart2_countries.png", bbox_inches="tight")
plt.close()
print("Chart 2 saved")

# Chart 3: Content growth by year
q3 = pd.read_sql_query("SELECT release_year, COUNT(*) AS total FROM netflix WHERE release_year >= 2010 AND release_year <= 2021 GROUP BY release_year ORDER BY release_year", conn)
plt.figure(figsize=(10,5))
plt.plot(q3["release_year"], q3["total"], marker="o", color="#E50914", linewidth=2)
plt.fill_between(q3["release_year"], q3["total"], alpha=0.2, color="#E50914")
plt.title("Netflix Content Growth (2010-2021)")
plt.xlabel("Year")
plt.ylabel("Titles Added")
plt.grid(True, alpha=0.3)
plt.savefig("chart3_growth.png", bbox_inches="tight")
plt.close()
print("Chart 3 saved")

# Chart 4: Top ratings
q4 = pd.read_sql_query("SELECT rating, COUNT(*) AS total FROM netflix GROUP BY rating ORDER BY total DESC LIMIT 8", conn)
plt.figure(figsize=(8,5))
plt.bar(q4["rating"], q4["total"], color="#E50914")
plt.title("Netflix Content by Rating")
plt.ylabel("Count")
plt.savefig("chart4_ratings.png", bbox_inches="tight")
plt.close()
print("Chart 4 saved")

conn.close()
print("All charts saved!")
