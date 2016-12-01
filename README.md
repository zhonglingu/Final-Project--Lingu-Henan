1. Our question
The major question we want to solve in our project is using tweets to predict stock trend for investors. Every day, thousands of people publish their opinions of a specific stock on twitter. Some people suggest buy, while others suggest sell and rest of them are just discussing about it. This aggregated information from the public is an untapped area for financial analysis.

Our basic idea is to first filter tweets containing the stock we want to analyze. Then we'll make a dictionary reflecting people’s attitudes on different stocks. Based on that, in the last step, we could analyze people's different perception on different stocks and present our data to investors accordingly.

2. Basic functions & Datasource
Our web application has two basic functions.
Firstly, we will present some basic financial data of the stock onto our webpage and plot graph for investors’ reference.
Secondly, we'll retrieve data from Twitter and after doing text analysis, present our outcome to investors for their reference.  

Our data are extracted from two sources: the first one is from Yahoo finance, and the second one is from Twitter API.

3. Launching our website
When launching our website, you need to change two paths in the "generate_graph" part in the HL/dev/datasource file, since we're plotting and saving the pictures on our own computers every time. After entering your own local path then the program will run smoothly. 
