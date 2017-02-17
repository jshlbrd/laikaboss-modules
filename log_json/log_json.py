# Copyright 2017 Josh Liburdi
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

from laikaboss.si_module import SI_MODULE
from laikaboss.clientLib import getJSON
from laikaboss.util import get_option

class LOG_JSON(SI_MODULE):
    '''Module for writing to JSON log on Laika server'''

    def __init__(self,):
        self.module_name = "LOG_JSON"
    def _run(self, scanObject, result, depth, args):
        save_path = get_option(args, 'savepath', 'jsonsavepath', '/tmp/laika.log')
        with open(save_path,"ab") as json_out:
            json_out.write(getJSON(result) + "\n")
