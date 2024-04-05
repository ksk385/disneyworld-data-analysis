### Disney World Activity Data Analysis

This is a project for me to learn some data analysis techniques. The goal is to analyze the activities available at Disney World for an upcoming trip I have to plan. The data is extracted from the Disney World website and saved in `raw-activities-response.json`. The data is then processed and saved in `activities.csv`. The data is then analyzed to answer some questions I have about the activities.

### Getting Started

0. Create a python environment

```bash
python3 -m venv venv
```

1. Activate the python environment

```bash
source venv/bin/activate
```

2. Install the required packages

```bash
pip install -r requirements.txt
```

3. Bring in the raw data from disney world website and save it in `raw-activities-response.json`

4. Run the code

```bash
python process_activities.py
```
