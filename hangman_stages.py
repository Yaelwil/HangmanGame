hangman_stages = [
    '''
     ------
     |    |
          |
          |
          |
          |
          |
    ----------
    ''',  # Stage 0: No incorrect guesses (full hangman figure is not shown)

    '''
     ------
     |    |
     O    |
          |
          |
          |
          |
    ----------
    ''',  # Stage 1: Head added

    '''
     ------
     |    |
     O    |
     |    |
          |
          |
          |
    ----------
    ''',  # Stage 2: Body added

    '''
     ------
     |    |
     O    |
    /|    |
          |
          |
          |
    ----------
    ''',  # Stage 3: Left arm added

    '''
     ------
     |    |
     O    |
    /|\\   |
          |
          |
          |
    ----------
    ''',  # Stage 4: Right arm added

    '''
     ------
     |    |
     O    |
    /|\\   |
    /     |
          |
          |
    ----------
    ''',  # Stage 5: Left leg added

    '''
     ------
     |    |
     O    |
    /|\\   |
    / \\   |
          |
          |
    ----------
    '''  # Stage 6: Full figure (game over, all parts added)
]