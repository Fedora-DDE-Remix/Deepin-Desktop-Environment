%global srcname dtkdeclarative

Name:           dtk6declarative
Version:        6.7.54
Release:        2%{?dist}
Summary:        Deepin widget development toolkit based on QtQuick/QtQml
License:        LGPL-3.0-or-later
URL:            https://github.com/linuxdeepin/dtkdeclarative
Source0:        %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz
Patch0:         https://raw.githubusercontent.com/Fedora-DDE-Remix/Deepin-Desktop-Environment/refs/heads/main/dtkdeclarative/01-qt611-palette.patch

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  ninja-build
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6QuickControls2)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6ShaderTools)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Qt6ToolsTools)
BuildRequires:  cmake(Qt6CorePrivate)
BuildRequires:  cmake(Qt6QmlPrivate)
BuildRequires:  cmake(Qt6QuickPrivate)
BuildRequires:  cmake(Qt6QuickControls2Private)
BuildRequires:  cmake(Dtk6Core) >= %{version}
BuildRequires:  cmake(Dtk6Gui) >= %{version}
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  doxygen

%description
dtkdeclarative is a widget development toolkit based on QtQuick/QtQml, a
substitute for dtkwidget.  It covers the existing QML widgets and adds DTK
visual effects and color schemes.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       dtkcommon-devel%{_isa}

%description    devel
This package contains development files for %{name}.

%prep
%autosetup -n %{srcname}-%{version} -p1

%build
%cmake -GNinja -DDTK5=OFF \
  -DINCLUDE_INSTALL_DIR=%{_includedir}/dtk6/DDeclarative \
  -DQCH_INSTALL_DESTINATION=%{_qt6_docdir} \
  -DDTK_VERSION=%{version}
%cmake_build

%install
%cmake_install

%files
%license LICENSE
%doc README.md
%{_libdir}/libdtk6declarative.so.6*
%dir %{_libdir}/dtk6/DDeclarative
%{_libdir}/dtk6/DDeclarative/dtk6-exhibition
%{_qt6_qmldir}/Chameleon/
%{_qt6_qmldir}/org/deepin/dtk/
%{_datadir}/dtk6/DDeclarative/translations/

%files devel
%dir %{_includedir}/dtk6
%{_includedir}/dtk6/DDeclarative/
%{_libdir}/cmake/Dtk6Declarative/
%{_libdir}/pkgconfig/dtk6declarative.pc
%{_libdir}/libdtk6declarative.so
%{_qt6_archdatadir}/mkspecs/modules/*.pri
%{_qt6_docdir}/dtkdeclarative.qch
%{_datadir}/qtcreator/templates/wizards/projects/qml6-app-template/

%changelog
* Sun Nov 22 2026 mozixun <mozixun@fedoraproject.org> - 6.7.54-2
- Fix the QML DTK.makeIconPalette() crash with Qt 6.11.

* Sat Nov 21 2026 mozixun <mozixun@fedoraproject.org> - 6.7.54-1
- Initial Fedora package (DTK 6.7.54, Qt 6 only).
