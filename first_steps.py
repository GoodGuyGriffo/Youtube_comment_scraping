import requests

api_key = "AIzaSyDofIhaRG0P3uvcDi34sqNTvWWdcpm455U"
video_id = "ZIxaGgTY8UM&t=485s"

# get video general data
video_info_url = f"https://www.googleapis.com/youtube/v3/videos?part=snippet&id={video_id}&key={api_key}"
video_info_response = requests.get(video_info_url)
video_info_data = video_info_response.json()


# get youtube video comments
comments_url = f"https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId={video_id}&key={api_key}"
comments_response = requests.get(comments_url)
comments_data = comments_response.json()


# extract the comments
comments = [item["snippet"]["topLevelComment"]["snippet"]["textDisplay"] for item in comments_data["items"]]



# ok lets get swifty
comments_url = f"https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId={video_id}&order=relevance&key={api_key}"
comments_response = requests.get(comments_url)
comments_data = comments_response.json()
next_comment_page = comments_data["nextPageToken"]
comments = [item["snippet"]["topLevelComment"]["snippet"]["textDisplay"] for item in comments_data["items"]]
print(comments)


second_comments_url = f"https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId={video_id}&order=relevance&pageToken={next_comment_page}&key={api_key}"
second_comments_response = requests.get(second_comments_url)
second_comments_data = second_comments_response.json()
second_comments = [item["snippet"]["topLevelComment"]["snippet"]["textDisplay"] for item in second_comments_data["items"]]
print(second_comments)

