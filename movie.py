import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",user="root",passwd="root123",database="koushiki"
)
print("hello")
cursor=mydb.cursor()

# sql_query = "insert into koushiki (movie_duration,number_of_songs,song_duration,interval_time) VALUES ("97 min",4,"4 min","70 min")"

from moviepy.editor import *
from moviepy.audio import *

clip = VideoFileClip("koushiki/source/Pulp Fiction (1994)/Pulp.Fiction.1994.720p.BrRip.x264.YIFY.mp4")
audio_tracks = clip.audio.reader.nchannels
print(audio_tracks)

import json
import subprocess

infile = "/content/Pulp.Fiction.1994.720p.BrRip.x264.YIFY.mp4"
command = "ffprobe -v quiet -print_format json -show_format -show_streams {}".format(infile)

# Run the FFprobe command and capture its output
output = subprocess.check_output(command, shell=True)

# Parse the JSON output
data = json.loads(output)

# Extract the duration from the JSON data
duration = data.get("format", {}).get("duration")

# Print the duration
print("Duration:", duration)



s="insert into koushiki (movie_duration,number_of_songs,song_duration,interval_time) values (%s,%s,%s,%s)"
b1=(duration,audio_tracks,"4 min","70 min")
cursor.execute(s,b1)
mydb.commit()


