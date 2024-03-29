#####################################################################
# -*- coding: iso-8859-1 -*-                                        #
#                                                                   #
# Frets on Fire                                                     #
# Copyright (C) 2006 Sami Ky�stil�                                  #
#                                                                   #
# This program is free software; you can redistribute it and/or     #
# modify it under the terms of the GNU General Public License       #
# as published by the Free Software Foundation; either version 2    #
# of the License, or (at your option) any later version.            #
#                                                                   #
# This program is distributed in the hope that it will be useful,   #
# but WITHOUT ANY WARRANTY; without even the implied warranty of    #
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the     #
# GNU General Public License for more details.                      #
#                                                                   #
# You should have received a copy of the GNU General Public License #
# along with this program; if not, write to the Free Software       #
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,        #
# MA  02110-1301, USA.                                              #
#####################################################################

import pygame
import os
import Log


class Video:
  def __init__(self, caption = "Game"):
    self.screen     = None
    self.caption    = caption
    self.fullscreen = False
    self.flags      = True

  def setMode(self, resolution, fullscreen = False, flags = pygame.DOUBLEBUF,
              multisamples = 0):
    if fullscreen:
      flags |= pygame.FULLSCREEN
      
    self.flags      = flags
    self.fullscreen = fullscreen

    try:    
      pygame.display.quit()
    except:
      pass
      
    pygame.display.init()
    
      

    try:
      self.screen = pygame.display.set_mode(resolution, flags)
    except Exception, e:
      Log.error(str(e))
      if multisamples:
        Log.warn("Video setup failed. Trying without antialiasing.")
        multisamples = 0
        self.screen = pygame.display.set_mode(resolution, flags)
      else:
        Log.error("Video setup failed. Make sure your graphics card supports 32 bit display modes.")
        raise

    pygame.display.set_caption(self.caption)
    pygame.mouse.set_visible(False)

    return bool(self.screen)
    
  def toggleFullscreen(self):
    assert self.screen
    
    return pygame.display.toggle_fullscreen()

  def flip(self):
    pygame.display.flip()

  def getVideoModes(self):
    return pygame.display.list_modes()
