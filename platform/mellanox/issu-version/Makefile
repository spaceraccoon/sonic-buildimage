#
# Copyright (c) 2019-2021 NVIDIA CORPORATION & AFFILIATES.
# Apache-2.0
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
.ONESHELL:
SHELL = /bin/bash
.SHELLFLAGS += -e

MAIN_TARGET = issu-version
BUSTER_FILES_PATH = /sonic/target/files/buster

$(addprefix $(DEST)/, $(MAIN_TARGET)): $(DEST)/% :
ifneq (,$(findstring buster,$(DEST)))
	sx_sdk --version | egrep -o 'ISSU [0-9]+' > $(DEST)/$(MAIN_TARGET) || {
		echo "ISSU version is undefined: $(sx_sdk --version)"
		rm $(DEST)/$(MAIN_TARGET)
		exit 1
	}
else
	cp $(BUSTER_FILES_PATH)/$(MAIN_TARGET) $(DEST)/$(MAIN_TARGET)
endif
