explode_rtf.py
================

This module explodes RTF files. It uses python-oletools.
python-oletools can be accessed here: http://www.decalage.info/python/oletools

Sample output
```
"objectSize": 3222,
"fileType": [
  "officex"
],
"level": 2,
"filename": "e_rtf_index_1900063",
"depth": 1,
"sourceModule": "EXPLODE_RTF",
"flags": [],
```

Installation
---
* Install python-oletools (http://www.decalage.info/python/oletools)
* Put explode_rtf.py in directory laikaboss/laikaboss/modules/
* Modify dispatch.yara to include the module
```
rule type_is_rtf
{
    meta:
        scan_modules = "EXPLODE_RTF"
        file_type = "rtf"
    condition:
        uint32(0) == 0x74725c7b
}
```
