# Batch Image Resize for Telegram

Used for resize images, especially for large amounts of images.

Orignally coded to resize a batch of images in order to fit the Telegram stickers' requirement, hence the output images are `512 * (>=512)` pixels, you can change it in the code via variable 'maxsize'.

Note:
* `SourceCode.py` is an old version created in 2016 
* `telegramSticker.py` is the newer version 

# Execuable fil User Guide:

Copy the .exe file to where your images are, then run it by double click or right-click and run, a new folder called 'OutputImages' will be created in which contains images resized to `512 * (>=512)` resloution, with alpha/opacity reserved if exists.

Note:
* the `.exe` file is generated back to 2016, it does not work very well. The new version works great but is too big to upload. 
* You might experience Windows defender errors when running this 

