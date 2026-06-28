# Netflix Content Analysis
A data analyst project using SQL and Python to analyze 8,809 Netflix titles.

## Business Questions Answered
- Does Netflix focus more on Movies or TV Shows?
- Which countries produce the most content?
- How has Netflix content grown year by year?
- Who are the top directors on Netflix?
- What content ratings dominate the platform?

## Key Findings
- Netflix has 6,132 Movies and 2,677 TV Shows — Movies dominate 70% of content
- United States leads with 2,819 titles — India is second with 972
- Netflix peaked at 1,147 new titles in 2018
- TV-MA is the most common rating — Netflix targets adult audiences
- Martin Scorsese and Steven Spielberg are among top directors

## Tech Stack
- Python (Pandas, Matplotlib)
- SQLite (SQL queries)
- Kaggle Dataset: Netflix Movies and TV Shows

## Project Structure
- setup.py — loads CSV into SQLite database
- queries.py — 5 SQL analysis queries
- visualize.py — 4 charts (bar, line, horizontal bar)
- netflix.db — SQLite database
- charts — PNG visualizations

## How to Run
pip install pandas matplotlib
python setup.py
python queries.py
python visualize.py
