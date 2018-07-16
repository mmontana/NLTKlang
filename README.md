### NLKTKlang



```python
import model

text_en = "This is an english text."
print(model.language(text_en))
text_de = "www.github.com https://www.wikipedia.org Das ist ein ''**&§§$*!? deutscher Text mit Artefakten ++ @MENTION @SOME @PERSONX"
print(model.language(text_de))
```

    english
    german
