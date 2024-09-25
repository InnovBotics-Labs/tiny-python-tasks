"""Database script"""
STAGES = [r'''
  +---+
  |   |
  O   |
 /|\\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

LOGO = r'''
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \\ / _` | '_ \\ / _` | '_ ` _ \\ / _` | '_ \\ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\\__,_|_| |_|\\__, |_| |_| |_|\\__,_|_| |_|
                    __/ |                      
                   |___/    '''

LIVES_FOR_EACH_LEVEL = {
    'easy': 7,
    'medium': 5,
    'hard': 3
}
