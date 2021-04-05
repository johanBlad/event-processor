# Bucket for Templates
aws s3 mb s3://event-processor-sqs
aws s3 rb s3://event-processor-sqs [--force]


aws cloudformation package \
    --s3-bucket event-processor-sqs \
    --template-file template.yml \
    --output-template-file dist/template-packaged.yml

aws cloudformation deploy \
    --template-file dist/template-packaged.yml \
    --stack-name event-processor-sqs \
    --capabilities CAPABILITY_IAM 


# Can only be used without SAM templates
aws cloudformation create-stack \
    --stack-name event-processor-sqs \
    --template-body file://template.yml \
    --capabilities CAPABILITY_IAM CAPABILITY_AUTO_EXPAND 


aws cloudformation delete-stack \
    --stack-name event-processor-sqs 
