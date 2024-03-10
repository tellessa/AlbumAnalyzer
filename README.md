# AlbumAnalyzer

https://albumanalyzer-wt2kaqjzrq-uw.a.run.app/

Have you ever wanted to know the musical keys of each song on an album differ from each other?
Whether you're an artist yourself or an avid music connoissuer, it can be fascinating to explore.
Perhaps you know how to play music by ear and want to add your own instrumentation as you play along with your favorite album from start to finish.
AlbumAnalyzer makes this task easy by giving you a visual representation of the key of each song on an album.

It's simple, just type in the name of the album you want to analyze, and press the search (magnifying glass) icon to the right of your search term.
AlbumAnalyzer takes your search term and outputs a graph which helps visualize the key of each track on the album.

## Quickstart:

To run AlbumAnalyzer, download python 3.9 or later and check "add to path".
Once python is in the environment path variable, open a terminal, and run the following commands

```bash
git clone https://github.com/tellessa/AlbumAnalyzer.git
```

```bash
cd AlbumAnalyzer
```

```bash
python -m venv .venv
```

```bash
.venv/scripts/activate
```

```bash
python -m pip install -r requirements.txt
```
Finally, before running the server, you'll need to obtain a spotify client id and a spotify client secret, and store them in environment variables.
To obtain these credentials, see the Spotify API docs: https://developer.spotify.com/documentation/web-api/concepts/apps.
Once you have them, replace foobar and foobar2 with each of them and export them into the environment before finally running the server:
```bash
export SPOTIFY_CLIENT_ID=foobar; export SPOTIFY_CLIENT_SECRET=foobar2
```
```bash
python manage.py runserver
```
