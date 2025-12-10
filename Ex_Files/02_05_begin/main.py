import os  #eine bibliothek, die es uns ermöglicht, mit dem Betriebssystem zu interagieren (keys, modes usw.)

DEVELOPMENT = "development"
PRODUCTION = "production"
STAGING = "staging"
CODE_SPACE = "code_space"
LOCAL = "local"

current_env = os.environ.get("ENV_NAME", DEVELOPMENT) #erstes Argument ist der Name der Umgebungsvariable, zweites Argument ist der Standardwert, falls die Variable nicht gesetzt ist.

if current_env == DEVELOPMENT:
    print("Development environment")
elif current_env == PRODUCTION:
    print("Production environment")
elif current_env == STAGING:
    print("Staging environment")
elif current_env in [CODE_SPACE, LOCAL]:
    print("Codespace or local environment")
else:
    print("Unknown environment")


#Befehle für verschiedene Terminals im Video:

#er hat folgendes in der Konsole eingegeben, um die Umgebungsvariable zu setzen (BASH Umgebung _Linux/MacOS_):
#--- export ENV_NAME='aaa' --- ->das ist für bash

# für powerShell (Windows): $Env:ENV_NAME = "aaa"	
# für CMD (Windows): set ENV_NAME=aaa
# für python debug consol: os.environ["ENV_NAME"] = "aaa"

# damit hat es dann ein unknown environment ausgegeben, weil 'aaa' nicht in den definierten Umgebungen ist.
# mit seinem Befehl (export) hat er ein evrioment variable erstellt, die er in seinem python script, dann geändert hat.
#-----------------------------------------------------------------------------------------------------------------------#

#wichtig bash ist leerzeichen-empfindlich, also kein Leerzeichen um das '=' Zeichen herum.

# perplexity erklärung 
# Kurze Antwort: In Bash ist das Leerzeichen vor oder nach dem Gleichheitszeichen bei einer Zuweisung wichtig — "export ENV_NAME='staging'" funktioniert, "export ENV_NAME= 'staging'" nicht, weil Bash das nachfolgende Token als separaten Befehl/Argument interpretiert. Leerzeichen in der Form "VAR= value" sind deshalb ein Problem.

# Warum das obere funktioniert
# In Bash setzt die Syntax VAR=VALUE die Variable; export VAR=VALUE markiert sie zusätzlich als Umgebungsvariable für Kindprozesse. Bei export ENV_NAME='staging' wird ENV_NAME dem Wert "staging" zugewiesen und exportiert, weil keine Leerzeichen innerhalb der Zuweisung sind.

# Warum das untere nicht funktioniert
# Wenn ein Leerzeichen vor dem Wert steht, also export ENV_NAME= 'staging', sieht die Shell das so:

# export wird aufgerufen mit dem ersten Argument ENV_NAME= (eine Zuweisung ohne Wert), und

# das nächste Token 'staging' wird als weiteres Argument (ein eigenständiges Wort) behandelt.
# Das führt typischerweise dazu, dass die Variable nicht wie erwartet gesetzt wird oder die Shell einen Fehler/unerwartetes Verhalten zeigt, weil die Zuweisung nicht korrekt parsiert wird.

# Regeln und Tipps zu Leerzeichen im Terminal
# Bei Variablenzuweisungen darf kein Leerzeichen ums "="-Zeichen stehen: VAR=VALUE ist korrekt; VAR = VALUE ist falsch.

# Wenn der Wert Leerzeichen enthalten soll, dann den Wert in Anführungszeichen setzen: VAR="a value with spaces" oder VAR='a value with spaces'.

# Beispiel korrekt:

# export PATH="$PATH:/home/user/bin"

# export GREETING="hello world"

# Beispiel falsch:

# export GREETING = "hello world" (wird nicht als Zuweisung interpretiert)

# Wie Bash Tokens parst (einfach erklärt)
# Die Shell teilt die Eingabe in Tokens (Wörter) anhand von Leerzeichen, es sei denn, sie sind in Anführungszeichen oder escaped.

# Eine Zuweisung wie NAME=value ist ein einziges Token. NAME= value wird in zwei Token aufgespalten (NAME= und value), also keine gültige Zuweisung mehr.

# Hinweise zu anderen Shells
# Das Verhalten mit Leerzeichen um "=" gilt für POSIX-Shells (Bash, sh, dash) generell.

# In PowerShell ist die Syntax anders (z. B. $Env:ENV_NAME = "staging"), dort ist das $-Präfix Teil der Variablen-Syntax und Leerzeichen um "=" sind in dieser Zuweisungssyntax in der Regel kein Problem.

# Wenn gewünscht, kann ein kurzes Beispiel gezeigt werden, wie das in Bash (Terminal) und in PowerShell exakt aussieht, sowie wie man prüft, ob die Variable gesetzt wurde (z. B. echo $ENV_NAME in Bash bzw. echo $Env:ENV_NAME in PowerShell).