## Challange description

Given the following folder structure of videos from several locations:

* Videos
  * Oslo
    * Video_20230801161010.mp4
    * Video_20230801171212.mp4
    * Video_20230801181313.mp4
  * Bergen
    * Video_20230901121010.mp4
    * Video_20230901131414.mp4
    * Video_20230901141212.mp4
  * Trondheim
    * Video_20230701080808.mp4
    * Video_20230701090808.mp4
  * Tromsø
    * Video_20230601070000.mp4
    * Video_20230601080203.mp4

*Note:*
  * *For each location; next video starts when previous ends. No gaps. No overlaps.*
  * *The files are just example files, and are empty.*

And snippet of label document as shown here:

| timestamp | label |
|:----------|------:|
| 2023-08-01 16:10:10 | hund |
| 2023-08-01 16:19:12 | katt |
| 2023-08-01 16:28:14 | bil |
| 2023-08-01 16:37:16 | høne |
| 2023-08-01 16:46:18 | fly |
| 2023-08-01 16:55:20 | buss |
| 2023-08-01 17:04:22 | hund |

## The challenge would be

Create a script, that can be run from the command line.

* It should read the timestamped labels CSV file.
* Traverse folder structure for video files.  
* Join these data and find corresponding 
  * Path to video file
  * Location
  * Duration in seconds into the video where label is flagged.
* Output a csv file with following headers
  * timestamp
  * label
  * location
  * video_file
  * seconds_into
* Language could be either Python or NodeJS
* You can freely choose to use whichever library you want to make the job easier.
* Feel free to ask if you have problems or questions.
