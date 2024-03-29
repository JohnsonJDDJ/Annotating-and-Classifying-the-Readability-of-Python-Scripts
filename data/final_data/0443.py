# This file is dual licensed under the terms of the Apache License, Version
# 2.0, and the BSD License. See the LICENSE file in the root of this repository
# for complete details.


import typing

from cryptography.hazmat.primitives.asymmetric import dh
from cryptography.hazmat.primitives.asymmetric.types import (
    PRIVATE_KEY_TYPES,
    PUBLIC_KEY_TYPES,
)


def load_pem_private_key(
    data: bytes,
    password: typing.Optional[bytes],
    backend: typing.Any = None,
    *,
    unsafe_skip_rsa_key_validation: bool = False,
) -> PRIVATE_KEY_TYPES:
    from cryptography.hazmat.backends.openssl.backend import backend as ossl

    return ossl.load_pem_private_key(
        data, password, unsafe_skip_rsa_key_validation
    )


def load_pem_public_key(
    data: bytes, backend: typing.Any = None
) -> PUBLIC_KEY_TYPES:
    from cryptography.hazmat.backends.openssl.backend import backend as ossl

    return ossl.load_pem_public_key(data)


def load_pem_parameters(
    data: bytes, backend: typing.Any = None
) -> "dh.DHParameters":
    from cryptography.hazmat.backends.openssl.backend import backend as ossl

    return ossl.load_pem_parameters(data)


def load_der_private_key(
    data: bytes,
    password: typing.Optional[bytes],
    backend: typing.Any = None,
    *,
    unsafe_skip_rsa_key_validation: bool = False,
) -> PRIVATE_KEY_TYPES:
    from cryptography.hazmat.backends.openssl.backend import backend as ossl

    return ossl.load_der_private_key(
        data, password, unsafe_skip_rsa_key_validation
    )


def load_der_public_key(
    data: bytes, backend: typing.Any = None
) -> PUBLIC_KEY_TYPES:
    from cryptography.hazmat.backends.openssl.backend import backend as ossl

    return ossl.load_der_public_key(data)


def load_der_parameters(
    data: bytes, backend: typing.Any = None
) -> "dh.DHParameters":
    from cryptography.hazmat.backends.openssl.backend import backend as ossl

    return ossl.load_der_parameters(data)