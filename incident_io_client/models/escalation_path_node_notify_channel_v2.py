from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.escalation_path_node_notify_channel_v2_time_to_ack_interval_condition import (
    EscalationPathNodeNotifyChannelV2TimeToAckIntervalCondition,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.escalation_path_target_v2 import EscalationPathTargetV2


T = TypeVar("T", bound="EscalationPathNodeNotifyChannelV2")


@_attrs_define
class EscalationPathNodeNotifyChannelV2:
    """
    Example:
        {'targets': [{'id': 'lawrencejones', 'schedule_mode': 'currently_on_call', 'type': 'user', 'urgency': 'high'}],
            'time_to_ack_interval_condition': 'active', 'time_to_ack_seconds': 1800,
            'time_to_ack_weekday_interval_config_id': '01FCNDV6P870EA6S7TK1DSYDG0'}

    Attributes:
        targets (List['EscalationPathTargetV2']): The targets for this level Example: [{'id': 'lawrencejones',
            'schedule_mode': 'currently_on_call', 'type': 'user', 'urgency': 'high'}].
        time_to_ack_interval_condition (Union[Unset, EscalationPathNodeNotifyChannelV2TimeToAckIntervalCondition]): If
            the time to ack is relative to a time window, this defines whether we move when the window is active or inactive
            Example: active.
        time_to_ack_seconds (Union[Unset, int]): How long should we wait for this level to acknowledge before
            escalating? Example: 1800.
        time_to_ack_weekday_interval_config_id (Union[Unset, str]): If the time to ack is relative to a time window,
            this identifies which window it is relative to Example: 01FCNDV6P870EA6S7TK1DSYDG0.
    """

    targets: List["EscalationPathTargetV2"]
    time_to_ack_interval_condition: Union[
        Unset, EscalationPathNodeNotifyChannelV2TimeToAckIntervalCondition
    ] = UNSET
    time_to_ack_seconds: Union[Unset, int] = UNSET
    time_to_ack_weekday_interval_config_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        targets = []
        for targets_item_data in self.targets:
            targets_item = targets_item_data.to_dict()
            targets.append(targets_item)

        time_to_ack_interval_condition: Union[Unset, str] = UNSET
        if not isinstance(self.time_to_ack_interval_condition, Unset):
            time_to_ack_interval_condition = self.time_to_ack_interval_condition.value

        time_to_ack_seconds = self.time_to_ack_seconds

        time_to_ack_weekday_interval_config_id = (
            self.time_to_ack_weekday_interval_config_id
        )

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "targets": targets,
            }
        )
        if time_to_ack_interval_condition is not UNSET:
            field_dict[
                "time_to_ack_interval_condition"
            ] = time_to_ack_interval_condition
        if time_to_ack_seconds is not UNSET:
            field_dict["time_to_ack_seconds"] = time_to_ack_seconds
        if time_to_ack_weekday_interval_config_id is not UNSET:
            field_dict[
                "time_to_ack_weekday_interval_config_id"
            ] = time_to_ack_weekday_interval_config_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.escalation_path_target_v2 import EscalationPathTargetV2

        d = src_dict.copy()
        targets = []
        _targets = d.pop("targets")
        for targets_item_data in _targets:
            targets_item = EscalationPathTargetV2.from_dict(targets_item_data)

            targets.append(targets_item)

        _time_to_ack_interval_condition = d.pop("time_to_ack_interval_condition", UNSET)
        time_to_ack_interval_condition: Union[
            Unset, EscalationPathNodeNotifyChannelV2TimeToAckIntervalCondition
        ]
        if isinstance(_time_to_ack_interval_condition, Unset):
            time_to_ack_interval_condition = UNSET
        else:
            time_to_ack_interval_condition = (
                EscalationPathNodeNotifyChannelV2TimeToAckIntervalCondition(
                    _time_to_ack_interval_condition
                )
            )

        time_to_ack_seconds = d.pop("time_to_ack_seconds", UNSET)

        time_to_ack_weekday_interval_config_id = d.pop(
            "time_to_ack_weekday_interval_config_id", UNSET
        )

        escalation_path_node_notify_channel_v2 = cls(
            targets=targets,
            time_to_ack_interval_condition=time_to_ack_interval_condition,
            time_to_ack_seconds=time_to_ack_seconds,
            time_to_ack_weekday_interval_config_id=time_to_ack_weekday_interval_config_id,
        )

        escalation_path_node_notify_channel_v2.additional_properties = d
        return escalation_path_node_notify_channel_v2

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
