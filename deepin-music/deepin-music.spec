%global debug_package %{nil}

Name:           deepin-music
Version:        7.0.73
Release:        1%{?dist}
Summary:        Music player for the Deepin desktop environment
License:        GPL-3.0-or-later
URL:            https://github.com/linuxdeepin/deepin-music
Source0:        %{url}/archive/%{version}/deepin-music-%{version}.tar.gz
Patch0:         https://raw.githubusercontent.com/Fedora-DDE-Remix/Deepin-Desktop-Environment/refs/heads/main/deepin-music/01-use-pic-for-shared-lib.patch

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  ninja-build
BuildRequires:  pkgconf-pkg-config
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6Multimedia)
BuildRequires:  cmake(Qt6Sql)
BuildRequires:  cmake(Qt6Core5Compat)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  qt6-linguist
BuildRequires:  cmake(Dtk6Core)
BuildRequires:  cmake(Dtk6Gui)
BuildRequires:  cmake(Dtk6Declarative)
BuildRequires:  pkgconfig(mpris-qt6)
BuildRequires:  pkgconfig(taglib)
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libswresample)
BuildRequires:  pkgconfig(icu-i18n)
BuildRequires:  vlc-devel
BuildRequires:  sdl2-compat-devel

Requires:       vlc
Requires:       sdl2-compat
Requires:       ffmpeg-free
Requires:       dtk6declarative
Requires:       qt6-qt5compat
Requires:       qt6-qtmultimedia
Requires:       qt6-qtdeclarative
Requires:       deepin-desktop-base

%description
deepin-music is a local music player with a clean Deepin UI, playlist and
album management, lyrics, equalizer support and VLC-based playback.

%prep
%autosetup -n deepin-music-%{version} -p1

%build
%cmake -GNinja \
  -DCMAKE_BUILD_TYPE=Release \
  -DAPP_VERSION=%{version} \
  -DVERSION=%{version}
%cmake_build

%install
%cmake_install
rm -f %{buildroot}%{_libdir}/libdmusic.so
strip --strip-unneeded %{buildroot}%{_bindir}/deepin-music
strip --strip-unneeded %{buildroot}%{_libdir}/libdmusic.so.1.0.0

%files
%license LICENSE
%doc README.md CHANGELOG.md
%{_bindir}/deepin-music
%{_libdir}/libdmusic.so.*
%{_datadir}/deepin-music/translations/
%{_datadir}/applications/deepin-music.desktop
%{_datadir}/icons/hicolor/scalable/apps/deepin-music.svg
%{_datadir}/deepin-manual/manual-assets/application/deepin-music/
%{_datadir}/dsg/configs/org.deepin.music/

%changelog
* Mon Nov 23 2026 mozixun <mozixun@fedoraproject.org> - 7.0.73-1
- Initial Fedora package using the system VLC, FFmpeg, TagLib, SDL2 and
  mpris-qt6 libraries.
