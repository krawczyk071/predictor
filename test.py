import soccerdata as sd

# from pathlib import Path
# chpath=r"C:\Users\krawc\OneDrive\Documents\code\drivers\geckodriver.exe"
# chpath=Path(chpath)
ws = sd.WhoScored(
    leagues="ENG-Premier League",
    seasons=2021,
    #   path_to_browser=chpath
)
