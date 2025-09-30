# This program will print out the following items to the console:
#   - my full name
#   - my preferred pronouns
#   - my favorite movie
#   - my favorite food

def main(*args, **kwargs):
    full_name = 'Zachary James Adams'
    pronouns  = 'he/him'
    fav_movie = 'The Lord of the Rings: The Fellowship of the Ring'
    fav_food  = 'chicken nuggets, for they are numerous and simple'

    template_string = \
    f'My full name is {full_name} and my pronouns are ({pronouns}).\n'+ \
    f'My favorite movie is "{fav_movie}".\n'+ \
    f'My favorite food is {fav_food}.'
   
    print(template_string)



if __name__ == '__main__':
    main()
