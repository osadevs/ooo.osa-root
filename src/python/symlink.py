#!/bin/env python
# -*- encoding: utf-8 -*-
#<!--++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++--> 
#<!--                Open Simulation Architecture (OSA)                  -->
#<!--                                                                    -->
#<!--      This software is distributed under the terms of the           -->
#<!--           CECILL-C FREE SOFTWARE LICENSE AGREEMENT                 -->
#<!--  (see http://www.cecill.info/licences/Licence_CeCILL-C_V1-en.html) -->
#<!--                                                                    -->
#<!--  Copyright © 2006-2015 Université Nice Sophia Antipolis            -->
#<!--  Contact author: Olivier Dalle (olivier.dalle@unice.fr)            -->
#<!--                                                                    -->
#<!--  Parts of this software development were supported and hosted by   -->
#<!--  INRIA from 2006 to 2015, in the context of the common research    -->
#<!--  teams of INRIA and I3S, UMR CNRS 7172 (MASCOTTE, COATI, OASIS and -->
#<!--  SCALE).                                                           -->
#<!--++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++--> 
"""
Usage: symlink -c|-d

Creates or removes symbolic links to maven sub-modules in current directory.

Options:
    -c: creates symlinks
    -d: rmoves symlinks
"""


import os,sys,string

def link():
    try:
        os.symlink("../ooo.maven-config","ooo.maven-config")
        print """
     vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
     >>>>> Symlinks created. Rerun last maven command. <<<<<
     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
"""
    except:
        pass
    
def unlink():
    try:
        os.unlink("ooo.maven-config")
        print "Symlinks cleared."
    except:
        pass


if len(sys.argv) > 0:
    if sys.argv[1] == "-c":
        link()
    elif sys.argv[1] == "-d":
        unlink()
    else:
        print help(__name__)
