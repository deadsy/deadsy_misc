#! /usr/bin/python

ifile = 'test.gc'

import ply.lex as lex

# token names
tokens = (
  'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
  'NUMBER',
  'FLOAT',
  'COMMENT',
)

t_A = r'A|a'
t_B = r'B|b'
t_C = r'C|c'
t_D = r'D|d'
t_E = r'E|e'
t_F = r'F|f'
t_G = r'G|g'
t_H = r'H|h'
t_I = r'I|i'
t_J = r'J|j'
t_K = r'K|k'
t_L = r'L|l'
t_M = r'M|m'
t_N = r'N|n'
t_O = r'O|o'
t_P = r'P|p'
t_Q = r'Q|q'
t_R = r'R|r'
t_S = r'S|s'
t_T = r'T|t'
t_U = r'U|u'
t_V = r'V|v'
t_W = r'W|w'
t_X = r'X|x'
t_Y = r'Y|y'
t_Z = r'Z|z'

t_NUMBER = r'\d+'
t_FLOAT = r'[+-]*\d+\.\d+'
t_COMMENT = r'\(.*\)|%.*'

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

# Define a rule so we can track line numbers
def t_newline(t):
  r'\r*\n+'
  t.lexer.lineno += len(t.value)

# Error handling rule
def t_error(t):
  print "illegal character '%s'" % t.value[0]
  t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

def main():
  f = open(ifile, 'r')
  x = f.read()
  f.close()

  lexer.input(x)

  while True:
    tok = lexer.token()
    if not tok: break      # No more input
    print tok

main()
