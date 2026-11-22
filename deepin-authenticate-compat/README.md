# deepin-authenticate OpenSSL 3 compatibility shim

The Deepin `deepin-authenticate` binaries are built against OpenSSL 3.0 and
import the legacy `EVP_sm4_cbc` and `EVP_sm4_ecb` helpers with the
`OPENSSL_3.0.0` symbol version. Fedora 45 ships OpenSSL 4 as the system
library and `openssl3-libs` 3.5 as a compatibility library, but 3.5 no longer
exports those two SM4 helpers.

`sm4_compat.c` implements both symbols on top of the provider API
(`EVP_CIPHER_fetch`). The version script exports them as `OPENSSL_3.0.0`.
The resulting library is added as a `DT_NEEDED` entry to the proprietary
authentication binaries with `patchelf`, so it is loaded before the SM4
symbols are resolved. No global `LD_PRELOAD` is required.

The spec lists the shim sources as individual raw GitHub `SourceN` URLs, so
COPR can build it directly from the online spec without a source archive.

Build inside the Fedora build container:

```sh
gcc -O2 -fPIC -shared -o libdeepin_openssl3_compat.so sm4_compat.c \
    -Wl,--version-script=sm4_compat.map \
    -L/build/rootfs/usr/lib64 -Wl,-l:libcrypto.so.3 \
    -Wl,-rpath,/usr/lib64
```

Then install the library to `/usr/lib64` and patch the consumers:

```sh
patchelf --add-needed libdeepin_openssl3_compat.so \
    /usr/lib/deepin-authenticate/deepin-authentication
patchelf --add-needed libdeepin_openssl3_compat.so \
    /usr/lib64/security/pam_deepin_authentication.so
```
