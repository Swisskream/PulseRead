import json
import boto3
import os

bedrock_runtime = boto3.client('bedrock-runtime', region_name='us-west-2')
s3 = boto3.client('s3')

def lambda_handler(event, context):
    # 1. Extract the S3 object info from the event
    record = event['Records'][0]
    bucket = record['s3']['bucket']['name']
    key = record['s3']['object']['key']

    # 2. Read the content of the file
    response = s3.get_object(Bucket=bucket, Key=key)
    raw_text = response['Body'].read().decode('utf-8')

    # 3. Create prompt for Bedrock
    prompt = f"Summarize the following customer feedback:\n\n{raw_text}\n\nSummary:"

    # 4. Call Bedrock model
    bedrock_response = bedrock_runtime.invoke_model(
        modelId='amazon.titan-text-lite-v1',
        body=json.dumps({"prompt": prompt, "max_tokens": 200}),
        contentType='application/json'
    )

    result = json.loads(bedrock_response['body'].read())
    summary = result.get('completion', '[No summary returned]')

    # 5. Save summary to second S3 bucket
    summary_bucket = 'pulseread-summary-bucket'
    summary_key = key.replace(".txt", "_summary.txt")

    s3.put_object(
        Bucket='pulseread-summary-bucket',
        Key=summary_key,
        Body=summary.encode('utf-8')
    )

    # 6. Log result (can extend to another S3 bucket or DynamoDB)
    print(f"Summary:\n{summary}")

    return {
        'statusCode': 200,
        'body': json.dumps({'summary': summary})
    }

