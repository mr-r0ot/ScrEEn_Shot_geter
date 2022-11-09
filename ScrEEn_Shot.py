import time
from PIL import ImageGrab

while True:
    name = input('  Enter name file save <<  ')
    kkk = input('   Enter format file save  <<  ')
    time.sleep(3)
    sc = ImageGrab.grab()
    sc.save(name+'.'+kkk)
    print('    Ok ')
