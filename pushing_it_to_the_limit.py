import requests

api_key = "AIzaSyDofIhaRG0P3uvcDi34sqNTvWWdcpm455U"
video_id = "ZIxaGgTY8UM&t=485s"

comments = []
page_number = 0


# first request
comments_url = f"https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId={video_id}&order=relevance&key={api_key}"
comments_response = requests.get(comments_url)
comments_data = comments_response.json()
next_comment_page = comments_data["nextPageToken"]
page_number = page_number + 1


for item in comments_data["items"]:
    comments.append(item["snippet"]["topLevelComment"]["snippet"]["textDisplay"])


# ok now that we have gotten our first 20 comments lets grab 4 lots of 20 more
while page_number < 500:
    print(f"page {page_number}")
    comments_url = f"https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId={video_id}&order=relevance&pageToken={next_comment_page}&key={api_key}"
    comments_response = requests.get(comments_url)
    comments_data = comments_response.json()
    for item in comments_data["items"]:
        comments.append(item["snippet"]["topLevelComment"]["snippet"]["textDisplay"])
    page_number = page_number + 1


print(len(comments))
