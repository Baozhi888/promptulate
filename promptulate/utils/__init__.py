# Copyright (c) 2023 promptulate
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
# Copyright Owner: Zeeland
# GitHub Link: https://github.com/Undertone0809/
# Project Link: https://github.com/Undertone0809/promptulate
# Contact Email: zeeland@foxmail.com

from promptulate.utils.color_print import print_text
from promptulate.utils.core_utils import (
    get_default_storage_path,
    get_cache,
    generate_conversation_id,
)
from promptulate.utils.logger import get_logger, enable_log, enable_log_no_file
from promptulate.utils.openai_key_pool import export_openai_key_pool
from promptulate.utils.proxy import set_proxy_mode
from promptulate.utils.singleton import Singleton, AbstractSingleton
from promptulate.utils.string_template import StringTemplate

__all__ = [
    "generate_conversation_id",
    "set_proxy_mode",
    "get_logger",
    "enable_log",
    "enable_log_no_file",
    "get_cache",
    "get_default_storage_path",
    "Singleton",
    "AbstractSingleton",
    "export_openai_key_pool",
    "StringTemplate",
    "print_text",
]
