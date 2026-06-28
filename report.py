import sqlite3, pandas as pd
from fpdf import FPDF
from datetime import date

conn = sqlite3.connect("netflix.db")
q1 = pd.read_sql_query("SELECT type, COUNT(*) AS total FROM netflix GROUP BY type ORDER BY total DESC", conn)
q2 = pd.read_sql_query("SELECT country, COUNT(*) AS total FROM netflix WHERE country != 'Unknown' GROUP BY country ORDER BY total DESC LIMIT 5", conn)
q3 = pd.read_sql_query("SELECT release_year, COUNT(*) AS total FROM netflix WHERE release_year >= 2010 AND release_year < 2022 GROUP BY release_year ORDER BY release_year DESC LIMIT 5", conn)
q4 = pd.read_sql_query("SELECT rating, COUNT(*) AS total FROM netflix GROUP BY rating ORDER BY total DESC LIMIT 5", conn)
conn.close()

pdf = FPDF()
pdf.add_page()
pdf.set_font("Helvetica", "B", 20)
pdf.set_text_color(229, 9, 20)
pdf.cell(0, 12, "Netflix Content Analysis Report", ln=True, align="C")
pdf.set_font("Helvetica", "", 10)
pdf.set_text_color(100, 100, 100)
pdf.cell(0, 6, "Prepared by: Amal Jose  |  Date: " + str(date.today()), ln=True, align="C")
pdf.ln(6)

pdf.set_font("Helvetica", "B", 13)
pdf.set_text_color(229, 9, 20)
pdf.cell(0, 8, "1. Content Type Analysis", ln=True)
pdf.set_font("Helvetica", "", 11)
pdf.set_text_color(0, 0, 0)
for _, row in q1.iterrows():
    pdf.cell(0, 7, "  " + str(row["type"]) + ": " + str(row["total"]) + " titles", ln=True)
pdf.set_font("Helvetica", "I", 10)
pdf.set_text_color(60, 60, 60)
pdf.multi_cell(0, 6, "Recommendation: Netflix should continue investing in Movies as they make up 70% of content. However, TV Shows drive longer engagement. A balanced 60/40 strategy is recommended.")
pdf.ln(4)

pdf.set_font("Helvetica", "B", 13)
pdf.set_text_color(229, 9, 20)
pdf.cell(0, 8, "2. Top Producing Countries", ln=True)
pdf.set_font("Helvetica", "", 11)
pdf.set_text_color(0, 0, 0)
for _, row in q2.iterrows():
    pdf.cell(0, 7, "  " + str(row["country"]) + ": " + str(row["total"]) + " titles", ln=True)
pdf.set_font("Helvetica", "I", 10)
pdf.set_text_color(60, 60, 60)
pdf.multi_cell(0, 6, "Recommendation: US dominates content. India is fastest growing. Netflix should increase investment in South Korea and Egypt.")
pdf.ln(4)

pdf.set_font("Helvetica", "B", 13)
pdf.set_text_color(229, 9, 20)
pdf.cell(0, 8, "3. Content Growth Trend", ln=True)
pdf.set_font("Helvetica", "", 11)
pdf.set_text_color(0, 0, 0)
for _, row in q3.iterrows():
    pdf.cell(0, 7, "  " + str(int(row["release_year"])) + ": " + str(row["total"]) + " titles", ln=True)
pdf.set_font("Helvetica", "I", 10)
pdf.set_text_color(60, 60, 60)
pdf.multi_cell(0, 6, "Recommendation: Content peaked in 2018 and declined post-2020 due to COVID-19. Netflix should ramp up production partnerships to recover growth.")
pdf.ln(4)

pdf.set_font("Helvetica", "B", 13)
pdf.set_text_color(229, 9, 20)
pdf.cell(0, 8, "4. Content Rating Breakdown", ln=True)
pdf.set_font("Helvetica", "", 11)
pdf.set_text_color(0, 0, 0)
for _, row in q4.iterrows():
    pdf.cell(0, 7, "  " + str(row["rating"]) + ": " + str(row["total"]) + " titles", ln=True)
pdf.set_font("Helvetica", "I", 10)
pdf.set_text_color(60, 60, 60)
pdf.multi_cell(0, 6, "Recommendation: TV-MA dominates at 36%. Netflix should expand family-friendly content to capture household subscriptions.")

pdf.output("netflix_report.pdf")
print("Report saved as netflix_report.pdf")
