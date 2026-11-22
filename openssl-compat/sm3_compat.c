// SPDX-FileCopyrightText: 2026 Fedora DDE port
// SPDX-License-Identifier: GPL-3.0-or-later
//
// Fedora 45's OpenSSL 4 libcrypto no longer exports the legacy EVP_sm3()
// helper.  Provide a provider-backed shim with the OPENSSL_3.0.0 symbol
// version so binaries built against OpenSSL 3 keep working.

#include <openssl/evp.h>

const EVP_MD *EVP_sm3(void)
{
    return EVP_get_digestbyname("SM3");
}
