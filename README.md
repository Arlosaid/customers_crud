# Lambda CRUD Project

This project is an integrative CRUD exposed via API Gateway that uses AWS Lambda and MySQL to manage customer data. Below are the instructions for setting up the environment, installing dependencies, running migrations with Alembic, and deploying with Serverless.

## Project Structure

lambda_crud/
├── .serverless/
├── alembic/
│ ├── versions/
│ │ └── 82a22c93777c_customer_table.py
│ ├── env.py
│ ├── README
│ └── script.py.mako
├── app/
│ ├── pycache/
│ └── api/
│ ├── pycache/
│ ├── init.py
│ ├── controller.py
│ ├── repository.py
│ └── schemas.py
├── db/
│ ├── pycache/
│ ├── init.py
│ ├── app_lambda.py
│ ├── database.py
│ ├── model.py
│ ├── settings.py
├── venv/
├── .env
├── .gitignore
├── alembic.ini
├── global-bundle.pem
├── package.json
├── package-lock.json
├── README.md
├── requirements.txt
├── schema.sql
└── serverless.yml

perl
Copiar código

## Environment Setup

1. **Clone the repository**:
    ```bash
    git clone https://github.com/your-username/your-repo.git
    cd your-repo
    ```

2. **Create and activate a virtual environment**:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Configure environment variables**:
    Create a `.env` file in the root of the project with the following variables:
    ```env
    DATABASE_URL=mysql+pymysql://user:password@localhost/database_name
    ```

## Alembic Migrations

1. **Initialize Alembic**:
    If Alembic is not initialized, run:
    ```bash
    alembic init alembic
    ```

2. **Create a new migration**:
    ```bash
    alembic revision --autogenerate -m "Migration comment"
    ```

3. **Apply the migrations**:
    ```bash
    alembic upgrade head
    ```

## Deployment with Serverless

1. **Install Serverless**:
    ```bash
    npm install -g serverless
    ```

2. **Configure AWS CLI**:
    Make sure your AWS credentials are configured. If not, configure them with:
    ```bash
    aws configure
    ```

3. **Deploy the service**:
    ```bash
    serverless deploy
    ```

## Usage

To test the project, you can use tools like Postman or cURL to make requests to the endpoints exposed by API Gateway.