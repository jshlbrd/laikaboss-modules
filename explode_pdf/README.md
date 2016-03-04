explode_pdf.py
================

This module explodes PDF files and extracts any streams within the file. It uses pdfminer for stream extraction.

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
* Install pdfminer (https://github.com/euske/pdfminer)
* Put explode_pdf.py in directory laikaboss/laikaboss/modules
* Modify dispatch.yara to include the module
```
rule type_is_pdf
{
    meta:
        scan_modules = "EXPLODE_PDF"
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
