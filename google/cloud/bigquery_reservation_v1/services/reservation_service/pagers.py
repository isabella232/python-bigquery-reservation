# -*- coding: utf-8 -*-

# Copyright 2020 Google LLC
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

from typing import Any, AsyncIterable, Awaitable, Callable, Iterable, Sequence, Tuple

from google.cloud.bigquery_reservation_v1.types import reservation


class ListReservationsPager:
    """A pager for iterating through ``list_reservations`` requests.

    This class thinly wraps an initial
    :class:`~.reservation.ListReservationsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``reservations`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListReservations`` requests and continue to iterate
    through the ``reservations`` field on the
    corresponding responses.

    All the usual :class:`~.reservation.ListReservationsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., reservation.ListReservationsResponse],
        request: reservation.ListReservationsRequest,
        response: reservation.ListReservationsResponse,
        *,
        metadata: Sequence[Tuple[str, str]] = ()
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (:class:`~.reservation.ListReservationsRequest`):
                The initial request object.
            response (:class:`~.reservation.ListReservationsResponse`):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = reservation.ListReservationsRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterable[reservation.ListReservationsResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = self._method(self._request, metadata=self._metadata)
            yield self._response

    def __iter__(self) -> Iterable[reservation.Reservation]:
        for page in self.pages:
            yield from page.reservations

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListReservationsAsyncPager:
    """A pager for iterating through ``list_reservations`` requests.

    This class thinly wraps an initial
    :class:`~.reservation.ListReservationsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``reservations`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListReservations`` requests and continue to iterate
    through the ``reservations`` field on the
    corresponding responses.

    All the usual :class:`~.reservation.ListReservationsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[reservation.ListReservationsResponse]],
        request: reservation.ListReservationsRequest,
        response: reservation.ListReservationsResponse,
        *,
        metadata: Sequence[Tuple[str, str]] = ()
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (:class:`~.reservation.ListReservationsRequest`):
                The initial request object.
            response (:class:`~.reservation.ListReservationsResponse`):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = reservation.ListReservationsRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterable[reservation.ListReservationsResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = await self._method(self._request, metadata=self._metadata)
            yield self._response

    def __aiter__(self) -> AsyncIterable[reservation.Reservation]:
        async def async_generator():
            async for page in self.pages:
                for response in page.reservations:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListCapacityCommitmentsPager:
    """A pager for iterating through ``list_capacity_commitments`` requests.

    This class thinly wraps an initial
    :class:`~.reservation.ListCapacityCommitmentsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``capacity_commitments`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListCapacityCommitments`` requests and continue to iterate
    through the ``capacity_commitments`` field on the
    corresponding responses.

    All the usual :class:`~.reservation.ListCapacityCommitmentsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., reservation.ListCapacityCommitmentsResponse],
        request: reservation.ListCapacityCommitmentsRequest,
        response: reservation.ListCapacityCommitmentsResponse,
        *,
        metadata: Sequence[Tuple[str, str]] = ()
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (:class:`~.reservation.ListCapacityCommitmentsRequest`):
                The initial request object.
            response (:class:`~.reservation.ListCapacityCommitmentsResponse`):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = reservation.ListCapacityCommitmentsRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterable[reservation.ListCapacityCommitmentsResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = self._method(self._request, metadata=self._metadata)
            yield self._response

    def __iter__(self) -> Iterable[reservation.CapacityCommitment]:
        for page in self.pages:
            yield from page.capacity_commitments

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListCapacityCommitmentsAsyncPager:
    """A pager for iterating through ``list_capacity_commitments`` requests.

    This class thinly wraps an initial
    :class:`~.reservation.ListCapacityCommitmentsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``capacity_commitments`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListCapacityCommitments`` requests and continue to iterate
    through the ``capacity_commitments`` field on the
    corresponding responses.

    All the usual :class:`~.reservation.ListCapacityCommitmentsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[reservation.ListCapacityCommitmentsResponse]],
        request: reservation.ListCapacityCommitmentsRequest,
        response: reservation.ListCapacityCommitmentsResponse,
        *,
        metadata: Sequence[Tuple[str, str]] = ()
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (:class:`~.reservation.ListCapacityCommitmentsRequest`):
                The initial request object.
            response (:class:`~.reservation.ListCapacityCommitmentsResponse`):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = reservation.ListCapacityCommitmentsRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterable[reservation.ListCapacityCommitmentsResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = await self._method(self._request, metadata=self._metadata)
            yield self._response

    def __aiter__(self) -> AsyncIterable[reservation.CapacityCommitment]:
        async def async_generator():
            async for page in self.pages:
                for response in page.capacity_commitments:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListAssignmentsPager:
    """A pager for iterating through ``list_assignments`` requests.

    This class thinly wraps an initial
    :class:`~.reservation.ListAssignmentsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``assignments`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListAssignments`` requests and continue to iterate
    through the ``assignments`` field on the
    corresponding responses.

    All the usual :class:`~.reservation.ListAssignmentsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., reservation.ListAssignmentsResponse],
        request: reservation.ListAssignmentsRequest,
        response: reservation.ListAssignmentsResponse,
        *,
        metadata: Sequence[Tuple[str, str]] = ()
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (:class:`~.reservation.ListAssignmentsRequest`):
                The initial request object.
            response (:class:`~.reservation.ListAssignmentsResponse`):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = reservation.ListAssignmentsRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterable[reservation.ListAssignmentsResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = self._method(self._request, metadata=self._metadata)
            yield self._response

    def __iter__(self) -> Iterable[reservation.Assignment]:
        for page in self.pages:
            yield from page.assignments

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListAssignmentsAsyncPager:
    """A pager for iterating through ``list_assignments`` requests.

    This class thinly wraps an initial
    :class:`~.reservation.ListAssignmentsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``assignments`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListAssignments`` requests and continue to iterate
    through the ``assignments`` field on the
    corresponding responses.

    All the usual :class:`~.reservation.ListAssignmentsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[reservation.ListAssignmentsResponse]],
        request: reservation.ListAssignmentsRequest,
        response: reservation.ListAssignmentsResponse,
        *,
        metadata: Sequence[Tuple[str, str]] = ()
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (:class:`~.reservation.ListAssignmentsRequest`):
                The initial request object.
            response (:class:`~.reservation.ListAssignmentsResponse`):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = reservation.ListAssignmentsRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterable[reservation.ListAssignmentsResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = await self._method(self._request, metadata=self._metadata)
            yield self._response

    def __aiter__(self) -> AsyncIterable[reservation.Assignment]:
        async def async_generator():
            async for page in self.pages:
                for response in page.assignments:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class SearchAssignmentsPager:
    """A pager for iterating through ``search_assignments`` requests.

    This class thinly wraps an initial
    :class:`~.reservation.SearchAssignmentsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``assignments`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``SearchAssignments`` requests and continue to iterate
    through the ``assignments`` field on the
    corresponding responses.

    All the usual :class:`~.reservation.SearchAssignmentsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., reservation.SearchAssignmentsResponse],
        request: reservation.SearchAssignmentsRequest,
        response: reservation.SearchAssignmentsResponse,
        *,
        metadata: Sequence[Tuple[str, str]] = ()
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (:class:`~.reservation.SearchAssignmentsRequest`):
                The initial request object.
            response (:class:`~.reservation.SearchAssignmentsResponse`):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = reservation.SearchAssignmentsRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterable[reservation.SearchAssignmentsResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = self._method(self._request, metadata=self._metadata)
            yield self._response

    def __iter__(self) -> Iterable[reservation.Assignment]:
        for page in self.pages:
            yield from page.assignments

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class SearchAssignmentsAsyncPager:
    """A pager for iterating through ``search_assignments`` requests.

    This class thinly wraps an initial
    :class:`~.reservation.SearchAssignmentsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``assignments`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``SearchAssignments`` requests and continue to iterate
    through the ``assignments`` field on the
    corresponding responses.

    All the usual :class:`~.reservation.SearchAssignmentsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[reservation.SearchAssignmentsResponse]],
        request: reservation.SearchAssignmentsRequest,
        response: reservation.SearchAssignmentsResponse,
        *,
        metadata: Sequence[Tuple[str, str]] = ()
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (:class:`~.reservation.SearchAssignmentsRequest`):
                The initial request object.
            response (:class:`~.reservation.SearchAssignmentsResponse`):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = reservation.SearchAssignmentsRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterable[reservation.SearchAssignmentsResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = await self._method(self._request, metadata=self._metadata)
            yield self._response

    def __aiter__(self) -> AsyncIterable[reservation.Assignment]:
        async def async_generator():
            async for page in self.pages:
                for response in page.assignments:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)