users2_query = """
SELECT u.user_id, u.display_name, u.image_url
FROM "Users" u
JOIN "UserProfiles" up
ON u.user_id = up.user_id
WHERE u.user_id in %(user_ids)s
"""

top_artists2_query = """
SELECT *
FROM "TopArtists" ta 
WHERE ta.user_id in %(user_ids)s
ORDER BY ta.timeframe, ta.rank
"""

top_tracks2_query = """
SELECT *
FROM "TopTracks" tt
WHERE tt.user_id in %(user_ids)s
ORDER BY tt.timeframe, tt.rank
"""

top_genres2_query = """
SELECT *
FROM "TopGenres" tg
WHERE tg.user_id in %(user_ids)s
"""

music_features2_query = """
SELECT *
FROM "MusicFeatures" mf
WHERE mf.user_id in %(user_ids)s
"""

similar_artists_query = """
SELECT artist_id, artist, artist_url, artist_image
FROM "Artists"
WHERE artist_id in %(artist_ids)s
"""

similar_tracks_query = """
SELECT track_id, track, artists, album, track_url, album_image
FROM "Tracks"
WHERE track_id in %(track_ids)s
"""
