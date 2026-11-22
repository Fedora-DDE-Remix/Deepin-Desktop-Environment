// SPDX-FileCopyrightText: 2026 Fedora DDE port
// SPDX-License-Identifier: GPL-3.0-or-later
//
// OpenSSL 3.5 removed the legacy EVP_sm4_cbc()/EVP_sm4_ecb() helpers
// that the proprietary Deepin authentication binaries were built against.
// Provide them as provider-backed shims so the binaries can keep using
// Fedora's OpenSSL 3 compatibility library (openssl3-libs).

#include <openssl/evp.h>

const EVP_CIPHER *EVP_sm4_cbc(void)
{
    return EVP_CIPHER_fetch(NULL, "SM4-CBC", NULL);
}

const EVP_CIPHER *EVP_sm4_ecb(void)
{
    return EVP_CIPHER_fetch(NULL, "SM4-ECB", NULL);
}
