# 🤖 ChatBot – Assistant interactif GPT-3.5 en terminal

Ce projet Python met en place un chat interactif en ligne de commande (type terminal), capable de générer du texte via l'API GPT-3.5 d’OpenAI.  
L'utilisateur peut dialoguer avec le chatbot jusqu’à une limite de 20 prompts, avec un mot de passe requis à l’entrée pour sécuriser l'accès.

---

## 🚀 Fonctionnalités principales

- ✅ Envoi de requêtes dynamiques via `openai.Completion`
- 🔐 Vérification d’un mot de passe avant démarrage
- 🔁 Messages en boucle (max 20 prompts)
- 🔢 Compteur de prompts en temps réel
- 👋 Fermeture propre à la commande `Bye`

---

## 🛠️ Détails techniques

- Authentification simple (améliorable avec `getpass` ou `hashlib`)
- Limitation de requêtes intégrée (20 max)
- Utilisation de **GPT-3.5-turbo-instruct**
- Réponses personnalisées
- Code extensible : commandes supplémentaires possibles (`/reset`, `/help`, etc.)

---

## 🧠 Technologies utilisées

- Python 3.x
- API OpenAI (`openai`)
- Interface CLI (terminal)

---

🔐 *Pensez à sécuriser votre clé API dans une variable d’environnement ou un fichier `.env`*  
💬 *Projet idéal pour comprendre comment interfacer Python avec GPT de manière simple !*
