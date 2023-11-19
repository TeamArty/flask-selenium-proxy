#!/usr/bin/env bash
set -o errexit

STORAGE_DIR=/opt/render/project/.render

# > Download chrome
if [[ ! -d $STORAGE_DIR/chrome ]]; then
  echo "...Downloading Chrome"
  mkdir -p $STORAGE_DIR/chrome
  cd $STORAGE_DIR/chrome
  wget -P ./ https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
  dpkg -x ./google-chrome-stable_current_amd64.deb $STORAGE_DIR/chrome
  rm ./google-chrome-stable_current_amd64.deb
  cd $HOME/project/src
else
  echo "...Using Chrome from cache"
fi

ls /opt/render/project/.render/chrome/opt/google/chrome
which chromedriver
# > IMPORTANT - set this as the build command:
# export PATH="${PATH}:/opt/render/project/.render/chrome/opt/google/chrome"; ./build.sh;
export PATH="${PATH}:/opt/render/project/.render/chrome/opt/google/chrome"
export CHROME_LOC="${PATH}:/opt/render/project/.render/chrome/opt/google/chrome"

# Custom build commands
pip install -r requirements.txt
