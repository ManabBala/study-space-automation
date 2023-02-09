import subprocess
import time
import pywinctl as pwc

from organizer import *
import settings as st
from virtual_desktop import *
from hack import unMaximizeChrome

initialVd = VirtualDesktop.current()

for vdName, vdContent in st.virtualDesktop.items():
    # print(vdName, vdContent)
    get_vd_by_name(vdName).go()
    for window, content in vdContent.items():
        appName = content["appName"]
        sizePosition = content["sizePosition"]
        # print(appName, sizePosition)

        if appName == "chrome":
            newWindow = True
            tabs = content["tabs"]
            # opening urls in respective chrome
            for tab, url in tabs.items():
                subprocess.run(f"{st.appsPath['chrome']} {'--new-window' if newWindow else ''} {url}")
                newWindow = False
            # moving Chrome window
            time.sleep(1)
            npw = pwc.getActiveWindow()
            if npw.isMaximized:
                unMaximizeChrome(1850, 15)
            if sizePosition == "full":
                npw.maximize()
            else:
                moveWindowTo(npw, *st.sizePositionDic[sizePosition])

        if appName == "anki":
            subprocess.Popen(f"{st.appsPath['anki']}")
            # moving anki window
            t = 0
            npw = pwc.getActiveWindow()
            while "Anki" not in npw.title:
                # print(t, npw)
                time.sleep(.5)
                npw = pwc.getActiveWindow()
                t += .5
            moveWindowTo(npw, *st.sizePositionDic[sizePosition])


time.sleep(2)
VirtualDesktop(1).go()
