# end-to-end-ml-project

git config --global user.email "youremail"

git config --global user.name "your user name"

#command to create environment

conda create -m env_name python=3.8 -y

conda activate env_name

pip install -r requirements.txt (installing the requiremetns)

# we are using ConfigBox to access the content or values in the form of dictionary (see the usage of configbox in common.py)

#each component workflow
1.update config.yaml
2.update schema.yaml
3.update params.yaml
4.update the entity (config_entity)
5.update the configuration manager in src config
6.update the components
7.update the pipeline
8.update main.py
9.update app.py

# Data validation:
in data validation we check if all the column names and data types are same as csv file.  we create a schemal.yaml file and enter all the column names along with their data type.

# data transformation
we are performing train test split. we access the dataset and perform train_test_split.
As we are considering the well organized dataset, i'm not performing any of th eda on this dataset.


# Model trainer
we dividie the trainig and testing data into .75,0.25 ratio and then we train the elasticnet model importing it from sklearn.linear_model

# model evolution
after training the model we evaluate the model using metrics like 


#create user app

# deployment steps
1. login to aws console
2. create IAM user for deployment
    #with specific access

    1. EC2 access : It is virtual machine
    2. ECR: Elastic Container registry to save your docker image in aws

    #Description: About the deployment
    1. Build docker image of the source code
    2. Push your docker image to ECR
    3. Launch Your EC2 
    4. Pull Your image from ECR in EC2
    5. Lauch your docker image in EC2

    #Policy:
    1. AmazonEC2ContainerRegistryFullAccess
    2. AmazonEC2FullAccess

3. Create ECR repo to store/save docker image
     872515257615.dkr.ecr.us-east-1.amazonaws.com/mlproject

4. create EC2 machine(Ubuntu)
5. Open EC2 and install docker in EC2 machine:
    #optinal

    sudo apt-get update -y

    sudo apt-get upgrade

    #required

    curl -fsSL https://get.docker.com -o get-docker.sh

    sudo sh get-docker.sh

    sudo usermod -aG docker ubuntu

    newgrp docker
6. configure EC2 as self-hosted runner
    setting>actions>runner>new self hosted runner> choose os> then run command one by one
7. setup github secrets:
    AWS_ACCESS_KEY_ID=

    AWS_SECRET_ACCESS_KEY=

    AWS_REGION = us-east-1

    AWS_ECR_LOGIN_URI = demo>>  566373416292.dkr.ecr.ap-south-1.amazonaws.com

    ECR_REPOSITORY_NAME = simple-app
