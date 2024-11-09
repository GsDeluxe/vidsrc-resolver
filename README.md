# vidsrc-resolver
Extract stream URLs from Vidsrc ( .net / .xyz / .pm / .in )

## Usage

### Install Requirements

```sh
pip install -r requirements.txt
```

TV
Playing episode 1 season 1 of [SUITS](https://www.themoviedb.org/tv/37680-suits)
```python
from vidsrc import VidSRC_Resolver # vidsrc.py
resolver = VidSRC_Resolver(media_type="tv", tmdb_id="37680", season=1, episode=1, verbosity=True)
stream = resolver.get_stream()
print(stream) # the m3u8 URL
resolver.play_stream()
```

Movie
Playing [Star Wars: The Force Awakens](https://www.themoviedb.org/movie/140607-star-wars-the-force-awakens)
```python
from vidsrc import VidSRC_Resolver # vidsrc.py
resolver = VidSRC_Resolver(media_type="movie", tmdb_id="140607", verbosity=True)
stream = resolver.get_stream()
print(stream) # the m3u8 URL
resolver.play_stream()
```
