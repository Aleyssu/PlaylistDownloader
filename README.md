# Personal Youtube playlist video updater

Automatically downloads music from personal private playlists like your Youtube liked videos or any public Youtube playlists using Python, [yt-dlp](https://github.com/yt-dlp/yt-dlp), and [FFmpeg](https://www.ffmpeg.org/). The compiled FFmpeg build from this repo is from https://github.com/BtbN/FFmpeg-Builds. 

Yt-dlp downloads the mp3s for you while FFmpeg attaches the video thumbnails to those mp3s.

How does this script work? It pulls your cookies from you Firefox browser to access your private playlists such as your liked videos playlist. I used Firefox to do this because browser_cookie3 (Python library for getting cookies) is having trouble getting cookies from browsers like Chrome and Edge right now. Note that those cookies contain vital private stuff like login info so don't share them with others. Don't worry, I'm not secretly stealing your cookies with this script, but feel free to read through the source code if that eases your mind.

## Usage

First, you'll need to have Firefox installed and be signed into Youtube in Firefox. Why? Because that's where we're gonna be getting your cookies to access your playlists from.

Make sure you have Python installed and the requirements. Use
```bash
pip install -r requirements.txt
```
to get them.

Simply put `UpdateSongs.py` in the directory where you want the videos to be downloaded and run it with 
```bash
python UpdateSongs.py
```
to automatically download all of your videos. Run it again whenever you want to update newly added videos to your collection.

Use 
```bash
python UpdateSongs.py force_redownload
```
To re-download all of your videos instead of just the newest added ones.

## Configuration
You can customize where your videos will be downloaded along with which playlists you're downloading from in `config.json`. 

By default, videos are downloaded into the same directory as the script and they're downloaded from your liked videos playlist.

## Shortcut

If you want to create a shortcut that you can quickly run to update your playlist, use 
```bash
python CreateExecutableShortcut.py
```
to quickly generate a shortcut for yourself. Feel free to change out `icon.ico` for whatever icon you want the shortcut to have.

## To-Do

- ~~Add the ability to sync between several playlists including other personal private playlists and public ones.~~
- Add the ability to sync videos from other platforms.
- Add the ability to download playlists in mp4 format so you can have some playlists as videos.
- ~~Add the ability to choose the download folders instead of dumping into the current directory.~~
- Make it so that when re-downloading all videos, old videos are purged. Sometimes the authors change the name of their videos so the old ones don't get overwritten when the new ones are downloaded.
- ~~Generate a shortcut which you can double-click to run the whole thing automatically~~
