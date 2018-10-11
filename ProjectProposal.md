
## [Google Analytics Customer Revenue Prediction](https://www.kaggle.com/c/ga-customer-revenue-prediction)

**Background and Client**  
The client here is the Google Merchandise Store or GStore where Google swag is sold. Their marketing teams are challenged to make appropriate investments in promotional strategies. Applying the 80/20 rule in this domain, would mean that only 20% of customers actually contribute towards revenue. If that is true and those 20% customers can be found out, it will immensely help the marketing team.

**Problem**  
Given the session details of various visits to the GStore, predict the total revenue for visitorId (representing customer). Either one or many of visits of a customer can generate revenue, so the goal is predict the total of all those revenues.

**Data**
The data has been provided by the client (through Kaggle). Each row in the dataset is one visit to the store. There are multiple columns which contain JSON blobs of varying depth. In one of those JSON columns, totals, the sub-column transactionRevenue contains the revenue information we are trying to predict. The raw data has 904K rows and 12 columns. Here are the various data fields:
  - fullVisitorId - A unique identifier for each user of the Google Merchandise Store.
  - channelGrouping - The channel via which the user came to the Store.
  - date - The date on which the user visited the Store.
  - device - The specifications for the device used to access the Store.
  - geoNetwork - This section contains information about the geography of the user.
  - sessionId - A unique identifier for this visit to the store.
  - socialEngagementType - Engagement type, either "Socially Engaged" or "Not Socially Engaged".
  - totals - This section contains aggregate values across the session.
  - trafficSource - This section contains information about the Traffic Source from which the session originated.
  - visitId - An identifier for this session. This is part of the value usually stored as the _utmb cookie. This is only unique to the user. For a completely unique ID, you should use a combination of fullVisitorId and visitId. The cookies named __utma through __utmz are stored by websites that choose to use Google Analytics to see how people visit their websites.
  - visitNumber - The session number for this user. If this is the first session, then this is set to 1.
  - visitStartTime - The timestamp (expressed as POSIX time).

**Solution Approach**
  - Understand the given data thoroughly. What type of files and data are given. What format the final solution should be.
  - Data cleaning. Resolve missing values. Transfrom data into required format if needed.
  - Exploratory data analysis. Visualize the data in different forms to get insights into.
  - Feature engineering. Data modeling. Derive new features if needed. Normalize feature if needed.
  - Try to fit different Classification algorithms like Logistic Regression, SVMs or Neural networks. Learn how these algorithms compare. Find the best model and use it for final predictions. While fitting the models keep in mind the cross validation methods to find best hyper parameters for the chosen algorithm.
  - Make a report mentioning the details about the chosen model and how to apply it to predict product categories for new products.
    
**Deliverables**
  - Code for the project well-documented on GitHub. Differnt .ipynb files for Data cleaning, EDA, feature engineering, Model fitting etc. Instructions to run the code to do the predictions for the new product's categories.
  - Final paper in GitHub explaining the problem, my approach and the findings. Include ideas for further research, as well as up to 3 concrete recommendations on how the client can use the findings. The document should have appropriate title such as Capstone_Project.
  - Slide deck for the project in GitHub. As a data scientist in a company, there is need to produce and present slide decks. Presentation should have appropriate title.
  - Share the project by presenting in office hour, online video or blog post.
    
    
