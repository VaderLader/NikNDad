def ask_ok(prompt, retries=4, complaint='Bitte Ja oder Nein!'):
   while True:
       ok = input(prompt)
       if ok in ('j', 'J', 'ja', 'Ja'): return True
       if ok in ('n', 'N', 'ne', 'Ne', 'Nein'): return False
       retries = retries - 1
       if retries < 0:
           raise IOError('Benutzer abgelehnt!')
       print(complaint)
