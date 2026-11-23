Name:           deepin-system-monitor-selinux
Version:        1.0.0
Release:        1%{?dist}
Summary:        SELinux policy for the Deepin system monitor
License:        GPL-2.0-or-later
URL:            https://github.com/Fedora-DDE-Remix/Deepin-Desktop-Environment
Source0:        https://raw.githubusercontent.com/Fedora-DDE-Remix/Deepin-Desktop-Environment/refs/heads/main/deepin-system-monitor-selinux/deepin_system_monitor.te
Source1:        https://raw.githubusercontent.com/Fedora-DDE-Remix/Deepin-Desktop-Environment/refs/heads/main/deepin-system-monitor-selinux/deepin_system_monitor.fc
BuildArch:      noarch
BuildRequires:  selinux-policy-devel

Requires:       deepin-system-monitor
Requires:       selinux-policy-targeted
Requires:       policycoreutils

%description
This package provides the SELinux policy used by the Deepin system monitor.
It allows systemd's init_t to set up the InaccessiblePaths mounts for
/etc/shadow and /etc/selinux without granting read or write access.

%prep
mkdir -p %{name}-%{version}
cp %{SOURCE0} %{name}-%{version}/deepin_system_monitor.te
cp %{SOURCE1} %{name}-%{version}/deepin_system_monitor.fc

%build
cd %{name}-%{version}
make -f /usr/share/selinux/devel/Makefile deepin_system_monitor.pp

%install
install -Dm644 %{name}-%{version}/deepin_system_monitor.pp %{buildroot}%{_datadir}/selinux/packages/deepin_system_monitor.pp

%post
if [ -x /usr/sbin/semodule ]; then
    /usr/sbin/semodule -i /usr/share/selinux/packages/deepin_system_monitor.pp 2>/dev/null || :
fi

%posttrans
:

%postun
if [ "$1" -eq 0 ] && [ -x /usr/sbin/semodule ]; then
    /usr/sbin/semodule -r deepin_system_monitor 2>/dev/null || :
fi

%files
%{_datadir}/selinux/packages/deepin_system_monitor.pp

%changelog
* Mon Nov 23 2026 mozixun <mozixun@fedoraproject.org> - 1.0.0-1
- Independent SELinux policy package for deepin-system-monitor.
