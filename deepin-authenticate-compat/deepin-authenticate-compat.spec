%global debug_package %{nil}

Name:           deepin-authenticate-compat
Version:        1.0.0
Release:        2%{?dist}
Summary:        OpenSSL 3 SM4 compatibility shim for Deepin authentication
License:        GPL-3.0-or-later
URL:            https://github.com/linuxdeepin/deepin-authenticate
Source0:        https://raw.githubusercontent.com/Fedora-DDE-Remix/Deepin-Desktop-Environment/refs/heads/main/deepin-authenticate-compat/sm4_compat.c
Source1:        https://raw.githubusercontent.com/Fedora-DDE-Remix/Deepin-Desktop-Environment/refs/heads/main/deepin-authenticate-compat/sm4_compat.map
Source2:        https://raw.githubusercontent.com/Fedora-DDE-Remix/Deepin-Desktop-Environment/refs/heads/main/deepin-authenticate-compat/README.md
Source3:        https://raw.githubusercontent.com/Fedora-DDE-Remix/Deepin-Desktop-Environment/refs/heads/main/deepin-authenticate-compat/LICENSE

BuildRequires:  gcc
BuildRequires:  openssl-devel
BuildRequires:  patchelf

Requires:       openssl-libs

%description
The proprietary Deepin authentication binaries import the OpenSSL 3.0
EVP_sm4_cbc and EVP_sm4_ecb helpers.  Fedora 45's OpenSSL 3 compatibility
library no longer exports them.  This package provides those two symbols on
top of the OpenSSL provider API and exports them with the OPENSSL_3.0.0
version, so the Deepin binaries can load without a global LD_PRELOAD.

%prep
%setup -q -T -c -n %{name}-%{version}
cp %{SOURCE0} sm4_compat.c
cp %{SOURCE1} sm4_compat.map
cp %{SOURCE2} README.md
cp %{SOURCE3} LICENSE

%build
gcc -O2 -fPIC -shared -o libdeepin_openssl3_compat.so sm4_compat.c \
  -Wl,--version-script=sm4_compat.map \
  -lcrypto

%install
install -Dm755 libdeepin_openssl3_compat.so \
  %{buildroot}%{_libdir}/libdeepin_openssl3_compat.so

%files
%license LICENSE
%doc README.md
%{_libdir}/libdeepin_openssl3_compat.so

%changelog
* Sun Nov 22 2026 mozixun <mozixun@fedoraproject.org> - 1.0.0-2
- Build from individual raw source URLs instead of a local tarball.

* Sat Nov 21 2026 mozixun <mozixun@fedoraproject.org> - 1.0.0-1
- Initial Fedora package.
