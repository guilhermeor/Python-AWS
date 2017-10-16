import boto3

s3 = boto3.resource('s3')
s3.Bucket('python-codes').delete_objects
(
    bucket.delete_objects
    (
    Delete=
        {
        'Objects': [
            {
                'Key': 'novoArquivo.txt'
            }]
        }
    )
)