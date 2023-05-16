from dataclasses import dataclass

@dataclass
class Song:
    Id: int
    Name: str
    Year: int
    Artist: str
    Shortname: str
    Bpm: int
    Duration: int
    Genre: str
    SpotifyId: str
    Album: str
