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
from laikaboss.objectmodel import QuitScanException, GlobalScanTimeoutError, GlobalModuleTimeoutError
from laikaboss import config
import tempfile
import os
from .pypackages.peepdf.PDFCore import PDFParser

class META_PDF(SI_MODULE):
    def __init__(self,):
        self.module_name = "META_PDF"
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

    			metaDict = pdf.getStats()

                # Unnecessary fields created by peepdf.
    			pdf_pop = ['Detection report','Detection','MD5','SHA1','SHA256']

    			for key in pdf_pop:
    				metaDict.pop(key,None)

    			for key,val in metaDict.iteritems():
    				scanObject.addMetadata(self.module_name, key, val)

    		except (QuitScanException, GlobalScanTimeoutError, GlobalModuleTimeoutError):
    			raise

        return moduleResult
