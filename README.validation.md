# Results of testing the .conllup file format using the ud-tools validator

## Level 1
```
*** PASSED ***
```

## Level 2
```
[Line 6 Sent 344431071296884736.1]: [L2 Syntax invalid-deprel] Invalid DEPREL value '_'.
[Line 6 Sent 344431071296884736.1]: [L2 Syntax unknown-deprel] Unknown DEPREL label: '_'

The following 37 relations are currently permitted in language [ud]:
acl, advcl, advmod, amod, appos, aux, case, cc, ccomp, clf, compound, conj, cop, csubj, dep, det, discourse, dislocated, expl, fixed, flat, goeswith, iobj, list, mark, nmod, nsubj, nummod, obj, obl, orphan, parataxis, punct, reparandum, root, vocative, xcomp
If a language needs a relation subtype that is not documented in the universal guidelines, the relation
must have a language-specific documentation page in a prescribed format.
See https://universaldependencies.org/contributing_language_specific.html for further guidelines.
Documented dependency relations can be specifically turned on/off for each language in which they are used.
See https://quest.ms.mff.cuni.cz/udvalidator/cgi-bin/unidep/langspec/specify_deprel.pl for details.

[Line 7 Sent 344431071296884736.1]: [L2 Syntax invalid-deprel] Invalid DEPREL value '_'.
[Line 7 Sent 344431071296884736.1]: [L2 Syntax unknown-deprel] Unknown DEPREL label: '_'
[Line 8 Sent 344431071296884736.1]: [L2 Syntax invalid-deprel] Invalid DEPREL value '_'.
[Line 8 Sent 344431071296884736.1]: [L2 Syntax unknown-deprel] Unknown DEPREL label: '_'
[Line 9 Sent 344431071296884736.1]: [L2 Syntax invalid-deprel] Invalid DEPREL value '_'.
[Line 9 Sent 344431071296884736.1]: [L2 Syntax unknown-deprel] Unknown DEPREL label: '_'
[Line 10 Sent 344431071296884736.1]: [L2 Syntax invalid-deprel] Invalid DEPREL value '_'.
[Line 10 Sent 344431071296884736.1]: [L2 Syntax unknown-deprel] Unknown DEPREL label: '_'
[Line 11 Sent 344431071296884736.1]: [L2 Syntax invalid-deprel] Invalid DEPREL value '_'.
[Line 11 Sent 344431071296884736.1]: [L2 Syntax unknown-deprel] Unknown DEPREL label: '_'
[Line 12 Sent 344431071296884736.1]: [L2 Syntax invalid-deprel] Invalid DEPREL value '_'.
[Line 12 Sent 344431071296884736.1]: [L2 Syntax unknown-deprel] Unknown DEPREL label: '_'
[Line 13 Sent 344431071296884736.1]: [L2 Syntax invalid-deprel] Invalid DEPREL value '_'.
[Line 13 Sent 344431071296884736.1]: [L2 Syntax unknown-deprel] Unknown DEPREL label: '_'
[Line 14 Sent 344431071296884736.1]: [L2 Syntax invalid-deprel] Invalid DEPREL value '_'.
[Line 14 Sent 344431071296884736.1]: [L2 Syntax unknown-deprel] Unknown DEPREL label: '_'
[Line 15 Sent 344431071296884736.1]: [L2 Format invalid-head] Invalid HEAD: '_'.
[Line 15 Sent 344431071296884736.1]: [L2 Syntax unknown-head] Undefined HEAD (no such ID): '_'.
[Line 15 Sent 344431071296884736.1]: [L2 Format invalid-head] Invalid HEAD: '_'.
...suppressing further errors regarding Syntax
[Line 15 Sent 344431071296884736.1]: [L2 Format invalid-head] Invalid HEAD: '_'.
[Line 15 Sent 344431071296884736.1]: [L2 Format invalid-head] Invalid HEAD: '_'.
[Line 15 Sent 344431071296884736.1]: [L2 Format invalid-head] Invalid HEAD: '_'.
[Line 15 Sent 344431071296884736.1]: [L2 Format invalid-head] Invalid HEAD: '_'.
[Line 15 Sent 344431071296884736.1]: [L2 Format invalid-head] Invalid HEAD: '_'.
[Line 15 Sent 344431071296884736.1]: [L2 Format invalid-head] Invalid HEAD: '_'.
[Line 15 Sent 344431071296884736.1]: [L2 Format invalid-head] Invalid HEAD: '_'.
[Tree number 1 on line 6 Sent 344431071296884736.1]: [L2 Format skipped-corrupt-tree] Skipping annotation tests because of corrupt tree structure.
[Line 23 Sent 344431071296884736.2]: [L2 Format invalid-head] Invalid HEAD: '_'.
[Line 23 Sent 344431071296884736.2]: [L2 Format invalid-head] Invalid HEAD: '_'.
[Line 23 Sent 344431071296884736.2]: [L2 Format invalid-head] Invalid HEAD: '_'.
[Line 23 Sent 344431071296884736.2]: [L2 Format invalid-head] Invalid HEAD: '_'.
[Line 23 Sent 344431071296884736.2]: [L2 Format invalid-head] Invalid HEAD: '_'.
[Tree number 2 on line 18 Sent 344431071296884736.2]: [L2 Format skipped-corrupt-tree] Skipping annotation tests because of corrupt tree structure.
[Line 29 Sent 344431071296884736.3]: [L2 Format invalid-head] Invalid HEAD: '_'.
[Line 29 Sent 344431071296884736.3]: [L2 Format invalid-head] Invalid HEAD: '_'.
[Line 29 Sent 344431071296884736.3]: [L2 Format invalid-head] Invalid HEAD: '_'.
...suppressing further errors regarding Format
Format errors: 97470
Syntax errors: 268593
*** FAILED *** with 366063 errors
```

# Results of testing the UPOS-XPOS correspondence using reldi-data validator (aggregated results)

```
    111 UPOS _ UposTag=X|_
     39 UPOS Y UposTag=ADJ|_
     27 UPOS Y UposTag=ADV|_
      1 UPOS Y UposTag=INTJ|_
    317 UPOS Y UposTag=NOUN|_
     35 UPOS Y UposTag=PART|_
     57 UPOS Y UposTag=PROPN|_
      1 UPOS Y UposTag=VERB|_
      6 UPOS Y UposTag=X|_
```
