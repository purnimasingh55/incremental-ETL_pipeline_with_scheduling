# Incremental ETL Pipeline with Scheduling

## Project Overview
This project demonstrates an **Incremental ETL (Extract, Transform, Load) Pipeline** with automated scheduling.  
The pipeline processes only newly added or updated records instead of reprocessing the entire dataset every time, improving efficiency and reducing execution time.

This mini project was created for practice purposes to understand:
- ETL workflow
- Incremental data loading
- Data transformation
- Workflow scheduling and automation
- Basic data engineering concepts

---

## Features
- Incremental data extraction
- Data transformation and cleaning
- Automated scheduled execution
- Logging and monitoring
- Efficient handling of new records
- Modular and reusable pipeline structure

---

## Tech Stack
- Python
- Pandas
- SQL / Database
- Scheduler (Cron / Airflow / Task Scheduler)
- CSV / Database Storage

---

## Project Structure

incremental-ETL_pipeline_with_scheduling/
│
├── data/                 # Input and output datasets
├── scripts/              # ETL scripts
├── logs/                 # Log files
├── scheduler/            # Scheduling configuration
├── requirements.txt      # Project dependencies
├── main.py               # Main pipeline execution file
└── README.md

---

## ETL Workflow

### 1. Extract
- Reads data from the source system/files/database
- Identifies newly added records using incremental logic

### 2. Transform
- Cleans and processes the data
- Handles missing values and formatting
- Applies required business rules

### 3. Load
- Loads transformed data into the target destination
- Avoids duplicate processing of already loaded records

### 4. Scheduling
- Automates the pipeline execution at regular intervals
- Ensures continuous and efficient data updates

---

## Incremental Loading Logic
The pipeline processes only:
- Newly inserted records
- Updated records since the last execution

### Benefits
- Faster execution
- Reduced resource consumption
- Better scalability

---

## How to Run the Project

### Clone the Repository

```bash
git clone https://github.com/purnimasingh55/incremental-ETL_pipeline_with_scheduling.git
```
## Navigate to the Project Folder

```bash
cd incremental-ETL_pipeline_with_scheduling
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Run the Pipeline

```bash
python main.py
```

---

## Future Improvements

- Add Airflow DAG implementation
- Cloud deployment
- Real-time streaming support
- Email alerts for pipeline failures
- Docker containerization
- Unit testing and CI/CD integration

---

## Learning Outcomes

Through this project, I learned:

- How ETL pipelines work
- Incremental data processing concepts
- Workflow automation and scheduling
- Data transformation techniques
- Writing modular and maintainable Python code

---

## Author

**Purnima Singh**
