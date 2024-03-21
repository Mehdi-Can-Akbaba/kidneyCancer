import os
import shutil
import random

# Veri setinin bulunduğu ana klasör
data_folder = './data/datasetkc2/'

# Train ve validation klasörlerinin oluşturulması
train_folder = './data/datasetkc2/train/'
val_folder = './data/datasetkc2/val/'

os.makedirs(train_folder, exist_ok=True)
os.makedirs(val_folder, exist_ok=True)

# Veri setindeki sınıfların listesi (Cyst, Normal, Stone, Tumor)
classes = ['Cyst', 'Normal', 'Stone', 'Tumor']

# Her sınıf için train ve validation klasörlerine kopyalanacak dosyaların oranı (örneğin, 80% train, 20% validation)
split_ratio = 0.8

# Her sınıf için veri setini train ve validation klasörlerine kopyalama
for class_name in classes:
    class_folder = os.path.join(data_folder, class_name)
    class_train_folder = os.path.join(train_folder, class_name)
    class_val_folder = os.path.join(val_folder, class_name)

    os.makedirs(class_train_folder, exist_ok=True)
    os.makedirs(class_val_folder, exist_ok=True)

    # Sınıfa ait tüm dosyaların listelenmesi
    files = os.listdir(class_folder)
    # Dosyaların karıştırılması
    random.shuffle(files)
    # Dosyaların train ve validation klasörlerine kopyalanması
    split_index = int(len(files) * split_ratio)
    train_files = files[:split_index]
    val_files = files[split_index:]

    for file in train_files:
        src = os.path.join(class_folder, file)
        dst = os.path.join(class_train_folder, file)
        shutil.copy(src, dst)

    for file in val_files:
        src = os.path.join(class_folder, file)
        dst = os.path.join(class_val_folder, file)
        shutil.copy(src, dst)

print("Veri seti train ve val klasörlerine başarıyla bölündü.")
