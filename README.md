# Civic Auth Demo Portfolio

This simple Flask application demonstrates how to integrate [Civic](https://www.civic.com/) authentication in a portfolio website. The site lists a few dummy projects and allows users to authenticate using the Civic login widget.

## Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Set environment variables for your Civic app:
   ```bash
   export CIVIC_APP_ID=<your_app_id>
   export FLASK_SECRET=<random_secret>
   ```
3. Run the application:
   ```bash
   python app.py
   ```
   The site will be available at `http://localhost:5000`.

This project uses the Civic JS snippet as described in the [Civic Flask integration docs](https://docs.civic.com/integration/python/flask).
