/*
 * SPDX-FileCopyrightText: 2026 Fedora DDE port
 * SPDX-License-Identifier: GPL-3.0-or-later
 *
 * Build-time compatibility header for OpenSSL 4.
 *
 * Fedora 45's OpenSSL 4 headers still declare EVP_sm3(), but libcrypto 4
 * no longer exports the symbol.  Map the call to the provider-backed digest
 * lookup so unmodified DDE sources compile against Fedora's OpenSSL.
 *
 * This header deliberately does not include <openssl/evp.h>; it is used with
 * -include before the source's own includes and only needs the opaque type
 * and the digest lookup prototype.
 */
#ifndef OPENSSL_SM3_COMPAT_H
#define OPENSSL_SM3_COMPAT_H

#ifdef __cplusplus
extern "C" {
#endif

struct evp_md_st;
const struct evp_md_st *EVP_get_digestbyname(const char *name);

#ifdef __cplusplus
}
#endif

#ifndef EVP_sm3
#define EVP_sm3() EVP_get_digestbyname("SM3")
#endif

#endif /* OPENSSL_SM3_COMPAT_H */
