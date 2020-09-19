from pynotifier import Notification
#also install win10toast (pip install win10toast --if you use pip)
Notification(title='alert',
             description="If you don't start coding you'll get wasted",
             icon_path=r'C:\\Users\\saketh\\Downloads\\code-red-color-motivation.ico',  #if you have jpg file convert it to icon
             duration=5,
             urgency=Notification.URGENCY_CRITICAL
             ).send()
