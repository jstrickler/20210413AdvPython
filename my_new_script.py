#!/usr/bin/env python
#!/Users/jstrick/.env/my_virtual_env/bin/python
"""
This is the doc string for the module/script.
"""
# other imports  (standard library, standard non-library, local)
import sys

# constants (AKA global variables -- keep these to a minimum)
MAX_TRIES = 5

def foobar():
    pass

# main function
def main(args):
    """
    This is the docstring for the main() function

    :param args: Command line arguments.
    :return: None
    """
    # config = get_config() # from file or command line
    # data = read_data()
    # result = process_data(data)
    # output_data(result)

    function1()
    foobar()

# other functions
def function1():
    """
    This is the docstring for function1().

    :return: None
    """
    pass

if __name__ == '__main__':
    main(sys.argv[1:])  # Pass command line args (minus script name) to main()
