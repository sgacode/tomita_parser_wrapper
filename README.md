Simple wrapper for tomita parser + sample configs

Example persons parse:

```python
from tomita.parser import TomitaParser
from tomita import appglobals

text = 'Яков Миркин (заведующий отделом международных рынков капитала Института мировой экономики и международных отношений РАН)'
parser = TomitaParser(appglobals.CONFIG_PERSONS)
result = parser.parse(text)
```