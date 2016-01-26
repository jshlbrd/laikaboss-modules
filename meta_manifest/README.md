meta_manifest.py
================

This module parses Java manifest files. It uses python-javatools.
python-javatools can be accessed here: https://github.com/obriencj/python-javatools

Sample output
```
"META_MANIFEST": {
  "Manifest-Version": "1.0",
  "Created-By": "1.5.0_22 (Sun Microsystems Inc.)"
}
```

Installation
---
* Install python-javatools (https://github.com/obriencj/python-javatools)
* Put meta_manifest.py in directory laikaboss/laikaboss/modules/
* Modify dispatch.yara to include the module
```
rule type_is_metainf_manifest
{
    meta:
        scan_modules = "META_MANIFEST"
    strings:
        $a = { 4d 61 6e 69 66 65 73 74 }
    condition:
        $a at 0 and ext_parentModules contains "EXPLODE_ZIP"
}
```
