Name:           deepin-image-viewer
Version:        6.1.4
Release:        1%{?dist}
Summary:        Image viewer for the Deepin desktop environment

License:        GPL-3.0-or-later AND CC0-1.0 AND CC-BY-4.0
URL:            https://github.com/linuxdeepin/deepin-image-viewer
Source0:        %{url}/archive/%{version}/deepin-image-viewer-%{version}.tar.gz
Patch0:         https://raw.githubusercontent.com/Fedora-DDE-Remix/Deepin-Desktop-Environment/refs/heads/main/deepin-image-viewer/01-system-opencv.patch

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  ninja-build
BuildRequires:  qt6-linguist
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6Concurrent)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6PrintSupport)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Dtk6Core)
BuildRequires:  cmake(Dtk6Widget)
BuildRequires:  cmake(Dtk6Declarative)
BuildRequires:  pkgconfig(deepin-ocr-plugin-manager)
BuildRequires:  pkgconfig(ncnn)
BuildRequires:  pkgconfig(opencv4)
BuildRequires:  pkgconfig(libraw)

Requires:       deepin-ocr-plugin-manager
Requires:       dtk6declarative
Requires:       qt6-qtdeclarative
Requires:       qt6-qt5compat
Requires:       qt6-qtsvg
Requires:       hicolor-icon-theme
Recommends:     qt6-qtimageformats
Recommends:     kf6-kimageformats
Recommends:     deepin-manual

%description
Deepin Image Viewer is an image viewing tool with a fashion interface and
smooth performance.  It supports common image formats, RAW images, basic
editing and OCR-based live text.

%prep
%autosetup -n deepin-image-viewer-%{version} -p1

%build
%cmake -GNinja -DQT_VERSION_MAJOR=6 -DDTK_VERSION_MAJOR=6
%cmake_build

%install
%cmake_install

%files
%license LICENSE.txt
%doc README.md
%{_bindir}/deepin-image-viewer
%{_libdir}/qt6/plugins/imageformats/libxraw.so*
%{_datadir}/applications/deepin-image-viewer.desktop
%{_datadir}/applications/context-menus/deepin-print-pictures.conf
%{_datadir}/dbus-1/services/com.deepin.imageViewer.service
%{_datadir}/deepin-image-viewer/
%{_datadir}/deepin-manual/manual-assets/application/deepin-image-viewer/
%{_datadir}/dsg/configs/org.deepin.imageviewer/
%{_datadir}/icons/hicolor/scalable/apps/deepin-image-viewer.svg

%changelog
* Sun Nov 22 2026 mozixun <mozixun@fedoraproject.org> - 6.1.4-1
- Initial Fedora package.
