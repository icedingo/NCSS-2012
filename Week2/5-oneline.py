for num in [ x[0] for x in [ __import__('re').findall(r'(?<!\d)(?:(?:(?:(?:\+61[- ]?\d[- ]?)|(?:0\d[- ]?)|(?:\(0\d\)[- ]))?(?:(?:\d{4}[- ]\d{4})|(?:\d{8})))|(?:(?:(?:\+61[- ]?)|\d)\d(?:(?:\d{2}[- ]\d{3}[- ]\d{3})|(?:\d{8}))))(?!\d)',line) for line in open('numbers.txt')] if len(x) > 0 ]:print num