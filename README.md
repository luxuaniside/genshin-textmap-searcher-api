# Genshin Impact Textmap Searcher API
A REST API built with Python and FastAPI for to find specific text entries through the textmap of Genshin Impact.
Provides EN and CHS versions of the text, alongside the text source and the game version where said line was added.

Live demo WIP.

## Features
- EN and CHS
- Singular and mass text entries search

## Tech Stack
- Python
- FastAPI
- Pydantic
- Uvicorn
- SQLAlchemy
- PostgreSQL

### Notes 
A maximum of 1,000 entries are retreived for every single text query.
In the cases of mass search queries, this is 1,000 per.

### Possible Additions
Unsure for now.

## Disclaimer
This is an unofficial, fan-made Genshin Impact wish simulator. It is not affiliated with, endorsed by, or sponsored by HoYoverse or Cognosphere.

Genshin Impact and its associated characters, names, trademarks, artwork, and other intellectual property belong to their respective rights holders. This project's license applies only to its original code and does not grant rights to third-party intellectual property.

Genshin Impact is a trademark of its respective rights holders.

## Credits
https://gitlab.com/Dimbreath/animegamedata2 Thank you dimbreath.