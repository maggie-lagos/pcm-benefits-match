# pcm-benefits-match
Web application to manage transactions for the Petworth Community Market benefits matching program.


### Getting Started

1. Set your docker environment variables
    ```bash
    DJANGO_SECRET_KEY=mysecretkey
    DEBUG=True
    DJANGO_LOGLEVEL=info
    DJANGO_ALLOWED_HOSTS=localhost
    DATABASE_ENGINE=postgresql_psycopg2
    DATABASE_NAME=benefitsmatch
    DATABASE_USERNAME=dbuser
    DATABASE_PASSWORD=dbpassword
    DATABASE_HOST=db
    DATABASE_PORT=5432
    ```

1. Start the compose stack
    ```bash
    docker compose up --build
    ```

1. Navigate your browser to:
```
localhost:80
```

### AWS Deployment

```
# Get the ECR repository URL from the output
export ECR_REPO=$(terraform output -raw ecr_repository_url)

# Login to ECR
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin $ECR_REPO

# Build your Docker image
cd backend
docker build -t $ECR_REPO:latest .

# Push the image to ECR
docker push $ECR_REPO:latest
```
