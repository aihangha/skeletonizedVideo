#!/usr/bin/env python
from moviepy.editor import *
def time_symetrize(clip):
    """ Returns the clip played forwards then backwards. In case
    you are wondering, vfx (short for Video FX) is loaded by
    >>> from moviepy.editor import * """
    return concatenate([clip, clip.fx( vfx.time_mirror )])

clip = (VideoFileClip("HorseRunning.mp4", audio=False)
        .subclip(9,15)
        .fx( time_symetrize ))

clip.write_gif('hor4.gif', fps=15, fuzz=2)