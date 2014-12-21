def ask_ok(prompt, retries=4, complaint='Bitte Ja oder Nein!'):
   while True:
       ok = input(prompt)
       if ok in ('j', 'J', 'ja', 'Ja', 'y', '1'): return True
       if ok in ('n', 'N', 'ne', 'Ne', 'Nein', '0'): return False
       retries = retries - 1
       if retries < 0:
           raise IOError('Benutzer abgelehnt!')
       print(complaint)
raise IOError('Hier hat sich wohl ein Fehler eingeschlichen :)')
string = ask_ok('(y/n)', 5, 'Ja')
print (string)
