import os
import csv
import sys
import utils.hdf5_getters as hdf5_getters

import glob
import string
import json
import numpy as np
import pandas as pd

punc_re = r"[^\P{P}]+"


def hdf5_to_csv(directory):
    with open("msds.csv", "w") as csvfile:
        index = 0
        # Column headers
        headers = "index,artist_name,danceability,duration,end_of_fade_in,energy,key,key_confidence,loudness,mode," \
                  "mode_confidence,artist_hotttness,song_hotttness,start_of_fade_out,tempo,time_signature," \
                  "time_signature_confidence,title,release,year"
        csvfile.write(headers)
        csvfile.write("\n")
        # Recursively visit every sub-dir until we find the h5 files
        for root, dirs, filenames in os.walk(directory):
            for file in filenames:
                print(os.path.join(root, file))
                # Use the hd5 wrappers to open the file
                h5_file = hdf5_getters.open_h5_file_read(os.path.join(root, file))
                # EXTRACT FEATURES!!!! and remove punctuation from strings

                # Artist name
                artist_name = hdf5_getters.get_artist_name(h5_file)
                # artist = re.sub(punc_re, "", artist_name)
                artist = artist_name.decode('UTF-8')

                # Danceability
                danceability = hdf5_getters.get_danceability(h5_file)

                # Duration
                duration = hdf5_getters.get_duration(h5_file)

                # End of fade in
                end_of_fade_in = hdf5_getters.get_end_of_fade_in(h5_file)

                # Energy
                energy = hdf5_getters.get_energy(h5_file)

                # Key
                key = hdf5_getters.get_key(h5_file)

                # Key confidence
                key_confidence = hdf5_getters.get_key_confidence(h5_file)

                # Loudness
                loudness = hdf5_getters.get_loudness(h5_file)

                # Mode
                mode = hdf5_getters.get_mode(h5_file)

                # Mode confidence
                mode_confidence = hdf5_getters.get_mode_confidence(h5_file)

                # artist HOTTTNESS
                artist_hotttness = hdf5_getters.get_artist_hotttnesss(h5_file)

                # song HOTTTNESS
                song_hotttness = hdf5_getters.get_song_hotttnesss(h5_file)

                # Start of fade out
                start_of_fade_out = hdf5_getters.get_start_of_fade_out(h5_file)

                # Tempo
                tempo = hdf5_getters.get_tempo(h5_file)

                # Time signature
                time_signature = hdf5_getters.get_time_signature(h5_file)

                # Time signature confidence
                time_signature_confidence = hdf5_getters.get_time_signature_confidence(h5_file)

                # Song title
                song_title = hdf5_getters.get_title(h5_file)
                # title = re.sub(punc_re, "", song_title)
                title = song_title.decode('UTF-8')

                # Release (I think this means the album title)
                release = hdf5_getters.get_release(h5_file).decode('UTF-8')

                # Year
                year = hdf5_getters.get_year(h5_file)

                # Number of songs in file?
                num_songs = hdf5_getters.get_num_songs(h5_file)

                # Close the file
                h5_file.close()

                data = str(index) + "," + artist + "," + str(danceability) + "," + str(duration) + "," + str(end_of_fade_in) + "," + \
                       str(energy) + "," + str(key) + "," + str(key_confidence) + "," + str(loudness) + "," + \
                       str(mode) + "," + str(mode_confidence) + "," + str(artist_hotttness) + "," + str(song_hotttness)\
                       + "," + str(start_of_fade_out) + "," + str(tempo) + "," + str(time_signature) + "," + \
                       str(time_signature_confidence) + "," + title + "," + release + "," + str(year)
                csvfile.write(data)
                csvfile.write("\n")
                index += 1
                # print("{} by {}".format(title, artist))
                # print("{} songs in ^this^ file".format(num_songs))
        print(index)


if __name__ == "__main__":
    hdf5_to_csv(sys.argv[1])
