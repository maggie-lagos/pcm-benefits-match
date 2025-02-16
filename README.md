# pcm-benefits-match
Webapp for managing the Petworth Community Market benefits matching program

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

