# local-stack-fastapi

Fastapi integration with localstack

## Running the project

1. Clone the repository
2. Run `docker-compose up` to start the localstack services
3. Create an aws user

```shell
aws --endpoint-url=http://localhost:4566 iam create-user --user-name <name>
```

4. Create an access key for the user

```shell
aws --endpoint-url=http://localhost:4566 iam create-access-key --user-name <name>
```

5. Create a bucket with read and write permissions

```shell
aws --endpoint-url=http://localhost:4566 s3api create-bucket --bucket localstack-bucket
aws --endpoint-url=http://localhost:4566 s3api put-bucket-acl --bucket localstack-bucket --acl public-read
```

6. Create a `.env` file in the root of the project with the following content:

```shell
AWS_ACCESS_KEY_ID=<access key from localstack>
AWS_SECRET_ACCESS_KEY=<secret key from localstack>
AWS_DEFAULT_REGION="us-east-1"
AWS_BUCKET_NAME="localstack-bucket"
```

7. Run fastapi with `fastapi dev app/app.py`
8. Access the swagger documentation at `http://localhost:8000/docs`
