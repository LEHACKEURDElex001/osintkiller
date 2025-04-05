import os
import time
from datetime import datetime

# Couleurs console
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
BOLD = "\033[1m"
RESET = "\033[0m"

def slow(text, delay=0.005):
    for c in text:
        print(c, end='', flush=True)
        time.sleep(delay)
    print()

# Tête de mort stylée
def skull():
    os.system("clear")
    skull_art = RED + BOLD + r'''
     ██████╗ ███████╗██╗███╗   ██╗████████╗██╗  ██╗██╗██╗     
    ██╔════╝ ██╔════╝██║████╗  ██║╚══██╔══╝██║  ██║██║██║     
    ██║  ███╗█████╗  ██║██╔██╗ ██║   ██║   ███████║██║██║     
    ██║   ██║██╔══╝  ██║██║╚██╗██║   ██║   ██╔══██║██║██║     
    ╚██████╔╝███████╗██║██║ ╚████║   ██║   ██║  ██║██║███████╗
     ╚═════╝ ╚══════╝╚═╝╚═╝  ╚═══╝   ╚═╝   ╚═╝  ╚═╝╚═╝╚══════╝
    '''
    slow(skull_art, 0.001)
    slow(CYAN + BOLD + "\n    OSINTKILLER - Pseudo / Email / Numéro Scanner\n" + RESET, 0.01)

# Menu principal
def menu():
    slow(GREEN + BOLD + "\n[1] DOX - Recherche complète (pseudo, email)", 0.01)
    slow("[2] INFO - Recherche rapide (leaks, moteurs, hunter)" + RESET, 0.01)
    choix = input(CYAN + "\n>>> Choisis une option : " + RESET)

    if choix == "1":
        dox_mode()
    elif choix == "2":
        info_mode()
    else:
        print(RED + "Option invalide. Relance le script." + RESET)

# Mode DOX
def dox_mode():
    cible = input(CYAN + "\n[+] Entrez un pseudo ou email : " + RESET)
    now = datetime.now().strftime("%Y%m%d_%H%M")
    fichier = f"data/dox_{cible}_{now}.txt"

    slow(YELLOW + "[*] Recherche en cours sur les réseaux..." + RESET, 0.01)

    liens = [
        f"https://github.com/{cible}",
        f"https://instagram.com/{cible}",
        f"https://snapchat.com/add/{cible}",
        f"https://discord.com/users/{cible}",
        f"https://twitter.com/{cible}",
        f"https://reddit.com/user/{cible}",
        f"https://tiktok.com/@{cible}",
        f"https://facebook.com/{cible}",
        f"https://youtube.com/@{cible}",
        f"https://duckduckgo.com/?q={cible}",
    ]

    os.makedirs("data", exist_ok=True)
    with open(fichier, "w") as f:
        for lien in liens:
            f.write(lien + "\n")

    slow(GREEN + f"[✓] Résultats sauvegardés dans {fichier}" + RESET, 0.01)

# Mode INFO
def info_mode():
    cible = input(CYAN + "\n[+] Entrez un pseudo ou email : " + RESET)
    now = datetime.now().strftime("%Y%m%d_%H%M")
    fichier = f"data/info_{cible}_{now}.txt"

    slow(YELLOW + "[*] Recherche rapide..." + RESET, 0.01)

    liens = [
        f"https://duckduckgo.com/?q={cible}",
        f"https://haveibeenpwned.com/unifiedsearch/{cible}",
        f"https://hunter.io/search/{cible}",
    ]

    os.makedirs("data", exist_ok=True)
    with open(fichier, "w") as f:
        for lien in liens:
            f.write(lien + "\n")

    slow(GREEN + f"[✓] Résultats sauvegardés dans {fichier}" + RESET, 0.01)

# Lancement
if __name__ == "__main__":
    skull()
    menu()
