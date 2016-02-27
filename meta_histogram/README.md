meta_histogram.py
================

This module creates a textual histogram for each scanned file. 

Sample output
```
"META_HISTOGRAM": {
          "HISTOGRAM": {
            "}": 132,
            "y": 126,
            "u": 139,
            ...
            "\u007f": 157,
            "\u0002": 116,
            "\u0006": 126
          }
        },
```

Installation
---
* Put meta_histogram.py in directory laikaboss/laikaboss/modules/
* Modify dispatch.yara to include the module (placed under General Rules)
```
rule meta_histogram
{
    meta:
        scan_modules = "META_HISTOGRAM"
    condition:
        true
}
```
