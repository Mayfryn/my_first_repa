s = "Hello! My name is Mayfryn!"
n = "8945734956643107"
# capitalize(	)
# Return a copy of the string with only its first character capitalized.
print(s.capitalize())

# center(	width[, fillchar])
# Return centered in a string of length width. Padding is done using the specified fillchar (default is a space). Changed in version 2.4: Support for the fillchar argument.
print(s.center(100,' '))

# count(	sub[, start[, end]])
# Return the number of occurrences of substring sub in string S[start:end]. Optional arguments start and end are interpreted as in slice notation.
print(s.count(' '))
print(s.count('a'))

# str.casefold()
# Return a casefolded copy of the string. Casefolded strings may be used for caseless matching.
# Casefolding is similar to lowercasing but more aggressive because it is intended to remove all case distinctions in a string. For example, the German lowercase letter 'ß' is equivalent to "ss". Since it is already lowercase, lower() would do nothing to 'ß'; casefold() converts it to "ss".
# The casefolding algorithm is described in section 3.13 of the Unicode Standard.
print(s.casefold())

# str.endswith(suffix[, start[, end]])
# Return True if the string ends with the specified suffix, otherwise return False. suffix can also be a tuple of suffixes to look for. With optional start, test beginning at that position. With optional end, stop comparing at that position
print(s.endswith('n!'))
print(s.endswith('ning'))

# ????????????str.expandtabs(tabsize=8)
# Return a copy of the string where all tab characters are replaced by one or more spaces, depending on the current column and the given tab size. Tab positions occur every tabsize characters (default is 8, giving tab positions at columns 0, 8, 16 and so on). To expand the string, the current column is set to zero and the string is examined character by character. If the character is a tab (\t), one or more space characters are inserted in the result until the current column is equal to the next tab position. (The tab character itself is not copied.) If the character is a newline (\n) or return (\r), it is copied and the current column is reset to zero. Any other character is copied unchanged and the current column is incremented by one regardless of how the character is represented when printed.
print(s.expandtabs(tabsize=16))

# str.find(sub[, start[, end]])
# Return the lowest index in the string where substring sub is found within the slice s[start:end]. Optional arguments start and end are interpreted as in slice notation. Return -1 if sub is not found
print(s.find('Ma'))

# str.format(*args, **kwargs)
# Perform a string formatting operation. The string on which this method is called can contain literal text or replacement fields delimited by braces {}. Each replacement field contains either the numeric index of a positional argument, or the name of a keyword argument. Returns a copy of the string where each replacement field is replaced with the string value of the corresponding argument.
print("The sum of 1 + 2 is {0}".format(1+2))
# 'The sum of 1 + 2 is 3'
# See Format String Syntax for a description of the various formatting options that can be specified in format strings.
#
# Note When formatting a number (int, float, complex, decimal.Decimal and subclasses) with the n type (ex: '{:n}'.format(1234)), the function temporarily sets the LC_CTYPE locale to the LC_NUMERIC locale to decode decimal_point and thousands_sep fields of localeconv() if they are non-ASCII or longer than 1 byte, and the LC_NUMERIC locale is different than the LC_CTYPE locale. This temporary change affects other threads.
# Changed in version 3.7: When formatting a number with the n type, the function sets temporarily the LC_CTYPE locale to the LC_NUMERIC locale in some cases.


# str.format_map(mapping)
# Similar to str.format(**mapping), except that mapping is used directly and not copied to a dict. This is useful if for example mapping is a dict subclass:
#
# >>>
# class Default(dict):
#     def __missing__(self, key):
#         return key
#
# '{name} was born in {country}'.format_map(Default(name='Guido'))
# 'Guido was born in country'
# New in version 3.2.

# str.index(sub[, start[, end]])
# Like find(), but raise ValueError when the substring is not found.
print(s.index(' '))
print(s.index('i'))


# str.isalnum()
# Return True if all characters in the string are alphanumeric and there is at least one character, False otherwise. A character c is alphanumeric if one of the following returns True: c.isalpha(), c.isdecimal(), c.isdigit(), or c.isnumeric().
print(s.isalnum())

# str.isalpha()
# Return True if all characters in the string are alphabetic and there is at least one character, False otherwise. Alphabetic characters are those characters defined in the Unicode character database as “Letter”, i.e., those with general category property being one of “Lm”, “Lt”, “Lu”, “Ll”, or “Lo”. Note that this is different from the “Alphabetic” property defined in the Unicode Standard.
print(s.isalpha())

# str.isascii()
# Return True if the string is empty or all characters in the string are ASCII, False otherwise. ASCII characters have code points in the range U+0000-U+007F.


# str.isdecimal()
# Return True if all characters in the string are decimal characters and there is at least one character, False otherwise. Decimal characters are those that can be used to form numbers in base 10, e.g. U+0660, ARABIC-INDIC DIGIT ZERO. Formally a decimal character is a character in the Unicode General Category “Nd”.
print(n.isdecimal())

# str.isdigit()
# Return True if all characters in the string are digits and there is at least one character, False otherwise. Digits include decimal characters and digits that need special handling, such as the compatibility superscript digits. This covers digits which cannot be used to form numbers in base 10, like the Kharosthi numbers. Formally, a digit is a character that has the property value Numeric_Type=Digit or Numeric_Type=Decimal.
print(n.isdigit())

# str.isidentifier()

# str.islower()
# Return True if all cased characters in the string are lowercase and there is at least one cased character, False otherwise.
print(n.islower())
print(s.islower())

# str.isnumeric()
# Return True if all characters in the string are numeric characters, and there is at least one character, False otherwise. Numeric characters include digit characters, and all characters that have the Unicode numeric value property, e.g. U+2155, VULGAR FRACTION ONE FIFTH. Formally, numeric characters are those with the property value Numeric_Type=Digit, Numeric_Type=Decimal or Numeric_Type=Numeric.
print(n.isnumeric())


# str.isprintable()
# Return True if all characters in the string are printable or the string is empty, False otherwise. Nonprintable characters are those characters defined in the Unicode character database as “Other” or “Separator”, excepting the ASCII space (0x20) which is considered printable. (Note that printable characters in this context are those which should not be escaped when repr() is invoked on a string. It has no bearing on the handling of strings written to sys.stdout or sys.stderr.)
print(s.isprintable())

# str.isspace()
# Return True if there are only whitespace characters in the string and there is at least one character, False otherwise.
print(s.isspace())


# str.istitle()
# Return True if the string is a titlecased string and there is at least one character, for example uppercase characters may only follow uncased characters and lowercase characters only cased ones. Return False otherwise.
print(s.istitle())


# str.isupper()
# Return True if all cased characters 4 in the string are uppercase and there is at least one cased character, False otherwise.
print(s.isupper())


# str.join(iterable)
# Return a string which is the concatenation of the strings in iterable. A TypeError will be raised if there are any non-string values in iterable, including bytes objects. The separator between elements is the string providing this method.
print(s.join("IIII"))

# str.ljust(width[, fillchar])
# Return the string left justified in a string of length width. Padding is done using the specified fillchar (default is an ASCII space). The original string is returned if width is less than or equal to len(s).
print(s.ljust(100, '*'))


# str.lower()
# Return a copy of the string with all the cased characters 4 converted to lowercase.
print(s.lower())


# str.lstrip([chars])
# Return a copy of the string with leading characters removed. The chars argument is a string specifying the set of characters to be removed. If omitted or None, the chars argument defaults to removing whitespace. The chars argument is not a prefix; rather, all combinations of its values are stripped:
print('   spacious   '.lstrip())
print(s.lstrip('H'))

# static str.maketrans(x[, y[, z]])

# str.partition(sep)
# Split the string at the first occurrence of sep, and return a 3-tuple containing the part before the separator, the separator itself, and the part after the separator. If the separator is not found, return a 3-tuple containing the string itself, followed by two empty strings.
print((s.partition('My')))


# str.replace(old, new[, count])
# Return a copy of the string with all occurrences of substring old replaced by new. If the optional argument count is given, only the first count occurrences are replaced.
print(s.replace('Hello', 'Hi'))


# str.rfind(sub[, start[, end]])
# Return the highest index in the string where substring sub is found, such that sub is contained within s[start:end]. Optional arguments start and end are interpreted as in slice notation. Return -1 on failure.
print(s.rfind('a'))


# str.rindex(sub[, start[, end]])
# Like rfind() but raises ValueError when the substring sub is not found.
print(s.rindex(' '))


# str.rjust(width[, fillchar])
# Return the string right justified in a string of length width. Padding is done using the specified fillchar (default is an ASCII space). The original string is returned if width is less than or equal to len(s).
print(s.rjust(100, '#'))


# str.rpartition(sep)
# Split the string at the last occurrence of sep, and return a 3-tuple containing the part before the separator, the separator itself, and the part after the separator. If the separator is not found, return a 3-tuple containing two empty strings, followed by the string itself.
print((s.rpartition('a')))


# str.rsplit(sep=None, maxsplit=-1)
# Return a list of the words in the string, using sep as the delimiter string. If maxsplit is given, at most maxsplit splits are done, the rightmost ones. If sep is not specified or None, any whitespace string is a separator. Except for splitting from the right, rsplit() behaves like split() which is described in detail below.
print(s.rsplit())
print(s.rsplit(sep='a'))


# str.rstrip([chars])
# Return a copy of the string with trailing characters removed. The chars argument is a string specifying the set of characters to be removed. If omitted or None, the chars argument defaults to removing whitespace. The chars argument is not a suffix; rather, all combinations of its values are stripped:
print('   spacious   '.rstrip())
print('mississippi'.rstrip('ipz'))


# str.split(sep=None, maxsplit=-1)
# Return a list of the words in the string, using sep as the delimiter string. If maxsplit is given, at most maxsplit splits are done (thus, the list will have at most maxsplit+1 elements). If maxsplit is not specified or -1, then there is no limit on the number of splits (all possible splits are made).
#
# If sep is given, consecutive delimiters are not grouped together and are deemed to delimit empty strings (for example, '1,,2'.split(',') returns ['1', '', '2']). The sep argument may consist of multiple characters (for example, '1<>2<>3'.split('<>') returns ['1', '2', '3']). Splitting an empty string with a specified separator returns [''].
print('1,2,3,4,5'.split(sep=',', maxsplit=2))


# str.splitlines([keepends])
# Return a list of the lines in the string, breaking at line boundaries. Line breaks are not included in the resulting list unless keepends is given and true.
print('ab c\n\nde fg\rkl\r\n'.splitlines())
print('ab c\n\nde fg\rkl\r\n'.splitlines(keepends=True))

# str.startswith(prefix[, start[, end]])
# Return True if string starts with the prefix, otherwise return False. prefix can also be a tuple of prefixes to look for. With optional start, test string beginning at that position. With optional end, stop comparing string at that position.
print(s.startswith('Hell'))

# str.strip([chars])
# Return a copy of the string with the leading and trailing characters removed. The chars argument is a string specifying the set of characters to be removed. If omitted or None, the chars argument defaults to removing whitespace. The chars argument is not a prefix or suffix; rather, all combinations of its values are stripped:
print('   spacious   '.strip())



# str.swapcase()
# Return a copy of the string with uppercase characters converted to lowercase and vice versa. Note that it is not necessarily true that s.swapcase().swapcase() == s.
print(s.swapcase())


# str.title()
# Return a titlecased version of the string where words start with an uppercase character and the remaining characters are lowercase.
print("they're bill's friends from the UK".title())



# str.translate(table)

# str.upper()
# Return a copy of the string with all the cased characters 4 converted to uppercase. Note that s.upper().isupper() might be False if s contains uncased characters or if the Unicode category of the resulting character(s) is not “Lu” (Letter, uppercase), but e.g. “Lt” (Letter, titlecase).
print(s.upper())


# str.zfill(width)
# Return a copy of the string left filled with ASCII '0' digits to make a string of length width. A leading sign prefix ('+'/'-') is handled by inserting the padding after the sign character rather than before. The original string is returned if width is less than or equal to len(s).
print("42".zfill(5))
print("-42".zfill(5))