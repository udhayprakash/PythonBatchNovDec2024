# AWS

## AWS CLI

### 1. Install AWS CLI

    $ curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
    $ unzip awscliv2.zip

    $ sudo ./aws/install

    $  aws --version
    aws-cli/2.23.2 Python/3.12.6 Linux/6.5.0-1025-azure exe/x86_64.ubuntu.20

### 2. configuration

    In AWs, create IAM User, attach a group and policy, and then under 
        User -> <specific user> -> Security credentials -> Create Access key
    
    $ code ~/.aws/credentials

        [default]
        aws_access_key_id = YOUR_ACCESS_KEY_ID
        aws_secret_access_key = YOUR_SECRET_ACCESS_KEY


    $ code ~/.aws/config

        [default]
        region = eu-west-1
        output = json

        [profile terraform]
        role_arn = arn:aws:iam::ACCOUNT_ID:role/TerraformAccessRole
        source_profile = default


### Verification

    $ aws sts get-caller-identity

To View Current Configuration

    $ aws configure list


To get specific configuration

    $ aws configure get aws_access_key_id
    $ aws configure get region
    $ aws configure get output

To set Specific Configuration Values

    $ aws configure set aws_access_key_id AKIAIOSFODNN7EXAMPLE
    $ aws configure set aws_secret_access_key wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
    $ aws configure set region us-west-2
    $ aws configure set output table

To Configure Multiple Profiles

    $ aws configure --profile myprofile

To remove or clear specific configuration values:

    $ aws configure set aws_access_key_id ""
    $ aws configure set region ""

### Using Environment variables

These credentials can be passed as environment variables, instead of storing in config files

    export AWS_ACCESS_KEY_ID=AKIAIOSFODNN7EXAMPLE
    export AWS_SECRET_ACCESS_KEY=wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
    export AWS_DEFAULT_REGION=us-east-1

