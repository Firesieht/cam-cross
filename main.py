import sys

import cv2 as cv
from sys import exit


def start(camNumber):
    cam = cv.VideoCapture(camNumber)
    while True:
        sucess, img = cam.read()
        cv.putText(img, "cam " + str(camNumber), (25, 25), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 1)
        height, width = img.shape[:2]

        cv.line(img, (width // 2, 0), (width // 2, height), (0, 0, 255), 1)
        cv.line(img, (0, height // 2), (width, height // 2), (0, 0, 255), 1)

        cv.imshow("stream", img)
        key = cv.waitKey(1)
        if key == 27:
            cv.destroyAllWindows()
            break
    cam.release()
    cv.destroyAllWindows()


camNumber = 0


def сhangeCam():
    global camNumber
    try:
        camNumber = int(input("Введите номер камеры:"))
        print("Нажмите ESC для выхода")
        print("press ESC to exit")

        start(camNumber)
    except:
        print("Неверный ввод!")
        сhangeCam()


if __name__ == "__main__":
    print("Эта штука выводит крестик на изображение камеры")
    text = input("Запустить? (да/нет/сменить камеру):")
    if ["да", "д", "yes", "y"].__contains__(text):
        print("Нажмите ESC для выхода")
        print("press ESC to exit")
        start(camNumber)
    elif ["сменить", "с", "сменить камеру", "change cam", "c", "change"].__contains__(text):
        сhangeCam()
    elif ["нет", "н", "no", "n"].__contains__(text):
        exit()


