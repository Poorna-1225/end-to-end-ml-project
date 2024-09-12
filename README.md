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

#Data validation:
in data validation we check if all the column names and data types are same as csv file.  we create a schemal.yaml file and enter all the column names along with their data type.

# data transformation
we are performing train test split. we access the dataset and perform train_test_split.
As we are considering the well organized dataset, i'm not performing any of th eda on this dataset.
