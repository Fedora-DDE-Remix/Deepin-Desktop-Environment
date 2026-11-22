%global debug_package %{nil}

Name:           openssl-compat
Version:        1.0.0
Release:        2%{?dist}
Summary:        OpenSSL 3 SM3/SM4 compatibility shims for Fedora
License:        GPL-3.0-or-later
URL:            https://github.com/linuxdeepin/dde-file-manager
Source0:        https://raw.githubusercontent.com/Fedora-DDE-Remix/Deepin-Desktop-Environment/refs/heads/main/openssl-compat/sm3_compat.c
Source1:        https://raw.githubusercontent.com/Fedora-DDE-Remix/Deepin-Desktop-Environment/refs/heads/main/openssl-compat/sm4_compat.c
Source2:        https://raw.githubusercontent.com/Fedora-DDE-Remix/Deepin-Desktop-Environment/refs/heads/main/openssl-compat/openssl-compat.map
Source3:        https://raw.githubusercontent.com/Fedora-DDE-Remix/Deepin-Desktop-Environment/refs/heads/main/openssl-compat/openssl-sm3-compat.h
Source4:        https://raw.githubusercontent.com/Fedora-DDE-Remix/Deepin-Desktop-Environment/refs/heads/main/openssl-compat/LICENSE
Source5:        https://raw.githubusercontent.com/Fedora-DDE-Remix/Deepin-Desktop-Environment/refs/heads/main/openssl-compat/README.md

BuildRequires:  gcc
BuildRequires:  openssl-devel
BuildRequires:  make

%description
Fedora 45's OpenSSL 4 no longer exports the OpenSSL 3 SM3/SM4 helper
functions.  This package provides provider-backed compatibility symbols so
unmodified DDE components and the proprietary Deepin authentication binaries
can build and run against Fedora's OpenSSL.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package contains the build-time SM3 compatibility header.

%prep
%setup -q -T -c -n %{name}-%{version}
cp %{SOURCE0} sm3_compat.c
cp %{SOURCE1} sm4_compat.c
cp %{SOURCE2} openssl-compat.map
cp %{SOURCE3} openssl-sm3-compat.h
cp %{SOURCE4} LICENSE
cp %{SOURCE5} README.md

%build
gcc -O2 -fPIC -shared -Wl,-soname,libopenssl_compat.so.0 \
  -Wl,--version-script=openssl-compat.map \
  -o libopenssl_compat.so.0.0.0 \
  sm3_compat.c sm4_compat.c -lcrypto
ln -sf libopenssl_compat.so.0.0.0 libopenssl_compat.so.0
ln -sf libopenssl_compat.so.0 libopenssl_compat.so

%install
install -d %{buildroot}%{_libdir} %{buildroot}%{_includedir}/openssl-compat
install -m755 libopenssl_compat.so.0.0.0 %{buildroot}%{_libdir}/
ln -sf libopenssl_compat.so.0.0.0 %{buildroot}%{_libdir}/libopenssl_compat.so.0
ln -sf libopenssl_compat.so.0 %{buildroot}%{_libdir}/libopenssl_compat.so
install -m644 openssl-sm3-compat.h %{buildroot}%{_includedir}/openssl-compat/

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%license LICENSE
%{_libdir}/libopenssl_compat.so.0*

%files devel
%{_includedir}/openssl-compat/openssl-sm3-compat.h
%{_libdir}/libopenssl_compat.so

%changelog
* Sun Nov 22 2026 mozixun <mozixun@fedoraproject.org> - 1.0.0-2
- Build from individual raw source URLs instead of a local tarball.

* Sat Nov 21 2026 mozixun <mozixun@fedoraproject.org> - 1.0.0-1
- Initial Fedora package.
