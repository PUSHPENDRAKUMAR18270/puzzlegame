#Antakshari Game

import random
#Backend
class SongLoader:
    def __init__(self, fileName):
        #open the file for reading lyrics
        fh = open(fileName, "r")
        #define a list to hold the song lyrics
        self.allSongs = []
        #read the file line by line
        for x in fh:
            #"  this is   done  \n".strip() --> "this is   done"
            x = x.strip()
            if len(x) > 0:
                self.allSongs.append(x)

        #close the file
        fh.close()

    def getAllSongs(self):
        return  self.allSongs

#Logic
class GameManager:
    def __init__(self, ref):
        self.songLdr = ref


    def distributeSongs(self):
        #fetch the buffer
        all = self.songLdr.getAllSongs()
        #shuffle it
        random.shuffle(all)
        #slice it
        ls1 = all[0::2]
        ls2 = all[1::2]
        return  ls1, ls2

class SysPlayer:
    def __init__(self, ls):
        self.songs = ls
        self.opponentLoses = []

    def getSong(self, start):
        matches = []

        for x in self.songs:
            if x.startswith(start):
                matches.append(x)

        if len(matches) > 0:
            selected = 0
            i = 0
            for x in matches:
                if x[len(x)-1] in self.opponentLoses:
                    selected = i
                    break
                i+=1
            #remove and return the selected song from song list
            self.songs.remove(matches[selected])
            return matches[selected]
        else:
            return None

    def getAnySong(self):
        if len(self.songs) > 0:
            selected = 0 #default
            i = 0
            for x in self.songs:
                if x[len(x)-1] in self.opponentLoses:
                    selected = i
                    break
                i += 1
            #remove and return the selected song from song list
            temp = self.songs[selected]
            self.songs.pop(selected)
            return temp
        else:
            return None

    def addToOpponentsLoss(self, x):
        self.opponentLoses.append(x)

    def getRemainingSongCount(self):
        return len(self.songs)

class Antakshari:
    def __init__(self, ref):
        self.gMgr = ref

    def play(self, playerName):
        print("Game Begins")
        print("Player1:", playerName)
        print("Player2: System")

        ls1, ls2 = self.gMgr.distributeSongs()
        sp = SysPlayer(ls2)

        gameOver= False

        current = 1
        score1 = 0
        score2 = 0
        initiate = True #sing any song
        respond = False
        i = 1
        now = ""
        while not gameOver:
            print(playerName, "score:", score1)
            print("System score:", score2)

            if current == 1:
                print(playerName," to play")

                if initiate:
                    print("Select a song from list")
                    i = 1
                    for x in ls1:
                        print(i, ")", x)
                        i += 1
                    ch = int(input("Enter Choice"))
                    if ch < 1 or ch > len(ls1):
                        print("Wrong choice")
                    else:
                        now = ls1[ch-1]
                        print(playerName, " sings ", now)
                        ls1.pop(ch-1)
                        initiate = False
                        respond = True #play a song starting with a particular alphabet
                        current = 2 #system to play

                elif respond:
                    print("Select a song starting with",now[len(now)-1],"from list")
                    i = 1
                    for x in ls1:
                        print(i, ")", x)
                        i += 1
                    print("-1 to give up")

                    ch = int(input("Enter Choice"))

                    if ch == -1:
                        print(playerName, "gives up")
                        sp.addToOpponentsLoss(now[len(now)-1])
                        print("System gets a point")
                        print(playerName, "to sing any song")
                        initiate = True
                        respond = False
                        score2 += 1
                        current = 1

                    elif ch < 1 or ch > len(ls1) or not ls1[ch-1].startswith(now[len(now)-1]):
                        print("Wrong choice")
                    else:
                        now = ls1[ch-1]
                        print(playerName, " sings ", now)
                        ls1.pop(ch-1)
                        initiate = False
                        respond = True
                        current = 2

            elif current ==2:
                print("System to play")
                if initiate:
                    #initiate a song
                    now = sp.getAnySong()
                    print("System sings", now)
                    initiate = False
                    respond = True
                    current = 1
                elif respond:
                    now =sp.getSong(now[len(now)-1])
                    if now is None:
                        print("System gives up")
                        print(playerName, "gets a point")
                        print("System to play any song")
                        initiate = True
                        respond = False
                        current = 2
                        score1 += 1
                    else:
                        print("System sings ", now)
                        initiate = False
                        respond = True
                        current = 1

            if len(ls1) == 0 or sp.getRemainingSongCount() == 0:
                gameOver = True


        if score1 > score2:
            print(playerName, "wins")
        elif score2 > score1:
            print("System wins ")
        else:
            print("Game Draw")

def main():
    sldr = SongLoader("d:/songs.txt")
    gMgr = GameManager(sldr)
    ashr = Antakshari(gMgr)
    plyr = input("Enter player name")
    ashr.play(plyr)

main()
