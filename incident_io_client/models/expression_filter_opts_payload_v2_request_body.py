from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.condition_group_payload_v2_request_body import (
        ConditionGroupPayloadV2RequestBody,
    )


T = TypeVar("T", bound="ExpressionFilterOptsPayloadV2RequestBody")


@_attrs_define
class ExpressionFilterOptsPayloadV2RequestBody:
    """
    Example:
        {'condition_groups': [{'conditions': [{'operation': 'one_of', 'param_bindings': [{'array_value': [{'literal':
            'SEV123', 'reference': 'incident.severity'}], 'value': {'literal': 'SEV123', 'reference':
            'incident.severity'}}], 'subject': 'incident.severity'}]}]}

    Attributes:
        condition_groups (List['ConditionGroupPayloadV2RequestBody']): The conditions to apply to this filter Example:
            [{'conditions': [{'operation': 'one_of', 'param_bindings': [{'array_value': [{'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}], 'subject':
            'incident.severity'}]}].
    """

    condition_groups: List["ConditionGroupPayloadV2RequestBody"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        condition_groups = []
        for condition_groups_item_data in self.condition_groups:
            condition_groups_item = condition_groups_item_data.to_dict()
            condition_groups.append(condition_groups_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "condition_groups": condition_groups,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.condition_group_payload_v2_request_body import (
            ConditionGroupPayloadV2RequestBody,
        )

        d = src_dict.copy()
        condition_groups = []
        _condition_groups = d.pop("condition_groups")
        for condition_groups_item_data in _condition_groups:
            condition_groups_item = ConditionGroupPayloadV2RequestBody.from_dict(
                condition_groups_item_data
            )

            condition_groups.append(condition_groups_item)

        expression_filter_opts_payload_v2_request_body = cls(
            condition_groups=condition_groups,
        )

        expression_filter_opts_payload_v2_request_body.additional_properties = d
        return expression_filter_opts_payload_v2_request_body

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
