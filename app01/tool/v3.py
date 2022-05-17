#!/usr/bin/env python
# --*--coding: utf-8 --*--

import re
file = '/static/xxx/sda.png'

result = re.search('jpg|png',file)
print(result.group())
