import sys

COMMANDS = {
    "i": lambda x, y: (x+1, y),
    "d": lambda x, y: (x-1, y),
    "s": lambda x, y: (x*x, y),
    "o": lambda x, y: (print_accum(x, char=False), y),
    "c": lambda x, y: (print_accum(x, char=True), y),
    "w": lambda x, y: print_world(x, y),
    "(": lambda x, y: parse_parens(x, y, loop=False),
    "{": lambda x, y: parse_parens(x, y, loop=True),
    "h": lambda x, y: sys.exit()
}

POP = lambda x: (x[0], x[1:])

def find_matching_paren(in_str, open_sym, close_sym):
    """"""
    count = 1
    for i, char in enumerate(in_str):
        if char == open_sym:
            count += 1
        elif char == close_sym:
            count -= 1
        if count == 0:
            return i
    return -1


def parse_parens(x,y, loop=False):
    """If we find either ( or { then do one of the following:

       * For (, execute the statement in the parens if the
         accumulator is > 0
       * For {, execute the statement in the parens 10 times"""
    close_paren = "}" if loop else ")"
    open_paren = "{" if loop else "("
    close_paren_indx = find_matching_paren(y, open_paren, close_paren)

    if (x > 0 and not loop) and close_paren_indx > 0:
        x = deadfish(y[:close_paren_indx], accum=x)

    if loop and close_paren_indx > 0:
        for i in range(10):
            x = deadfish(y[:close_paren_indx], accum=x)

    return x, y[close_paren_indx+1:]


def reset_accum(x):
    """Reset accumulator to 0 if it is either -1 or 256"""
    return ((0 if x[0] in (-1, 256) else x[0]), x[1])


def print_world(x, y, out=sys.stdout):
    """Write Hello, World! to the selected output device"""
    out.write("Hello, World!",)
    return (x,y)


def print_accum(x, char=False, out=sys.stdout):
    """Print accumulator to screen.  Defaults to plain integer,
    if char is True then try to convert to a unicode character"""
    out.write((chr(x) if char else str(x)),)
    return x


def deadfish(cmd, accum=0):
    """deadfish~"""
    if not cmd: return accum
    c, cmd = POP(cmd)
    if c in COMMANDS:
        accum, cmd = reset_accum(COMMANDS[c](accum, cmd))

    return deadfish(cmd, accum=accum)


def deadfish_cli(accum=0):
    """Display >> prompt, and parse whatever string is input using
    deadfish()"""
    while True:
        accum = deadfish(raw_input(">>"), accum=accum)
        print

if __name__ == "__main__":
    deadfish_cli()
