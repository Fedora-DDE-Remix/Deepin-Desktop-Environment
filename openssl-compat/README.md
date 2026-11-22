OpenSSL 3/4 SM3 and SM4 compatibility shims
==========================================

Fedora 45 ships OpenSSL 4.  Its headers still declare the OpenSSL 3 SM3/SM4
helpers, but libcrypto 4 no longer exports:

- `EVP_sm3()`
- `EVP_sm4_cbc()`
- `EVP_sm4_ecb()`

This package provides:

- `libopenssl_compat.so.0` exporting the three symbols with the
  `OPENSSL_3.0.0` symbol version, implemented with the OpenSSL provider API.
- `openssl-sm3-compat.h`, a build-time header that maps `EVP_sm3()` to
  `EVP_get_digestbyname("SM3")` without changing DDE source.

`util-dfm` builds with `-include openssl-sm3-compat.h`; the proprietary
`deepin-authenticate` binaries can load `libopenssl_compat.so.0` through
`patchelf --add-needed`.

COPR builds this package directly from the online spec.  The spec lists each
file as an individual raw GitHub `SourceN` URL, so no local source archive is
needed.
