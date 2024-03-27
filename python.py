import boto3
import json

ec2_client = boto3.client('ec2')

#filter the values
response = ec2_client.describe_instances()
instance_id = response['Reservations'][0]['Instances'][0]['InstanceId']

# Retrieve the value of instance
response = ec2_client.describe_instance_attribute(InstanceId=instance_id, Attribute='instanceType')
instance_type = response['InstanceType']['Value']

# Construct metadata dictionary
ec2_metadata = {
    "instance_id": instance_id,
    "instance_type": instance_type
}

print(json.dumps(ec2_metadata, indent=4))
