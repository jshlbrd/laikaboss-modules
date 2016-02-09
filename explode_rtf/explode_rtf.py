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
from laikaboss.objectmodel import ModuleObject, ExternalVars
from laikaboss import config
import tempfile
import os
from oletools import rtfobj

class EXPLODE_RTF(SI_MODULE):
	def __init__(self,):
		self.module_name = "EXPLODE_RTF"
		self.TEMP_DIR = '/tmp/laikaboss_tmp'
		if hasattr(config, 'tempdir'):
			self.TEMP_DIR = config.tempdir.rstrip('/')
		if not os.path.isdir(self.TEMP_DIR):
			os.mkdir(self.TEMP_DIR)
			os.chmod(self.TEMP_DIR, 0777)

	def _run(self, scanObject, result, depth, args):
		moduleResult = []

		with tempfile.NamedTemporaryFile(dir=self.TEMP_DIR) as temp_file:
			temp_file_name = temp_file.name
			temp_file.write(scanObject.buffer)
			temp_file.flush()

			# rtfobj v 0.02 has two objects in the rtf iter
			if rtfobj.__version__ == str(0.02):
				for index, obj_data in rtfobj.rtf_iter_objects(temp_file_name):
					name = 'index_' + str(index)
					try:
						moduleResult.append(ModuleObject(buffer=obj_data, externalVars=ExternalVars(filename='e_rtf_%s' % name)))
					except:
						scanObject.addFlag('explode_rtf:err:explode_%s_failed' % name)
						pass

			# rtfobj v 0.03 has three objects in the rtf iter
			elif rtfobj.__version__ == str(0.03):
				for index, obj_len, obj_data in rtfobj.rtf_iter_objects(temp_file_name):
					name = 'index_' + str(index)
					try:
						moduleResult.append(ModuleObject(buffer=obj_data, externalVars=ExternalVars(filename='e_rtf_%s' % name)))
					except:
						scanObject.addFlag('explode_rtf:err:explode_%s_failed' % name)
						pass

		return moduleResult
