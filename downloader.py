import csv
import os
import sys
from pytube import innertube
innertube._cache_dir = os.path.join('./', '.cache')
innertube._token_file = os.path.join(innertube._cache_dir, 'tokens.json')
from pydub import AudioSegment
from pytube import YouTube
import re
import subprocess
import math
import numpy as np


class SplitWavAudio():
    def __init__(self, filepath):
        self.filename = filepath.split('/')[-1]
        self.folder = '/'.join(filepath.split('/')[:-1])
        self.audio = AudioSegment.from_wav(filepath)
    
    def get_duration(self):
        return self.audio.duration_seconds
    
    def single_split(self, from_min, to_min, split_filename):
        t1 = from_min * 60 * 1000
        t2 = to_min * 60 * 1000
        split_audio = self.audio[t1:t2]
        split_audio.export(self.folder + '/' + split_filename, format='wav')
        
    def multiple_split(self, min_per_split):
        total_mins = math.ceil(self.get_duration() / 60)
        inx = 0
        for i in np.arange(0, total_mins, min_per_split):
            inx += 1
            split_fn = self.filename.split('.')[0] + '_' + str(int(inx)) + '.wav'
                        
            #split_fn = self.filename.split('.')[0] + '_' + str(int(i)) + 'm' + str(int((i%1)*60)) + 's-' + str(int(min([i+min_per_split, %self.get_duration() / 60]))) + 'm' + str(int(((min([i+min_per_split, self.get_duration() / 60]))%1)*60)) + 's.wav'
                
            self.single_split(i, i+min_per_split, split_fn)
            print(str(i) + ' Done')
            if i == total_mins - min_per_split:
                print('All splited successfully')


def convert_to_wav(source, destination, split_dur):
    command = 'ffmpeg -i ' + source + ' -ab 160k -ac 2 -ar 44100 -vn ' + destination
    subprocess.call(command, shell=True)
    split_wav = SplitWavAudio(destination)
    split_wav.multiple_split(min_per_split=split_dur)




if __name__ == '__main__':
    if len(sys.argv)!=3:
        print("Usage: python downloder.py <output dir> <split duration>")
        sys.exit(0)
    url_list = 'IBND_Dataset_Details.csv' # Fold_Name,Debate_Name,Link,Total_Duration (minutes),Is link active?
    opDir = sys.argv[1]
    split_dur = float(sys.argv[2])
    with open(url_list, newline='\n') as csvfile:
        csv_data = csv.DictReader(csvfile, delimiter=',')
        
        for row in csv_data:
            
            fold = row['Fold_Name'].strip().split('_')[1]
            if not os.path.exists(opDir+'/data/fold_'+fold):
                os.makedirs(opDir+'/data/fold_'+fold)
            opDir_path = opDir+'/data/fold_'+fold
            if not os.path.exists(opDir_path + '/video/'):
                os.makedirs(opDir_path + '/video/')
            if not os.path.exists(opDir_path + '/audio/'):
                os.makedirs(opDir_path + '/audio/')
            print(row['Debate_Name'])
            if ' ' in row['Debate_Name']:
                title = '_'.join(row['Debate_Name'].strip().split(' '))
            else:
                title = row['Debate_Name']
            title = re.sub(r'[^a-zA-Z0-9]', '_', title)
            fName = opDir_path + '/' + title + ''
            
            url = row['Link'].strip()
            print('Title: ', title)
            print('URL: ',url)
            
            done = False
            list_downloaded_trailers = []


            save_dir = opDir_path + '/video/'
            fName = title + '.mp4'

            try:
                yt = YouTube(url, use_oauth=True, allow_oauth_cache=True)
                print(f'Downloading {title} Filename={fName} Title={yt.title}')
                yt = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
                if not os.path.exists(opDir_path + '/video/'):
                    os.makedirs(opDir_path + '/video/')
                yt.download(save_dir, filename=fName)
                wav_fName = save_dir.replace('video','audio') + fName.split('.')[0] + '.wav'
                convert_to_wav(save_dir + fName, wav_fName, split_dur)

                print(f'\t{fName} downloaded.')
            except KeyboardInterrupt:
                print('Interrupted')
                sys.exit(130)
            except:
                print('\tDownload Error')
                
