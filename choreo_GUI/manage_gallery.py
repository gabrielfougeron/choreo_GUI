import os
import json
import subprocess
import shutil

def sort_dirs_list_inplace(the_dict):

    the_dict["dirs"].sort(key=lambda x: x["name"])

    for sub_dir in the_dict["dirs"]:
        sort_dirs_list_inplace(sub_dir)
        
default_gallery_root = os.path.join(os.path.dirname(__file__))

def install_official_gallery(gallery_root = default_gallery_root, overwrite=False, TryOffline = True):

    gallery_dest_path = os.path.join(gallery_root, 'choreo-gallery')
    
    if os.path.isdir(gallery_dest_path):
        if overwrite:
            shutil.rmtree(gallery_dest_path)
        else:
            gallery_descriptor_filename = os.path.join(gallery_dest_path, "gallery_descriptor.json")
            if not os.path.isfile(gallery_descriptor_filename):
                make_gallery_descriptor(gallery_root)
            return
    
    if TryOffline:
 
        gallery_src_path = os.path.join(os.path.dirname(__file__), os.pardir, os.pardir, "choreo-gallery", "choreo-gallery")
        if os.path.isdir(gallery_src_path):
            
            os.makedirs(gallery_dest_path)       
            shutil.copytree(gallery_src_path, gallery_dest_path, dirs_exist_ok=True)
            make_gallery_descriptor(gallery_root)
            return
        
    if os.path.isdir('tmp'):
        shutil.rmtree('tmp')
    
    os.mkdir('tmp')
    os.chdir('tmp')
    
    subprocess.run(["git","clone", "https://github.com/gabrielfougeron/choreo_gallery.git"])
    os.makedirs(gallery_dest_path)
    gallery_src_path = os.path.join('choreo_gallery','choreo-gallery')
    shutil.move(gallery_src_path, gallery_dest_path)
    
    os.chdir(os.pardir)
    shutil.rmtree('tmp')
    
    make_gallery_descriptor(gallery_root)

def make_gallery_descriptor(gallery_root = default_gallery_root, out_filename = "gallery_descriptor.json"):

    Gallery_dict = {}

    for (dirpath, dirnames, filenames) in os.walk(os.path.join(gallery_root, 'choreo-gallery')):
        
        parts = os.path.relpath(dirpath, start=gallery_root).split(os.sep)

        npy_json_pairs = {}
        for the_file in filenames:
            base, ext = os.path.splitext(the_file)
            if ext in ['.npy','.json']:
                if not(base in npy_json_pairs):
                    npy_json_pairs[base] = {}
                npy_json_pairs[base][ext] = os.path.join(*parts,the_file)

        folder_dict = {}
        folder_dict.setdefault('name', parts.pop())
        folder_dict.setdefault('dirs', [])
        folder_dict.setdefault('files', npy_json_pairs)

        if len(parts) > 0 :
            # Move to current dir
            curr = Gallery_dict
            while (len(parts) > 0 ):
                seek = parts.pop(0)
                for sub_folder in curr['dirs']:
                    if (sub_folder["name"] == seek):
                        curr = sub_folder
            # Add the folder dict to the list of dirs
            curr['dirs'].append(folder_dict)

        else:
            Gallery_dict = folder_dict
            
    sort_dirs_list_inplace(Gallery_dict)

    jsonString = json.dumps(Gallery_dict, indent=4, sort_keys=True)

    with open(os.path.join(gallery_root, out_filename), "w") as jsonFile:
        jsonFile.write(jsonString)


