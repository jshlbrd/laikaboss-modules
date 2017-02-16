log_json.py
================

This module writes the output of Laika results as JSON to a user-specified file. (If no user-specified file is provided, then the file is written to /tmp/laika.log.) When LB is deployed as client-server configuration, this can be used to store results on the server(s) running the laikad service.

Installation
---
* Put log_json.py in directory laikaboss/laikaboss/modules/
* Modify conditional-dispatch.yara to include the module
```
rule LOG_JSON
{
    meta:
        scan_modules = "LOG_JSON(savepath=/path/to/file.log)"
        priority = "50"
    condition:
        root_object
}
```
