#
# Copyright (c) 2020-2021 NVIDIA CORPORATION & AFFILIATES.
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
from sonic_platform_base.sonic_thermal_control.thermal_condition_base import ThermalPolicyConditionBase
from sonic_platform_base.sonic_thermal_control.thermal_json_object import thermal_json_object


class FanCondition(ThermalPolicyConditionBase):
    def get_fan_info(self, thermal_info_dict):
        from .thermal_infos import FanInfo
        if FanInfo.INFO_NAME in thermal_info_dict and isinstance(thermal_info_dict[FanInfo.INFO_NAME], FanInfo):
            return thermal_info_dict[FanInfo.INFO_NAME]
        else:
            return None


@thermal_json_object('fan.any.absence')
class AnyFanAbsenceCondition(FanCondition):
    def is_match(self, thermal_info_dict):
        fan_info_obj = self.get_fan_info(thermal_info_dict)
        return len(fan_info_obj.get_absence_fans()) > 0 if fan_info_obj else False


@thermal_json_object('fan.all.absence')
class AllFanAbsenceCondition(FanCondition):
    def is_match(self, thermal_info_dict):
        fan_info_obj = self.get_fan_info(thermal_info_dict)
        return len(fan_info_obj.get_presence_fans()) == 0 if fan_info_obj else False


@thermal_json_object('fan.all.presence')
class AllFanPresenceCondition(FanCondition):
    def is_match(self, thermal_info_dict):
        fan_info_obj = self.get_fan_info(thermal_info_dict)
        return len(fan_info_obj.get_absence_fans()) == 0 if fan_info_obj else False


@thermal_json_object('fan.any.fault')
class AnyFanFaultCondition(FanCondition):
    def is_match(self, thermal_info_dict):
        fan_info_obj = self.get_fan_info(thermal_info_dict)
        return len(fan_info_obj.get_fault_fans()) > 0 if fan_info_obj else False


@thermal_json_object('fan.all.good')
class AllFanGoodCondition(FanCondition):
    def is_match(self, thermal_info_dict):
        fan_info_obj = self.get_fan_info(thermal_info_dict)
        return len(fan_info_obj.get_fault_fans()) == 0 if fan_info_obj else False


class PsuCondition(ThermalPolicyConditionBase):
    def get_psu_info(self, thermal_info_dict):
        from .thermal_infos import PsuInfo
        if PsuInfo.INFO_NAME in thermal_info_dict and isinstance(thermal_info_dict[PsuInfo.INFO_NAME], PsuInfo):
            return thermal_info_dict[PsuInfo.INFO_NAME]
        else:
            return None


@thermal_json_object('psu.any.absence')
class AnyPsuAbsenceCondition(PsuCondition):
    def is_match(self, thermal_info_dict):
        psu_info_obj = self.get_psu_info(thermal_info_dict)
        return len(psu_info_obj.get_absence_psus()) > 0 if psu_info_obj else False


@thermal_json_object('psu.all.absence')
class AllPsuAbsenceCondition(PsuCondition):
    def is_match(self, thermal_info_dict):
        psu_info_obj = self.get_psu_info(thermal_info_dict)
        return len(psu_info_obj.get_presence_psus()) == 0 if psu_info_obj else False


@thermal_json_object('psu.all.presence')
class AllPsuPresenceCondition(PsuCondition):
    def is_match(self, thermal_info_dict):
        psu_info_obj = self.get_psu_info(thermal_info_dict)
        return len(psu_info_obj.get_absence_psus()) == 0 if psu_info_obj else False
