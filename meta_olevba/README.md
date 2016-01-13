meta_olevba.py
================

This module identifies VBA macro code in OLE files and parses the code. It uses olevba from python-oletools. 
python-oletools can be accessed here: http://www.decalage.info/python/oletools

Sample output (BlackEnergy .XLS Dropper 97b7577d13cf5e3bf39cbe6d3f0a7732, 01/2016)
```
    "META_OLEVBA": {
      "VBA string": "%TMP%\\vba_macro.exe - Environ(\"TMP\") & \"\\vba_macro.exe\"",
      "IOC": "vba_macro.exe - Executable file name",
      "Suspicious": [
        "Open - May open a file",
        "Shell - May run an executable file or a system command",
        "Binary - May read or write a binary file (if combined with Open)",
        "Environ - May read system environment variables",
        "Put - May write to a file (if combined with Open)",
        "Hex Strings - Hex-encoded strings were detected, may be used to obfuscate strings (option --decode to see all)",
        "VBA obfuscated Strings - VBA string expressions were detected, may be used to obfuscate strings (option --decode to see all)"
      ]
    },
```
