import os
import sys
import argparse

from choreo_GUI import default_gallery_root, install_official_gallery
from choreo_GUI import serve_GUI

GUI_parser = argparse.ArgumentParser(
    description = """ Launches the GUI server.
    
    Access the GUI by typing `http://127.0.0.1:8000 <http://127.0.0.1:8000>`_ in your favorite internet browser after launching the server.
    
    """,
    prog = 'choreo_GUI',
)

default_Workspace = './'

GUI_parser.add_argument(
    '-f', '--foldername',
    default = default_gallery_root,
    dest = 'gallery_root',
    help = f'Gallery root.',
    metavar = '',
)

def GUI(cli_args):

    args = GUI_parser.parse_args(cli_args)
    
    if args.gallery_root != default_gallery_root:
        raise NotImplementedError
    
    GalleryExists = (
        os.path.isdir(os.path.join(args.gallery_root,'choreo-gallery'))
        and os.path.isfile(os.path.join(args.gallery_root,'gallery_descriptor.json'))
    )
    
    if not GalleryExists:
        print("Gallery not found. Installing official gallery.")
        install_official_gallery()
    
    dist_dir = os.path.join(args.gallery_root,'python_dist')
    
    if os.path.isdir(dist_dir):
        
        for f in os.listdir(dist_dir):
            if ('.whl' in f) and ('pyodide' in f):
                FoundPyodideWheel = True
                break
        else:
            FoundPyodideWheel = False
    else:
        FoundPyodideWheel = False
    
    if not FoundPyodideWheel:
        print("Warning : Pyodide wheel not found")
    
    serve_GUI()

def entrypoint_GUI():
    GUI(sys.argv[1:])
