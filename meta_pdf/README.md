meta_pdf.py
================

This module parses and collects metadata from PDF files. It uses peepdf for PDF parsing.

Users have the option to specify force and loose mode for peepdf parsing in the dispatch.yara file (by default, both modes are set to True). Peepdf can be accessed here: https://github.com/jesparza/peepdf

Sample output
```
"META_PDF": {
  "Size": "4293677",
  "Encryption Algorithms": [],
  "File": "tmp5jHjF8",
  "Updates": "1",
  "Streams": "31",
  "Binary": "True",
  "Errors": [],
  "Versions": [
   {
     "Events": "None",
     "Objects with JS code": "None",
     "Encoded": "None",
     "URLs": "None",
     "Elements": "None",
     "Streams": [
       "0",
       []
     ],
     "Objects": [
       "1",
       [
         37
       ]
     ],
     "Info": "36",
     "Xref Streams": "None",
     "Errors": "None",
     "Compressed Objects": "None",
     "Object Streams": "None",
     "Vulns": "None",
     "Actions": "None",
     "Catalog": "38"
   },
   {
     "Events": {
       "/Names": [
         38,
         14
       ]
     },
     "Objects with JS code": "None",
     "Encoded": [
       "30",
      [
        84,
        54,
        57,
        59,
        61,
        63,
        64,
        66,
        67,
        70,
        71,
        72,
        73,
        74,
        75,
        76,
        77,
        78,
        79,
        80,
        81,
        82,
        3,
        4,
        5,
        6,
        7,
        9,
        20,
        34
      ]
    ],
    "Decoding Errors": "None",
    "URLs": "None",
    "Elements": {
     "/EmbeddedFile": [
       9
     ],
     "/EmbeddedFiles": [
       39
     ]
    },
    "Streams": [
     "31",
     [
       84,
       54,
       57,
       59,
       61,
       63,
       64,
       66,
       67,
       70,
       71,
       72,
       73,
       74,
       75,
       76,
       77,
       78,
       79,
       80,
       81,
       82,
       3,
       4,
       5,
       6,
       7,
       9,
       17,
       20,
       34
     ]
    ],
    "Objects": [
     "83",
     [
       1,
       2,
       ...
       83,
       84
     ]
    ],
    "Info": "None",
    "Xref Streams": "None",
    "Errors": "None",
    "Compressed Objects": "None",
    "Object Streams": "None",
    "Vulns": "None",
    "Actions": "None",
    "Catalog": "None"
    }
    ],
    "Encrypted": "False",
    "Objects": "84",
    "Comments": "0",
    "Linearized": "True",
    "Version": "1.3"
    },
```

Installation
---
* Mkdir pypackages in directory laikaboss/laikaboss/modules
* Create empty \__init__.py file in directory laikaboss/laikaboss/modules/pypackages
* Git clone peepdf in directory laikaboss/laikaboss/modules/pypackages
* Create empty \__init__.py file in directory laikaboss/laikaboss/modules/pypackages/peepdf
* Put meta_pdf.py in directory laikaboss/laikaboss/modules
* Modify dispatch.yara to include the module
```
rule type_is_pdf
{
    meta:
        scan_modules = "META_PDF(loose=True,force=True)"
        file_type = "pdf"
    strings:
        $pdf1 = { 25 50 44 46 2d ?? 2e } // %PDF-.(dot)
        $pdf2 = { 25 50 44 46 2d }
    condition:

        ($pdf1 in (0 .. 1024) or $pdf2 at 0) and not (type_is_zip or
                                                      type_is_msoffice2007 or
                                                      type_is_tar or
                                                      type_is_rar)
}
```
