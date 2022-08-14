Edubo Test - Andrej Dunda
Dobrý den, aplikace se správně spustí při splnění následujícíh kroků:
  1. operační systém má nainstalovanou verzi Pythonu 3.0.0 a vyšší
  2. V příkazovém řádku je otevřeno virtuální prostředí otevřením souboru "activate" v adresáři "edubo-test-main/venv/Scripts/"
     (Správné spuštění virtuálního prostředí poznáte označením "(venv)" na začátku aktivního příkazového řádku)
  3. Ve virtuálním prostředí musí být nainstalovaný Flask (pip install flask) a Flask-Mail (pip install Flask-Mail)
  4. Aplikace se spustí v adresáři "edubo-test-main" příkazem "flask run"
  
Pokud jsou výše uvedené podmínky splněny, aplikace se spustí na adrese "http://localhost:5000/"
Pozn.: Může se stát, že obnovení hesla s odesláním na email bude fungovat jen na WindowsOS. Pro případné zobrazení hesla otevřete soubor "user_db.txt"
