import os
import shutil

if not os.path.isdir('./ItemsAdder'):
    os.mkdir('./ItemsAdder') 
    os.mkdir('./ItemsAdder/data') 
    print("Please put the ItemsAdder folder in the same directory as this file.")
    exit()
if os.path.exists("./Output"):
    shutil.rmtree('./Output')
itemadder = './ItemsAdder/data/resource_pack/assets'
for get_namespace in os.listdir(itemadder):
    if not os.path.exists("./Output"):
        os.mkdir('./Output') 
    if not os.path.exists("./Output/ItemsAdder"):
        os.mkdir('./Output/ItemsAdder') 
    if not os.path.exists("./Output/ItemsAdder/contents"):
        os.mkdir('./Output/ItemsAdder/contents') 
    if not os.path.exists("./Output/ItemsAdder/contents/"+get_namespace):
        os.mkdir('./Output/ItemsAdder/contents/'+get_namespace) 
    shutil.copytree('./ItemsAdder/data/resource_pack','./Output/ItemsAdder/contents/'+get_namespace+'/resourcepack')
    shutil.copytree('./ItemsAdder/data/items_packs/'+get_namespace,'./Output/ItemsAdder/contents/'+get_namespace+'/configs')
    print("convert "+get_namespace)    