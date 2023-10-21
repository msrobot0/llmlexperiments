from colorama import Fore, Style, init

init(autoreset=True)

plant_art = {
    "rose": f"{Fore.RED} @@@{Fore.RESET}\n{Fore.RED} @@@{Fore.RESET}\n{Fore.RED} @@@{Fore.RESET}\n{Fore.RED} @@@{Fore.RESET}\n{Fore.GREEN}  |  {Fore.RESET}\n{Fore.GREEN} / \\ {Fore.RESET}",
    "palm tree": f"{Fore.GREEN}    ^ {Fore.RESET}\n{Fore.GREEN}   ^^^{Fore.RESET}\n{Fore.GREEN}  ^^^^{Fore.RESET}\n{Fore.GREEN} ^^^^^{Fore.RESET}\n{Fore.YELLOW} ^^^^^{Fore.RESET}",
    "sunflower": f"{Fore.YELLOW}   ##   {Fore.RESET}\n{Fore.YELLOW}   ##   {Fore.RESET}\n{Fore.YELLOW} ###### {Fore.RESET}\n{Fore.YELLOW}   ##   {Fore.RESET}\n{Fore.YELLOW}   ##   {Fore.RESET}",
    "tulip": f"{Fore.RED}  ooo  {Fore.RESET}\n{Fore.RED} ooooo {Fore.RESET}\n{Fore.RED}  ooo  {Fore.RESET}\n{Fore.GREEN}  | |  {Fore.RESET}\n{Fore.GREEN}  | |  {Fore.RESET}",
    "daisy": f"{Fore.WHITE}  ooo  {Fore.RESET}\n{Fore.WHITE} ooooo {Fore.RESET}\n{Fore.WHITE}  ooo  {Fore.RESET}\n{Fore.WHITE}  | |  {Fore.RESET}\n{Fore.WHITE}  | |  {Fore.RESET}",
    "cactus": f"{Fore.GREEN}  __   {Fore.RESET}\n{Fore.GREEN} /  \\  {Fore.RESET}\n{Fore.GREEN} |  |  {Fore.RESET}\n{Fore.GREEN} \__/  {Fore.RESET}\n{Fore.GREEN}  ||  {Fore.RESET}",
    "tall grass": f"{Fore.GREEN}  ||   {Fore.RESET}\n{Fore.GREEN}  ||   {Fore.RESET}\n{Fore.GREEN}  ||   {Fore.RESET}\n{Fore.GREEN}  ||   {Fore.RESET}\n{Fore.GREEN}  ||   {Fore.RESET}",
    "bluebell": f"{Fore.BLUE}   *   {Fore.RESET}\n{Fore.BLUE}  ***  {Fore.RESET}\n{Fore.BLUE}   *   {Fore.RESET}\n{Fore.CYAN}  | |  {Fore.RESET}\n{Fore.CYAN}  | |  {Fore.RESET}",
    "lily": f"{Fore.WHITE}  @@@  {Fore.RESET}\n{Fore.WHITE} @@@@ {Fore.RESET}\n{Fore.WHITE}  @@@  {Fore.RESET}\n{Fore.WHITE}  | |  {Fore.RESET}\n{Fore.WHITE}  | |  {Fore.RESET}",
    "pansy": f"{Fore.MAGENTA}   o   {Fore.RESET}\n{Fore.MAGENTA}  ooo  {Fore.RESET}\n{Fore.MAGENTA}   o   {Fore.RESET}\n{Fore.MAGENTA}  | |  {Fore.RESET}\n{Fore.MAGENTA}  | |  {Fore.RESET}",
    "dandelion": f"{Fore.YELLOW}   o   {Fore.RESET}\n{Fore.YELLOW}  ooo  {Fore.RESET}\n{Fore.YELLOW}   o   {Fore.RESET}\n{Fore.YELLOW}  | |  {Fore.RESET}\n{Fore.YELLOW}  | |  {Fore.RESET}",
    "lavender": f"{Fore.MAGENTA}   *   {Fore.RESET}\n{Fore.MAGENTA}  ***  {Fore.RESET}\n{Fore.MAGENTA}   *   {Fore.RESET}\n{Fore.CYAN}  | |  {Fore.RESET}\n{Fore.CYAN}  | |  {Fore.RESET}",
    "tulip": f"{Fore.RED}  ooo  {Fore.RESET}\n{Fore.RED} ooooo {Fore.RESET}\n{Fore.RED}  ooo  {Fore.RESET}\n{Fore.GREEN}  | |  {Fore.RESET}\n{Fore.GREEN}  | |  {Fore.RESET}",
    "cherry blossom": f"{Fore.MAGENTA}  /\\  {Fore.RESET}\n{Fore.MAGENTA} (__) {Fore.RESET}\n{Fore.MAGENTA}  \\/  {Fore.RESET}\n{Fore.CYAN}  | |  {Fore.RESET}\n{Fore.CYAN}  | |  {Fore.RESET}",
    "moss": f"{Fore.GREEN}  ##   {Fore.RESET}\n{Fore.GREEN} ####  {Fore.RESET}\n{Fore.GREEN}  ##   {Fore.RESET}\n{Fore.GREEN}  ##   {Fore.RESET}\n{Fore.GREEN}  ##   {Fore.RESET}",
    "fern": f"{Fore.GREEN}  ||   {Fore.RESET}\n{Fore.GREEN}  ||   {Fore.RESET}\n{Fore.GREEN}  ||   {Fore.RESET}\n{Fore.GREEN}  ||   {Fore.RESET}\n{Fore.GREEN}  ||   {Fore.RESET}",
    "orchid": f"{Fore.MAGENTA}   *   {Fore.RESET}\n{Fore.MAGENTA}  * *  {Fore.RESET}\n{Fore.MAGENTA}   *   {Fore.RESET}\n{Fore.CYAN}  | |  {Fore.RESET}\n{Fore.CYAN}  | |  {Fore.RESET}",
    "buttercup": f"{Fore.YELLOW}   *   {Fore.RESET}\n{Fore.YELLOW}  ***  {Fore.RESET}\n{Fore.YELLOW}   *   {Fore.RESET}\n{Fore.YELLOW}  | |  {Fore.RESET}\n{Fore.YELLOW}  | |  {Fore.RESET}",
    "ivy": f"{Fore.GREEN}  __   {Fore.RESET}\n{Fore.GREEN}  \\ \\  {Fore.RESET}\n{Fore.GREEN}  |||  {Fore.RESET}\n{Fore.GREEN}  |||  {Fore.RESET}\n{Fore.GREEN}  |||  {Fore.RESET}",
    "lily of the valley": f"{Fore.WHITE}  ooo  {Fore.RESET}\n{Fore.WHITE} ooo o {Fore.RESET}\n{Fore.WHITE} oooo  {Fore.RESET}\n{Fore.YELLOW}  | |  {Fore.RESET}\n{Fore.YELLOW}  | |  {Fore.RESET}",
    "sage": f"{Fore.GREEN}  ##   {Fore.RESET}\n{Fore.GREEN} ###  {Fore.RESET}\n{Fore.GREEN} #### {Fore.RESET}\n{Fore.GREEN} ###  {Fore.RESET}\n{Fore.GREEN}  ##   {Fore.RESET}",
    "morning glory": f"{Fore.BLUE}   *   {Fore.RESET}\n{Fore.BLUE}  ***  {Fore.RESET}\n{Fore.BLUE}  * * {Fore.RESET}\n{Fore.CYAN}  | |  {Fore.RESET}\n{Fore.CYAN}  | |  {Fore.RESET}",
    "lavender": f"{Fore.MAGENTA}   *   {Fore.RESET}\n{Fore.MAGENTA}  ***  {Fore.RESET}\n{Fore.MAGENTA}   *   {Fore.RESET}\n{Fore.CYAN}  | |  {Fore.RESET}\n{Fore.CYAN}  | |  {Fore.RESET}",
    "bouquet": f"{Fore.RED} /~~~\\{Fore.RESET}\n{Fore.RED} \\^_^/{Fore.RESET}\n{Fore.RED} /_O_\\{Fore.RESET}\n{Fore.GREEN}  | |  {Fore.RESET}\n{Fore.GREEN}  | |  {Fore.RESET}",
    "carnation": f"{Fore.RED}  @@@  {Fore.RESET}\n{Fore.RED} @@@@ {Fore.RESET}\n{Fore.RED}  @@@  {Fore.RESET}\n{Fore.GREEN}  | |  {Fore.RESET}\n{Fore.GREEN}  | |  {Fore.RESET}",
    "tiger lily": f"{Fore.GREEN}  /\\  {Fore.RESET}\n{Fore.GREEN} (__) {Fore.RESET}\n{Fore.GREEN}  ||  {Fore.RESET}\n{Fore.GREEN}  ||  {Fore.RESET}\n{Fore.GREEN}  ||  {Fore.RESET}",
    "poppy": f"{Fore.RED}  ooo  {Fore.RESET}\n{Fore.RED} ooooo {Fore.RESET}\n{Fore.RED}  ooo  {Fore.RESET}\n{Fore.GREEN}  | |  {Fore.RESET}\n{Fore.GREEN}  | |  {Fore.RESET}",
    "lotus": f"{Fore.MAGENTA}   *   {Fore.RESET}\n{Fore.MAGENTA}  * *  {Fore.RESET}\n{Fore.MAGENTA}   *   {Fore.RESET}\n{Fore.CYAN}  | |  {Fore.RESET}\n{Fore.CYAN}  | |  {Fore.RESET}",
    "marigold": f"{Fore.YELLOW}   *   {Fore.RESET}\n{Fore.YELLOW}  ***  {Fore.RESET}\n{Fore.YELLOW}   *   {Fore.RESET}\n{Fore.YELLOW}  | |  {Fore.RESET}\n{Fore.YELLOW}  | |  {Fore.RESET}",
    "peony": f"{Fore.MAGENTA}  ooo  {Fore.RESET}\n{Fore.MAGENTA} ooooo {Fore.RESET}\n{Fore.MAGENTA}  ooo  {Fore.RESET}\n{Fore.CYAN}  | |  {Fore.RESET}\n{Fore.CYAN}  | |  {Fore.RESET}",
    "lilac": f"{Fore.MAGENTA}   @   {Fore.RESET}\n{Fore.MAGENTA}  @@@  {Fore.RESET}\n{Fore.MAGENTA} @@@@ {Fore.RESET}\n{Fore.MAGENTA}  @@@  {Fore.RESET}\n{Fore.MAGENTA}   @   {Fore.RESET}",
}

def generate_plant_art(plant_name):
    plant_name = plant_name.lower()
    if plant_name in plant_art:
        print(plant_art[plant_name])
    else:
        print(f"Sorry, I don't have ASCII art for {plant_name}.")

if __name__ == "__main__":
    user_input = input("Enter the name of a plant: ")
    generate_plant_art(user_input)

