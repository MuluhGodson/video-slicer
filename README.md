# video-slicer
> Trim your video files for training ML Models.
> While training a model for use in A.I, we needed a way to prepare our training data. 
> We had a lot of video files and our use case didn't require long video files so this script was
> written to solve that. We just feed in the video files and it trims it down to the size we want with all the 
> audio files. A metadata.csv file is also created which contains all the timestamps for each gif produced. 
> So if you are in need of this kind of use case or just wanna create gifs, this is a faily good tool to use.

## Setting things up
- Create two folders, Videos and Output.
- In the Output folder, create two more folders, audio and gif
- In the Videos folder, place all the video files you want trimmed.

> The trimmed video gifs will be placed in the gif folder, the audio for each gif will be placed in the audio folder.
> You can change how the duration for which the videos are trimmed by editing the **gif_duration** parameter of the code.

### Thanks 
> This script is written using modules from the MoviePy library. [MoviePy](https://zulko.github.io/moviepy/)
