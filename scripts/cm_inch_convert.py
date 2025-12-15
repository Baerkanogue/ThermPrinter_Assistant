from colorama import Fore


def convert() -> None:
    cm: float = 0.0
    CM_TO_INCH_RATIO: float = 0.39370079

    while not cm:
        try:
            cm = float(input(f"{Fore.YELLOW}Length in centimeter(s):{Fore.RESET} "))
        except Exception as error:
            print(f"{Fore.RED}Error:{Fore.RESET} {error}")

    print(f"{Fore.GREEN}Length in inches:{Fore.RESET} {cm * CM_TO_INCH_RATIO}")


def main() -> None:
    is_looping: bool = True
    while is_looping:
        convert()
        is_loop_str: str = ""
        while is_loop_str != "y" and is_loop_str != "n":
            is_loop_str = input(f"{Fore.YELLOW}Again ? Y/N:{Fore.RESET} ").lower()
        is_looping = False if is_loop_str == "n" else True
    print(f"{Fore.YELLOW}Closing...{Fore.RESET}")


if __name__ == "__main__":
    main()
