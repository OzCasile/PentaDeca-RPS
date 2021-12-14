# Oz Casile
# SDEV 140
# Nick Laplante
# FINAL PROJECT

# Imports
import random
from tkinter import *


# Instructions Window
def InstructWindow():
    window = Toplevel(Home)
    window.title("How to Play:")
    window.geometry("400x100")
    ReadMe = Label(window, text = "Welcome to PentaDeca Rock Paper Scissors! Here's how to play: You will choose 15 battle options (see 'Help' for more details). From there, it's as easy as pushing a button. Keep playing until you're satisfied!", wraplength=400)
    KillReadMe = Button(window, text = "Close Instructions", command = lambda: window.destroy())
    ReadMe.pack()
    KillReadMe.pack()


# Build 15-Option RPS
def PentaDeca():
    PentaDeca = Toplevel(Home)
    PentaDeca.title("PentaDeca RPS")
    PentaDeca.geometry("1200x700")

    # Win Lose Conditions Per Element per Game Mode

    # Rock
    def Rock():
        ComPlay = ComOpt[str(random.randint(0,14))]
        if ComPlay == "RockImg":
            Result = "Stalemate"
            Display.config(text = Result)
        elif ComPlay == "FireImg" or ComPlay == "ScissorsImg" or ComPlay == "SnakeImg" or ComPlay == "PersonImg" or ComPlay == "TreeImg" or ComPlay == "WolfImg" or ComPlay == "SpongeImg":
            Result = "The Player Wins"
            Display.config(text = Result)
        else:
            Result = "The Machine Wins"
            Display.config(text = Result)

        # Fix Choice Pics
        PlayPic.config(image = RockImg)
        if ComPlay == "RockImg":
            ComPic.config(image = RockImg )
        elif ComPlay == "FireImg":
            ComPic.config(image = FireImg)
        elif ComPlay == "ScissorsImg":
            ComPic.config(image = ScissorsImg)
        elif ComPlay == "SnakeImg":
            ComPic.config(image = SnakeImg)
        elif ComPlay == "PersonImg":
            ComPic.config(image = PersonImg)
        elif ComPlay == "TreeImg":
            ComPic.config(image = TreeImg)
        elif ComPlay == "WolfImg":
            ComPic.config(image = WolfImg)
        elif ComPlay == "SpongeImg":
            ComPic.config(image = SpongeImg)
        elif ComPlay == "PaperImg":
            ComPic.config(image = PaperImg)
        elif ComPlay == "AirImg":
            ComPic.config(image = AirImg)
        elif ComPlay == "WaterImg":
            ComPic.config(image = WaterImg)
        elif ComPlay == "DragonImg":
            ComPic.config(image = DragonImg)
        elif ComPlay == "DevilImg":
            ComPic.config(image = DevilImg)
        elif ComPlay == "LightningImg":
            ComPic.config(image = LightningImg)
        else:
            ComPic.config(image = GunImg)

        
        

      
    # Fire
    def Fire():
        ComPlay = ComOpt[str(random.randint(0,14))]
        if ComPlay == "FireImg":
            Result = "Stalemate"
            Display.config(text = Result)
        elif ComPlay == "ScissorsImg" or ComPlay == "SnakeImg" or ComPlay == "PersonImg" or ComPlay == "TreeImg" or ComPlay == "WolfImg" or ComPlay == "SpongeImg" or ComPlay == "PaperImg":
            Result = "The Player Wins"
            Display.config(text = Result)
        else:
            Result = "The Machine Wins"
            Display.config(text = Result)

        # Fix Choice Pics
        PlayPic.config(image = FireImg)
        if ComPlay == "RockImg":
            ComPic.config(image = RockImg )
        elif ComPlay == "FireImg":
            ComPic.config(image = FireImg)
        elif ComPlay == "ScissorsImg":
            ComPic.config(image = ScissorsImg)
        elif ComPlay == "SnakeImg":
            ComPic.config(image = SnakeImg)
        elif ComPlay == "PersonImg":
            ComPic.config(image = PersonImg)
        elif ComPlay == "TreeImg":
            ComPic.config(image = TreeImg)
        elif ComPlay == "WolfImg":
            ComPic.config(image = WolfImg)
        elif ComPlay == "SpongeImg":
            ComPic.config(image = SpongeImg)
        elif ComPlay == "PaperImg":
            ComPic.config(image = PaperImg)
        elif ComPlay == "AirImg":
            ComPic.config(image = AirImg)
        elif ComPlay == "WaterImg":
            ComPic.config(image = WaterImg)
        elif ComPlay == "DragonImg":
            ComPic.config(image = DragonImg)
        elif ComPlay == "DevilImg":
            ComPic.config(image = DevilImg)
        elif ComPlay == "LightningImg":
            ComPic.config(image = LightningImg)
        else:
            ComPic.config(image = GunImg)

        


    # Scissors
    def Scissors():
        ComPlay = ComOpt[str(random.randint(0,14))]
        if ComPlay == "ScissorsImg":
            Result = "Stalemate"
            Display.config(text = Result)
        elif ComPlay == "SnakeImg" or ComPlay == "PersonImg" or ComPlay == "TreeImg" or ComPlay == "WolfImg" or ComPlay == "SpongeImg" or ComPlay == "PaperImg" or ComPlay == "AirImg":
            Result = "The Player Wins"
            Display.config(text = Result)
        else:
            Result = "The Machine Wins"
            Display.config(text = Result)

        # Fix Choice Pics
        PlayPic.config(image = ScissorsImg)
        if ComPlay == "RockImg":
            ComPic.config(image = RockImg )
        elif ComPlay == "FireImg":
            ComPic.config(image = FireImg)
        elif ComPlay == "ScissorsImg":
            ComPic.config(image = ScissorsImg)
        elif ComPlay == "SnakeImg":
            ComPic.config(image = SnakeImg)
        elif ComPlay == "PersonImg":
            ComPic.config(image = PersonImg)
        elif ComPlay == "TreeImg":
            ComPic.config(image = TreeImg)
        elif ComPlay == "WolfImg":
            ComPic.config(image = WolfImg)
        elif ComPlay == "SpongeImg":
            ComPic.config(image = SpongeImg)
        elif ComPlay == "PaperImg":
            ComPic.config(image = PaperImg)
        elif ComPlay == "AirImg":
            ComPic.config(image = AirImg)
        elif ComPlay == "WaterImg":
            ComPic.config(image = WaterImg)
        elif ComPlay == "DragonImg":
            ComPic.config(image = DragonImg)
        elif ComPlay == "DevilImg":
            ComPic.config(image = DevilImg)
        elif ComPlay == "LightningImg":
            ComPic.config(image = LightningImg)
        else:
            ComPic.config(image = GunImg)

        


    # Snake
    def Snake():
        ComPlay = ComOpt[str(random.randint(0,14))]
        if ComPlay == "SnakeImg":
            Result = "Ssssstalemate"
            Display.config(text = Result)
        elif ComPlay == "PersonImg" or ComPlay == "TreeImg" or ComPlay == "WolfImg" or ComPlay == "SpongeImg" or ComPlay == "PaperImg" or ComPlay == "AirImg" or ComPlay == "WaterImg":
            Result = "The Player Wins"
            Display.config(text = Result)
        else:
            Result = "The Machine Wins"
            Display.config(text = Result)

        # Fix Choice Pics
        PlayPic.config(image = SnakeImg)
        if ComPlay == "RockImg":
            ComPic.config(image = RockImg )
        elif ComPlay == "FireImg":
            ComPic.config(image = FireImg)
        elif ComPlay == "ScissorsImg":
            ComPic.config(image = ScissorsImg)
        elif ComPlay == "SnakeImg":
            ComPic.config(image = SnakeImg)
        elif ComPlay == "PersonImg":
            ComPic.config(image = PersonImg)
        elif ComPlay == "TreeImg":
            ComPic.config(image = TreeImg)
        elif ComPlay == "WolfImg":
            ComPic.config(image = WolfImg)
        elif ComPlay == "SpongeImg":
            ComPic.config(image = SpongeImg)
        elif ComPlay == "PaperImg":
            ComPic.config(image = PaperImg)
        elif ComPlay == "AirImg":
            ComPic.config(image = AirImg)
        elif ComPlay == "WaterImg":
            ComPic.config(image = WaterImg)
        elif ComPlay == "DragonImg":
            ComPic.config(image = DragonImg)
        elif ComPlay == "DevilImg":
            ComPic.config(image = DevilImg)
        elif ComPlay == "LightningImg":
            ComPic.config(image = LightningImg)
        else:
            ComPic.config(image = GunImg)

        

          
    # Person
    def Person():
        ComPlay = ComOpt[str(random.randint(0,14))]
        if ComPlay == "PersonImg":
            Result = "Stalemate"
            Display.config(text = Result)
        elif ComPlay == "TreeImg" or ComPlay == "WolfImg" or ComPlay == "SpongeImg" or ComPlay == "PaperImg" or ComPlay == "AirImg" or ComPlay == "WaterImg" or ComPlay == "DragonImg":
            Result = "The Player Wins"
            Display.config(text = Result)
        else:
            Result = "The Machine Wins"
            Display.config(text = Result)

        # Fix Choice Pics
        PlayPic.config(image = PersonImg)
        if ComPlay == "RockImg":
            ComPic.config(image = RockImg )
        elif ComPlay == "FireImg":
            ComPic.config(image = FireImg)
        elif ComPlay == "ScissorsImg":
            ComPic.config(image = ScissorsImg)
        elif ComPlay == "SnakeImg":
            ComPic.config(image = SnakeImg)
        elif ComPlay == "PersonImg":
            ComPic.config(image = PersonImg)
        elif ComPlay == "TreeImg":
            ComPic.config(image = TreeImg)
        elif ComPlay == "WolfImg":
            ComPic.config(image = WolfImg)
        elif ComPlay == "SpongeImg":
            ComPic.config(image = SpongeImg)
        elif ComPlay == "PaperImg":
            ComPic.config(image = PaperImg)
        elif ComPlay == "AirImg":
            ComPic.config(image = AirImg)
        elif ComPlay == "WaterImg":
            ComPic.config(image = WaterImg)
        elif ComPlay == "DragonImg":
            ComPic.config(image = DragonImg)
        elif ComPlay == "DevilImg":
            ComPic.config(image = DevilImg)
        elif ComPlay == "LightningImg":
            ComPic.config(image = LightningImg)
        else:
            ComPic.config(image = GunImg)

                


    # Tree
    def Tree():
        ComPlay = ComOpt[str(random.randint(0,14))]
        if ComPlay == "TreeImg":
            Result = "Stalemate"
            Display.config(text = Result)
        elif ComPlay == "WolfImg" or ComPlay == "SpongeImg" or ComPlay == "PaperImg" or ComPlay == "AirImg" or ComPlay == "WaterImg" or ComPlay == "DragonImg" or ComPlay == "DevilImg":
            Result = "The Player Wins"
            Display.config(text = Result)
        else:
            Result = "The Machine Wins"
            Display.config(text = Result)

        # Fix Choice Pics
        PlayPic.config(image = TreeImg)
        if ComPlay == "RockImg":
            ComPic.config(image = RockImg )
        elif ComPlay == "FireImg":
            ComPic.config(image = FireImg)
        elif ComPlay == "ScissorsImg":
            ComPic.config(image = ScissorsImg)
        elif ComPlay == "SnakeImg":
            ComPic.config(image = SnakeImg)
        elif ComPlay == "PersonImg":
            ComPic.config(image = PersonImg)
        elif ComPlay == "TreeImg":
            ComPic.config(image = TreeImg)
        elif ComPlay == "WolfImg":
            ComPic.config(image = WolfImg)
        elif ComPlay == "SpongeImg":
            ComPic.config(image = SpongeImg)
        elif ComPlay == "PaperImg":
            ComPic.config(image = PaperImg)
        elif ComPlay == "AirImg":
            ComPic.config(image = AirImg)
        elif ComPlay == "WaterImg":
            ComPic.config(image = WaterImg)
        elif ComPlay == "DragonImg":
            ComPic.config(image = DragonImg)
        elif ComPlay == "DevilImg":
            ComPic.config(image = DevilImg)
        elif ComPlay == "LightningImg":
            ComPic.config(image = LightningImg)
        else:
            ComPic.config(image = GunImg)

        


    # Wolf
    def Wolf():
        ComPlay = ComOpt[str(random.randint(0,14))]
        if ComPlay == "WolfImg":
            Result = "Stalemate"
            Display.config(text = Result)
        elif ComPlay == "SpongeImg" or ComPlay == "PaperImg" or ComPlay == "AirImg" or ComPlay == "WaterImg" or ComPlay == "DragonImg" or ComPlay == "DevilImg" or ComPlay == "LightningImg":
            Result = "The Player Wins"
            Display.config(text = Result)
        else:
            Result = "The Machine Wins"
            Display.config(text = Result)

        # Fix Choice Pics
        PlayPic.config(image = WolfImg)
        if ComPlay == "RockImg":
            ComPic.config(image = RockImg )
        elif ComPlay == "FireImg":
            ComPic.config(image = FireImg)
        elif ComPlay == "ScissorsImg":
            ComPic.config(image = ScissorsImg)
        elif ComPlay == "SnakeImg":
            ComPic.config(image = SnakeImg)
        elif ComPlay == "PersonImg":
            ComPic.config(image = PersonImg)
        elif ComPlay == "TreeImg":
            ComPic.config(image = TreeImg)
        elif ComPlay == "WolfImg":
            ComPic.config(image = WolfImg)
        elif ComPlay == "SpongeImg":
            ComPic.config(image = SpongeImg)
        elif ComPlay == "PaperImg":
            ComPic.config(image = PaperImg)
        elif ComPlay == "AirImg":
            ComPic.config(image = AirImg)
        elif ComPlay == "WaterImg":
            ComPic.config(image = WaterImg)
        elif ComPlay == "DragonImg":
            ComPic.config(image = DragonImg)
        elif ComPlay == "DevilImg":
            ComPic.config(image = DevilImg)
        elif ComPlay == "LightningImg":
            ComPic.config(image = LightningImg)
        else:
            ComPic.config(image = GunImg)

        

           
    # Sponge
    def Sponge():
        ComPlay = ComOpt[str(random.randint(0,14))]
        if ComPlay == "SpongeImg":
            Result = "Stalemate"
            Display.config(text = Result)
        elif ComPlay == "PaperImg" or ComPlay == "AirImg" or ComPlay == "WaterImg" or ComPlay == "DragonImg" or ComPlay == "DevilImg" or ComPlay == "LightningImg" or ComPlay == "GunImg":
            Result = "The Player Wins"
            Display.config(text = Result)
        else:
            Result = "The Machine Wins"
            Display.config(text = Result)

        # Fix Choice Pics
        PlayPic.config(image = SpongeImg)
        if ComPlay == "RockImg":
            ComPic.config(image = RockImg )
        elif ComPlay == "FireImg":
            ComPic.config(image = FireImg)
        elif ComPlay == "ScissorsImg":
            ComPic.config(image = ScissorsImg)
        elif ComPlay == "SnakeImg":
            ComPic.config(image = SnakeImg)
        elif ComPlay == "PersonImg":
            ComPic.config(image = PersonImg)
        elif ComPlay == "TreeImg":
            ComPic.config(image = TreeImg)
        elif ComPlay == "WolfImg":
            ComPic.config(image = WolfImg)
        elif ComPlay == "SpongeImg":
            ComPic.config(image = SpongeImg)
        elif ComPlay == "PaperImg":
            ComPic.config(image = PaperImg)
        elif ComPlay == "AirImg":
            ComPic.config(image = AirImg)
        elif ComPlay == "WaterImg":
            ComPic.config(image = WaterImg)
        elif ComPlay == "DragonImg":
            ComPic.config(image = DragonImg)
        elif ComPlay == "DevilImg":
            ComPic.config(image = DevilImg)
        elif ComPlay == "LightningImg":
            ComPic.config(image = LightningImg)
        else:
            ComPic.config(image = GunImg)

        

          
    # Paper
    def Paper():
        ComPlay = ComOpt[str(random.randint(0,14))]
        if ComPlay == "PaperImg":
            Result = "Stalemate"
            Display.config(text = Result)
        elif ComPlay == "AirImg" or ComPlay == "WaterImg" or ComPlay == "DragonImg" or ComPlay == "DevilImg" or ComPlay == "LightningImg" or ComPlay == "GunImg" or ComPlay == "RockImg":
            Result = "The Player Wins"
            Display.config(text = Result)
        else:
            Result = "The Machine Wins"
            Display.config(text = Result)

        # Fix Choice Pics
        PlayPic.config(image = PaperImg)
        if ComPlay == "RockImg":
            ComPic.config(image = RockImg )
        elif ComPlay == "FireImg":
            ComPic.config(image = FireImg)
        elif ComPlay == "ScissorsImg":
            ComPic.config(image = ScissorsImg)
        elif ComPlay == "SnakeImg":
            ComPic.config(image = SnakeImg)
        elif ComPlay == "PersonImg":
            ComPic.config(image = PersonImg)
        elif ComPlay == "TreeImg":
            ComPic.config(image = TreeImg)
        elif ComPlay == "WolfImg":
            ComPic.config(image = WolfImg)
        elif ComPlay == "SpongeImg":
            ComPic.config(image = SpongeImg)
        elif ComPlay == "PaperImg":
            ComPic.config(image = PaperImg)
        elif ComPlay == "AirImg":
            ComPic.config(image = AirImg)
        elif ComPlay == "WaterImg":
            ComPic.config(image = WaterImg)
        elif ComPlay == "DragonImg":
            ComPic.config(image = DragonImg)
        elif ComPlay == "DevilImg":
            ComPic.config(image = DevilImg)
        elif ComPlay == "LightningImg":
            ComPic.config(image = LightningImg)
        else:
            ComPic.config(image = GunImg)

        


    # Air
    def Air():
        ComPlay = ComOpt[str(random.randint(0,14))]
        if ComPlay == "AirImg":
            Result = "Stalemate"
            Display.config(text = Result)
        elif ComPlay == "WaterImg" or ComPlay == "DragonImg" or ComPlay == "DevilImg" or ComPlay == "LightningImg" or ComPlay == "GunImg" or ComPlay == "RockImg" or ComPlay == "FireImg":
            Result = "The Player Wins"
            Display.config(text = Result)
        else:
            Result = "The Machine Wins"
            Display.config(text = Result)

        # Fix Choice Pics
        PlayPic.config(image = AirImg)
        if ComPlay == "RockImg":
            ComPic.config(image = RockImg )
        elif ComPlay == "FireImg":
            ComPic.config(image = FireImg)
        elif ComPlay == "ScissorsImg":
            ComPic.config(image = ScissorsImg)
        elif ComPlay == "SnakeImg":
            ComPic.config(image = SnakeImg)
        elif ComPlay == "PersonImg":
            ComPic.config(image = PersonImg)
        elif ComPlay == "TreeImg":
            ComPic.config(image = TreeImg)
        elif ComPlay == "WolfImg":
            ComPic.config(image = WolfImg)
        elif ComPlay == "SpongeImg":
            ComPic.config(image = SpongeImg)
        elif ComPlay == "PaperImg":
            ComPic.config(image = PaperImg)
        elif ComPlay == "AirImg":
            ComPic.config(image = AirImg)
        elif ComPlay == "WaterImg":
            ComPic.config(image = WaterImg)
        elif ComPlay == "DragonImg":
            ComPic.config(image = DragonImg)
        elif ComPlay == "DevilImg":
            ComPic.config(image = DevilImg)
        elif ComPlay == "LightningImg":
            ComPic.config(image = LightningImg)
        else:
            ComPic.config(image = GunImg)

        
            

    # Water
    def Water():
        ComPlay = ComOpt[str(random.randint(0,14))]
        if ComPlay == "WaterImg":
            Result = "Stalemate"
            Display.config(text = Result)
        elif ComPlay == "DragonImg" or ComPlay == "DevilImg" or ComPlay == "LightningImg" or ComPlay == "GunImg" or ComPlay == "RockImg" or ComPlay == "FireImg" or ComPlay == "ScissorsImg":
            Result = "The Player Wins"
            Display.config(text = Result)
        else:
            Result = "The Machine Wins"
            Display.config(text = Result)

        # Fix Choice Pics
        PlayPic.config(image = WaterImg)
        if ComPlay == "RockImg":
            ComPic.config(image = RockImg )
        elif ComPlay == "FireImg":
            ComPic.config(image = FireImg)
        elif ComPlay == "ScissorsImg":
            ComPic.config(image = ScissorsImg)
        elif ComPlay == "SnakeImg":
            ComPic.config(image = SnakeImg)
        elif ComPlay == "PersonImg":
            ComPic.config(image = PersonImg)
        elif ComPlay == "TreeImg":
            ComPic.config(image = TreeImg)
        elif ComPlay == "WolfImg":
            ComPic.config(image = WolfImg)
        elif ComPlay == "SpongeImg":
            ComPic.config(image = SpongeImg)
        elif ComPlay == "PaperImg":
            ComPic.config(image = PaperImg)
        elif ComPlay == "AirImg":
            ComPic.config(image = AirImg)
        elif ComPlay == "WaterImg":
            ComPic.config(image = WaterImg)
        elif ComPlay == "DragonImg":
            ComPic.config(image = DragonImg)
        elif ComPlay == "DevilImg":
            ComPic.config(image = DevilImg)
        elif ComPlay == "LightningImg":
            ComPic.config(image = LightningImg)
        else:
            ComPic.config(image = GunImg)

        
            

    # Dragon
    def Dragon():
        ComPlay = ComOpt[str(random.randint(0,14))]
        if ComPlay == "DragonImg":
            Result = "Stalemate"
            Display.config(text = Result)
        elif ComPlay == "DevilImg" or ComPlay == "LightningImg" or ComPlay == "GunImg" or ComPlay == "RockImg" or ComPlay == "FireImg" or ComPlay == "ScissorsImg" or ComPlay == "SnakeImg":
            Result = "The Player Wins"
            Display.config(text = Result)
        else:
            Result = "The Machine Wins"
            Display.config(text = Result)

        # Fix Choice Pics
        PlayPic.config(image = DragonImg)
        if ComPlay == "RockImg":
            ComPic.config(image = RockImg )
        elif ComPlay == "FireImg":
            ComPic.config(image = FireImg)
        elif ComPlay == "ScissorsImg":
            ComPic.config(image = ScissorsImg)
        elif ComPlay == "SnakeImg":
            ComPic.config(image = SnakeImg)
        elif ComPlay == "PersonImg":
            ComPic.config(image = PersonImg)
        elif ComPlay == "TreeImg":
            ComPic.config(image = TreeImg)
        elif ComPlay == "WolfImg":
            ComPic.config(image = WolfImg)
        elif ComPlay == "SpongeImg":
            ComPic.config(image = SpongeImg)
        elif ComPlay == "PaperImg":
            ComPic.config(image = PaperImg)
        elif ComPlay == "AirImg":
            ComPic.config(image = AirImg)
        elif ComPlay == "WaterImg":
            ComPic.config(image = WaterImg)
        elif ComPlay == "DragonImg":
            ComPic.config(image = DragonImg)
        elif ComPlay == "DevilImg":
            ComPic.config(image = DevilImg)
        elif ComPlay == "LightningImg":
            ComPic.config(image = LightningImg)
        else:
            ComPic.config(image = GunImg)

        
            

    # Devil
    def Devil():
        ComPlay = ComOpt[str(random.randint(0,14))]
        if ComPlay == "DevilImg":
            Result = "Stalemate"
            Display.config(text = Result)
        elif ComPlay == "LightningImg" or ComPlay == "GunImg" or ComPlay == "RockImg" or ComPlay == "FireImg" or ComPlay == "ScissorsImg" or ComPlay == "SnakeImg" or ComPlay == "PersonImg":
            Result = "The Player Wins"
            Display.config(text = Result)
        else:
            Result = "The Machine Wins"
            Display.config(text = Result)

        # Fix Choice Pics
        PlayPic.config(image = DevilImg)
        if ComPlay == "RockImg":
            ComPic.config(image = RockImg )
        elif ComPlay == "FireImg":
            ComPic.config(image = FireImg)
        elif ComPlay == "ScissorsImg":
            ComPic.config(image = ScissorsImg)
        elif ComPlay == "SnakeImg":
            ComPic.config(image = SnakeImg)
        elif ComPlay == "PersonImg":
            ComPic.config(image = PersonImg)
        elif ComPlay == "TreeImg":
            ComPic.config(image = TreeImg)
        elif ComPlay == "WolfImg":
            ComPic.config(image = WolfImg)
        elif ComPlay == "SpongeImg":
            ComPic.config(image = SpongeImg)
        elif ComPlay == "PaperImg":
            ComPic.config(image = PaperImg)
        elif ComPlay == "AirImg":
            ComPic.config(image = AirImg)
        elif ComPlay == "WaterImg":
            ComPic.config(image = WaterImg)
        elif ComPlay == "DragonImg":
            ComPic.config(image = DragonImg)
        elif ComPlay == "DevilImg":
            ComPic.config(image = DevilImg)
        elif ComPlay == "LightningImg":
            ComPic.config(image = LightningImg)
        else:
            ComPic.config(image = GunImg)

        
            

    # Lightning
    def Lightning():
        ComPlay = ComOpt[str(random.randint(0,14))]
        if ComPlay == "LightningImg":
            Result = "Stalemate"
            Display.config(text = Result)
        elif ComPlay == "GunImg" or ComPlay == "RockImg" or ComPlay == "FireImg" or ComPlay == "ScissorsImg" or ComPlay == "SnakeImg" or ComPlay == "PersonImg" or ComPlay == "TreeImg":
            Result = "The Player Wins"
            Display.config(text = Result)
        else:
            Result = "The Machine Wins"
            Display.config(text = Result)

        # Fix Choice Pics
        PlayPic.config(image = LightningImg)
        if ComPlay == "RockImg":
            ComPic.config(image = RockImg )
        elif ComPlay == "FireImg":
            ComPic.config(image = FireImg)
        elif ComPlay == "ScissorsImg":
            ComPic.config(image = ScissorsImg)
        elif ComPlay == "SnakeImg":
            ComPic.config(image = SnakeImg)
        elif ComPlay == "PersonImg":
            ComPic.config(image = PersonImg)
        elif ComPlay == "TreeImg":
            ComPic.config(image = TreeImg)
        elif ComPlay == "WolfImg":
            ComPic.config(image = WolfImg)
        elif ComPlay == "SpongeImg":
            ComPic.config(image = SpongeImg)
        elif ComPlay == "PaperImg":
            ComPic.config(image = PaperImg)
        elif ComPlay == "AirImg":
            ComPic.config(image = AirImg)
        elif ComPlay == "WaterImg":
            ComPic.config(image = WaterImg)
        elif ComPlay == "DragonImg":
            ComPic.config(image = DragonImg)
        elif ComPlay == "DevilImg":
            ComPic.config(image = DevilImg)
        elif ComPlay == "LightningImg":
            ComPic.config(image = LightningImg)
        else:
            ComPic.config(image = GunImg)

        
            

    # Gun
    def Gun():
        ComPlay = ComOpt[str(random.randint(0,14))]
        if ComPlay == "GunImg":
            Result = "Stalemate"
            Display.config(text = Result)
        elif ComPlay == "RockImg" or ComPlay == "FireImg" or ComPlay == "ScissorsImg" or ComPlay == "SnakeImg" or ComPlay == "PersonImg" or ComPlay == "TreeImg" or ComPlay == "WolfImg":
            Result = "The Player Wins"
            Display.config(text = Result)
        else:
            Result = "The Machine Wins"
            Display.config(text = Result)

        # Fix Choice Pics
        PlayPic.config(image = GunImg)
        if ComPlay == "RockImg":
            ComPic.config(image = RockImg )
        elif ComPlay == "FireImg":
            ComPic.config(image = FireImg)
        elif ComPlay == "ScissorsImg":
            ComPic.config(image = ScissorsImg)
        elif ComPlay == "SnakeImg":
            ComPic.config(image = SnakeImg)
        elif ComPlay == "PersonImg":
            ComPic.config(image = PersonImg)
        elif ComPlay == "TreeImg":
            ComPic.config(image = TreeImg)
        elif ComPlay == "WolfImg":
            ComPic.config(image = WolfImg)
        elif ComPlay == "SpongeImg":
            ComPic.config(image = SpongeImg)
        elif ComPlay == "PaperImg":
            ComPic.config(image = PaperImg)
        elif ComPlay == "AirImg":
            ComPic.config(image = AirImg)
        elif ComPlay == "WaterImg":
            ComPic.config(image = WaterImg)
        elif ComPlay == "DragonImg":
            ComPic.config(image = DragonImg)
        elif ComPlay == "DevilImg":
            ComPic.config(image = DevilImg)
        elif ComPlay == "LightningImg":
            ComPic.config(image = LightningImg)
        else:
            ComPic.config(image = GunImg)
    
##############################################################################         

    # Frames for organization
    LabelFrame = Frame(PentaDeca)
    LabelFrame.pack(pady = 25)
    ChoiceFrame = Frame(PentaDeca)
    ChoiceFrame.pack(pady = 20)
    DisplayFrame = Frame(PentaDeca)
    DisplayFrame.pack(pady =15)
    ButtonFrame = Frame(PentaDeca)
    ButtonFrame.pack(pady=10)
    
    # Player/Com Labels
    PlayTag = Label(LabelFrame, text = "Player",font = 10)
    Versus = Label(LabelFrame, text = "VS", font = "normal 10 bold")
    ComTag = Label(LabelFrame, text = "Machine", font = 10)
 
    PlayTag.pack(side = LEFT)
    Versus.pack(side = LEFT)
    ComTag.pack(side = LEFT)

    # Option Display Initialization
    PlayPic = Label(ChoiceFrame, image = UnknownImg)
    ComPic = Label(ChoiceFrame, image= UnknownImg)
    PlayPic.pack(side = LEFT)
    ComPic.pack(side = LEFT)

    
    # Result Display
    Display = Label(DisplayFrame, text = "", font = "normal 20 bold", bg = "white", width = 15 , borderwidth = 2, relief = "solid")
    Display.pack(pady = 20)

    # Battle Buttons
    Rock = Button(ButtonFrame, text = "Rock", command = Rock)
    Fire = Button(ButtonFrame, text = "Fire", command = Fire)
    Scissors = Button(ButtonFrame, text = "Scissors", command = Scissors)
    Snake = Button(ButtonFrame, text = "Snake", command = Snake)
    Person = Button(ButtonFrame, text = "Person", command = Person)
    Tree = Button(ButtonFrame, text = "Tree", command = Tree)
    Wolf = Button(ButtonFrame, text = "Wolf", command = Wolf)
    Sponge = Button(ButtonFrame, text = "Sponge", command = Sponge)
    Paper = Button(ButtonFrame, text = "Paper", command = Paper)
    Air = Button(ButtonFrame, text = "Air", command = Air)
    Water = Button(ButtonFrame, text = "Water", command = Water)
    Dragon = Button(ButtonFrame, text = "Dragon", command = Dragon)
    Devil = Button(ButtonFrame, text = "Devil", command = Devil)
    Lightning = Button(ButtonFrame, text = "Lightning", command = Lightning)
    Gun = Button(ButtonFrame, text = "Gun", command = Gun)
    
    # Control Buttons
    Inst = Button(ButtonFrame, text = "Help", command = PentaDecaInst)
    KillGame = Button(ButtonFrame, text = "Quit", command = lambda: PentaDeca.destroy())
    # Format Buttons and Labels
    PlayTag.pack(side = LEFT, padx = 10, pady =10)
    ComTag.pack(padx = 10, pady =10)
    Inst.pack(side = LEFT, padx=50, pady=10)
    Rock.pack(side = LEFT, padx=10, pady=10)
    Fire.pack(side = LEFT, padx=10, pady=10)
    Scissors.pack(side = LEFT, padx=10, pady=10)
    Snake.pack(side = LEFT, padx=10, pady=10)
    Person.pack(side = LEFT, padx=10, pady=10)
    Tree.pack(side = LEFT, padx=10, pady=10)
    Wolf.pack(side = LEFT, padx=10, pady=10)
    Sponge.pack(side = LEFT, padx=10, pady=10)
    Paper.pack(side = LEFT, padx=10, pady=10)
    Air.pack(side = LEFT, padx=10, pady=10)
    Water.pack(side = LEFT, padx=10, pady=10)
    Dragon.pack(side = LEFT, padx=10, pady=10)
    Devil.pack(side = LEFT, padx=10, pady=10)
    Lightning.pack(side = LEFT, padx=10, pady=10)
    Gun.pack(side = LEFT, padx=10, pady=10)
    KillGame.pack(side = LEFT, padx=50, pady=10)
    
# PentaDeca Instructions
def PentaDecaInst():
    PentaDecaInst = Toplevel(Home)
    PentaDecaInst.title("What Beats What")
    
# Label all advantage combos
    ReadRock = Label(PentaDecaInst, text = "Rock beats Fire, Scissors, Snake, Person, Tree, Wolf, and Sponge")
    ReadFire = Label(PentaDecaInst, text = "Fire beats Scissors, Snake, Person, Tree, Wolf, Sponge, and Paper")
    ReadScissors = Label(PentaDecaInst, text = "Scissors beat Snake, Person, Tree, Wolf, Sponge, Paper, and Air")
    ReadSnake = Label(PentaDecaInst, text = "Snake beatsss Person, Tree, Wolf, Sponge, Paper, Air, and Water")
    ReadPerson = Label(PentaDecaInst, text = "Person beats Tree, Wolf, Sponge, Paper, Air, Water, and Dragon")
    ReadTree = Label(PentaDecaInst, text = "Tree beats Wolf, Sponge, Paper, Air, Water, Dragon, and Devil")
    ReadWolf = Label(PentaDecaInst, text = "Wolf beats Sponge, Paper, Air, Water, Dragon, Devil, and Lightning")
    ReadSponge = Label(PentaDecaInst, text = "Sponge beats Paper, Air, Water, Dragon, Devil, Lightning, and Gun")
    ReadPaper = Label(PentaDecaInst, text = "Paper beats Air, Water, Dragon, Devil, Lightning, Gun, and Rock")
    ReadAir = Label(PentaDecaInst, text = "Air beats Water, Dragon, Devil, Lightning, Gun, Rock, and Fire")
    ReadWater = Label(PentaDecaInst, text = "Water beats Dragon, Devil, Lightning, Gun, Rock, Fire, and Scissors")
    ReadDragon = Label(PentaDecaInst, text = "Dragon beats Devil, Lightning, Gun, Rock, Fire, Scissors, and Snake")
    ReadDevil = Label(PentaDecaInst, text = "Devil beats Lightning, Gun, Rock, Fire, Scissors, Snake, and Human")
    ReadLightning = Label(PentaDecaInst, text = "Lightning beats Gun, Rock, Fire, Scissors, Snake, Human, and Tree")
    ReadGun = Label(PentaDecaInst, text = "Gun beats Rock, Fire, Scissors, Snake, Human, Tree, and Wolf")


    
# Kill Switch
    KillInst = Button(PentaDecaInst, text = "Close", command = lambda: PentaDecaInst.destroy())

# Pack it
    ReadRock.pack(pady = 10)
    ReadFire.pack(pady = 10)
    ReadScissors.pack(pady = 10)
    ReadSnake.pack(pady = 10)
    ReadPerson.pack(pady = 10)
    ReadTree.pack(pady = 10)
    ReadWolf.pack(pady = 10)
    ReadSponge.pack(pady = 10)
    ReadPaper.pack(pady = 10)
    ReadAir.pack(pady = 10)
    ReadWater.pack(pady = 10)
    ReadDragon.pack(pady = 10)
    ReadDevil.pack(pady = 10)
    ReadLightning.pack(pady = 10)
    ReadGun.pack(pady = 10)
    KillInst.pack(pady = 10)

######################################################################

# GUI Main/Game set up
Home = Tk()
Home.title("Main Menu")

# Image Initialize
UnknownImg = PhotoImage(file = "Unknown.png")
RockImg = PhotoImage(file = "Rock.png")
FireImg = PhotoImage(file = "Fire.png")
ScissorsImg = PhotoImage(file = "Scissors.png")
SnakeImg = PhotoImage(file = "Snake.png")
PersonImg = PhotoImage(file = "Person.png")
TreeImg = PhotoImage(file = "Tree.png")
WolfImg = PhotoImage(file = "Wolf.png")
SpongeImg = PhotoImage(file = "Sponge.png")
PaperImg = PhotoImage(file = "Paper.png")
AirImg = PhotoImage(file = "Air.png")
WaterImg = PhotoImage(file = "Water.png")
DragonImg = PhotoImage(file = "Dragon.png")
DevilImg = PhotoImage(file = "Devil.png")
LightningImg = PhotoImage(file = "Lightning.png")
GunImg = PhotoImage(file = "Gun.png")


# Computer Options
ComOpt = {"0":"RockImg", "1":"FireImg", "2":"ScissorsImg", "3":"SnakeImg", "4":"PersonImg", "5":"TreeImg", "6":"WolfImg", "7":"SpongeImg", "8":"PaperImg", "9":"AirImg", "10":"WaterImg", "11":"DragonImg", "12":"DevilImg", "13":"LightningImg", "14":"GunImg"}

# Beginning Buttons
Instructions = Button(Home, text = "Instructions",command = InstructWindow)
GameStart = Button(Home, text = "Play Game", command = PentaDeca)
KillStart = Button(Home, text = "Quit", command = lambda: Home.destroy())

#Home Pic
HomeImg = PhotoImage(file = "PentaDeca Star.png")
HomePic = Label(Home, image = HomeImg)

#Format Buttons and Picture
HomePic.pack()
Instructions.pack(side = LEFT, padx = 25)
GameStart.pack(side = LEFT, padx = 25)
KillStart.pack(side = LEFT, padx = 25)

