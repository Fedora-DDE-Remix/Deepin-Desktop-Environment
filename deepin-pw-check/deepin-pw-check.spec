%global debug_package %{nil}

Name:           deepin-pw-check
Version:        6.0.13
Release:        2%{?dist}
Summary:        Password validation library and service for DDE
License:        GPL-2.0-only
URL:            https://github.com/linuxdeepin/deepin-pw-check
Source0:        %{url}/archive/%{version}/deepin-pw-check-%{version}.tar.gz
Patch0:         https://raw.githubusercontent.com/Fedora-DDE-Remix/Deepin-Desktop-Environment/refs/heads/main/deepin-pw-check/01-use-shipped-policy.patch
Patch1:         https://raw.githubusercontent.com/Fedora-DDE-Remix/Deepin-Desktop-Environment/refs/heads/main/deepin-pw-check/02-Mangle-Suit-Cracklib2.9.6.patch

BuildRequires:  gcc
BuildRequires:  golang
BuildRequires:  make
BuildRequires:  gettext
BuildRequires:  pam-devel
BuildRequires:  cracklib-devel
BuildRequires:  iniparser-devel

Requires:       cracklib
Requires:       iniparser
Requires:       polkit

%description
deepin-pw-check provides the password validation library, the PAM module and
the small D-Bus service used by the DDE account and authentication panels.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cracklib-devel
Requires:       iniparser-devel

%description    devel
This package contains development files for %{name}.

%prep
%autosetup -n deepin-pw-check-%{version} -p1

%build
export GO111MODULE=on
export GOFLAGS="-mod=mod"
export GOPATH=%{_builddir}/gopath
%make_build PREFIX=%{_prefix} libdir=/%{_lib} \
  PAM_MODULE_DIR=%{_libdir}/security \
  PKG_FILE_DIR=%{_libdir}/pkgconfig

%install
export GO111MODULE=on
export GOFLAGS="-mod=mod"
export GOPATH=%{_builddir}/gopath
%make_install PREFIX=%{_prefix} libdir=/%{_lib} \
  PAM_MODULE_DIR=%{_libdir}/security \
  PKG_FILE_DIR=%{_libdir}/pkgconfig
# The upstream Makefile installs the shared library into /usr/lib, not
# /usr/lib64.  Move it to the Fedora library directory.
mkdir -p %{buildroot}%{_libdir}
mv %{buildroot}%{_prefix}/lib/libdeepin_pw_check* %{buildroot}%{_libdir}/

%post
%systemd_post deepin-passwd-conf.service

%preun
%systemd_preun deepin-passwd-conf.service

%postun
%systemd_postun_with_restart deepin-passwd-conf.service

%files
%license LICENSE
%doc README.md
%{_bindir}/pwd-conf-update
%{_libexecdir}/deepin-pw-check/deepin-pw-check
%{_libdir}/libdeepin_pw_check.so.1*
%{_libdir}/security/pam_deepin_pw_check.so
%{_datadir}/dbus-1/system.d/
%{_datadir}/dbus-1/system-services/
%{_datadir}/polkit-1/actions/
%{_unitdir}/deepin-passwd-conf.service
%{_datadir}/locale/*/LC_MESSAGES/deepin-pw-check.mo

%files devel
%{_includedir}/deepin_pw_check.h
%{_libdir}/libdeepin_pw_check.so
%{_libdir}/libdeepin_pw_check.a
%{_libdir}/pkgconfig/libdeepin_pw_check.pc

%changelog
* Sun Nov 22 2026 mozixun <mozixun@fedoraproject.org> - 6.0.13-2
- Point GOPATH at the build directory so the Go module cache is writable.

* Sat Nov 21 2026 mozixun <mozixun@fedoraproject.org> - 6.0.13-1
- Initial Fedora package.
