import os,shutil
folders={
 'videos':['.mp4'],
 'audios':['.wav','.mp3'],
 'images':['.jpg','.png'],
 'documents':['.doc','.xlsx','.xls','.pdf','.zip','.rar'],
}
#print(folders)
#for folder_name in folders:
#    print(folder_name,folders[folder_name])

def rename_folder():
    for folder in os.listdir(directory):
        if os.path.isdir(os.path.join(directory,folder))==True:
            os.rename(os.path.join(directory,folder),os.path.join(directory,folder.lower()))

def create_move(ext,file_name):
    find=False
    for folder_name in folders:
        if "."+ext in folders[folder_name]:
            if folder_name not in os.listdir(directory):
                os.mkdir(os.path.join(directory,folder_name))
            shutil.move(os.path.join(directory,file_name),os.path.join(directory,folder_name))
            find=True
            break
    if find!=True:
        if other_name not in os.listdir(directory):
            os.mkdir(os.path.join(directory,other_name))
        shutil.move(os.path.join(directory,file_name),os.path.join(directory,other_name))

        
        

directory=input("Enter the location")
other_name=input("Enter the folder name for unknown files")
rename_folder()
all_files=os.listdir(directory)
length=len(all_files)
count=1
#print(all_files)
for i in all_files:
    if os.path.isfile(os.path.join(directory,i))==True:
        #print("yes")
        create_move(i.split(".")[-1],i)
    print(f"Total files :{length}| Done :{count} | Left: {length-count}")
    count+=1
