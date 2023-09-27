# YouTube API resources needed:
# channel
# channelSection
# video
# Channels.contentDetails.relatedPlaylists.uploads
from googleapiclient.discovery import Resource
import datetime

def get_channel_content_details(api_client: Resource, part: str, username: str) -> dict:
    request = api_client.channels().list(
        part=part,
        forUsername=username
    )
    return request.execute()

def get_channel_upload_id(channel_content_details: dict) -> str:
    content_details = channel_content_details["items"][0]
    uploads = content_details["contentDetails"]["relatedPlaylists"]
    return uploads["uploads"]

def get_channel_uploads(
    api_client: Resource,
    part: str, 
    max_results: int,
    playlist_id: str) -> dict:
    request = api_client.playlistItems().list(
        part=part,
        maxResults=max_results,
        playlistId=playlist_id
    )
    return request.execute()

def get_uploads_from_to_interval(
    channel_uploads: dict,
    start_datetime: datetime.datetime,
    end_datetime: datetime.datetime) -> dict:
    pass
