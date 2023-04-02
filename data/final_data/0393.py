# Copyright 2017-present Open Networking Foundation
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
# Copyright (c) 2008 The Board of Trustees of The Leland Stanford Junior University
# Copyright (c) 2011, 2012 Open Networking Foundation
# Copyright (c) 2012, 2013 Big Switch Networks, Inc.
# See the file LICENSE.pyloxi which should have been included in the source distribution
# Automatically generated by LOXI from template toplevel_init.py
# Do not modify

version_names = {
    1: "1.0",
    2: "1.1",
    3: "1.2",
    4: "1.3",
    5: "1.4",
}

def protocol(ver):
    """
    Import and return the protocol module for the given wire version.
    """
    if ver == 1:
        import of10
        return of10

    if ver == 2:
        import of11
        return of11

    if ver == 3:
        import of12
        return of12

    if ver == 4:
        import of13
        return of13

    if ver == 5:
        import of14
        return of14

    raise ValueError

class ProtocolError(Exception):
    """
    Raised when failing to deserialize an invalid OpenFlow message.
    """
    pass

class Unimplemented(Exception):
    """
    Raised when an OpenFlow feature is not yet implemented in PyLoxi.
    """
    pass

def unimplemented(msg):
    raise Unimplemented(msg)

class OFObject(object):
    """
    Superclass of all OpenFlow classes
    """
    def __init__(self, *args):
        raise NotImplementedError("cannot instantiate abstract class")

    def __ne__(self, other):
        return not self.__eq__(other)

    def show(self):
        import loxi.pp
        return loxi.pp.pp(self)