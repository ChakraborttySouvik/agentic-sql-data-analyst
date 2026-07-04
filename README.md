# 🤖 Agentic SQL Data Analyst

An AI-powered Data Analytics application that converts natural language questions into PostgreSQL SQL queries using Google's Gemini LLM.

The application automatically validates generated SQL, executes safe read-only queries, generates business insights, visualizes results with charts, and exports reports through an interactive Streamlit dashboard.

---

# 🚀 Features

- Natural Language to SQL using Google Gemini
- FastAPI REST Backend
- Streamlit Interactive Frontend
- PostgreSQL Database Integration
- Automatic SQL Validation
- SQL Auto-Correction
- Business Insight Generation
- Interactive Data Visualization
- Automatic Chart Generation
- Report Export
- Conversation Memory
- Secure Read-Only SQL Execution
- Dashboard Analytics

---

# 🏗️ System Architecture

```

User Question
│
▼
Streamlit Frontend
│
▼
FastAPI Backend
│
▼
Google Gemini LLM
│
▼
SQL Generator
│
▼
SQL Validator
│
▼
PostgreSQL Database
│
▼
Query Execution
│
▼
Business Insights
│
▼
Charts & Reports

```

---

# 🛠️ Tech Stack

| Category | Technology |
|----------|------------|
| Language | Python |
| Frontend | Streamlit |
| Backend | FastAPI |
| Database | PostgreSQL |
| LLM | Google Gemini |
| Framework | LangChain |
| Data Processing | Pandas |
| Visualization | Plotly, Matplotlib |
| SQL Driver | Psycopg2 |
| Authentication | Environment Variables |
| Version Control | Git & GitHub |

---

# 📂 Project Structure

```

agentic-sql-data-analyst/

├── agent1/
│ ├── chart_generator.py
│ ├── correction_loop.py
│ ├── export_report.py
│ ├── insights.py
│ ├── memory.py
│ ├── tools.py
│ └── agent_controller.py
│
├── api/
│ └── main.py
│
├── practice/
│ ├── customers.csv
│ ├── orders.csv
│ ├── products.csv
│ ├── order_items.csv
│ ├── sql_generator.py
│ ├── sql_validator.py
│ ├── run_query.py
│ ├── schema_reader.py
│ └── load_data.py
│
├── app.py
├── main.py
├── requirements.txt
├── README.md
└── .env.example

```

---

# ⚙️ Installation

## Clone Repository

```bash
git clone https://github.com/yourusername/agentic-sql-data-analyst.git

cd agentic-sql-data-analyst
```

---

## Create Virtual Environment

### Windows

```bash
python -m venv venv

venv\Scripts\activate
```

### Linux / Mac

```bash
python3 -m venv venv

source venv/bin/activate
```

---

## Install Requirements

```bash
pip install -r requirements.txt
```

---

# 🔑 Configure Environment Variables

Create a `.env` file.

Example:

```env
GOOGLE_API_KEY=YOUR_GEMINI_API_KEY

DB_HOST=localhost
DB_PORT=5432
DB_NAME=agentic_sql_analyst
DB_USER=postgres
DB_PASSWORD=your_password

APP_USERNAME=admin
APP_PASSWORD=admin123
```

---

# 🗄️ Load Sample Database

Move into the practice folder

```bash
cd practice
```

Load sample data

```bash
python load_data.py
```

---

# ▶️ Run Backend

```bash
uvicorn api.main:app --reload
```

Backend URL

```
http://127.0.0.1:8000
```

Swagger API Documentation

```
http://127.0.0.1:8000/docs
```

---

# ▶️ Run Frontend

```bash
streamlit run app.py
```

---

# 💬 Example Questions

```
Show all orders

Show total revenue

Show revenue by category

Show revenue by country

Show top 5 products by revenue

Show monthly sales

Show top customers

Show delivered orders

Show highest selling products

Show average order value
```

---

# 📊 Dashboard Features

✅ KPI Cards

- Total Revenue
- Total Orders
- Total Customers
- Total Products

✅ Charts

- Revenue by Category
- Revenue by Country
- Top Products
- Orders by Status

✅ Analysis

- SQL Generation
- Query Result Table
- Business Insights
- Export Report

---

# 🔒 SQL Safety

Only Read-Only SQL queries are allowed.

Blocked SQL statements:

- DELETE
- UPDATE
- INSERT
- DROP
- ALTER
- CREATE
- TRUNCATE

---

# 📷 Screenshots

Create an `images` folder.

Example:

```
images/

login.png

dashboard.png

sql.png

result.png

chart.png

report.png
```


## Login

<img width="1910" height="915" alt="msedge_2HqDN7GDkn" src="https://github.com/user-attachments/assets/8a97a99d-e521-430d-9a47-385fa100db47" />



## Dashboard

<img width="1910" height="915" alt="image" src="https://github.com/user-attachments/assets/11cddbef-4682-4be3-a960-b3f330fb8df9" />


## SQL Generation

<img width="1600" height="1203" alt="WhatsApp Image 2026-07-03 at 1 08 26 PM" src="https://github.com/user-attachments/assets/08f6e51c-1524-4e82-a964-56600e9beba1" />

## Query Result

<img width="1600" height="1331" alt="WhatsApp Image 2026-07-03 at 1 09 36 PM" src="https://github.com/user-attachments/assets/51b56bcf-1913-4f3f-9aab-3dcd54b3adfa" />


# Charts

<img width="1600" height="1454" alt="WhatsApp Image 2026-07-03 at 1 12 08 PM" src="https://github.com/user-attachments/assets/03fb6512-61a4-4f73-96f5-46de1186f62b" />




# 📈 Workflow

```
User Question

↓

Streamlit UI

↓

FastAPI API

↓

Google Gemini

↓

SQL Generation

↓

SQL Validation

↓

PostgreSQL

↓

Query Result

↓

Business Insight

↓

Chart Generation

↓

Export Report
```

---

# 🎯 Future Enhancements

- Retrieval-Augmented Generation (RAG)
- Multi-PDF Knowledge Base
- Multi-Agent Workflow
- User Authentication with JWT
- Cloud Deployment
- Docker Support
- Role-Based Access
- Dashboard Filters
- Voice Query Support

---

# 👨‍💻 Author

**Souvik Chakraborty**

PG Diploma in Big Data Analytics (PG-DAC/BDA)

Tech Stack:

Python • SQL • PostgreSQL • FastAPI • Streamlit • LangChain • Google Gemini • Machine Learning • Data Analytics

---

# ⭐ If you like this project

Please consider giving it a ⭐ on GitHub.

---

# 📄 License

This project is developed for educational and portfolio purposes.
