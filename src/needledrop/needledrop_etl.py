# YouTube API resources needed:
# channel
# channelSection
# video
# Channels.contentDetails.relatedPlaylists.uploads
import os
from pprint import pprint
import src.needledrop.extract as extract

from dotenv import load_dotenv
import googleapiclient.discovery

def main():
    load_dotenv()

    YOUTUBE_DATA_API_KEY = os.getenv("YOUTUBE_DATA_API_KEY")

    API_SERVICE_NAME = "youtube"
    API_VERSION = "v3"

    # Extract phase:
    # create an API client
    youtube = googleapiclient.discovery.build(
        serviceName=API_SERVICE_NAME, 
        version=API_VERSION,
        developerKey=YOUTUBE_DATA_API_KEY
    )
    
    channel_content_details = extract.get_channel_content_details(
        api_client=youtube,
        part="contentDetails",
        username="theneedledrop"
    )

    channel_upload_id = extract.get_channel_upload_id(channel_content_details)

    channel_uploads = extract.get_channel_uploads(
        api_client=youtube,
        part="id,snippet",
        max_results=50,
        playlist_id=channel_upload_id
    )

    pprint(channel_uploads)
    


if __name__ == "__main__":
    main()
