# reldi-normtagner-hr
Twitter-based training dataset for non-standard Croatian

`vert_2_conllu.py` is used for transforming the old vert format into the conllu format. The conllu format should be the reference format.

Validating the conllu format can be done with UD tools like this:
```
python ../tools/validate.py --lang HR --level 1 reldi-normtagner-hr.conllu
```
This test should be passed completely.

```
python ../tools/validate.py --lang HR --level 2 reldi-normtagner-hr.conllu
```

In this test only format and syntax errors should be identified, something along this:

```
Format errors: 97430
Syntax errors: 268473
```

Validating UPOS, FEATS and XPOS:

```
python ../hr500k/check_xpos_upos_feats.py ../hr500k/mte5-udv2.mapping reldi-normtagner-hr.conllu reldi-normtagner-hr.uposxpos.txt|sort|uniq -c
```

It should complain only about Y XPOS tags as these are not mapped automatically.

```
  39 UPOS Y UposTag=ADJ|_
  27 UPOS Y UposTag=ADV|_
 317 UPOS Y UposTag=NOUN|_
  57 UPOS Y UposTag=PROPN|_
   1 UPOS Y UposTag=VERB|_
   1 XPOS Y UposTag=INTJ|_
  35 XPOS Y UposTag=PART|_
   6 XPOS Y UposTag=X|_
```
