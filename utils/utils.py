import subprocess as sp
import soundfile as sf
from pedalboard import Pedalboard, Reverb
from math import trunc


def slowedreverb(audio, output):

    if '.wav' not in audio:
        print('Audio needs to be .wav! Converting...')
        sp.call(f'ffmpeg -i "{audio}" tmp.wav', shell = True)
        audio = 'tmp.wav'
        
    # Import audio file
    print('Importing audio...')
    audio, sample_rate = sf.read(audio)

    # Slow audio
    print('Slowing audio...')
    sample_rate -= trunc(sample_rate*0.08)

    # Add reverb
    print('Adding reverb...')
    board = Pedalboard([Reverb(
        room_size=0.75,
        damping=0.5,
        wet_level=0.08,
        dry_level=0.2
        )])


    # Add effects
    effected = board(audio, sample_rate)

    # Export audio
    print('Exporting audio...')
    sf.write('tmp2.wav', effected, sample_rate)
    sp.call(f'sox "tmp2.wav" "{output}" delay 0.02', shell=True)
    sp.call('del tmp.wav tmp2.wav',shell=True)


if "__main__" == __name__:
    slowedreverb('lofi\A.R. Rahman, Arijit Singh - Enna Sona.mp3', 'test1.wav')