import pyautogui
import random
import time

# Configuration de sécurité pour pyautogui
pyautogui.FAILSAFE = True  # Permet d'arrêter le script en déplaçant la souris dans un coin

def trembler_souris():
    try:
        print("Le programme va faire trembler la souris.")
        print("Déplacez la souris dans un coin de l'écran pour arrêter.")
        
        # Pause de 3 secondes pour donner le temps à l'utilisateur de se préparer
        time.sleep(3)
        
        # Position initiale
        start_x, start_y = pyautogui.position()
        
        while True:
            # Générer de petits déplacements aléatoires entre -5 et 5 pixels
            delta_x = random.randint(-5, 5)
            delta_y = random.randint(-5, 5)
            
            # Déplacer la souris rapidement
            pyautogui.moveRel(delta_x, delta_y, duration=0.01)
            
            # Retourner près de la position initiale pour maintenir la zone de tremblement
            if random.random() < 0.2:  # 20% de chance de recentrage
                current_x, current_y = pyautogui.position()
                if abs(current_x - start_x) > 20 or abs(current_y - start_y) > 20:
                    pyautogui.moveTo(start_x + random.randint(-10, 10), 
                                    start_y + random.randint(-10, 10), 
                                    duration=0.05)
            
            # Très courte pause pour ne pas surcharger le système
            time.sleep(0.01)
            
    except KeyboardInterrupt:
        print("\nProgramme arrêté par l'utilisateur.")

if __name__ == "__main__":
    trembler_souris()