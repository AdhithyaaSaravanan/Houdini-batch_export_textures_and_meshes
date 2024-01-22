# Houdini batch export textures and meshes

## Tool Summary

This script batch exports multiple 3D meshes and their corresponding 
textures maps into a well organised folder structure with the specified
naming convention. This works in combination with the UE5 tool to map 
textures to 3D meshes. 

## Note

This script was solely written for specific uses within a personal project. 
The aim was to produce a quick script to automate a repetitive task. 
It is not ready to be integrated into other people's workflows, 
unless further changes are made in the code. In the future, I will add 
error checking and testing to make it more reliable, and also potentially 
a UI to make it artist friendly. But the main logic is there :)

## Input

This script works in relation to a topnet set up to generate variations 
of hard surface assets.
It scrubs through the specified frames in the houdini timeline 
and generates meshes and texture maps and organises them in a clean 
folder tree in the specified output directory, while conforming to the 
naming conventions of the pipeline. It uses the specified texture bake node
in the script to do so.

## Output

A sample output folder is provided in the repo to demonstrate an example. 
An underscore is assumed in the file names when string concatenation 
is specified in the below examples.

### Template Output Folder Tree
````
├───Assets
│       "sm" + asset_name + verion
└───Textures
    ├───asset_name + verion
    │       "t" + asset_name + albedo + verion
    │       "t" + asset_name + normal + verion
    │       "t" + asset_name + occlusion + verion
    │       "t" + asset_name + rough + verion
    │       "t" + asset_name + spec + verion
````

### Example Output Folder Tree
````
├───Assets
│       sm_test_rock_v001.fbx
└───Textures
    ├───test_rock_v001
    │       t_test_rock_albedo_v001.tga
    │       t_test_rock_normal_v001.tga
    │       t_test_rock_occlusion_v001.tga
    │       t_test_rock_rough_v001.tga
    │       t_test_rock_spec_v001.tga
    │       t_test_rock_v001.exr
    │       t_test_rock_v001.tga
````