import pygame
import os

def play_music(music_file, loop=True, volume=1.0): # DEFINE MY VOLUME ARGUMENTS
    pygame.mixer.init()
    pygame.mixer.music.load('assets/christmas/Music/music 1.mp3')
    pygame.mixer.music.set_volume(volume)
    pygame.mixer.music.play(loops=-1, start=0.0) # INDICATES INFINITE LOOPING TO RESET AT THE BEGINNING ONCE ENDED


def stop_music():
    pygame.mixer.music.stop()
