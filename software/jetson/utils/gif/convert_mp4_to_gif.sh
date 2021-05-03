#!/usr/bin/env bash

# File:        utils/gif/convert_mp4_to_gif.sh
# By:          Samuel Duclos
# For:         Myself
# Usage:       bash <MP4_FILE>
# Example:     bash convert_mp4_to_gif.sh valid_test
# Description: MP4 to GIF converter.

MP4_FILE_WITHOUT_EXTENSION=$1

sudo apt install ffmpeg

echo "Converting ${MP4_FILE_WITHOUT_EXTENSION}.mp4 to ${MP4_FILE_WITHOUT_EXTENSION}.gif..."
ffmpeg -ss 30 -t 3 -i ${MP4_FILE_WITHOUT_EXTENSION}.mp4 -vf "fps=10,scale=320:-1:flags=lanczos,split[s0][s1];[s0]palettegen[p];[s1][p]paletteuse" -loop 0 ${MP4_FILE_WITHOUT_EXTENSION}.gif
echo "Converted ${MP4_FILE_WITHOUT_EXTENSION}.mp4 to ${MP4_FILE_WITHOUT_EXTENSION}.gif."

