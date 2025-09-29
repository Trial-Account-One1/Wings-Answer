Data Analytics & Insights : Mini-Project - Digital - Recommendation Engine_FP
Course ID: 79469

import pandas as pd
import numpy as np

# --- 1. Load Data ---
# Load training data: assumes 'train.csv' has headers
df_full = pd.read_csv('train.csv')
# Load target user IDs: assumes 'recommendation.csv' has NO header
df_target = pd.read_csv('recommendation.csv', names=['user_id'], header=None)

# Extract list of target users
target_users = df_target['user_id'].unique()

# --- 2. Calculate Top 10 Most Popular Songs ---
# Group by song_id and sum the listen_count
song_popularity = df_full.groupby('song_id')['listen_count'].sum()

# Get the Top 10 most popular song IDs
top_10_songs = song_popularity.nlargest(10).index.tolist()

print("Top 10 Most Popular Songs (used for all recommendations):")
print(top_10_songs)
print(f"\nTotal unique target users: {len(target_users)}")

# --- 3. Generate and Save Output File in Submission Format ---
submission_rows = []
output_file = 'popularity_baseline_submission.csv' 
K = 10

for user_id in target_users:
    # Assign the same top 10 songs to every user
    song_ids = top_10_songs
    
    # Create the comma-separated string: user_id,song_1,song_2,...
    song_ids_str = ','.join(map(str, song_ids))
    
    submission_row = f"{user_id},{song_ids_str}"
    submission_rows.append(submission_row)

# Save the rows to the CSV file without headers
with open(output_file, 'w') as f:
    f.write('\n'.join(submission_rows))

print(f"\n--- Submission File Saved: {output_file} ---")
print("Example Row (user_id,song_1,...):")
print(submission_rows[0])

# rename the output_file.csv to recommendations.csv and run (rename the original recommendations.csv to some other name after the output file is generated

