from bing_image_downloader import downloader
import os

kelime="Mustafa Kemal Atatürk" #Aramak istediğiniz kelime
adet=100 #İndirmek istediğiniz resim adeti

masaustu=os.path.join(os.path.expanduser("~"),"Desktop")
dizin=os.path.join(masaustu,"Resimler")


if os.path.exists(dizin):
    downloader.download(kelime,limit=adet,output_dir=dizin)
else:
    os.makedirs(dizin)
    downloader.download(kelime,limit=adet,output_dir=dizin)


