Name:           dde-api-selinux
Version:        1.0.0
Release:        1%{?dist}
Summary:        SELinux policy for dde-api helper services
License:        GPL-2.0-or-later
URL:            https://github.com/Fedora-DDE-Remix/Deepin-Desktop-Environment
Source0:        https://raw.githubusercontent.com/Fedora-DDE-Remix/Deepin-Desktop-Environment/refs/heads/main/dde-api-selinux/dde_api.te
Source1:        https://raw.githubusercontent.com/Fedora-DDE-Remix/Deepin-Desktop-Environment/refs/heads/main/dde-api-selinux/dde_api.fc
BuildArch:      noarch
BuildRequires:  selinux-policy-devel

Requires:       dde-api
Requires:       selinux-policy-targeted
Requires:       policycoreutils

%description
This package provides the SELinux policy used by dde-api.  It marks the
helper executables in /usr/lib/deepin-api as bin_t so systemd starts them in
unconfined_service_t instead of leaving them in init_t.

%prep
mkdir -p %{name}-%{version}
cp %{SOURCE0} %{name}-%{version}/dde_api.te
cp %{SOURCE1} %{name}-%{version}/dde_api.fc

%build
cd %{name}-%{version}
make -f /usr/share/selinux/devel/Makefile dde_api.pp

%install
install -Dm644 %{name}-%{version}/dde_api.pp %{buildroot}%{_datadir}/selinux/packages/dde_api.pp

%post
if [ -x /usr/sbin/semodule ]; then
    /usr/sbin/semodule -i /usr/share/selinux/packages/dde_api.pp 2>/dev/null || :
fi
[ -e /usr/lib/deepin-api ] && /usr/sbin/restorecon -R /usr/lib/deepin-api 2>/dev/null || :

%posttrans
[ -e /usr/lib/deepin-api ] && /usr/sbin/restorecon -R /usr/lib/deepin-api 2>/dev/null || :

%postun
if [ "$1" -eq 0 ] && [ -x /usr/sbin/semodule ]; then
    /usr/sbin/semodule -r dde_api 2>/dev/null || :
    [ -e /usr/lib/deepin-api ] && /usr/sbin/restorecon -R /usr/lib/deepin-api 2>/dev/null || :
fi

%files
%{_datadir}/selinux/packages/dde_api.pp

%changelog
* Mon Nov 23 2026 mozixun <mozixun@fedoraproject.org> - 1.0.0-1
- Independent SELinux policy package for dde-api.
