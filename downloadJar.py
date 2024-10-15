import subprocess
import os
from threading import Thread
import main
import customtkinter as Ctk

javaPath = r'"C:\Program Files\Java\jdk-21\bin\java.exe" '
test = r"C:\Users\cocop\Desktop\test1\."
# def download_file_with_progress(url, output_path, progress_bar):

def executerBat(batDir, version):
    batDir = str(batDir)
    def creerBat(batDir):
        with open(batDir, 'w') as bat_file:
            bat_file.write(f'java -Xmx4G -jar spigot-{version}.jar nogui')
        if os.path.exists(batDir):
            print(f"Le fichier {batDir} a été créé avec succès.")
        else:
            print("Une erreur est survenue lors de la création du fichier.")

    creerBat(batDir)
    process = subprocess.Popen(["cmd", "/k", batDir], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    isEulaAsked = False
    while isEulaAsked != True:
        output = process.stdout.readline()
        if output == "You need to agree to the EULA in order to run the server. Go to eula.txt for more info.":
            isEulaAsked=True
            eulaWindow = Ctk.CTk()
            eulaExplaned = Ctk.CTkLabel(master=eulaWindow, text="En cliquant sur le bouton 'accepter', vous vous engagez à respecter l'EULA\nCe dernier est visible sur le site de mojang : https://aka.ms/MinecraftEULA\nVous confirmez agréer a ses conditions et futures modifications.")
            acceptEulaButton = Ctk.CTkButton(master=eulaWindow, text="Accepter")
            CancelEulaButton = Ctk.CTkButton(master=eulaWindow, text="Refuser")

            eulaExplaned.pack()
            acceptEulaButton.pack()
            CancelEulaButton.pack()

            eulaWindow.mainloop()




def spigot(version, output_dir):
    print("démarrage du telechargement du jar spigot.")
    # Créer le répertoire de sortie si nécessaire
    os.makedirs(output_dir, exist_ok=True)

    command = [
        "cmd", "/c", "start", "cmd", "/k",
        f"cd C:\\Users\\cocop\\PycharmProjects\\Cubex - apparence\\ressources && "
        f"{javaPath}-jar BuildTools.jar --rev {version} --output-dir {output_dir} --compile spigot"
    ]

    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)

    isBuildEnded = False

    while isBuildEnded !=True:
        output = process.stdout.readline()
        output = output.decode('utf-8').strip()
        print(output)

        if "BUILD SUCCESS" in output:
            isBuildEnded = True
            print("Build succes. Installation du JAR spigot 1.20.1 avec succes.")
            print("Tentative d'execution du bat d'installation du fichier.")
            executerBat(output_dir, version)
        elif "BUILD" in output and not "SUCCES" in output:
            isBuildEnded = True
            subprocess.run(["cmd", "/c", "start", "cmd", "/k", "color 4 && echo ERREUR LORS DU TELECHARGEMENT DU FICHIER JAR. && echo Merci de contacter un administrateur. && pause && exit"])


    print(f"Spigot {version} a été généré dans {output_dir}")

spigot("1.20.1", f'{test}')