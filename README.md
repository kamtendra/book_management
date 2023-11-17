# Book Management | Codemonk

This is a Django project using Django Rest Framework for building a RESTful API.

## Prerequisites

- Python (3.x)
- Pipenv (optional, but recommended for virtual environment management)

## Getting Started

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/your-repo.git
    cd your-repo
    ```

2. **Set up a virtual environment:**

    ```bash
    # If using Pipenv
    pipenv install

    # If using virtualenv
    python -m venv <your_virtual_environment>
    source <your_virtual_environment>/bin/activate  # On Linux/Mac
    .\your_virtual_environment\Scripts\activate  # On Windows
    pip install -r requirements.txt
    ```

3. **Install and run Redis:**

    Ensure that [Redis](https://redis.io/download) is installed and running locally.

4. **Run Migrations:**

    ```bash
    python manage.py migrate
    ```

5. **Create a superuser:**

    ```bash
    python manage.py createsuperuser
    ```

6. **Start Celery worker and beat:**

    ```bash
    celery -A <your_project_name> worker --loglevel=info
    celery -A <your_project_name> beat --loglevel=info
    ```

7. **Run the development server:**

    ```bash
    python manage.py runserver
    ```

8. **Access the API documentation:**

    - Open your browser and go to `http://127.0.0.1:8000/api/docs/` for Django Rest Framework documentation.
    - For Swagger/OpenAPI documentation, visit `http://127.0.0.1:8000/api/swagger/`.

## Environment Variables

Make sure to set the following environment variables:

- `DJANGO_SETTINGS_MODULE`: Set it to `<your_project_name>.settings` (e.g., `your_project.settings`).


