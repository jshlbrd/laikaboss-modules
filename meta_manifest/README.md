meta_java_manifest.py
================

This module parses Java manifest files. It uses python-javatools.
python-javatools can be accessed here: https://github.com/obriencj/python-javatools

Sample output
```
"META_JAVA_MANIFEST": {
          "Main-Class": "com.zero1.SandroRatClient.DroidJack",
          "Manifest-Version": "1.0",
          "Class-Path": ". DroidJack_lib/commons-codec-1.6.jar DroidJack_lib/commons-logging-1.1.1.jar DroidJack_lib/fluent-hc-4.2.5.jar DroidJack_lib/httpclient-4.2.5.jar DroidJack_lib/httpclient-cache-4.2.5.jar DroidJack_lib/httpcore-4.2.4.jar DroidJack_lib/httpmime-4.2.5.jar DroidJack_lib/sqljet-1.1.8.jar DroidJack_lib/sqlite-jdbc-3.7.2.jar DroidJack_lib/kryonet-2.21-all.jar DroidJack_lib/quaqua.jar DroidJack_lib/zip4j_1.3.2.jar DroidJack_lib/jaad-0.8.4.jar DroidJack_lib/commons-io-2.4.jar"
        }
```

Installation
---
* Install python-javatools (https://github.com/obriencj/python-javatools)
* Put meta_java_manifest.py in directory laikaboss/laikaboss/modules/
* Modify dispatch.yara to include the module
```
rule type_is_metainf_manifest
{
    meta:
        scan_modules = "META_JAVA_MANIFEST"
    strings:
        $a = { 4d 61 6e 69 66 65 73 74 }
    condition:
        $a at 0 and ext_parentModules contains "EXPLODE_ZIP"
}
```
