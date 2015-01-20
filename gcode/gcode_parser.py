#! /usr/bin/python

ifile = 'test.gc'


#------------------------------------------------------------------------------
# lexer

import ply.lex as lex

# token names
tokens = (
  'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
  'INTEGER',
  'DECIMAL',
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

t_INTEGER = r'\d+'
t_DECIMAL = r'[+-]*\d*\.\d*'

def t_COMMENT(t):
  r'\(.*\)|[;%].*'
  pass

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \r\t'

# Define a rule so we can track line numbers
def t_newline(t):
  r'\n'
  t.lexer.lineno += len(t.value)

# Error handling rule
def t_error(t):
  print "illegal character '%s'" % t.value[0]
  t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

#------------------------------------------------------------------------------
# parser

import ply.yacc as yacc

def p_lines(p):
  '''lines : lines line
           | line'''
  pass

def p_line(p):
  '''line : line_number
          | line_number words
          | words'''
  pass

def p_words(p):
  '''words : words word
           | word'''
  pass

def p_line_number(p):
  '''line_number : N INTEGER'''
  print('%s%s' % (p[1], p[2]))

def p_word(p):
  '''word : general_function
          | tool_selection
          | misc_function
          | feed_rate
          | spindle_speed
          | tool_length_offset_index
          | x_axis
          | y_axis
          | z_axis
          | a_axis
          | b_axis
          | c_axis'''

def p_general_function(p):
  'general_function : G INTEGER'
  print('%s%s' % (p[1], p[2]))

def p_tool_selection(p):
  'tool_selection : T INTEGER'
  print('%s%s' % (p[1], p[2]))

def p_misc_function(p):
  'misc_function : M INTEGER'
  print('%s%s' % (p[1], p[2]))

def p_feed_rate(p):
  'feed_rate : F DECIMAL'
  print('%s%s' % (p[1], p[2]))

def p_spindle_speed(p):
  'spindle_speed : S INTEGER'
  print('%s%s' % (p[1], p[2]))

def p_tool_length_offset_index(p):
  'tool_length_offset_index : H INTEGER'
  print('%s%s' % (p[1], p[2]))

def p_x_axis(p):
  'x_axis : X DECIMAL'
  print('%s%s' % (p[1], p[2]))

def p_y_axis(p):
  'y_axis : Y DECIMAL'
  print('%s%s' % (p[1], p[2]))

def p_z_axis(p):
  'z_axis : Z DECIMAL'
  print('%s%s' % (p[1], p[2]))

def p_a_axis(p):
  'a_axis : A DECIMAL'
  print('%s%s' % (p[1], p[2]))

def p_b_axis(p):
  'b_axis : B DECIMAL'
  print('%s%s' % (p[1], p[2]))

def p_c_axis(p):
  'c_axis : C DECIMAL'
  print('%s%s' % (p[1], p[2]))

# Error rule for syntax errors
def p_error(p):
  print "syntax error at token", p.type
  # Just discard the token and tell the parser it's okay.
  parser.errok()

parser = yacc.yacc()

#------------------------------------------------------------------------------

def main():
  f = open(ifile, 'r')
  x = f.read()
  f.close()

  #lexer.input(x)

  #while True:
    #tok = lexer.token()
    #if not tok: break      # No more input
    #print tok

  result = parser.parse(x)
  print result

main()

#------------------------------------------------------------------------------


