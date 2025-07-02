# PulseRead

Real-time AI-powered insights from customer feedback, at scale.

PulseRead is a serverless AWS solution that automatically ingests, processes, and summarizes user-generated content—such as product reviews, social media posts, or form submissions. Using Amazon S3 for storage, AWS Lambda for event-driven compute, and Amazon Bedrock for text summarization, PulseRead empowers teams to extract concise, actionable insights from noisy raw text.

### Tech Stack
- **AWS S3** – Store raw input and summary output  
- **AWS Lambda** – Process inputs and invoke Bedrock  
- **Amazon Bedrock** – Summarize customer feedback  
- **Terraform** – Infrastructure as code  
- **Python** – Lambda logic and text utils  