import sqlite3
import pandas as pd
conn = sqlite3.connect("netflix.db")

print("Q1: Movies vs TV Shows")
q1 = pd.read_sql_query("SELECT type, COUNT(*) AS total FROM netflix GROUP BY type ORDER BY total DESC", conn)
print(q1.to_string(index=False))

print("\nQ2: Top 10 countries")
q2 = pd.read_sql_query("SELECT country, COUNT(*) AS total FROM netflix WHERE country != \"Unknown\" GROUP BY country ORDER BY total DESC LIMIT 10", conn)
print(q2.to_string(index=False))

print("\nQ3: Content by year")
q3 = pd.read_sql_query("SELECT release_year, COUNT(*) AS total FROM netflix WHERE release_year >= 2010 GROUP BY release_year ORDER BY release_year DESC LIMIT 10", conn)
print(q3.to_string(index=False))

print("\nQ4: Top 10 directors")
q4 = pd.read_sql_query("SELECT director, COUNT(*) AS total FROM netflix WHERE director != \"Unknown\" GROUP BY director ORDER BY total DESC LIMIT 10", conn)
print(q4.to_string(index=False))

print("\nQ5: Most common ratings")
q5 = pd.read_sql_query("SELECT rating, COUNT(*) AS total FROM netflix GROUP BY rating ORDER BY total DESC", conn)
print(q5.to_string(index=False))

conn.close()
print("\nDone!")
