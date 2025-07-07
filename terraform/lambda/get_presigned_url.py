import json
import boto3
import os

s3 = boto3.client('s3')
bucket_name = os.environ.get('INPUT_BUCKET_NAME', 'pulseread-input-bucket')

def lambda_handler(event, context):
    filename = event['queryStringParameters'].get('filename')

    if not filename:
        return {
            'statusCode': 400,
            'body': json.dumps({'error': 'Filename is required'})
        }
    
    presigned_url = s3.generate_presigned_url(
        'put_object',
        Params={'Bucket': bucket_name, 'Key': filename, 'ContentType': 'text/plain'},
        ExpiresIn=300
    )

    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Origin': '*'
        },
        'body': json.dumps({'url': presigned_url})
    }