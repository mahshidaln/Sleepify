from tracks.py import *

def get_audio_analysis():
    audio_analysis = []
    for i in range(len(tracks_uri)):
        if(tracks_preview[i] != None):
            audio_analysis.append(sp.audio_analysis(tracks_uri[i]))
    return audio_analysis

def get_audio_featues():
    audio_features = []
    for i in range(len(tracks_uri)):
        if(tracks_preview[i] != None):
            audio_features.append(sp.audio_features(tracks_uri[i]))
    return audio_features
