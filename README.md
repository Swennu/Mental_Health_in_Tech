# Mental_Health_in_Tech
## Svend Sakkool, Tambet Osman
Introduction
The fast-paced nature of the IT workplace often contributes to high levels of stress and burnout among employees. Recognizing the importance of mental health, our project leverages survey data from the “OSMI Mental Health in Tech Survey” to predict whether an individual is likely to seek mental health support. By building a predictive model, we aim to provide early insights that can reduce stress and promote employee well-being. This approach combines the power of data-driven analysis with a proactive focus on mental health in the tech industry.
## Models
The predictive model is in a jupiter notebook [models.ipynb](https://github.com/Swennu/Mental_Health_in_Tech/blob/main/model.py). Use this to replicate the results of our project.
## Data
The data is stored in [/data](https://github.com/Swennu/Mental_Health_in_Tech/tree/main/Data) folder. There are 2 files. The original survey.csv and the one we modified data_cleaned.csv. There also is [data_cleaning.py](https://github.com/Swennu/Mental_Health_in_Tech/blob/main/Data_cleaning.py), it contains all the code for cleaning the survey data. To run it use [main.py](https://github.com/Swennu/Mental_Health_in_Tech/blob/main/main.py). Last file related to data is [Controlling_data.py](https://github.com/Swennu/Mental_Health_in_Tech/blob/main/Controlling_data.py) It is just used to see all the unique values of the dataset.
Our predictive models used the data_cleaned.csv
## Concclusion
Analysis of the survey data revealed key factors associated with seeking mental health support. The top features influencing treatment-seeking behavior included: care options, anonymity, family history of mental illness, supervisor support, and workplace
benefits. Association rule mining highlighted some common patterns: 
Employees with access to care options and a family history were more likely to seek treatment.
Anonymity and supportive supervisors slightly decreased the likelihood of seeking help, which wasn’t excpected.
Access to workplace benefits often accompanied treatment-seeking behavior.
These findings suggest that being aware of family history, company offered mental health resources and supportive policies can encourage employees to seek help when needed.

