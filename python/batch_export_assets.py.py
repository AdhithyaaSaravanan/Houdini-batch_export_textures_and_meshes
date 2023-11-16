import hou
import os


tool_output_path = "Your/Tool/Output"    

all_textures_output_path = make_folder(tool_output_path, 'Textures')
all_assets_output_path = make_folder(tool_output_path, 'Assets')


def make_folder(directory, folder_name):
    folder_path = os.path.join(directory, folder_name).replace('\\', '/')
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)
    return folder_path

    
def get_file_paths(file_names, parent_directory):
    all_file_paths = []
    
    for file in file_names:
        file_path = os.path.join(parent_directory, file).replace('\\', '/')
        all_file_paths.append(file_path)
        
    return all_file_paths
    
    
def rename_files():
    
    texture_folder_paths = get_file_paths(os.listdir(all_textures_output_path), all_textures_output_path)
    
    for texture_folder_path in texture_folder_paths:
        folder_name = os.path.basename(texture_folder_path)
        version_no = folder_name[-4:]
        
        all_files = os.listdir(texture_folder_path)
        
        new_file_names = []
        for file in all_files:
            name_split = file.split('.')
            new_file_name = name_split[0] + '_' + version_no + '.' + name_split[1]
            new_file_names.append(new_file_name)
        
        src_files = get_file_paths(all_files, texture_folder_path)
        dest_files = get_file_paths(new_file_names, texture_folder_path)
        
        for src, dest in zip(src_files, dest_files):
            os.rename(src, dest)

    
def export_textures_and_fbx():
    
    for i in range(1, 11):
        # Export all the textures
        textures_folder_common_name = 'test_rock'
        version_no = 'v{:03d}'.format(i)
        unique_texture_folder_name = textures_folder_common_name + '_' + version_no
        
        unique_texture_folder_path = make_folder(all_textures_output_path, unique_texture_folder_name)
        
        unique_texture_name = 't_' + textures_folder_common_name + '.exr'
        individual_textures_name_path = os.path.join(unique_texture_folder_path, unique_texture_name).replace('\\', '/')
        
        texture_node = hou.node('/out/baketexture1')
        parm = texture_node.parm('vm_uvobject1')
        
        texture_node.setParms({'vm_uvoutputpicture1': individual_textures_name_path})
        texture_node.render((i, i))        
   
        
        # Export all the assets
        unique_asset_name = 'sm_' + unique_texture_folder_name
        unique_asset_path = os.path.join(all_assets_output_path, unique_asset_name).replace('\\', '/')

        fbx_export_node = hou.node('/obj/low_res/rop_fbx1')       
        fbx_export_node.setParms({'sopoutput': unique_asset_path})
        fbx_export_node.render((i, i))
       
        
     
    
#export_textures_and_fbx()
#rename_files()
