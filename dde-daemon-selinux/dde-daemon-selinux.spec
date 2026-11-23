Name:           dde-daemon-selinux
Version:        1.0.0
Release:        1%{?dist}
Summary:        SELinux policy for dde-daemon system helpers
License:        GPL-2.0-or-later
URL:            https://github.com/Fedora-DDE-Remix/Deepin-Desktop-Environment
Source0:        https://raw.githubusercontent.com/Fedora-DDE-Remix/Deepin-Desktop-Environment/refs/heads/main/dde-daemon-selinux/dde_daemon.te
Source1:        https://raw.githubusercontent.com/Fedora-DDE-Remix/Deepin-Desktop-Environment/refs/heads/main/dde-daemon-selinux/dde_daemon.fc
BuildArch:      noarch
BuildRequires:  selinux-policy-devel

Requires:       dde-daemon
Requires:       selinux-policy-targeted
Requires:       policycoreutils

%description
This package provides the SELinux policy used by dde-daemon.  It marks the
helpers in /usr/lib/deepin-daemon as bin_t and allows systemd's init_t to
perform the /etc/shadow InaccessiblePaths mount used by the service sandbox.

%prep
mkdir -p %{name}-%{version}
cp %{SOURCE0} %{name}-%{version}/dde_daemon.te
cp %{SOURCE1} %{name}-%{version}/dde_daemon.fc

%build
cd %{name}-%{version}
make -f /usr/share/selinux/devel/Makefile dde_daemon.pp

%install
install -Dm644 %{name}-%{version}/dde_daemon.pp %{buildroot}%{_datadir}/selinux/packages/dde_daemon.pp

%post
if [ -x /usr/sbin/semodule ]; then
    /usr/sbin/semodule -i /usr/share/selinux/packages/dde_daemon.pp 2>/dev/null || :
fi
[ -e /usr/lib/deepin-daemon ] && /usr/sbin/restorecon -R /usr/lib/deepin-daemon 2>/dev/null || :

%posttrans
[ -e /usr/lib/deepin-daemon ] && /usr/sbin/restorecon -R /usr/lib/deepin-daemon 2>/dev/null || :

%postun
if [ "$1" -eq 0 ] && [ -x /usr/sbin/semodule ]; then
    /usr/sbin/semodule -r dde_daemon 2>/dev/null || :
    [ -e /usr/lib/deepin-daemon ] && /usr/sbin/restorecon -R /usr/lib/deepin-daemon 2>/dev/null || :
fi

%files
%{_datadir}/selinux/packages/dde_daemon.pp

%changelog
* Mon Nov 23 2026 mozixun <mozixun@fedoraproject.org> - 1.0.0-1
- Independent SELinux policy package for dde-daemon.
