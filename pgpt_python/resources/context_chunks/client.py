# This file was auto-generated by Fern from our API Definition.

import typing
import urllib.parse
from json.decoder import JSONDecodeError

from ...core.api_error import ApiError
from ...core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ...core.jsonable_encoder import jsonable_encoder
from ...errors.unprocessable_entity_error import UnprocessableEntityError
from ...types.chunks_response import ChunksResponse
from ...types.context_filter import ContextFilter
from ...types.http_validation_error import HttpValidationError

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class ContextChunksClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def chunks_retrieval(
        self,
        *,
        text: str,
        context_filter: typing.Optional[ContextFilter] = OMIT,
        limit: typing.Optional[int] = OMIT,
        prev_next_chunks: typing.Optional[int] = OMIT,
    ) -> ChunksResponse:
        """
        Given a `text`, returns the most relevant chunks from the ingested documents.

        The returned information can be used to generate prompts that can be
        passed to `/completions` or `/chat/completions` APIs. Note: it is usually a very
        fast API, because only the Embeddings model is involved, not the LLM. The
        returned information contains the relevant chunk `text` together with the source
        `document` it is coming from. It also contains a score that can be used to
        compare different results.

        The max number of chunks to be returned is set using the `limit` param.

        Previous and next chunks (pieces of text that appear right before or after in the
        document) can be fetched by using the `prev_next_chunks` field.

        The documents being used can be filtered using the `context_filter` and passing
        the document IDs to be used. Ingested documents IDs can be found using
        `/ingest/list` endpoint. If you want all ingested documents to be used,
        remove `context_filter` altogether.

        Parameters:
            - text: str.

            - context_filter: typing.Optional[ContextFilter].

            - limit: typing.Optional[int].

            - prev_next_chunks: typing.Optional[int].
        """
        _request: typing.Dict[str, typing.Any] = {"text": text}
        if context_filter is not OMIT:
            _request["context_filter"] = context_filter
        if limit is not OMIT:
            _request["limit"] = limit
        if prev_next_chunks is not OMIT:
            _request["prev_next_chunks"] = prev_next_chunks
        _response = self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "v1/chunks"),
            json=jsonable_encoder(_request),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(ChunksResponse, _response.json())  # type: ignore
        if _response.status_code == 422:
            raise UnprocessableEntityError(pydantic.parse_obj_as(HttpValidationError, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncContextChunksClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def chunks_retrieval(
        self,
        *,
        text: str,
        context_filter: typing.Optional[ContextFilter] = OMIT,
        limit: typing.Optional[int] = OMIT,
        prev_next_chunks: typing.Optional[int] = OMIT,
    ) -> ChunksResponse:
        """
        Given a `text`, returns the most relevant chunks from the ingested documents.

        The returned information can be used to generate prompts that can be
        passed to `/completions` or `/chat/completions` APIs. Note: it is usually a very
        fast API, because only the Embeddings model is involved, not the LLM. The
        returned information contains the relevant chunk `text` together with the source
        `document` it is coming from. It also contains a score that can be used to
        compare different results.

        The max number of chunks to be returned is set using the `limit` param.

        Previous and next chunks (pieces of text that appear right before or after in the
        document) can be fetched by using the `prev_next_chunks` field.

        The documents being used can be filtered using the `context_filter` and passing
        the document IDs to be used. Ingested documents IDs can be found using
        `/ingest/list` endpoint. If you want all ingested documents to be used,
        remove `context_filter` altogether.

        Parameters:
            - text: str.

            - context_filter: typing.Optional[ContextFilter].

            - limit: typing.Optional[int].

            - prev_next_chunks: typing.Optional[int].
        """
        _request: typing.Dict[str, typing.Any] = {"text": text}
        if context_filter is not OMIT:
            _request["context_filter"] = context_filter
        if limit is not OMIT:
            _request["limit"] = limit
        if prev_next_chunks is not OMIT:
            _request["prev_next_chunks"] = prev_next_chunks
        _response = await self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "v1/chunks"),
            json=jsonable_encoder(_request),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(ChunksResponse, _response.json())  # type: ignore
        if _response.status_code == 422:
            raise UnprocessableEntityError(pydantic.parse_obj_as(HttpValidationError, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
