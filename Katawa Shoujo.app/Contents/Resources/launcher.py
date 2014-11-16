#!/usr/bin/pythonw
# The Ren'Py launcher for Macintosh.

_mac_version = (6, 10, 1)

# Fix platform on older macs.
import platform

def mac_ver(*args, **kwargs):
    return ('10', ('', '', ''), 'RenPy')

platform.mac_ver = mac_ver


def mac_imports():
    """
    This function imports the libraries that are needed by Ren'Py. This is
    so that py2app will pull them in, but they won't pollute this namespace.
    """

    import renpy.bootstrap
    import renpy
    import pygame
    import _renpy
    import pysdlsound
    import nativemidi
    import cPickle
    import pickle

def mac_version(required):

    import EasyDialogs as ed
    import sys

    if required > _mac_version:

        message = "This version of the Ren'Py launcher is too old to run this game. You have version %d.%d.%d, while the game requires version %d.%d.%d.\n\nPlease go to http://www.renpy.org, and download the latest version of the launcher." % \
                  (_mac_version[0], _mac_version[1], _mac_version[2],
                   required[0], required[1], required[2])
                   
        
        ed.Message(message)
        sys.exit(0)
    

def mac_find_game():
    """
    Returns a path to the .py or .pyw file that should be run in order to
    play the game.
    """

    import EasyDialogs as ed
    import aepack
    import os.path
    import os
    import sys

    # See if we were given a file through drag-and-drop or on the
    # command line.  If so, we can run it.
    if len(sys.argv) > 1:
        return sys.argv[1]	

    # Check the current (Resources) directory for a game we can
    # possibly run. That game will be in the autorun directory.

    autorundir = os.environ.get('RESOURCEPATH', '.') + '/autorun/'

    if os.path.isdir(autorundir):
        for fn in os.listdir(autorundir):
            if fn.endswith(".py") or fn.endswith(".pyw"):
                return autorundir + fn

    # Look for a python file with the same name as the application.
    fn = os.environ.get('RESOURCEPATH', None)
    if fn[-1] == '/':
        fn = fn[:-1]
    if fn.endswith(".app/Contents/Resources"):
        fn = fn[:-len(".app/Contents/Resources")]
    
    if os.path.exists(fn + ".py"):
        return fn + ".py"    

    # If there's a single python file in the same directory as the app, 
    # run it.
    autorundir = os.environ.get('RESOURCEPATH', '.') + '/../../..'
    autorundir = os.path.abspath(autorundir)

    files = [ ]

    if os.path.isdir(autorundir):
        for fn in os.listdir(autorundir):
            if fn.endswith(".py"):
                files.append(autorundir + "/" + fn)

    if len(files) == 1:
        return files[0]

    renpy = { }

    # Ask the user to give us a .py or .pyw file.
    def filter(*args):
        fn = aepack.unpack(args[0]).as_pathname()

        dirname = os.path.dirname(fn)
        if dirname not in renpy:
            renpy[dirname] = os.path.isdir(dirname + "/renpy") or os.path.exists(dirname + "/renpy.zip")

        if renpy[dirname] and (fn.endswith(".py") or fn.endswith(".pyw")):
            return True

        if os.path.isdir(fn):
            return True

        return False

    message = "Please choose a .py or .pyw file to run."
    title = "KSAbridged " + ".".join([str(i) for i in _mac_version])
    
    fn = ed.AskFileForOpen(message=message,
                           windowTitle=title,
                           filterProc=filter)

    return fn


def mac_main():

    import sys
    import os
    import os.path
    import EasyDialogs as ed

    # Find the executable, and run it.
    contents = "/".join(os.environ['RESOURCEPATH'].split('/')[:-1])
    sys.executable = contents + "/MacOS/KSAbridged"

    # print sys.executable

    fn = mac_find_game()

    # We were unable to find a game, so give up.
    if not fn:
        return

    # Find the directory containing a game.
    dirname = os.path.dirname(fn)

    # Setup the path that files are imported from.
    sys.path.append(dirname)

    # Change director to the path containing the game.
    os.chdir(os.environ.get('RENPY_LAUNCHER_DIR', dirname))

    # Set sys.argv to the name of the file we will run, followed by 
    # the directory, followed by additional arguments
    sys.argv = [ fn ] + sys.argv[2:]

    # Init the Mac OS X side of things... probably not necessary,
    # but can't hurt. 
    try:
        import pygame.macosx
        pygame.macosx.init()
    except:
        pass

    # Begin executing the Ren'Py game.
    execfile(fn, globals(), globals())

    # That's all, folks.
    
if __name__ == "__main__":
    mac_main()
    
