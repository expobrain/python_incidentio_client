from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.incident_updates_v2_list_response_body import (
    IncidentUpdatesV2ListResponseBody,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    incident_id: Union[Unset, None, str] = UNSET,
    page_size: Union[Unset, None, int] = 25,
    after: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = f"{client.base_url}/v2/incident_updates"

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["incident_id"] = incident_id

    params["page_size"] = page_size

    params["after"] = after

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[IncidentUpdatesV2ListResponseBody]:
    if response.status_code == HTTPStatus.OK:
        response_200 = IncidentUpdatesV2ListResponseBody.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[IncidentUpdatesV2ListResponseBody]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    incident_id: Union[Unset, None, str] = UNSET,
    page_size: Union[Unset, None, int] = 25,
    after: Union[Unset, None, str] = UNSET,
) -> Response[IncidentUpdatesV2ListResponseBody]:
    """List Incident Updates V2

     List all incident updates for an organisation, or for a specific incident.

    Args:
        incident_id (Union[Unset, None, str]):
        page_size (Union[Unset, None, int]):  Default: 25.
        after (Union[Unset, None, str]):

    Returns:
        Response[IncidentUpdatesV2ListResponseBody]
    """

    kwargs = _get_kwargs(
        client=client,
        incident_id=incident_id,
        page_size=page_size,
        after=after,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    incident_id: Union[Unset, None, str] = UNSET,
    page_size: Union[Unset, None, int] = 25,
    after: Union[Unset, None, str] = UNSET,
) -> Optional[IncidentUpdatesV2ListResponseBody]:
    """List Incident Updates V2

     List all incident updates for an organisation, or for a specific incident.

    Args:
        incident_id (Union[Unset, None, str]):
        page_size (Union[Unset, None, int]):  Default: 25.
        after (Union[Unset, None, str]):

    Returns:
        Response[IncidentUpdatesV2ListResponseBody]
    """

    return sync_detailed(
        client=client,
        incident_id=incident_id,
        page_size=page_size,
        after=after,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    incident_id: Union[Unset, None, str] = UNSET,
    page_size: Union[Unset, None, int] = 25,
    after: Union[Unset, None, str] = UNSET,
) -> Response[IncidentUpdatesV2ListResponseBody]:
    """List Incident Updates V2

     List all incident updates for an organisation, or for a specific incident.

    Args:
        incident_id (Union[Unset, None, str]):
        page_size (Union[Unset, None, int]):  Default: 25.
        after (Union[Unset, None, str]):

    Returns:
        Response[IncidentUpdatesV2ListResponseBody]
    """

    kwargs = _get_kwargs(
        client=client,
        incident_id=incident_id,
        page_size=page_size,
        after=after,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    incident_id: Union[Unset, None, str] = UNSET,
    page_size: Union[Unset, None, int] = 25,
    after: Union[Unset, None, str] = UNSET,
) -> Optional[IncidentUpdatesV2ListResponseBody]:
    """List Incident Updates V2

     List all incident updates for an organisation, or for a specific incident.

    Args:
        incident_id (Union[Unset, None, str]):
        page_size (Union[Unset, None, int]):  Default: 25.
        after (Union[Unset, None, str]):

    Returns:
        Response[IncidentUpdatesV2ListResponseBody]
    """

    return (
        await asyncio_detailed(
            client=client,
            incident_id=incident_id,
            page_size=page_size,
            after=after,
        )
    ).parsed