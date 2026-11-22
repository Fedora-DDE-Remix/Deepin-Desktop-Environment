Name:           dde-calendar
Version:        6.6.9
Release:        1%{?dist}
Summary:        Calendar application for the Deepin desktop environment

License:        LGPL-3.0-or-later AND LGPL-2.0-or-later AND GPL-3.0-or-later
URL:            https://github.com/linuxdeepin/dde-calendar
Source0:        %{url}/archive/%{version}/dde-calendar-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  ninja-build
BuildRequires:  qt6-linguist
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6Sql)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6Concurrent)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Dtk6Core)
BuildRequires:  cmake(Dtk6Widget)
BuildRequires:  cmake(Dtk6Gui)
BuildRequires:  pkgconfig(libical)

Requires:       dde-api
Requires:       deepin-qt6integration
Requires:       dtk6widget
Requires:       hicolor-icon-theme
Recommends:     deepin-manual

%description
DDE Calendar is a daily planner for the Deepin desktop environment.  It
combines a calendar view with events, reminders and a small calendar service.

%prep
%autosetup -n dde-calendar-%{version} -p1

%build
%cmake -GNinja \
  -DWITH_AIASSISTANT_PLUGIN=OFF \
  -DBUILD_TESTING=OFF \
  -DCMAKE_INSTALL_SYSCONFDIR=%{_sysconfdir}
%cmake_build

%install
%cmake_install

%post
%systemd_user_post dde-calendar.service com.dde.calendarserver.calendar.service com.dde.calendarserver.calendar.timer

%preun
%systemd_user_preun dde-calendar.service com.dde.calendarserver.calendar.service com.dde.calendarserver.calendar.timer

%postun
%systemd_user_postun_with_restart dde-calendar.service com.dde.calendarserver.calendar.service com.dde.calendarserver.calendar.timer

%files
%license LICENSE
%doc README.md
%{_bindir}/dde-calendar
%{_libexecdir}/deepin-daemon/dde-calendar-service
%{_userunitdir}/dde-calendar.service
%{_userunitdir}/com.dde.calendarserver.calendar.service
%{_userunitdir}/com.dde.calendarserver.calendar.timer
%{_datadir}/applications/dde-calendar.desktop
%{_datadir}/dbus-1/services/com.deepin.Calendar.service
%{_datadir}/dbus-1/services/com.deepin.dataserver.Calendar.service
%{_datadir}/metainfo/org.deepin.calendar.metainfo.xml
%{_datadir}/dde-calendar/
%{_datadir}/deepin-manual/manual-assets/application/dde-calendar/
%{_datadir}/deepin-debug-config/deepin-debug-config.d/org.deepin.dde.calendar.json
%{_datadir}/deepin-log-viewer/deepin-log.conf.d/dde-calendar.json
%{_datadir}/dsg/configs/org.deepin.dde.calendar/
%config(noreplace) %{_sysconfdir}/xdg/autostart/dde-calendar-service.desktop

%changelog
* Sun Nov 22 2026 mozixun <mozixun@fedoraproject.org> - 6.6.9-1
- Initial Fedora package.
