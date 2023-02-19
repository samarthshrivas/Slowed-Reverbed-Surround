
  <h1 align="center">Slowed+Reverb+Surround </h1>



<!-- ABOUT THE PROJECT -->
## About The Project

This is a try to automaically convert songs to lofi version of that song



##### Original
https://user-images.githubusercontent.com/59404247/219949725-a60a5289-ea28-4b33-8d54-7638a41e939a.mov

##### LOFI Version
https://user-images.githubusercontent.com/59404247/219949718-1c496dac-10ae-4cc4-8c74-e3af9b7c430a.mov



### Built With

Python




<!-- GETTING STARTED -->
## Getting Started

## Docker 
Docker is also available [HERE]()

### Installation

The following libraries are tools are required for this project to run:

Make sure ffmpeg and sox is installed on device:
####Linux : 
`
sudo apt install ffmpeg sox
`

#### Windows : 

ffmpeg : https://ffmpeg.org/download.html
sox : https://sourceforge.net/projects/sox/

#### Python libraries (Required)

`
pip install -r requirements.txt
`


<!-- USAGE EXAMPLES -->
## Usage
Its rearly simple to use this script 
```
from utils import slowedreverb
slowedreverb('input.wav', 'output.wav')
```


_For more examples, please refer to the [Examples](https://github.com/samarthshrivas/Slowed-Reverbed/tree/main/example)_



