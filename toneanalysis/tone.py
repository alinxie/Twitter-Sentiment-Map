import json
from watson_developer_cloud import ToneAnalyzerV3

def main():

    tweets = open('input.txt', 'r')

    tone_analyzer = ToneAnalyzerV3(
        username='fae1b7aa-7534-4fda-b5d1-775076ca668c',
        password='TbzeEoT4cxHi',
        version='2016-05-19')
    
    tones = open('output.txt', 'w')

    #for s in tweets:
    s = tweets.read()
    tones.write(json.dumps(tone_analyzer.tone(text = s, tones = 'emotion', sentences = False), indent=2))

main()
