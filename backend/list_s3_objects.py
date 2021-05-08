import boto3
import json

bucket = "dev-image-repo-bucket"
s3 = boto3.client("s3")


def list(event, context):
    try:
        body = s3.list_objects_v2(Bucket=bucket)

        response = {
            "statusCode": 200,
            "headers": {"Access-Control-Allow-Origin": "*"},
            "body": json.dumps(body, default=str),
        }
    except Exception as e:
        response = {
            "statusCode": 500,
            "headers": {"Access-Control-Allow-Origin": "*"},
            "body": json.dumps({"error": str(e)}),
        }
    finally:
        return response
