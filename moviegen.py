from __future__ import print_function
from copy import deepcopy
import random
import sys
from time import sleep

SEASONS =   ['Spring', 'Summer', 'Fall', 'Winter']
YEARS =     ['2014', '2014', '2015', '2016', '2017']
DIRECTORS = ['Wes Anderson', 'Quentin Tarantino', 'Michael Bay', 'Steven Spielberg', 'Gus Van Sant', 'M. Night Shyamalan', 'Julie Taymor', 'Spike Lee', 'Mel Brooks', 
                'David Lynch', 'Woody Allen', 'Christopher Nolan', 'Peter Jackson', 'George Lucas', 'J.J. Abrams', 'Tim Burton', 'Martin Scorcese', 'Tyler Perry',
                'the Coen Brothers', 'Tommy Wiseau', 'Michel Gondry', 'James Cameron', 'Steven Spielberg', 'Michael Bay', 'somebody you\'ve never heard of']
ACTORS =    ['Will Ferrell', 'Uma Thurman', 'Zach Galifianakis', 'Johnny Depp', 'Keanu Reeves', 'Tina Fey', 'Megan Fox', 'Jim Carrey', 'Jude Law', 'Jennifer Lopez',
                'Leonardo DiCaprio', 'Benedict Cumberbatch', 'Felicia Day', 'Hulk Hogan', 'Snoop Dogg', 'Owen Wilson', 'Zooey Deschanel', 'Pee-Wee Herman', 
                'Ray Romano', 'Drew Carey', 'Cate Blanchett', 'Morgan Freeman', 'Sarah Silverman', 'Lucy Liu', 'George Takei', 'William Shatner', 'Jackie Chan',
                'Patrick Stewart', 'Justin Timberlake', 'Miley Cyrus', 'Lindsey Lohan', 'Emma Watson', 'Elijah Wood', 'Bill Murray', 'Peter Dinklage', 'Tom Waits',
                'Ellen Page', 'Michael Cera', 'Angelina Jolie', 'Dwayne "The Rock" Johnson', 'Samuel L. Jackson', 'Halle Berry', 'Lady Gaga', 'Ellen Degeneres',
                'Mike Myers', 'Wil Wheaton', 'Elvira', 'Jack Nicholson', 'Nicolas Cage', 'Fran Drescher', 'Oprah Winfrey', 'Drew Barrymore', 'Jerry Seinfeld']
PLOTS =     ['a knuckle-biting action thriller', 'a musical about VERY flamboyant aliens', 'the bromance of the year', 'a fantasy adventure for the whole family', 
                'a psychedelic journey through time and space', 'an artful deconstruction of the absurdity of modern life', 'a tour-de-force of interpretive dance',
                'a CG-animated kids\' film with fuzzy animals', 'a gruesome scare-fest about a psychotic janitor', 'an absurdist comedy about male modeling',
                'a documentary exposing discrimination against hairless cat owners', 'a movie about nothing', 'a four-hour epic old-school western', 
                'a kung-fu movie set in the year 5000', 'the burning-hot romance of the decade', 'a hilarious comedy about pot-smoking dolphins', 
                'a coming-of-age adventure with a great classic rock soundtrack', 'an animated journey into the secret lives of sea cucumbers', 
                'a parody propaganda film for the Church of the Flying Spaghetti Monster', 'a character drama full of love, loss, and unnecessary nudity',
                'a romantic comedy with a secret twist', 'a gritty noir crime drama', 'an action blockbuster about giant robots fighting giant zombies']

def generate_movie(counter=0):
    directors = deepcopy(DIRECTORS)
    plots = deepcopy(PLOTS)
    while directors and plots:
        prompt_text = 'Press Enter to generate an awesome movie idea... ' if counter < 1 else 'Try again? (y/n) '
        prompt = raw_input(prompt_text)
        if prompt.lower().startswith('n'):
            quit()
        dots = 0
        while dots < 3:
            print('.', end=''); sys.stdout.flush(); sleep(1)
            dots += 1
        director = directors.pop(directors.index(random.choice(directors)))
        plot = plots.pop(plots.index(random.choice(plots)))
        print('\nComing %s %s...' % (random.choice(SEASONS), random.choice(YEARS))); sleep(1.5)
        print('%s and %s ' % (random.choice(ACTORS), random.choice(ACTORS)), end=''); sys.stdout.flush(); sleep(1.5)
        print('in %s!' % plot); sleep(1.5)
        print('Directed by %s.\n' % director); sleep(1.5)
        counter += 1
    generate_movie(counter=1)

print('\n--------------------------------------------\nWelcome to the Awesome Movie Idea Generator!\n--------------------------------------------\n')
generate_movie()