import time
from colorama import Fore, init

init(autoreset=True)

butterfly_frames = [
    [
        "     NXXXXX            ",
        "   KKKKKKKKKK NXXN       ",
        "   KKKKKKKK KK NXXN      ",
        "   KKKKKKKK KK NXXN      ",
        "   KKKKKKKK KK NXXN      ",
        "   KKKKKKKK KK NXXN      ",
        "   KKKKKKKKKK NXXN       ",
        "     NXXXXX            ",
        "                      ",
    ],
    [
        "     NXXXXX            ",
        "      KKKKKKKKKK NXXN       ",
        "      KKKKKKKK KK NXXN      ",
        "      KKKKKKKK KK NXXN      ",
        "      KKKKKKKK KK NXXN      ",
        "      KKKKKKKK KK NXXN      ",
        "     NXXXXX            ",
        "     NXXXXX            ",
        "                      ",
    ],
    [
        "     NXXXXX            ",
        "          KKKKKKKKKK NXXN       ",
        "          KKKKKKKK KK NXXN      ",
        "          KKKKKKKK KK NXXN      ",
        "          KKKKKKKK KK NXXN      ",
        "     NXXXXX            ",
        "     NXXXXX            ",
        "     NXXXXX            ",
        "                      ",
    ],
]

def animate_butterfly(frames, delay=0.2):
    for i in range(len(frames[0])):
        for frame in frames:
            print("\033[H")  # Move cursor to the top of the terminal
            for line in frame:
                print(line)
            time.sleep(delay)

if __name__ == "__main__":
    animate_butterfly(butterfly_frames)

