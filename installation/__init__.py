# -*- mode: python; encoding: utf-8 -*-
#
# Copyright 2012 Jens Lindström, Opera Software ASA
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not
# use this file except in compliance with the License.  You may obtain a copy of
# the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.  See the
# License for the specific language governing permissions and limitations under
# the License.

__doc__ = "Installation utilities."

import input
import process

import prereqs
import system
import paths
import files
import database
import config
import apache
import admin
import initd
import prefs
import git
import criticctl

modules = [prereqs,
           system,
           paths,
           files,
           database,
           config,
           apache,
           admin,
           initd,
           prefs,
           git,
           criticctl]
