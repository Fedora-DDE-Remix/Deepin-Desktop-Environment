Name:           ddm
Version:        0.5.0
Release:        7%{?dist}
Summary:        Deepin Display Manager
License:        GPL-2.0-or-later
URL:            https://github.com/linuxdeepin/ddm
Source0:        %{url}/archive/%{version}/ddm-%{version}.tar.gz
Source1:        https://raw.githubusercontent.com/Fedora-DDE-Remix/Deepin-Desktop-Environment/refs/heads/main/ddm/90-ddm.preset
Source2:        https://raw.githubusercontent.com/Fedora-DDE-Remix/Deepin-Desktop-Environment/refs/heads/main/ddm/ddm.pam
Source3:        https://raw.githubusercontent.com/Fedora-DDE-Remix/Deepin-Desktop-Environment/refs/heads/main/ddm/ddm-autologin.pam
Source4:        https://raw.githubusercontent.com/Fedora-DDE-Remix/Deepin-Desktop-Environment/refs/heads/main/ddm/ddm.te
Source5:        https://raw.githubusercontent.com/Fedora-DDE-Remix/Deepin-Desktop-Environment/refs/heads/main/ddm/ddm.fc

BuildRequires:  cmake
BuildRequires:  selinux-policy-devel
BuildRequires:  gcc-c++
BuildRequires:  ninja-build
BuildRequires:  extra-cmake-modules
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Dtk6Core)
BuildRequires:  cmake(Dtk6Tools)
BuildRequires:  cmake(TreelandProtocols) >= 0.5.3
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(pam)
BuildRequires:  pkgconfig(xau)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  systemd-devel
BuildRequires:  pam-devel
BuildRequires:  libXau-devel
BuildRequires:  wayland-devel

Requires:       accountsservice
Requires:       systemd
Requires:       systemd-pam
Requires:       pam
Requires:       %{name}-selinux = %{version}-%{release}

%description
DDM is the Deepin Display Manager, a Wayland greeter and session manager used
with the Treeland compositor.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package contains development files for %{name}.

%package        selinux
Summary:        SELinux policy for the Deepin Display Manager
Requires:       selinux-policy-targeted
Requires:       policycoreutils

%description    selinux
This package installs the SELinux file contexts that map DDM onto Fedora's
generic xdm_t display-manager domain: /usr/bin/ddm and /usr/libexec/ddm-helper
use xdm_exec_t, /run/ddm uses xdm_var_run_t and /var/lib/ddm uses
xdm_var_lib_t.  It does not introduce a new SELinux domain.

%prep
%autosetup -n ddm-%{version} -p1

%build
%cmake -GNinja -DBUILD_MAN_PAGES=OFF -DWERROR=OFF
%cmake_build
cp %{SOURCE4} ddm.te
cp %{SOURCE5} ddm.fc
make -f /usr/share/selinux/devel/Makefile ddm.pp

%install
%cmake_install
install -Dm644 %{SOURCE1} %{buildroot}%{_presetdir}/90-ddm.preset
install -Dm644 %{SOURCE2} %{buildroot}%{_sysconfdir}/pam.d/ddm
install -Dm644 %{SOURCE3} %{buildroot}%{_sysconfdir}/pam.d/ddm-autologin
install -Dm644 ddm.pp %{buildroot}%{_datadir}/selinux/packages/ddm.pp

%post
%systemd_post ddm.service

%preun
%systemd_preun ddm.service

%postun
%systemd_postun_with_restart ddm.service

%post selinux
if [ -x /usr/sbin/semodule ]; then
    /usr/sbin/semodule -i /usr/share/selinux/packages/ddm.pp 2>/dev/null || :
fi
for p in /usr/bin/ddm /usr/libexec/ddm-helper /run/ddm /var/lib/ddm \
         /usr/lib/systemd/system/treeland.service; do
    [ -e "$p" ] && /usr/sbin/restorecon -R "$p" 2>/dev/null || :
done

%posttrans selinux
# treeland may be installed later in the same transaction.
[ -e /usr/lib/systemd/system/treeland.service ] && /usr/sbin/restorecon -R /usr/lib/systemd/system/treeland.service 2>/dev/null || :
/usr/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun selinux
if [ "$1" -eq 0 ] && [ -x /usr/sbin/semodule ]; then
    /usr/sbin/semodule -r ddm 2>/dev/null || :
    for p in /usr/bin/ddm /usr/libexec/ddm-helper /run/ddm /var/lib/ddm \
             /usr/lib/systemd/system/treeland.service; do
        [ -e "$p" ] && /usr/sbin/restorecon -R "$p" 2>/dev/null || :
    done
fi

%files
%license LICENSES/
%doc README.md
%{_bindir}/ddm
%{_libexecdir}/ddm-helper
%{_unitdir}/ddm.service
%{_presetdir}/90-ddm.preset
%{_sysusersdir}/dde.conf
%{_tmpfilesdir}/ddm.conf
%config(noreplace) %{_sysconfdir}/pam.d/ddm
%config(noreplace) %{_sysconfdir}/pam.d/ddm-autologin
%config(noreplace) %{_sysconfdir}/dbus-1/system.d/org.freedesktop.DisplayManager.conf
%config(noreplace) %{_sysconfdir}/dbus-1/system.d/org.deepin.DisplayManager.conf
%{_datadir}/ddm/
%{_datadir}/dsg/configs/org.deepin.dde.ddm/
%{_libdir}/libddm-common.so.0*

%files devel
%{_includedir}/ddm/
%{_libdir}/libddm-common.so
%{_libdir}/cmake/DDM/

%files selinux
%{_datadir}/selinux/packages/ddm.pp

%changelog
* Mon Nov 23 2026 mozixun <mozixun@fedoraproject.org> - 0.5.0-7
- Move the DDE /usr/lib/deepin-daemon and /usr/lib/deepin-api contexts into
  the dedicated dde-daemon-selinux and dde-api-selinux packages.

* Mon Nov 23 2026 mozixun <mozixun@fedoraproject.org> - 0.5.0-6
- Install a Fedora PAM stack with pam_selinux, password-auth/system-auth,
  pam_loginuid and pam_namespace so DDM logins get the correct user domain.
- Add ddm-selinux, mapping DDM onto the existing xdm_t SELinux domain and
  labelling /run/ddm and /var/lib/ddm with xdm_var_run_t/xdm_var_lib_t.
- Allow xdm_t to use dde-seatd/Treeland sockets under /run, label
  treeland.service as xdm_unit_file_t, and label the DDE daemons in
  /usr/lib/deepin-daemon and /usr/lib/deepin-api as bin_t.

* Sun Nov 22 2026 mozixun <mozixun@fedoraproject.org> - 0.5.0-5
- Require pkgconfig(systemd); systemd.pc lives in the systemd package and
  supplies the install directory variables.

* Sun Nov 22 2026 mozixun <mozixun@fedoraproject.org> - 0.5.0-4
- Use a raw URL for the systemd preset so COPR spec builds work.

* Sun Nov 22 2026 mozixun <mozixun@fedoraproject.org> - 0.5.0-3
- Enable ddm.service from the ddm package preset.

* Sun Nov 22 2026 mozixun <mozixun@fedoraproject.org> - 0.5.0-2
- Require systemd-pam for pam_systemd.so.

* Sat Nov 21 2026 mozixun <mozixun@fedoraproject.org> - 0.5.0-1
- Initial Fedora package.
