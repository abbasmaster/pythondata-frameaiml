import pandas as pd
import numpy as np

# Generate synthetic data for Dataframe 1
np.random.seed(0)
num_records = 100
subjects = ['Math', 'Science', 'History']
topics = ['Algebra', 'Biology', 'World War II']
accuracy = np.random.randint(50, 100, num_records)
avg_response_time = np.random.randint(10, 120, num_records)
data1 = {
    'Accuracy': accuracy,
    'Average Response Time (seconds)': avg_response_time,
    'Subject': np.random.choice(subjects, num_records),
    'Topic': np.random.choice(topics, num_records)
}
df1 = pd.DataFrame(data1)

# Generate synthetic data for Dataframe 2
topic_explanations = ['Introduction to algebraic equations', 'Cell structure and function', 'Causes and consequences of the Second World War']
data2 = {
    'Subject': np.random.choice(subjects, num_records),
    'Topic': np.random.choice(topics, num_records),
    'Topic_Explanation': np.random.choice(topic_explanations, num_records)
}
df2 = pd.DataFrame(data2)

# Define a function to generate RAG recommendation based on performance metrics
def generate_rag_recommendation(accuracy, avg_response_time):
    if accuracy >= 80 and avg_response_time <= 60:
        return 'Green'  # Excellent performance
    elif accuracy >= 60 and avg_response_time <= 90:
        return 'Amber'  # Good performance, but slower response time
    else:
        return 'Red'  # Poor performance

# Apply the function to generate RAG recommendations for each record in Dataframe 1
df1['RAG Recommendation'] = df1.apply(lambda row: generate_rag_recommendation(row['Accuracy'], row['Average Response Time (seconds)']), axis=1)

# Display the Dataframe 1 with RAG recommendations
print("Dataframe 1 with RAG recommendations:")
print(df1)

# Example query: Get topic explanation for topics recommended as 'Green'
green_topics = df1[df1['RAG Recommendation'] == 'Green']['Topic'].unique()
green_topic_explanations = df2[df2['Topic'].isin(green_topics)]['Topic_Explanation'].unique()
print("\nTopic explanations for topics recommended as 'Green':")
for topic_explanation in green_topic_explanations:
    print(topic_explanation)
