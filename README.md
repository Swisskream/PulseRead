# PulseRead

Real-time AI-powered insights from long-term content - at scale and in real time.

PulseRead is a fully serverless web application designed to help users quickly extract key information from lengthy text-based files. Whether you're processing product reviews, support emails, research notes, or feedback surveys, PulseRead uses AWS-powered AI to generate concise summaries that surface the most relevant ideas.

This project began as an experiment with Amazon Bedrock, and evolved into a full-stack experience with both cloud-native infrastructure and a user-friendly React frontend.

### Tech Stack
**Frontend**
- **React** - Interactive UI with ligh/dark mode
- **API Gateway** - Secure interface between client and backend

**Backend**
- **AWS S3** – Store raw input and summary output  
- **AWS Lambda** – Process inputs and invoke Bedrock  
- **Amazon Bedrock** – Summarize customer feedback  
- **DynamoDB** - Stores summary metadata
- **Terraform** – Infrastructure as code  
- **Python** – Lambda logic and text utils  

### Key Features
- Upload .txt files directly in the browser
- Summarized output using AI in seconds
- Toggle between light and dark UI modes
- Stores summaries and metadata for future extension
- Fully deployable via Terraform

https://jkinthecloud.com/PulseRead