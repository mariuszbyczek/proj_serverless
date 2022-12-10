
import boto3


if __name__ == '__main__':
    # Define the website configuration
    website_configuration = {
        'ErrorDocument': {'Key': 'error.html'},
        'IndexDocument': {'Suffix': 'index.html'},
    }

    # Set the website configuration
    s3 = boto3.client('s3')
    s3.put_bucket_website(Bucket='mariuszbucket',
                          WebsiteConfiguration=website_configuration)

