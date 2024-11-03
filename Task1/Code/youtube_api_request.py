import requests
import csv
import time
from datetime import datetime, timedelta

# Your API key here
API_KEY = 'AIzaSyAgEUF2fwC8BnoQNtBfb9x4ZbcvTggPKLA'
# Base URL for the YouTube API
BASE_URL = 'https://www.googleapis.com/youtube/v3/'


# Function to search for videos within a specific date range
def search_youtube(published_after, published_before):
    # Define the endpoint URL for the search functionality
    search_url = BASE_URL + 'search'
    video_items = []
    next_page_token = ''

    while True:
        # Set the parameters for the API request
        params = {
                'part': 'snippet',
                # 'snippet' returns basic details about each video (title, description, etc.)
                'type': 'video',  # We are specifically searching for videos
                'maxResults': 50,
                # Maximum number of results to return per request (API limit is 50)
                'publishedAfter': published_after,
                # Only include videos published after this date
                'publishedBefore': published_before,
                # Only include videos published before this date
                'relevanceLanguage': 'en',
                # Filter results to only include videos in English
                'order': 'viewCount',
                # Default is descending, no option for ascending in viewCount order,  # Order results by view count
                'key': API_KEY,  # API key for authentication
                'pageToken': next_page_token  # Token for pagination
        }

        # Make the request to the YouTube API using the requests library
        response = requests.get(search_url, params = params)
        # Check if the request was successful (status code 200 means OK)
        if response.status_code == 200:
            # Parse the response as JSON and extend the list of video items
            data = response.json()
            video_items.extend(data['items'])
            next_page_token = data.get('nextPageToken')

            # If there's no next page, break the loop
            if not next_page_token:
                break

            # Pause to avoid hitting rate limits
            time.sleep(1)
        else:
            # Print an error message if the request was not successful
            print(f"Error: {response.status_code} - {response.text}")
            return None

    # Get additional statistics for each video using the video IDs
    for i in range(0, len(video_items), 50):
        video_ids = ','.join(
                [item['id']['videoId'] for item in video_items[i:i + 50]])
        stats_url = BASE_URL + 'videos'
        stats_params = {
                'part': 'statistics',
                # Request statistics like view count and like count
                'id': video_ids,  # Comma-separated list of video IDs
                'key': API_KEY  # API key for authentication
        }

        stats_response = requests.get(stats_url, params = stats_params)
        if stats_response.status_code == 200:
            stats_data = stats_response.json()
            stats_items = {item['id']: item['statistics'] for item in
                           stats_data['items']}
            # Combine snippet and statistics data
            for item in video_items[i:i + 50]:
                video_id = item['id']['videoId']
                if video_id in stats_items:
                    item['statistics'] = stats_items[video_id]

    return video_items


# Function to write the video data to a CSV file
def write_to_csv(videos, filename = 'youtube_videos.csv'):
    # Define the CSV column headers
    headers = ['Title', 'Video ID', 'Published At', 'Description', 'View Count',
               'Like Count']

    # Open the CSV file in write mode
    with open(filename, mode = 'w', newline = '', encoding = 'utf-8') as file:
        writer = csv.writer(file)
        # Write the headers to the CSV file
        writer.writerow(headers)

        # Write each video's data to the CSV file
        for item in videos:
            title = item['snippet']['title']
            video_id = item['id']['videoId']
            published_at = item['snippet']['publishedAt']
            description = item['snippet']['description']
            view_count = item['statistics'][
                'viewCount'] if 'statistics' in item else 'N/A'
            like_count = item['statistics'].get('likeCount',
                                                'N/A') if 'statistics' in item else 'N/A'
            writer.writerow(
                    [title, video_id, published_at, description, view_count,
                     like_count])


# Example usage: search for YouTube videos over multiple date ranges
if __name__ == '__main__':
    start_date = datetime(2006, 3, 1)
    end_date = datetime(2006, 6, 1)
    delta = timedelta(days = 1)  # Split the date range into 2-week intervals
    all_results = []

    current_start = start_date
    while current_start < end_date:
        current_end = min(current_start + delta, end_date)
        published_after = current_start.isoformat("T") + "Z"
        published_before = current_end.isoformat("T") + "Z"
        print(current_end)
        print(published_before)
        results = search_youtube(published_after, published_before)
        if results:
            all_results.extend(results)

        current_start = current_end

    # If results were found, write them to a CSV file
    if all_results:
        write_to_csv(all_results)
        print("Video data has been written to youtube_videos.csv")
