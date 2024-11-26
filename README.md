# Thinking Machines DE Take Home

## Introduction
Hi! This repository was my attempt in landing a Data Engineering role in Thinking Machines. List of instructions are listed in the pdf: `Data Engineer Take-Home Exam.pdf`

## Directory Structure
- `images` - auxilliary images + drawio file of the architecture
- `Part 1` - part 1 of take home
    - `primes.ipynb` - Markdown of problem + solution + references
- `Part 2` - part 2 of take home
    - `ETL+webserver.ipynb` - notebook with markdowns explaining how I ETL'd the source dataset and how to setup the webserver API
    - `env_sample` - what your `.env` personal file should look like
    - `app` - fastapi source code in fetching per user filtered view of check-ins
        - `models` - pydantic dataclasses
        - `repository` - handler for postgres using psycopg2
        - `logger` - logging utilities
        - `main.py` - entrypoint
    - `tests` - tests for fast api app, details and screenshots of tests in `ETL+webserver.ipynb` under Appendix Section.
    - `scripts` - dockerfiles and scripts to build, start and cleanup
      
## Take Home Exam Architecture
- Everything is hosted on an EC2 instance on my Personal AWS Account
    - Interactive ETL with Spark + Jupyter (I would do EMR if I wasn't so cheap but in this usecase a single EC2 instance will suffice)
    - Database hosting with Postgres
    - Web server API with Fast API
- Domain is hosted via Route53 and routed to the Elastic Public IP Domain of the EC2 instance with select ports exposed via security groups

![My Image](images/TMDE.png)

## Results
I thought I did a great effort in this job attempt and my answers here are sufficient enough for a seasoned Data Engineer. Unfortunately Thinking Machines didn't select me for the role, might be because of the panel interview section
but maybe it just wasn't meant to be.