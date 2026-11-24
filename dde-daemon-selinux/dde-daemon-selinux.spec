Epoch:          1
Name:           dde-daemon-selinux
Version:        1.0.0
Release:        3%{?dist}
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
helpers in /usr/lib/deepin-daemon and the authentication binary in
/usr/lib/deepin-authenticate as bin_t, and allows systemd's init_t to perform
the /etc/shadow InaccessiblePaths mount used by the service sandbox.

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
for p in /usr/lib/deepin-daemon /usr/lib/deepin-authenticate /usr/lib/deepin-deepinid-daemon; do
    [ -e "$p" ] && /usr/sbin/restorecon -R "$p" 2>/dev/null || :
done

%posttrans
for p in /usr/lib/deepin-daemon /usr/lib/deepin-authenticate /usr/lib/deepin-deepinid-daemon; do
    [ -e "$p" ] && /usr/sbin/restorecon -R "$p" 2>/dev/null || :
done

%postun
if [ "$1" -eq 0 ] && [ -x /usr/sbin/semodule ]; then
    /usr/sbin/semodule -r dde_daemon 2>/dev/null || :
    for p in /usr/lib/deepin-daemon /usr/lib/deepin-authenticate /usr/lib/deepin-deepinid-daemon; do
        [ -e "$p" ] && /usr/sbin/restorecon -R "$p" 2>/dev/null || :
    done
fi

%files
%{_datadir}/selinux/packages/dde_daemon.pp

%changelog
* Tue Nov 24 2026 mozixun <mozixun@fedoraproject.org> - 1.0.0-3
- Label the deepin-deepinid sync helper as bin_t so D-Bus starts it in
  unconfined_service_t instead of system_dbusd_t.

* Tue Nov 24 2026 mozixun <mozixun@fedoraproject.org> - 1.0.0-2
- Label /usr/lib/deepin-authenticate as bin_t so systemd runs the
  authentication service in unconfined_service_t instead of init_t;
  this fixes the execmem denial and the restart loop.
- Set Epoch 1 so this policy package supersedes the old 6.x bundled
  policy packages.

* Mon Nov 23 2026 mozixun <mozixun@fedoraproject.org> - 1.0.0-1
- Independent SELinux policy package for dde-daemon.
