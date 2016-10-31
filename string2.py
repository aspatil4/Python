#!/usr/bin/python -tt

#Verbing Function
#Given a string, if its length is at least 3, 
#add 'ing' at its end.
#If the string already ends in 'ing', add 'ly' at the end
def verbing(s):
  if (len(s) >= 3 and s[-3:] != 'ing'):
	return s + 'ing'
  if(s[-3:] == 'ing'):
	return s + 'ly'
  else:
  	return s

#Not Bad Function
#Given a string, find the 1st occurance of substring 'not' and 'bad'.
#if 'bad' follows 'not', replace the whole 'not' ... 'bad' substring with 'good'
#Ex: 'This dinner is not that bad' results in: 'This dinner is good'
def not_bad(s):
  n = s.find('not')
  b = s.find('bad')

  if (n != -1 and b != -1 and b > n):
	s = s[:n] + 'good' +  s[b+3:]

  return s

#Front Back Function
#Divide a string into 2 halves.
#If the string length is even, both halves are of the same length.
#If the string length is odd, the first half will contain the extra character.
#Ex: 'abcde' the front half is 'abc' and back half is 'de'.
#Given 2 strings a and b, return a string of the form: a_front + b_front + a_back + b_back
def front_back(a,b):
  len_a = len(a)
  aHalf = len_a / 2
  if len_a % 2 != 0:
	aHalf = aHalf + 1

  a_front = a[:aHalf]
  a_back = a[aHalf:]

  len_b = len(b)
  bHalf = len_b / 2
  if len_b % 2 != 0:
	bHalf = bHalf + 1
  b_front = b[:bHalf]
  b_back = b[bHalf:]

  return a_front + b_front + a_back + b_back

#Simple Provided Test function used in the main() to print what each function returns vs. what it is supposed to return
def test(got,expected):
  if (got == expected):
	prefix = 'OK'
  else:
	prefix = 'X'
  print '%s got: %s expected %s' % (prefix, repr(got), repr(expected))

def main():
  print 'Verbing'
  test(verbing('hail'), 'hailing')
  test(verbing('knowing'), 'knowingly')

  print 'Not Bad'
  test(not_bad('This dinner is not that bad I love it and it is yummy'), 'This dinner is good I love it and it is yummy')

  print 'Front_Back'
  test(front_back('abcd', 'xy'), 'abxcdy')
  test(front_back('abcde', 'xyz'), 'abcxydez')
  test(front_back('kitten', 'donut'), 'kitdontenut')


if __name__ == '__main__':
	main()
