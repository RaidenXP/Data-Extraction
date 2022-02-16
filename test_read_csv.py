import pandas as pd

def readFile():
    gameDB = pd.read_csv('steam_games')
    print(gameDB)

if __name__ == "__main__":
    readFile()
