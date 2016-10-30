#!/usr/bin/python -tt

def mix_up(a,b):
  a_temp = b[:2] + a[2:]
  b_temp = a[:2] + b[2:]

  return a_temp + ' ' + b_temp

def test(got,expected):
  if got == expected:
	prefix = 'OK'
  else:
	prefix = 'X'
  
  print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))

def main():
  test(mix_up('mix', 'pod'), 'pox mid')


if __name__ == '__main__':
  main()
