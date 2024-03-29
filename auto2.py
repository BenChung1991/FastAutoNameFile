import os
import glob

#remember to modify file address
folder_path = '../images2'

new_filename_prefix = ''
start_index = 1
image_files = glob.glob(os.path.join(folder_path, '*.png'))

renamed_count = 0
skipped_count = 0

for i, image_file in enumerate(image_files):
    new_filename = f'{new_filename_prefix}{start_index + i}.png'
    new_file_path = os.path.join(folder_path, new_filename)
    
    # 檢查新檔案名稱是否已存在於目標資料夾中
    if os.path.exists(new_file_path):
        #print(f'File {new_filename} already exists. Skipping...')
        skipped_count += 1
    else:
        os.rename(image_file, new_file_path)
        #print(f'Renamed file: {image_file} to {new_filename}')
        renamed_count += 1

print(f'Total files renamed: {renamed_count}')
print(f'Total files skipped due to existing names: {skipped_count}')