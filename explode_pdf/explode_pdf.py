# Copyright 2016 Josh Liburdi
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from laikaboss.si_module import SI_MODULE
from laikaboss.objectmodel import ModuleObject, ExternalVars, ScanError
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdftypes import PDFStream, PDFObjectNotFound
from pdfminer.psparser import PSEOF
import cStringIO

class EXPLODE_PDF(SI_MODULE):
    def __init__(self,):
        self.module_name = "EXPLODE_PDF"

    def _run(self, scanObject, result, depth, args):
        moduleResult = []

        pdfBuffer = cStringIO.StringIO(scanObject.buffer)

        try:
            pdf = PDFParser(pdfBuffer)
            pdfDoc = PDFDocument(pdf)

            for xref in pdfDoc.xrefs:
                for objid in xref.get_objids():
                    try:
                        obj = pdfDoc.getobj(objid)
                        if isinstance(obj, dict):
                            for (key,val) in obj.iteritems():
                                if key in ['AA','OpenAction']:
                                    scanObject.addFlag('pdf:nfo:auto_action')
                                elif key in ['JS','Javascript']:
                                    scanObject.addFlag('pdf:nfo:js_embedded')
                        if isinstance(obj, PDFStream):
                            moduleResult.append(ModuleObject(buffer=obj.get_data(), externalVars=ExternalVars(filename='e_pdf_stream_%s' % objid)))

                    except PDFObjectNotFound:
                        scanObject.addFlag('pdf:err:missing_object_%s' % objid)
                    except ScanError:
                        raise

        except PSEOF:
            scanObject.addFlag('pdf:err:unexpected_eof')
        except ScanError:
            raise

        return moduleResult
