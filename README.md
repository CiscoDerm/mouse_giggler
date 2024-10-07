# 🖱️ Mouse Trembler 📳

> Faites trembler votre souris automatiquement ! Un script Python amusant et personnalisable.

[![Python Version](https://img.shields.io/badge/Python-3.6%2B-blue)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Contributions Welcome](https://img.shields.io/badge/Contributions-Welcome-brightgreen.svg)](CONTRIBUTING.md)

## 📖 Table des Matières

- [À Propos](#-à-propos)
- [Fonctionnalités](#-fonctionnalités)
- [Prérequis](#-prérequis)
- [Installation](#-installation)
- [Utilisation](#-utilisation)
- [Configuration](#-configuration)
- [Dépannage](#-dépannage)
- [Contribuer](#-contribuer)
- [Licence](#-licence)

## 🤔 À Propos

Mouse Trembler est un script Python ludique qui fait trembler automatiquement votre curseur de souris. Parfait pour :
- 🎮 Empêcher votre ordinateur de se mettre en veille
- 🔬 Tester la détection de mouvements
- 🎢 Simplement s'amuser !

## ✨ Fonctionnalités

- 🎯 Tremblement constant et localisé
- ⚡ Mouvements rapides et fluides
- 🛑 Arrêt d'urgence facile
- ⚙️ Paramètres personnalisables

## 📋 Prérequis

- Python 3.6 ou supérieur
- Module PyAutoGUI

## 💻 Installation

1. Clonez le dépôt :
```bash
git clone https://github.com/ciscoderm/mouse_giggler.git
cd mouse-trembler
```

2. Installez les dépendances :
```bash
pip install pyautogui
```

## 🚀 Utilisation

1. Lancez le script :
```bash
python3 mouse_giggler.py
```

2. Pour arrêter :
   - Déplacez rapidement la souris dans un coin de l'écran
   - OU appuyez sur `Ctrl+C` dans le terminal

## ⚙️ Configuration

Personnalisez le comportement en modifiant ces variables :

```python
TREMOR_AMPLITUDE = 5     # Amplitude du tremblement en pixels
MOVEMENT_DURATION = 0.01 # Durée de chaque mouvement en secondes
PAUSE_DURATION = 0.01    # Pause entre les mouvements
RECENTER_CHANCE = 0.2    # Probabilité de recentrage (0.0 à 1.0)
```

## 🔧 Dépannage

| Problème | Solution |
|----------|----------|
| Le script ne démarre pas | Vérifiez que PyAutoGUI est installé |
| Mouvements trop rapides | Augmentez `MOVEMENT_DURATION` |
| Mouvements trop lents | Diminuez `MOVEMENT_DURATION` |

## 🤝 Contribuer

Les contributions sont les bienvenues ! N'hésitez pas à :

1. 🍴 Forker le projet
2. 🔧 Créer une branche (`git checkout -b feature/AmazingFeature`)
3. 💾 Commit vos changements (`git commit -m 'Add AmazingFeature'`)
4. 📤 Push sur la branche (`git push origin feature/AmazingFeature`)
5. 📩 Ouvrir une Pull Request

## 📜 Licence

Ce projet est sous licence MIT. Voir le fichier [LICENSE](LICENSE) pour plus de détails.

---

<p align="center">
  Fait avec ❤️ par <a href="https://github.com/votre-nom">Votre Nom</a>
</p>
