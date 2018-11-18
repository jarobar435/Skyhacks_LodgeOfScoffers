import io
import os
import librosa
import audioop
import wave
import json
import sys

# Imports the Google Cloud client library
from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types
from google.cloud import vision_v1p3beta1 as vision


def getResponseFromGoogleCloud(gcs_uri):

    # Instantiates a client
    client = speech.SpeechClient()

    # Loads the audio into memory
    audio = types.RecognitionAudio(uri=gcs_uri)

    config = types.RecognitionConfig(

        encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=16000,
        language_code='en-US',
        enable_word_time_offsets=True)

    # Detects speech in the audio file
    operation = client.long_running_recognize(config, audio)

    print('Waiting for operation to complete...')
    response = operation.result()

    word_times = []
    for result in response.results:
        alternative = result.alternatives[0]
        for word_info in alternative.words:
            word_times.append({
                "word": word_info.word,
                "start": word_info.start_time.seconds + word_info.start_time.nanos * 1e-9,
                "end": word_info.end_time.seconds + word_info.end_time.nanos * 1e-9,
            })
    return json.dumps(word_times)




