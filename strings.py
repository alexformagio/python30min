multi_line_quote = ''' line 1
                       line2
                       line3'''

print(multi_line_quote)
print("\n" *5)
quotes_inside="\"using backslash\""
print(quotes_inside)
print(" %s %s %s " % ('single quotes',multi_line_quote,quotes_inside))

print("I don't like ", end="")
print('new line')
