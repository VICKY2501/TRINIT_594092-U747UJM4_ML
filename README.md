# TRINIT_594092-U747UJM4_ML

ML03 Topic: Crop Prediction

We will implement a Machine learning model which will predict most suitable crop on the basis of: 
1. Season - 'Kharif', 'Whole Year', 'Autumn', 'Rabi','Summer', 'Winter'.
2. Price - price range specified by user (min, max, modal etc).
3. Location - Indian States ('Nagaland','Tamil Nadu','Odisha','Goa','Tripura' etc).
4. Additional features if possible in later stage of project.

Since all the above features are not present in a single dataset, we are going to build a model for Season prediction on basis of Crop and Location from Dataset 2 
and then use this model to generate seasons for given Location, Crops in Dataset 1 so as to get required feature set for final recommendation. 
For deployment, We will consider Gradio or Streamlit Python Library. 

Process:
1. Build Season Prediction ML model from Dataset 2 using Location and Crop as training features.
2. Make a new Dataframe by - getting Seasons for given datapoints in Dataset 1.
3. Final DataFarme features - Location, Season, Price.
4. Suitable Crop Recommendation.
5. Deployment using Streamlit/Gradio library.

Following are the datasets that we will be using:
Dataset 1: https://www.kaggle.com/datasets/thammuio/all-agriculture-related-datasets-for-india
Dataset 2: https://www.kaggle.com/datasets/abhinand05/crop-production-in-india
