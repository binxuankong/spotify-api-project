# Spotify API Project

A simple project to explore the Spotify API to extract user's top artists and tracks.

Create a Spotify developer account [here](https://developer.spotify.com/) and set up an App. Request for a `Client Id` and `Client Secret` and put them in a `secrets.py` file as shown in `secrets_sample.py`.

The top artists and tracks data is available over three time spans, set in `time_range`
- `short_term`:   approximately last 4 weeks
- `medium_term`:  approximately last 6 months
- `long_term`: calculated from several years of data and including all new data as it becomes available

Change `limit` to set the number of top artists/tracks to obtain. (Minimum: 2, Maximum: 50)


### Requirements
```
pip install spotipy
```


Refer to the [Spotipy documentation](https://spotipy.readthedocs.io/en/2.16.0/) and the [Spotify Developers documentation](https://developer.spotify.com/documentation/) for more information.
