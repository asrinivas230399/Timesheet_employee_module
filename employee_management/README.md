# Employee Management Module

This project is a web application for managing employee data, including displaying, editing, and adding employee records, as well as collecting feedback. It is built using FastAPI and Jinja2 for templating.

## Features

- Display employee data with filters for name, position, and status.
- Edit employee records.
- Add new employee records.
- Submit feedback through a form.
- Load testing using Locust.

## Setup

1. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

2. Run the application:

   ```bash
   uvicorn app.main:app --reload
   ```

3. Access the application at `http://localhost:8000/employees`.

## Load Testing

To run load tests, use Locust:

```bash
locust -f app/locustfile.py
```

## Feedback

Feedback can be submitted through the `/feedback` endpoint.

## Review

This interface is ready for review by the PMO Team and Managers. Please provide feedback through the feedback form or contact the development team directly.
