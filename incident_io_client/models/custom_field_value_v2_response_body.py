from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.custom_field_option_v2_response_body import (
        CustomFieldOptionV2ResponseBody,
    )


T = TypeVar("T", bound="CustomFieldValueV2ResponseBody")


@attr.s(auto_attribs=True)
class CustomFieldValueV2ResponseBody:
    """
    Example:
        {'value_link': 'https://google.com/', 'value_numeric': '123.456', 'value_option': {'custom_field_id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'sort_key': 10, 'value': 'Product'},
            'value_text': 'This is my text field, I hope you like it'}

    Attributes:
        value_link (Union[Unset, str]): If the custom field type is 'link', this will contain the value assigned.
            Example: https://google.com/.
        value_numeric (Union[Unset, str]): If the custom field type is 'numeric', this will contain the value assigned.
            Example: 123.456.
        value_option (Union[Unset, CustomFieldOptionV2ResponseBody]):  Example: {'custom_field_id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'sort_key': 10, 'value': 'Product'}.
        value_text (Union[Unset, str]): If the custom field type is 'text', this will contain the value assigned.
            Example: This is my text field, I hope you like it.
    """

    value_link: Union[Unset, str] = UNSET
    value_numeric: Union[Unset, str] = UNSET
    value_option: Union[Unset, "CustomFieldOptionV2ResponseBody"] = UNSET
    value_text: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        value_link = self.value_link
        value_numeric = self.value_numeric
        value_option: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.value_option, Unset):
            value_option = self.value_option.to_dict()

        value_text = self.value_text

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if value_link is not UNSET:
            field_dict["value_link"] = value_link
        if value_numeric is not UNSET:
            field_dict["value_numeric"] = value_numeric
        if value_option is not UNSET:
            field_dict["value_option"] = value_option
        if value_text is not UNSET:
            field_dict["value_text"] = value_text

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.custom_field_option_v2_response_body import (
            CustomFieldOptionV2ResponseBody,
        )

        d = src_dict.copy()
        value_link = d.pop("value_link", UNSET)

        value_numeric = d.pop("value_numeric", UNSET)

        _value_option = d.pop("value_option", UNSET)
        value_option: Union[Unset, CustomFieldOptionV2ResponseBody]
        if isinstance(_value_option, Unset):
            value_option = UNSET
        else:
            value_option = CustomFieldOptionV2ResponseBody.from_dict(_value_option)

        value_text = d.pop("value_text", UNSET)

        custom_field_value_v2_response_body = cls(
            value_link=value_link,
            value_numeric=value_numeric,
            value_option=value_option,
            value_text=value_text,
        )

        custom_field_value_v2_response_body.additional_properties = d
        return custom_field_value_v2_response_body

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
