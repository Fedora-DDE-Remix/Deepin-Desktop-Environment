Name:           deepin-editor
Version:        6.6.4
Release:        3%{?dist}
Summary:        Text editor for the Deepin desktop environment
License:        GPL-3.0-or-later
URL:            https://github.com/linuxdeepin/deepin-editor
Source0:        %{url}/archive/%{version}/deepin-editor-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  ninja-build
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6Concurrent)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6WebEngineWidgets)
BuildRequires:  cmake(Qt6Core5Compat)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Dtk6Core)
BuildRequires:  cmake(Dtk6Widget)
BuildRequires:  cmake(KF6Codecs)
BuildRequires:  cmake(KF6SyntaxHighlighting)
BuildRequires:  pkgconfig(chardet)
BuildRequires:  pkgconfig(icu-i18n)
BuildRequires:  pkgconfig(icu-uc)
BuildRequires:  pkgconfig(uchardet)

Requires:       kf6-syntax-highlighting
Requires:       hicolor-icon-theme

%description
Deepin Editor is a simple and lightweight text editor for the Deepin desktop
environment, with syntax highlighting, tabbed editing and print support.

%prep
%autosetup -n deepin-editor-%{version} -p1

%build
%cmake -GNinja -DBUILD_TESTS=OFF -DQT_VERSION_MAJOR=6 -DDTK_VERSION_MAJOR=6
%cmake_build

%install
%cmake_install

%files
%license LICENSE.txt
%doc README.md
%{_bindir}/deepin-editor
%{_datadir}/applications/deepin-editor.desktop
%{_datadir}/deepin-editor/
%{_datadir}/deepin-manual/manual-assets/application/deepin-editor/
%{_datadir}/dsg/configs/org.deepin.editor/
%{_datadir}/icons/hicolor/scalable/apps/deepin-editor.svg

%changelog
* Sun Nov 22 2026 mozixun <mozixun@fedoraproject.org> - 6.6.4-3
- Add Qt6WebEngineWidgets.

* Sun Nov 22 2026 mozixun <mozixun@fedoraproject.org> - 6.6.4-2
- Add Qt6Svg.

* Sat Nov 21 2026 mozixun <mozixun@fedoraproject.org> - 6.6.4-1
- Initial Fedora package.
