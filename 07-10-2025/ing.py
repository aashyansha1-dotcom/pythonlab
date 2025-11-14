add_suffix = lambda s: (s + '1y') if s[-3:] == 'ing' else (s + 'ing')
print(add_suffix("run"))
print(add_suffix("running"))
