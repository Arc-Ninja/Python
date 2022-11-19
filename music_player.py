# Creator: Arc
# Copyright (c) 2022
# All Rights Reserved
# Total lines of code: 555 (including comments)
# Images in assests folder can be changed to change looks of the player.


from pydub import AudioSegment
import pygame
from pygame import K_LEFT, mixer
from os import walk
import os
import os
import sys
import sys

username = os.getlogin()
pygame.init()
mixer.init()
screen = pygame.display.set_mode((425, 575))


pygame.display.set_caption("Arc Music")
icon = pygame.image.load("assets\\headphone.png")
pygame.display.set_icon(icon)

# background
bgimg = pygame.image.load("assets\\bg.png")
lightblack = pygame.image.load("assets\\lightblack.jpg")
prussianblue = pygame.image.load("assets\\prussianblue.jpg")

# font
header_font = pygame.font.SysFont("Arial black", 16)
disp_font = pygame.font.SysFont("Arial", 16)

# header
header_title = "MY MUSIC"


def header(x, y):
    header_render = header_font.render(header_title, True, (255, 255, 255))
    screen.blit(lightblack, (x - 20, y - 40))
    screen.blit(header_render, (x, y))


# control_pannel
def control_panel(x, y):
    screen.blit(prussianblue, (x-183, y))
    music_time = str(int(pygame.mixer.music.get_pos()/1000))
    music_position = disp_font.render(music_time,True, (255,255,255))
    screen.blit(music_position,(x-170,y+20))


# button images
playimg = pygame.image.load("assets\\play.png")
pauseimg = pygame.image.load("assets\\pause.png")
nextimg = pygame.image.load("assets\\next.png")
previousimg = pygame.image.load("assets\\previous.png")

# directory
path = f"C:\\Users\\{username}\\Music\\music\\"
path_adder = f"C:\\Users\\{username}\\Music\\music\\"
songs = []
for (dirpath, dirnames, filenames) in walk(path):
    songs.extend(filenames)
    break


def directory(x, y):
    song_no = 0
    for song_no in songs:
        song_render = disp_font.render(song_no, True, (255, 255, 255))
        screen.blit(song_render, (x, y))
        y += 20


# songs
song = 0
try:
    src = path_adder + songs[song]
    dst = path_adder + songs[song].replace(".mp3", ".wav")
    audSeg = AudioSegment.from_mp3(src)
    audSeg.export(dst, format="wav")
    pygame.mixer.music.load(dst)
except:
    None

def play(self):
    src = path_adder + songs[song]
    dst = path_adder + songs[song].replace(".mp3", ".wav")
    audSeg = AudioSegment.from_mp3(src)
    audSeg.export(dst, format="wav")
    pygame.mixer.music.load(dst)
    pygame.mixer.music.play()
    music_state = "playing"

music_state = "stopped"
end_event = pygame.USEREVENT+1
pygame.mixer.music.set_endevent(end_event)
running = True
x = 10
y = 55


# MAIN WHILE LOOP
while running:
    screen.fill((0, 0, 0))
    screen.blit(bgimg, (0, 0))
    directory(x, y)
    control_panel(183, 515)
    header(20, 15)
    screen.blit(nextimg, (250, 513))
    screen.blit(previousimg, (116, 513))
    mouse_pos = pygame.mouse.get_pos()
    if y <= 55 - 20 * len(songs):
        song = 0
        y = 55
        try:
            try:
                pygame.mixer.music.unload()
                # os.remove(dst)           <--- This part may cause prob in future
                src = path_adder + songs[song]
                dst = path_adder + songs[song].replace(".mp3", ".wav")
                audSeg = AudioSegment.from_mp3(src)
                audSeg.export(dst, format="wav")
                pygame.mixer.music.load(dst)
                pygame.mixer.music.play()
                music_state = "playing"
            except:
                song += 1
                y -= 20
                src = path_adder + songs[song]
                dst = path_adder + songs[song].replace(".mp3", ".wav")
                audSeg = AudioSegment.from_mp3(src)
                audSeg.export(dst, format="wav")
                pygame.mixer.music.load(dst)
                pygame.mixer.music.play()
                music_state = "playing"
        except:
            pass
    else:
        None

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.mixer.music.unload()
            dst = path_adder + songs[song].replace(".mp3", ".wav")
            os.remove(dst)
            running = False

        # mouse keys
        if event.type == pygame.MOUSEBUTTONDOWN:

            # play/pause
            if (
                mouse_pos[0] >= 187
                and mouse_pos[0] <= 237
                and mouse_pos[1] >= 517
                and mouse_pos[1] <= 567
            ):
                if music_state == "paused":
                    music_state = "unpaused"
                    pygame.mixer.music.unpause()
                elif music_state == "stopped":
                    music_state = "playing"
                    pygame.mixer.music.play()
                else:
                    music_state = "paused"
                    pygame.mixer.music.pause()

            # next
            if (
                mouse_pos[0] >= 265
                and mouse_pos[0] <= 300
                and mouse_pos[1] >= 520
                and mouse_pos[1] <= 567
            ):
                if int(song) < (len(songs) - 1):
                    try:
                        try:
                            pygame.mixer.music.unload()
                            os.remove(dst)
                            song += 1
                            y -= 20
                            src = path_adder + songs[song]
                            dst = path_adder + songs[song].replace(".mp3", ".wav")
                            audSeg = AudioSegment.from_mp3(src)
                            audSeg.export(dst, format="wav")
                            pygame.mixer.music.load(dst)
                            pygame.mixer.music.play()
                            music_state = "playing"
                        except:
                            song += 1
                            y -= 20
                            src = path_adder + songs[song]
                            dst = path_adder + songs[song].replace(".mp3", ".wav")
                            audSeg = AudioSegment.from_mp3(src)
                            audSeg.export(dst, format="wav")
                            pygame.mixer.music.load(dst)
                            pygame.mixer.music.play()
                            music_state = "playing"
                    except:
                        pass
                elif int(song) == (len(songs) - 1):
                    song = 0
                    y = 55
                    try:
                        try:
                            pygame.mixer.music.unload()
                            os.remove(dst)
                            src = path_adder + songs[song]
                            dst = path_adder + songs[song].replace(".mp3", ".wav")
                            audSeg = AudioSegment.from_mp3(src)
                            audSeg.export(dst, format="wav")
                            pygame.mixer.music.load(dst)
                            pygame.mixer.music.play()
                            music_state = "playing"
                        except:
                            song += 1
                            y -= 20
                            src = path_adder + songs[song]
                            dst = path_adder + songs[song].replace(".mp3", ".wav")
                            audSeg = AudioSegment.from_mp3(src)
                            audSeg.export(dst, format="wav")
                            pygame.mixer.music.load(dst)
                            pygame.mixer.music.play()
                            music_state = "playing"
                    except:
                        pass
                else:
                    None

            # previous
            if (
                mouse_pos[0] >= 130
                and mouse_pos[0] <= 170
                and mouse_pos[1] >= 520
                and mouse_pos[1] <= 567
            ):
                if int(song) > 0:
                    try:
                        try:
                            pygame.mixer.music.unload()
                            os.remove(dst)
                            song -= 1
                            y += 20
                            src = path_adder + songs[song]
                            dst = path_adder + songs[song].replace(".mp3", ".wav")
                            audSeg = AudioSegment.from_mp3(src)
                            audSeg.export(dst, format="wav")
                            pygame.mixer.music.load(dst)
                            pygame.mixer.music.play()
                            music_state = "playing"
                        except:
                            song -= 1
                            y += 20
                            src = path_adder + songs[song]
                            dst = path_adder + songs[song].replace(".mp3", ".wav")
                            audSeg = AudioSegment.from_mp3(src)
                            audSeg.export(dst, format="wav")
                            pygame.mixer.music.load(dst)
                            pygame.mixer.music.play()
                            music_state = "playing"
                    except:
                        pass
                elif int(song) == 0:
                    song = len(songs) - 1
                    y = 55 - ((len(songs) - 1) * 20)
                    try:
                        try:
                            pygame.mixer.music.unload()
                            os.remove(dst)
                            src = path_adder + songs[song]
                            dst = path_adder + songs[song].replace(".mp3", ".wav")
                            audSeg = AudioSegment.from_mp3(src)
                            audSeg.export(dst, format="wav")
                            pygame.mixer.music.load(dst)
                            pygame.mixer.music.play()
                            music_state = "playing"
                        except:
                            song -= 1
                            y += 20
                            src = path_adder + songs[song]
                            dst = path_adder + songs[song].replace(".mp3", ".wav")
                            audSeg = AudioSegment.from_mp3(src)
                            audSeg.export(dst, format="wav")
                            pygame.mixer.music.load(dst)
                            pygame.mixer.music.play()
                            music_state = "playing"
                    except:
                        pass
                else:
                    None

            # selecting song
            if y >= 55 - 20 * len(songs):
                if mouse_pos[1] >= 55 and mouse_pos[1] <= 515:
                    if mouse_pos[1] >= 55 + 20 and mouse_pos[1] <= (55 + 20 * 2):
                        song = song + 1
                        y -= 20
                    elif mouse_pos[1] >= 55 + 20 * 2 and mouse_pos[1] <= (55 + 20 * 3):
                        song = song + 2
                        y -= 20 * 2
                    elif mouse_pos[1] >= 55 + 20 * 3 and mouse_pos[1] <= (55 + 20 * 4):
                        song = song + 3
                        y -= 20 * 3
                    elif mouse_pos[1] >= 55 + 20 * 4 and mouse_pos[1] <= (55 + 20 * 5):
                        song = song + 4
                        y -= 20 * 4
                    elif mouse_pos[1] >= 55 + 20 * 5 and mouse_pos[1] <= (55 + 20 * 6):
                        song = song + 5
                        y -= 20 * 5
                    elif mouse_pos[1] >= 55 + 20 * 6 and mouse_pos[1] <= (55 + 20 * 7):
                        song = song + 6
                        y -= 20 * 6
                    elif mouse_pos[1] >= 55 + 20 * 7 and mouse_pos[1] <= (55 + 20 * 8):
                        song = song + 7
                        y -= 20 * 7
                    elif mouse_pos[1] >= 55 + 20 * 8 and mouse_pos[1] <= (55 + 20 * 9):
                        song = song + 8
                        y -= 20 * 8
                    elif mouse_pos[1] >= 55 + 20 * 9 and mouse_pos[1] <= (55 + 20 * 10):
                        song = song + 9
                        y -= 20 * 9
                    elif mouse_pos[1] >= 55 + 20 * 10 and mouse_pos[1] <= (
                        55 + 20 * 11
                    ):
                        song = song + 10
                        y -= 20 * 10
                    elif mouse_pos[1] >= 55 + 20 * 11 and mouse_pos[1] <= (
                        55 + 20 * 12
                    ):
                        song = song + 11
                        y -= 20 * 11
                    elif mouse_pos[1] >= 55 + 20 * 12 and mouse_pos[1] <= (
                        55 + 20 * 13
                    ):
                        song = song + 12
                        y -= 20 * 12
                    elif mouse_pos[1] >= 55 + 20 * 13 and mouse_pos[1] <= (
                        55 + 20 * 14
                    ):
                        song = song + 13
                        y -= 20 * 13
                    elif mouse_pos[1] >= 55 + 20 * 14 and mouse_pos[1] <= (
                        55 + 20 * 15
                    ):
                        song = song + 14
                        y -= 20 * 14
                    elif mouse_pos[1] >= 55 + 20 * 15 and mouse_pos[1] <= (
                        55 + 20 * 16
                    ):
                        song = song + 15
                        y -= 20 * 15
                    elif mouse_pos[1] >= 55 + 20 * 16 and mouse_pos[1] <= (
                        55 + 20 * 17
                    ):
                        song = song + 16
                        y -= 20 * 16
                    elif mouse_pos[1] >= 55 + 20 * 17 and mouse_pos[1] <= (
                        55 + 20 * 18
                    ):
                        song = song + 17
                        y -= 20 * 17
                    elif mouse_pos[1] >= 55 + 20 * 18 and mouse_pos[1] <= (
                        55 + 20 * 19
                    ):
                        song = song + 18
                        y -= 20 * 18
                    elif mouse_pos[1] >= 55 + 20 * 19 and mouse_pos[1] <= (
                        55 + 20 * 20
                    ):
                        song = song + 19
                        y -= 20 * 19
                    elif mouse_pos[1] >= 55 + 20 * 20 and mouse_pos[1] <= (
                        55 + 20 * 21
                    ):
                        song = song + 20
                        y -= 20 * 20
                    elif mouse_pos[1] >= 55 + 20 * 21 and mouse_pos[1] <= (
                        55 + 20 * 22
                    ):
                        song = song + 21
                        y -= 20 * 21
                    elif mouse_pos[1] >= 55 + 20 * 22 and mouse_pos[1] <= (
                        55 + 20 * 23
                    ):
                        song = song + 22
                        y -= 20 * 22
                    elif mouse_pos[1] >= 55 + 20 * 23 and mouse_pos[1] <= (
                        55 + 20 * 24
                    ):
                        song = song + 23
                        y -= 20 * 23

                    else:
                        None
                    try:
                        try:
                            try:
                                pygame.mixer.music.unload()
                                os.remove(dst)
                                src = path_adder + songs[song]
                                dst = path_adder + songs[song].replace(".mp3", ".wav")
                                audSeg = AudioSegment.from_mp3(src)
                                audSeg.export(dst, format="wav")
                                pygame.mixer.music.load(dst)
                                pygame.mixer.music.play()
                                music_state = "playing"
                            except:
                                pygame.mixer.music.unload()
                                src = path_adder + songs[song]
                                dst = path_adder + songs[song].replace(".mp3", ".wav")
                                audSeg = AudioSegment.from_mp3(src)
                                audSeg.export(dst, format="wav")
                                pygame.mixer.music.load(dst)
                                pygame.mixer.music.play()
                                music_state = "playing"
                        except:
                            song += 1
                            y -= 20
                            src = path_adder + songs[song]
                            dst = path_adder + songs[song].replace(".mp3", ".wav")
                            audSeg = AudioSegment.from_mp3(src)
                            audSeg.export(dst, format="wav")
                            pygame.mixer.music.load(dst)
                            pygame.mixer.music.play()
                            music_state = "playing"
                    except:
                        pass
            else:
                None

        # keypress
        if event.type == pygame.KEYDOWN:
            # key space
            if event.key == pygame.K_SPACE:
                if music_state == "paused":
                    music_state = "unpaused"
                    pygame.mixer.music.unpause()
                elif music_state == "stopped":
                    music_state = "playing"
                    pygame.mixer.music.play()
                else:
                    music_state = "paused"
                    pygame.mixer.music.pause()

            # key right
            if event.key == pygame.K_RIGHT:
                if int(song) < (len(songs) - 1):
                    try:
                        try:
                            pygame.mixer.music.unload()
                            os.remove(dst)
                            song += 1
                            y -= 20
                            src = path_adder + songs[song]
                            dst = path_adder + songs[song].replace(".mp3", ".wav")
                            audSeg = AudioSegment.from_mp3(src)
                            audSeg.export(dst, format="wav")
                            pygame.mixer.music.load(dst)
                            pygame.mixer.music.play()
                            music_state = "playing"
                        except:
                            song += 1
                            y -= 20
                            src = path_adder + songs[song]
                            dst = path_adder + songs[song].replace(".mp3", ".wav")
                            audSeg = AudioSegment.from_mp3(src)
                            audSeg.export(dst, format="wav")
                            pygame.mixer.music.load(dst)
                            pygame.mixer.music.play()
                            music_state = "playing"
                    except:
                        pass
                elif int(song) == (len(songs) - 1):
                    song = 0
                    y = 55
                    try:
                        try:
                            pygame.mixer.music.unload()
                            os.remove(dst)
                            src = path_adder + songs[song]
                            dst = path_adder + songs[song].replace(".mp3", ".wav")
                            audSeg = AudioSegment.from_mp3(src)
                            audSeg.export(dst, format="wav")
                            pygame.mixer.music.load(dst)
                            pygame.mixer.music.play()
                            music_state = "playing"
                        except:
                            song += 1
                            y -= 20
                            src = path_adder + songs[song]
                            dst = path_adder + songs[song].replace(".mp3", ".wav")
                            audSeg = AudioSegment.from_mp3(src)
                            audSeg.export(dst, format="wav")
                            pygame.mixer.music.load(dst)
                            pygame.mixer.music.play()
                            music_state = "playing"
                    except:
                        pass
                else:
                    None

            # key left
            if event.key == pygame.K_LEFT:
                if int(song) > 0:
                    try:
                        try:
                            pygame.mixer.music.unload()
                            os.remove(dst)
                            song -= 1
                            y += 20
                            src = path_adder + songs[song]
                            dst = path_adder + songs[song].replace(".mp3", ".wav")
                            audSeg = AudioSegment.from_mp3(src)
                            audSeg.export(dst, format="wav")
                            pygame.mixer.music.load(dst)
                            pygame.mixer.music.play()
                            music_state = "playing"
                        except:
                            song -= 1
                            y += 20
                            src = path_adder + songs[song]
                            dst = path_adder + songs[song].replace(".mp3", ".wav")
                            audSeg = AudioSegment.from_mp3(src)
                            audSeg.export(dst, format="wav")
                            pygame.mixer.music.load(dst)
                            pygame.mixer.music.play()
                            music_state = "playing"
                    except:
                        pass
                elif int(song) == 0:
                    song = len(songs) - 1
                    y = 55 - ((len(songs) - 1) * 20)
                    try:
                        try:
                            pygame.mixer.music.unload()
                            os.remove(dst)
                            src = path_adder + songs[song]
                            dst = path_adder + songs[song].replace(".mp3", ".wav")
                            audSeg = AudioSegment.from_mp3(src)
                            audSeg.export(dst, format="wav")
                            pygame.mixer.music.load(dst)
                            pygame.mixer.music.play()
                            music_state = "playing"
                        except:
                            song -= 1
                            y += 20
                            src = path_adder + songs[song]
                            dst = path_adder + songs[song].replace(".mp3", ".wav")
                            audSeg = AudioSegment.from_mp3(src)
                            audSeg.export(dst, format="wav")
                            pygame.mixer.music.load(dst)
                            pygame.mixer.music.play()
                            music_state = "playing"
                    except:
                        pass
                else:
                    None
        #Next song when song ends
        if event.type == end_event:
            if int(song) < (len(songs) - 1):
                    try:
                        try:
                            pygame.mixer.music.unload()
                            os.remove(dst)
                            song += 1
                            y -= 20
                            src = path_adder + songs[song]
                            dst = path_adder + songs[song].replace(".mp3", ".wav")
                            audSeg = AudioSegment.from_mp3(src)
                            audSeg.export(dst, format="wav")
                            pygame.mixer.music.load(dst)
                            pygame.mixer.music.play()
                            music_state = "playing"
                        except:
                            song += 1
                            y -= 20
                            src = path_adder + songs[song]
                            dst = path_adder + songs[song].replace(".mp3", ".wav")
                            audSeg = AudioSegment.from_mp3(src)
                            audSeg.export(dst, format="wav")
                            pygame.mixer.music.load(dst)
                            pygame.mixer.music.play()
                            music_state = "playing"
                    except:
                        pass
            elif int(song) == (len(songs) - 1):
                song = 0
                y = 55
                try:
                    try:
                        pygame.mixer.music.unload()
                        os.remove(dst)
                        src = path_adder + songs[song]
                        dst = path_adder + songs[song].replace(".mp3", ".wav")
                        audSeg = AudioSegment.from_mp3(src)
                        audSeg.export(dst, format="wav")
                        pygame.mixer.music.load(dst)
                        music_state = "stopped"
                    except:
                        song += 1
                        y -= 20
                        src = path_adder + songs[song]
                        dst = path_adder + songs[song].replace(".mp3", ".wav")
                        audSeg = AudioSegment.from_mp3(src)
                        audSeg.export(dst, format="wav")
                        pygame.mixer.music.load(dst)
                        music_state = "stopped"
                except:
                    pass
            else:
                None

    if music_state == "paused":
        screen.blit(playimg, (183, 513))
    elif music_state == "stopped":
        screen.blit(playimg, (183, 513))
    else:
        screen.blit(pauseimg, (183, 513))

    pygame.display.update()
