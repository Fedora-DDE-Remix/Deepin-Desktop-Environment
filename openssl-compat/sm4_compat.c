// SPDX-FileCopyrightText: 2026 Fedora DDE port
// SPDX-License-Identifier: GPL-3.0-or-later
//
// OpenSSL 4 removed the legacy EVP_sm4_cbc()/EVP_sm4_ecb() helpers used by
// the proprietary Deepin authentication binaries.  Provide provider-backed
// shims with the OPENSSL_3.0.0 symbol version.

#include <openssl/evp.h>

const EVP_CIPHER *EVP_sm4_cbc(void)
{
    return EVP_CIPHER_fetch(NULL, "SM4-CBC", NULL);
}

const EVP_CIPHER *EVP_sm4_ecb(void)
{
    return EVP_CIPHER_fetch(NULL, "SM4-ECB", NULL);
}
