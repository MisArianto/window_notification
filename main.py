import os
from win10toast import ToastNotifier


def notification():
    # change dir to the scripts location
    os.chdir(os.path.dirname(os.path.realpath(__file__)))
    toast = ToastNotifier()  # Instance of ToastNotifier module
    title = "Notification"  # Title for message displayed
    message = "Follow Github.com/MisArianto"

    # place image in the same dir as script
    icon = "icon.ico"
    length = 30
    toast.show_toast(title, message, icon_path=icon, duration=length)


notification()
