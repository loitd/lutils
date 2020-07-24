import re

# Remember:
#     (?=) - positive lookahead
#     (?!) - negative lookahead
#     (?<=) - positive lookbehind
#     (?<!) - negative lookbehind
#     (?>) - atomic group (An atomic group exits a group and throws away alternative patterns after the first matched pattern inside the group (backtracking is disabled))

# EXPLAIN for sample string: foobarbarfoo
# bar(?=bar)     finds the 1st bar ("bar" which has "bar" after it)
# bar(?!bar)     finds the 2nd bar ("bar" which does not have "bar" after it)
# (?<=foo)bar    finds the 1st bar ("bar" which has "foo" before it)
# (?<!foo)bar    finds the 2nd bar ("bar" which does not have "foo" before it)
# (?<=foo)bar(?=bar)    finds the 1st bar ("bar" with "foo" before it and "bar" after it)
# (?>foo|foot)s applied to foots will match its 1st alternative foo, then fail as s does not immediately follow, and stop as backtracking is disabled
# (foo|foot)s applied to foots will match its 1st alternative foo, then fail as s does not immediately follow in foots, and backtrack to its 2nd alternative; match its 2nd alternative foot, then succeed as s immediately follows in foots, and stop.
# (?=REGEX_1)REGEX_2: Match only if REGEX_1 matches; after matching REGEX_1, the match is discarded and searching for REGEX_2 starts at the same STARTED position.

# https://regex101.com/r/HTiDo5/7/
# It must contain at least 2 uppercase English alphabet characters
# It must contain at least 3 digits (0-9)
# it should only contain alphanumeric characters
# No characters should repeat
# There must be exactly 10 characters
pat = r"^(?=(?:[a-z\d]*[A-Z]){2})(?=(?:\D*\d){3})(?:([a-zA-Z\d])(?!.*\1)){10}$"

# https://www.rexegg.com/regex-lookarounds.html
# 1. The password must have between six and ten word characters \w
# 2. It must include at least one lowercase character [a-z]
# 3. It must include at least three uppercase characters [A-Z]
# 4. It must include at least one digit \d

#         This lookahead asserts: at the current position in the string, what follows is the beginning of the string, six to ten word characters, and the very end of the string.
#         |              The lookahead asserts: at this position in the string (i.e., the beginning of the string), we can match zero or more characters that are not lowercase letters,
#         |              then we can match one lowercase letter. ---> we need to check that the password contains one lowercase letter
#         |              the simplest idea is to use .*[a-z]. That works, but the dot-star first shoots down to the end of the string, so we will always need to backtrack.
#         |              |               The lookahead asserts: at this position in the string (i.e., the beginning of the string), 
#         |                              we can do the following three times: match zero or more characters that are not uppercase letters 
#         |                              (the job of the negated character class [^A-Z] with the quantifier *), then match one uppercase letter 
#         |                              ---> we need to check that the password contains at least three uppercase letters.
#         |              |               |                      The lookahead asserts: at this position in the string (i.e., the beginning of the string), 
#         |              |               |                      we can match zero or more characters that are not digits (the job of the "not-a-digit" character class \D 
#         |              |                                      and the * quantifier), then we can match one digit. ---> To check that the string contains at least one digit
#         |              |               |                      |
#         |              |               |                      |
pat = r"\A(?=\w{6,10}\z)(?=[^a-z]*[a-z])(?=(?:[^A-Z]*[A-Z]){3})(?=\D*\d).*\z"


# It must start with a 4,5 or 6.
# It must contain exactly 16 digits.
# It must only consist of digits (0-9).
# It may have digits in groups of , separated by one hyphen "-".
# It must NOT use any other separator like ' ' , '_', etc.
# It must NOT have 4 or more consecutive repeated digits.
        #   Start with 4-6          
        #   |       Contains only \d or \- and length in 16-19. Dont forget ^ and $ signs
        #   |       |                    No more than 3 consecutive repeated digit
        #   |       |                    |                in form of 4 digits 1 hyphen x3 + 4 digits. Dont forget ^ and $ signs.
        #   |       |                    |                |                            Contains 3 hyphens or 0 hyphen. 
        #   |       |                    |                |                            |
        #   |       |                    |                |                            |
pat = r"^(?=^[4-6])(?=^([\d\-]){16,19}$)(?!.*([0-9])\1{3})(?=^((\d{4})\-?){3}(\d{4})$)(?=((.*[\-]){3})|((.*[\-]){0})).*$"

        #   No more then 3 consecutive repeated digits 
        #   |
pat2 = r"^(?!.*(\d)\1{3}).*$"



# should find alternating repetitive digits pairs in a given string. must not contain more than one alternating repetitive digit pair.
# Alternating repetitive digits are digits which repeat immediately after the next digit. 
# In other words, an alternating repetitive digit pair is formed by two equal digits that have just a single digit between them.

#          Get the first digit into group 1
#          |    Check to make sure next digit is not equal to 1st digit
#          |    |          Only 1 digit allowed
#          |    |          |   The 3rd one must equal to 1st
#          |    |          |   |
#          |    |          |   |
#          |    |          |   |
pat = r"(?=(\d)(?=(?:[^\1]){1}(\1)))"
pat = r"(?=(\d)(?=(?:[\d]){1}(\1)))"

# Range between 100000 to 999999
#         First char is from 1-9
#         |     Next 5 chars are from 0-9
#         |     |
#         |     |
pat = r"^([1-9][0-9]{5})$"
pat = r"^(?=[1-9][0-9]{5}$)" #use positive lookahead

# If there are symbols or spaces between two alphanumeric characters of the decoded script, then Neo replaces them with a single space '' for better readability.
#       Positive lookbehind to check if prev char is alphanumeric
#       |               Capture all special chars + spaces (+: 1 or more)
#       |               |           Check next char for alphanumeric
#       |               |           |
pat = r"(?<=[a-zA-Z0-9])[!@#$%&\s]+(?=[a-zA-Z0-9])"

# Find and replace
#             Pattern,ReplaceWith,OriginalString
# rem1 = re.sub(pat, r" ", orig.rstrip())


orig = r"1114562223333333333345556567765543332222214574555869769769797087087966575745747"


# pat = r"(\d)(\1*)"
# res = re.findall(pat, orig)
# num = len(re.findall(pat, orig))
# print(res)

# res = re.match(pat, orig, re.UNICODE)
# if res:
#     pass #matched
# else:
#     pass #not matched
