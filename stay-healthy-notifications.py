import time
from plyer import notification

if __name__ == "__main__":
    while True:
        notification.notify(
            title="Its time to stretch...",
            message="Give your spine a rest... Go and Stretch",
            app_icon="D:\github\python-mini-projects\yoga-pose.ico",  # or whatever path u saved the image on
            timeout=6
        )
        notification.notify(
            title="ITS TIME FOR EYE BREAK!!!",
            message="look far, you are a healthy star...",
            app_icon="D:\github\python-mini-projects\eyes.ico",
            timeout=6
        )
        time.sleep(20 * 20)

        notification.notify(
            title="GET HYDRATED!!!",
            message="8 glasses of water a day. Keep dehydration away...",
            app_icon="D:\github\python-mini-projects\water.ico",
            timeout=6
        )
        notification.notify(
            title="ITS TIME FOR EYE BREAK!!!",
            message="look far, you are a healthy star...",
            app_icon="D:\github\python-mini-projects\eyes.ico",
            timeout=6
        )
        time.sleep(20 * 20)
