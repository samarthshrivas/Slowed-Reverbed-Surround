import subprocess as sp
import soundfile as sf
from pedalboard import Pedalboard, Reverb
from math import trunc
import os
import sox


def slowedreverb(audio, output, room_size = 0.75, damping = 0.5, wet_level = 0.08, dry_level = 0.2, delay = 0.02, slowfactor = 0.08):

    if '.wav' not in audio:
        print('Audio needs to be .wav! Converting...')
        sp.call(f'ffmpeg -i "{audio}" tmp.wav', shell = True)
        audio = 'tmp.wav'
        
    # Import audio file
    print('Importing audio...')
    audio, sample_rate = sf.read(audio)

    # Slow audio
    print('Slowing audio...')
    sample_rate -= trunc(sample_rate*slowfactor)

    # Add reverb
    print('Adding reverb...')
    board = Pedalboard([Reverb(
        room_size=room_size,
        damping=damping,
        wet_level=wet_level,
        dry_level=dry_level
        )])


    # Add effects
    effected = board(audio, sample_rate)
    tfm = sox.Transformer()
    tfm.delay([delay])
    print('Exporting audio...')
    tfm.build(input_array=audio, sample_rate_in=sample_rate, output_filepath = output)
    # Export audio
    
    # sf.write('tmp2.wav', effected, sample_rate)
    # sp.call(f'sox "tmp2.wav" out.wav delay 0.02', shell=True)
    # sp.call(f'ffmpeg -i out.wav "{output}"')
    # sp.call('del tmp.wav tmp2.wav out.wav',shell=True)


if "__main__" == __name__:
    slowedreverb('../example/saware.wav', 'test1.wav')



