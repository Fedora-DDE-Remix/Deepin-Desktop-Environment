Name:           ddm-selinux
Version:        1.0.0
Release:        1%{?dist}
Summary:        SELinux policy for the Deepin Display Manager
License:        GPL-2.0-or-later
URL:            https://github.com/Fedora-DDE-Remix/Deepin-Desktop-Environment
Source0:        https://raw.githubusercontent.com/Fedora-DDE-Remix/Deepin-Desktop-Environment/refs/heads/main/ddm-selinux/ddm.te
Source1:        https://raw.githubusercontent.com/Fedora-DDE-Remix/Deepin-Desktop-Environment/refs/heads/main/ddm-selinux/ddm.fc
BuildArch:      noarch
BuildRequires:  selinux-policy-devel

Requires:       ddm
Requires:       selinux-policy-targeted
Requires:       policycoreutils

%description
This package provides the SELinux policy used by DDM.  It maps DDM onto the
generic xdm_t display-manager domain and supplies the file contexts for
DDM, its helper, /run/ddm, /var/lib/ddm and treeland.service.

%prep
mkdir -p %{name}-%{version}
cp %{SOURCE0} %{name}-%{version}/ddm.te
cp %{SOURCE1} %{name}-%{version}/ddm.fc

%build
cd %{name}-%{version}
make -f /usr/share/selinux/devel/Makefile ddm.pp

%install
install -Dm644 %{name}-%{version}/ddm.pp %{buildroot}%{_datadir}/selinux/packages/ddm.pp

%post
if [ -x /usr/sbin/semodule ]; then
    /usr/sbin/semodule -i /usr/share/selinux/packages/ddm.pp 2>/dev/null || :
fi
for p in /usr/bin/ddm /usr/libexec/ddm-helper /run/ddm /var/lib/ddm \
         /usr/lib/systemd/system/treeland.service; do
    [ -e "$p" ] && /usr/sbin/restorecon -R "$p" 2>/dev/null || :
done

%posttrans
for p in /usr/bin/ddm /usr/libexec/ddm-helper /run/ddm /var/lib/ddm \
         /usr/lib/systemd/system/treeland.service; do
    [ -e "$p" ] && /usr/sbin/restorecon -R "$p" 2>/dev/null || :
done
/usr/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun
if [ "$1" -eq 0 ] && [ -x /usr/sbin/semodule ]; then
    /usr/sbin/semodule -r ddm 2>/dev/null || :
    for p in /usr/bin/ddm /usr/libexec/ddm-helper /run/ddm /var/lib/ddm \
             /usr/lib/systemd/system/treeland.service; do
        [ -e "$p" ] && /usr/sbin/restorecon -R "$p" 2>/dev/null || :
    done
fi

%files
%{_datadir}/selinux/packages/ddm.pp

%changelog
* Mon Nov 23 2026 mozixun <mozixun@fedoraproject.org> - 1.0.0-1
- Independent SELinux policy package for DDM.
