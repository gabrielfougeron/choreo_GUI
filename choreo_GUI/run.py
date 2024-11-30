import os
import sys
import argparse

from choreo_GUI import default_gallery_root, install_official_gallery
from choreo_GUI import serve_GUI

def GUI(cli_args):
    
    parser = argparse.ArgumentParser(
        description = 'Launches choreo GUI')

    default_Workspace = './'
    parser.add_argument(
        '-f', '--foldername',
        default = default_gallery_root,
        dest = 'gallery_root',
        help = f'Gallery root.',
        metavar = '',
    )

    args = parser.parse_args(cli_args)
    
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
