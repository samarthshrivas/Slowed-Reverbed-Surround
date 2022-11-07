
  <h1 align="center">Slowed+Reverb+Surround </h1>



<!-- ABOUT THE PROJECT -->
## About The Project

This is a try to automaically convert simple songs to lofi type songs



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



