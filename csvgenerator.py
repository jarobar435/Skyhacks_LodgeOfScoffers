import GoogleAPI
import Merge
import json
import pandas as pd

"""
googlewavuri = 'gs://loza2018/sbc0014Mon.wav'

google_transcription = json.loads(
    GoogleAPI.getResponseFromGoogleCloud(googlewavuri))
gogle = open('google1sbc14', 'w+')
gogle.write(json.dumps(google_transcription))
"""


def the_func():
    googlers = open('google1sbc13', 'r')
    filecsv = '2h1-drugie.csv'

    matrix = pd.read_csv(filecsv,header=None)
    google_transcription_s = googlers.read()
    google_trans = json.loads(google_transcription_s)

    results = []

    for row in matrix.iterrows():
        name = row[1][3]
        first_word = 0
        last_word = 0
        error = 999999999
        start = float(row[1][1])
        end = float(row[1][2])
        for i in range(len(google_trans)):
            g_start = google_trans[i]["start"]
            if g_start > end:
                last_word = i
                break
        for i in range(len(google_trans)):
            g_end = google_trans[i]["end"]
            if g_end > start:
                first_word = i
                break
        res = []
        for trans in google_trans[first_word:last_word]:
            res.append(trans["word"])
        results.append([
            name,
            res
        ])
    return results

if __name__ == "__main__":
    results = the_func()
    for res in results:
        print("{}, {}".format(
            res[0],
            ' '.join(res[1])
        ))


"""
dockers = open('dockers','r')
googlers = open('google','r')
google_transcription_s = googlers.read()
docker_speakers_s = dockers.read()

google_transcription = json.loads(google_transcription_s)
docker_speakers = json.loads(docker_speakers_s)

kolekcja = []
idx=0

for i in docker_speakers:
    last_google=0
    start = i['start']
    end = i['end']
    kolekcja.append((i['speaker'],[]))
    for j in google_transcription:
        end_google = j['end']
        start_google = j['start']
        if end_google<=float(end):
            kolekcja[idx][1].append(j['word'])
            google_transcription = google_transcription[last_google:]
            last_google+=1
    idx+=1
"""


"""
[
 [1, string ],
 [2, string ],
 ...
]
"""

'''def the_func():
    dockers = open('dockers','r')
    googlers = open('google1','r')
    google_transcription_s = googlers.read()
    docker_speakers_s = dockers.read()
    google_trans = json.loads(google_transcription_s)
    docker_speakers = json.loads(docker_speakers_s)

    results = []

    google_iter = 0
    for speaker in docker_speakers:
        error = 999999999
        for i in range(google_iter, len(google_trans)):
            new_error = abs(float(speaker["end"]) - google_trans[i]["end"])
            if new_error <= error:
                error = new_error
            else:
                results.append([
                    int(speaker["speaker"]),
                    ' '.join([
                        trans["word"] for trans in google_trans[google_iter:i]
                    ])
                ])
                google_iter = i + 1
                break

    if google_iter != len(google_trans):
        results[-1][1] += ' ' + ' '.join([trans["word"]
                                         for trans in google_trans[google_iter:]])

    return results

if __name__ == "__main__":
    results = the_func()
    for res in results:
        print("{}: {}".format(res[0], res[1]))
'''
