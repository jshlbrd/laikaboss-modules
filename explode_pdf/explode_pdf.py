# Copyright 2015 Josh Liburdi
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
from laikaboss.objectmodel import ModuleObject, ExternalVars, QuitScanException, GlobalScanTimeoutError, GlobalModuleTimeoutError
from laikaboss import config
import tempfile
import os
from .pypackages.peepdf.PDFCore import PDFParser

class EXPLODE_PDF(SI_MODULE):
    def __init__(self,):
        self.module_name = "EXPLODE_PDF"
        self.TEMP_DIR = '/tmp/laikaboss_tmp'
        if hasattr(config, 'tempdir'):
                self.TEMP_DIR = config.tempdir.rstrip('/')
        if not os.path.isdir(self.TEMP_DIR):
                os.mkdir(self.TEMP_DIR)
                os.chmod(self.TEMP_DIR, 0777)

    def _run(self, scanObject, result, depth, args):
        moduleResult = []
        metaDict = {}

        if 'force' in args:
            force_mode = bool(args['force'])
        else:
            force_mode = True

        if 'loose' in args:
            loose_mode = bool(args['loose'])
        else:
            loose_mode = True

        with tempfile.NamedTemporaryFile(dir=self.TEMP_DIR) as temp_file:
            temp_file_name = temp_file.name
            temp_file.write(scanObject.buffer)
            temp_file.flush()

            try:
                pdfparser = PDFParser()
                ret,pdf = pdfparser.parse(temp_file_name, force_mode, loose_mode)

                # List of objects to explode.
                explode_objects = []

                for versions in pdf.getStats()['Versions']:
                    if versions['Objects with JS code'] != None:
                        # The list of JS code object references is always the second value in this list.
                        explode_objects += versions['Objects with JS code'][1]
                    if versions['Elements'] != None:
                        # The list of Elements contains multiple object references.
                        elements_list = ['/EmbeddedFile','/EmbeddedFiles','/Flash']
                        for key,val in versions['Elements'].iteritems():
                            if key in elements_list:
                                explode_objects += val

                for object_id in explode_objects:
                    name = 'stream_' + str(object_id)
                    pdf_object = pdf.getObject(object_id,None)
                    if pdf_object.getType() == 'stream':
                        try:
                            moduleResult.append(ModuleObject(buffer=pdf_object.getStream(), externalVars=ExternalVars(filename='e_pdf_%s' % name)))
                        except:
                            scanObject.addFlag('explode_pdf:err:explode_%s_failed' % name)
                            pass

            except (QuitScanException, GlobalScanTimeoutError, GlobalModuleTimeoutError):
            	raise

        return moduleResult
