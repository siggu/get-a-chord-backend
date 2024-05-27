from django.shortcuts import render, redirect
from googleapiclient.discovery import build
from django.conf import settings

# YouTube Data API 키 설정 (settings.py에 추가해야 함)
YOUTUBE_API_KEY = settings.YOUTUBE_API_KEY

def index(request):
    return render(request, 'youtube_search/index.html')

def search(request):
    if request.method == 'POST':
        query = request.POST['query']
        youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)
        search_response = youtube.search().list(
            q=query,
            part='id,snippet',
            maxResults=10
        ).execute()

        videos = []
        for search_result in search_response.get('items', []):
            if search_result['id']['kind'] == 'youtube#video':
                videos.append({
                    'title': search_result['snippet']['title'],
                    'video_id': search_result['id']['videoId'],
                    'thumbnail_url': search_result['snippet']['thumbnails']['default']['url']  # 썸네일 URL 추가
                })

        return render(request, 'youtube_search/search_results.html', {'videos': videos})

    return redirect('index')

def play(request, video_id):
    return render(request, 'youtube_search/play.html', {'video_id': video_id})
