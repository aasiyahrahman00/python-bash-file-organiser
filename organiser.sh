#!/bin/bash

# Prevent wildcard patterns from becoming literal text when no files match
shopt -s nullglob

# -p prevents errors if folders already exist
mkdir -p test-files/Images
mkdir -p test-files/Documents
mkdir -p test-files/Audio

# Move image files
for file in test-files/*.png
do 
   mv "$file" test-files/Images/
   echo "Moved $file to Images"
done 

# Move text files
for file in test-files/*.pdf test-files/*.txt
do
   mv "$file" test-files/Documents/
   echo "Moved $file to Documents"
done

# Move audio files
for file in test-files/*.mp3
do 
   mv "$file" test-files/Audio/
   echo "Moved $file to Audio"
done
