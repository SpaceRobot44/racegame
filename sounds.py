import pygame
from pygame import mixer

mixer.init()
mixer.music.load("Video Game Music.mp3")
mixer.music.play(-1)