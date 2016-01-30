explode_pdf.py
================

This module explodes PDF files and extracts any embedded files, Flash objects, and JavaScript code within the file. It uses peepdf for PDF parsing and object extraction.

Note that extraction can add several seconds to minutes of parsing time for PDF files that contain many object streams. Users have the option to specify force and loose mode for peepdf parsing in the dispatch.yara file. Peepdf can be accessed here: https://github.com/jesparza/peepdf

Sample output
```
 "objectSize": 10402,
      "fileType": [
        "officex"
      ],
      "level": 2,
      "filename": "e_pdf_stream_1430",
      "depth": 1,
      "sourceModule": "EXPLODE_PDF",
      "flags": [],
```

Installation
---
* Mkdir pypackages in directory laikaboss/laikaboss/modules
* Create empty \__init__.py file in directory laikaboss/laikaboss/modules/pypackages
* Git clone peepdf in directory laikaboss/laikaboss/modules/pypackages
* Create empty \__init__.py file in directory laikaboss/laikaboss/modules/pypackages/peepdf
* Put explode_pdf.py in directory laikaboss/laikaboss/modules
* Modify dispatch.yara to include the module
```
rule type_is_pdf
{
    meta:
	scan_modules = "EXPLODE_PDF(loose=True,force=True)"
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
