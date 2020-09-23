import pyqrcode
#install pyqrcode and pypng libaries
QRstring='https://github.com/saketh33/Data-cleaning-and-visualization'
url=pyqrcode.create(QRstring)
url.png('C:\\Users\\saketh\\Downloads\\githubqr.png',scale=8,module_color=(1,1,10))