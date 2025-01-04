"""
.. autoprogram:: choreo_GUI.run:GUI_parser
"""

from .http_server import serve_GUI
from .manage_gallery import make_gallery_descriptor, install_official_gallery, default_gallery_root
from .run import GUI