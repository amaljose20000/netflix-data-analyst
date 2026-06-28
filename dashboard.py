import sqlite3
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

conn = sqlite3.connect("netflix.db")

# Get data
q1 = pd.read_sql_query("SELECT type, COUNT(*) AS total FROM netflix GROUP BY type", conn)
q2 = pd.read_sql_query("SELECT country, COUNT(*) AS total FROM netflix WHERE country != \"Unknown\" GROUP BY country ORDER BY total DESC LIMIT 10", conn)
q3 = pd.read_sql_query("SELECT release_year, COUNT(*) AS total FROM netflix WHERE release_year >= 2010 AND release_year <= 2021 GROUP BY release_year ORDER BY release_year", conn)
q4 = pd.read_sql_query("SELECT rating, COUNT(*) AS total FROM netflix GROUP BY rating ORDER BY total DESC LIMIT 8", conn)
conn.close()

# Build dashboard
fig = make_subplots(
    rows=2, cols=2,
    subplot_titles=("Movies vs TV Shows", "Top 10 Countries", "Content Growth 2010-2021", "Content by Rating"),
    specs=[[{"type": "pie"}, {"type": "bar"}], [{"type": "scatter"}, {"type": "bar"}]]
)

# Chart 1 - Pie
fig.add_trace(go.Pie(labels=q1["type"], values=q1["total"], marker_colors=["#E50914","#221F1F"]), row=1, col=1)

# Chart 2 - Bar
fig.add_trace(go.Bar(x=q2["total"], y=q2["country"], orientation="h", marker_color="#E50914"), row=1, col=2)

# Chart 3 - Line
fig.add_trace(go.Scatter(x=q3["release_year"], y=q3["total"], mode="lines+markers", line=dict(color="#E50914", width=2)), row=2, col=1)

# Chart 4 - Bar
fig.add_trace(go.Bar(x=q4["rating"], y=q4["total"], marker_color="#E50914"), row=2, col=2)

fig.update_layout(
    title_text="Netflix Content Analysis Dashboard",
    title_font_size=24,
    showlegend=False,
    height=700,
    paper_bgcolor="#141414",
    plot_bgcolor="#141414",
    font=dict(color="white")
)

fig.write_html("dashboard.html")
print("Dashboard saved as dashboard.html")
