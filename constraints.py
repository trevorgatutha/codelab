import re
import pandas as pd
import numpy as np
from sentence_transformers import SentenceTransformer
import json
EMAIL_DOMAIN = "@gmail.com"
NAME_REGEX = re.compile(r'[^\w\s-]')
MALE_GENDER = "Male"
FEMALE_GENDER = "Female"




#Read male names from male_students.csv
male_df = pd.read_csv('male_students.csv')
males = male_df['First Name'].tolist()  # Assuming the column name is 'First Name'

# Read female names from female_students.csv
female_df = pd.read_csv('female_students.csv')
females = female_df['First Name'].tolist()  # Assuming the column name is 'First Name'

# Load LaBSE model
model = SentenceTransformer('paraphrase-multilingual-MiniLM-L12-v2')

# Generate embeddings for male and female names
male_embeddings = model.encode(males)
female_embeddings = model.encode(females)

# Calculate similarity matrix
male_norm = np.linalg.norm(male_embeddings, axis=0, keepdims=True)
female_norm = np.linalg.norm(female_embeddings, axis=0)

# Replace zero values with 1 to avoid division by zero
male_norm = np.where(male_norm == 0, 1, male_norm)
female_norm = np.where(female_norm == 0, 1, female_norm)

similarity_matrix = np.dot(male_embeddings, female_embeddings.T) / (male_norm * female_norm)

# Filter similarities with at least 50% similarity
filtered_similarities = []
for i in range(len(males)):
    for j in range(len(females)):
        if similarity_matrix[i][j] >= 0.5:
            filtered_similarities.append({
                'male_name': males[i],
                'female_name': females[j],
                'similarity': similarity_matrix[i][j]
            })

# Save filtered similarities to a JSON file
with open('similarity_results.json', 'w') as f:
    json.dump(filtered_similarities, f, indent=2)

print("Similarity results with at least 50% similarity saved to 'similarity_results.json'.")

from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

API_KEY = 'YOUR_API_KEY'
drive_service = build('drive', 'v3', developerKey=API_KEY)
file_metadata = {'name': 'photo.jpg'}
media = MediaFileUpload('C:\path/to/your/file/photo.jpg', resumable=True)
file = drive_service.files().create(body=file_metadata, media_body=media, fields='id').execute()