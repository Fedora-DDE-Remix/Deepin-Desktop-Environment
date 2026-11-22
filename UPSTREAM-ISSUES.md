# Upstream issues found while packaging DDE for Fedora 45

These are build- or distro-portability issues in upstream DDE projects.  They
are worked around in the specs in this directory and should be reported or
sent as patches upstream.  None of them is a behavioural DDE change.

## deepin-fcitx5configtool-plugin

- `src/CMakeLists.txt` and its subdirectories hard-code
  `CMAKE_CXX_STANDARD 17` and `CMAKE_CXX_FLAGS "-g -Wall"`.  The subdirectories
  override flags supplied by the caller.
- Fedora fcitx5 5.1.23 requires C++20 and needs the
  `Fcitx5/Utils` include directory plus `fcitx-utils/stringutils.h`.
- Suggested upstream fix: make the required C++ standard a cache option and
  add `Fcitx5::Utils` to the targets that include fcitx headers, instead of
  overriding `CMAKE_CXX_FLAGS` in subdirectories.
- Local workaround: `01-fedora-cxx20.patch` raises the standard to C++20 and
  adds the Fcitx5 Utils include directory plus the `stringutils.h` forced
  include.

## dde-api / DDEAPI CMake package

- `cmake/DDEAPI/DDEAPIConfig.cmake` sets
  `DDE_API_INCLUDE_DIRS "/usr/include"`.
- CMake turns that into `-isystem /usr/include` for every consumer.  GCC then
  treats `/usr/include` as an explicit system directory; libstdc++'s
  `#include_next <stdlib.h>` skips it and compilation fails with
  `stdlib.h: No such file or directory`.
- Suggested upstream fix: do not add `/usr/include` (it is a default include
  path), or use `${PACKAGE_PREFIX_DIR}/include` only for non-default prefixes.
- Local fix: the `dde-api` spec rewrites the installed
  `DDEAPIConfig.cmake` to use an empty include list.

## dde-shell

- `CMakeLists.txt` unconditionally adds `-Werror`.  Qt 6.11 deprecates
  `QSortFilterProxyModel::invalidateFilter()`, which then becomes a hard build
  failure.
- The executable is not compiled with `-fPIE`, but Fedora's default linker
  hardening passes `-pie`; linking fails with
  `relocation R_X86_64_32 ... can not be used when making a PIE object`.
- The example plugins are always built and pull in `OpenGL::GLX`.
- Suggested upstream fixes:
  - use `-Werror` only for the project's own CI, or add
    `-Wno-error=deprecated-declarations`;
  - add `-fPIE`/`POSITION_INDEPENDENT_CODE` for the `dde-shell` executable;
  - make the example plugins optional (`BUILD_EXAMPLES`);
  - use `QSortFilterProxyModel::beginFilterChange()`/`endFilterChange()` on
    Qt >= 6.10.
- Local workaround: `01-optional-examples.patch` makes examples optional;
  `02-strip-usr-include.patch` removes `/usr/include` from the imported
  OpenGL/X11 targets; the spec builds with
  `-DCMAKE_CXX_FLAGS="-Wno-deprecated-declarations -fPIE"`.  These are
  distro build adaptations, not behavioural changes.

## util-dfm

- `src/dfm-burn/dfm-burn-lib/private/dsm3hash.cpp` calls `EVP_sm3()`.
  OpenSSL 4 still declares it but no longer exports it from `libcrypto`.
- Suggested upstream fix: `EVP_get_digestbyname("SM3")` (works with OpenSSL 3
  and 4), or use `EVP_MD_fetch(NULL, "SM3", NULL)`.
- Local workaround: `01-openssl4-sm3.patch` changes the call to
  `EVP_get_digestbyname("SM3")`; `openssl-compat` provides the runtime symbol
  for the proprietary binaries.

## treeland / vendored wlroots

- The vendored wlroots checks `pixman-1 >= 0.46.4`; Fedora 45 ships 0.46.2.
- Suggested upstream fix: relax the check or make the pixman feature
  conditional; the DRM backend only needs the older API.
- Local workaround: `01-relax-pixman.patch`.

## dde-file-manager

- `cmake/DFMLibraryConfig.cmake` requires `libappimage`, which Fedora does not
  ship.
- `src/plugins/filemanager/dfmplugin-disk-encrypt-entry/utils/encryptutils.cpp`
  passes `QChar::unicode()` directly to `QString::arg`; Qt 6.11 requires an
  explicit `uint`.
- `CMAKE_INSTALL_SYSCONFDIR` data is installed below `/usr/etc` when the
  prefix is `/usr`.
- Suggested upstream fixes: make libappimage optional via the existing
  `DFM_DISABLE_APPIMAGE` switch, cast the `arg` argument, and install
  configuration to `${CMAKE_INSTALL_FULL_SYSCONFDIR}`.
- Local workaround: `01-fedora-disable-appimage-qt611.patch` and a spec
  `%install` move from `/usr/etc` to `/etc`.

## dde-daemon / dde-api Makefiles

- `make build` calls `deepin-policy-ts-convert` to regenerate polkit policies.
  That tool is not packaged in Fedora and the generated policy files are
  already in the source tree.
- `dde-daemon` installs units into `/lib/systemd` and libraries into `/usr/lib`
  regardless of the Fedora libdir; `dde-api` installs its library into
  `/usr/lib`.
- Suggested upstream fixes: ship pre-generated policy files, use
  `$(DESTDIR)$(PREFIX)/$(LIBDIR)` (or `GNUInstallDirs`), and install unit files
  with `CMAKE_INSTALL_FULL_SYSTEMDUNITDIR`/`_userunitdir`.
- Local workaround: skip policy regeneration and move files in the spec.

## dde-tray-loader

- `keybord_layout.json` is installed under `${CMAKE_INSTALL_PREFIX}/etc` when
  the prefix is `/usr`, producing `/usr/etc/dde-dock/...`.
- Suggested upstream fix: use `CMAKE_INSTALL_FULL_SYSCONFDIR`.
- Local workaround: move `/usr/etc/dde-dock` to `/etc/dde-dock` in `%install`.

## deepin-compressor

- `cmake/translation-generate.cmake` hard-codes `QT_LRELEASE` to
  `/lib/qt6/bin/lrelease`.
- Suggested upstream fix: use the `Qt6::lrelease` target or
  `${QT6_INSTALL_PREFIX}/${QT6_INSTALL_BINS}/lrelease`.
- Local workaround: spec rewrites the path to `%{_qt6_bindir}/lrelease`.

## deepin-deepinid-client

- The client pulls in Qt6 WebEngine, WebChannel and WebEngineWidgets.  This is
  a very large dependency for a login dialog; a lighter WebView or an
  out-of-process browser handoff would be preferable.

## deepin-authenticate (proprietary)

- The binaries import OpenSSL 3.0 `EVP_sm4_cbc()`/`EVP_sm4_ecb()` and
  `EVP_sm3()`, which OpenSSL 4 no longer exports.
- Suggested upstream fix: rebuild against OpenSSL 3/4 provider APIs or link
  the compatibility library.
- Local workaround: `openssl-compat` and `deepin-authenticate-compat`.

## dde-seatd

- The fork installs `seatd`, `seatd-launch` and `libseat.so.1`, which collide
  with Fedora's `seatd` package.
- Suggested upstream fix: provide a configure option for a private prefix or
  rename the fork's binaries/library.
- Local packaging: `dde-seatd` conflicts with Fedora `seatd`; it is not
  required by the Treeland session (Treeland uses Fedora `libseat`).

## deepin-desktop-base / deepin-default-settings

- Upstream data includes Debian-specific `/etc/lsb-release`, apt templates,
  PAM/sudoers/X11/sysctl configurations and LightDM snippets.
- These must not be installed on Fedora.  The specs install only the safe
  skel/XDG/version data and leave `/etc/lsb-release` to `fedora-release`.

## SeetaFace modules

- The 2.8-era CMake projects do not include `<cstdlib>`, `<functional>` or
  `<memory>` explicitly; GCC 16 fails on `std::malloc`, `std::function` and
  `std::allocator`.
- `seetaface-quality-assessor` forces its install prefix into a source-tree
  `build/` directory, ignoring `CMAKE_INSTALL_PREFIX`/`SEETA_INSTALL_PATH`.
- The common `include/seeta/Common/Struct.h` headers are installed by every
  module.  They should be provided by one common development package.
- Local workaround: the specs build with
  `-include cstdlib -include functional -include memory`, a small
  `01-install-prefix.patch` for the quality assessor, and a
  `seetaface-common` package from `seetaface-boxes`.

## deepin-face

- `deepin-face.pro` hard-codes `-L/usr/lib/auto`, `-L/usr/lib`, the Debian
  `c++/8` include path and the debug anti-spoofing library name
  `SeetaFaceAntiSpoofingX600d`.
- The systemd unit is installed to `/lib/systemd/system` instead of the
  Fedora `/usr/lib/systemd/system`.
- The service runs as the `deepin-daemon` user; the user is provided by
  `dde-api`'s `deepin-daemon.conf` sysusers file.
- Local workaround: `01-fedora-paths.patch` plus a spec `sed` for the unit
  path.

## deepin-ocr-plugin-manager / deepin-image-viewer

- Both projects require `opencv_mobile`, a Debian-specific packaging of an
  old OpenCV tree.  Fedora provides the system OpenCV 4 as `opencv4.pc`; the
  code only uses the core, imgproc and highgui modules.
- `deepin-ocr-plugin-manager` calls `ncnn::Extractor::set_vulkan_compute()`,
  which current ncnn releases removed.  The call only tuned per-extractor
  Vulkan usage; `create_extractor()` already follows the network option.
- Suggested upstream fixes: make the OpenCV pkg-config name a build option
  (`opencv4`/`opencv_mobile`) and drop the obsolete per-extractor Vulkan
  switch.
- Local workaround: `01-fedora-deps.patch` in the OCR manager spec and
  `01-system-opencv.patch` in the image viewer spec.

## deepin-reader

- The release tarball's `3rdparty/deepin-pdfium` copy contains
  `DPdfDoc::fileIdentifier()` and `DPdfPage::imageObjectRects()`, but the
  deepin-pdfium 1.5.8 release does not.  A source build against the system
  library therefore fails to compile.
- Building the bundled copy is the upstream default, but it drops a private
  `libdeepin-pdfium-reader` into the build and installs a conflicting
  `deepin-pdfium.pc`.
- Suggested upstream fix: release a deepin-pdfium version containing these
  two APIs, or make the reader depend on the released API only.
- Local workaround: `01-backport-reader-api.patch` in the deepin-pdfium spec
  backports the two methods; the reader builds with
  `-DUSE_PDFIUM_BUNDLE=OFF`.
- OFD support is disabled (`-DOFD_SUPPORT=OFF`) because Fedora does not ship
  the Rust `rofd-ffi` library.  PDF, DjVu, XPS/OXPS and DOCX remain enabled.
- DOCX conversion needs Fedora's `pandoc-cli` package (the binary is still
  named `pandoc`).

## deepin-scanner

- `cmake/translation-generate.cmake` treats a missing
  `Qt6_LUPDATE_EXECUTABLE`/`Qt6_LRELEASE_EXECUTABLE` as a reason to hard-code
  `/lib/qt6/bin/lupdate` and `/lib/qt6/bin/lrelease`.  Fedora installs the
  tools in `%{_qt6_bindir}`.
- Suggested upstream fix: use `find_program()` with `QT6_INSTALL_PREFIX` /
  `QT6_INSTALL_BINS`, or the Qt6 imported targets.
- Local workaround: the spec rewrites the fallback to `%{_qt6_bindir}`.

## deepin-system-monitor

- The build always runs `deepin-policy-ts-convert` and
  `deepin-desktop-ts-convert` to regenerate the polkit policy and desktop
  file.  Fedora does not ship these Deepin gettext helpers.
- Suggested upstream fix: install the translated files as shipped, or make
  the converters optional build-time tools.
- Local workaround: `01-skip-ts-convert.patch` drops the two custom targets;
  the already translated files are installed directly.

## deepin-voice-note

- `src/common/vnotea2tmanager.cpp` constructs a `QJsonDocument` but only
  includes `<QJsonParseError>`; Qt 6.11 no longer provides the transitive
  include.
- `assets/translate_generation.sh` calls bare `lupdate`/`lrelease`.  Fedora
  installs the Qt 6 tools as `lupdate-qt6`/`lrelease-qt6` in `/usr/bin`.
- Suggested upstream fix: include `<QJsonDocument>` explicitly and use the
  Qt CMake targets or a `command -v` fallback for the translation tools.
- Local workaround: `01-fedora-build-fixes.patch`, which also keeps the 77
  translation `.qm` files in the package.

## deepin-font-manager

- `deepin-font-preview-plugin/main.cpp` uses `Q_PLUGIN_METADATA` with IID
  macros defined only in the dfm headers.  Qt 6.8+ moc does not follow
  includes when expanding the IID, so the plugin fails with
  `Parse error at "IID"`.
- The preview plugin install destination hard-codes `lib/`, which bypasses
  `CMAKE_INSTALL_LIBDIR` and installs into `/usr/lib` on x86_64.
- Suggested upstream fix: define/export the IIDs in the same translation
  unit and use `CMAKE_INSTALL_LIBDIR` for the plugin destination.
- Local workaround: `01-qt6-moc-iid.patch`; the package still ships all 77
  translation `.qm` files.

## dde-seatd / DDM control socket

- DDM 0.5.0 requires `dde-seatd.service` and connects to
  `/run/dde-seatd-control.sock`.  The 0.9.3 tag only provides the old
  `seatd.service`/`/run/seatd.sock` interface and uses the `libseat` name.
- The 0.9.3-3 tag provides the control socket, renames the daemon to
  `dde-seatd`, and installs `libdde-seat` so it can coexist with Fedora's
  `libseat`.
- The package used here is built from 0.9.3-3; Fedora's `seatd` package is
  not required.

## ddm / pam_systemd

- DDM's Fedora PAM stack uses `pam_systemd.so`, but Fedora splits that module
  into `systemd-pam`.  Without it, `pam_open_session` fails with
  `Module is unknown` and DDM cannot open the user session.
- Local fix: the `ddm` package requires `systemd-pam`.

## dtkdeclarative / Qt 6.11 QML palette

- `DTK.makeIconPalette()` was declared with `const QQuickPalette *`.
  Qt 6.11's QML engine cannot build a meta object for that const pointer
  during a QML call and crashes in
  `QtPrivate::MetaObjectForType<const QQuickPalette *>`.
- Local fix: `01-qt611-palette.patch` changes the invokable to take a
  non-const `QQuickPalette *`, matching the QML property type.

## deepin-image-viewer / RAW plugin

- The `xraw` image plugin's `capabilities()` dereferences `device` without
  a null check.  `QImageReader::supportedImageFormats()` calls it with a
  null device, crashing every Qt application that enumerates image formats
  (including Treeland).
- Local fix: `02-raw-plugin-null-device.patch` returns an empty capability
  set when the device is null.

## dde-account-faces

- `accountsservice` owns `/var/lib/AccountsService/icons` with mode 0775;
  `dde-account-faces` owned the same directory with 0755, which RPM treats
  as a file conflict.
- Local fix: list the contents (`icons/*`) instead of owning the directory.

## COPR build order and dependency cycles

The first COPR import exposed three packaging mistakes that made the build
graph cyclic.  They were fixed without bootstrap packages:

- `dde-tray-loader` does not depend on `dde-shell` in upstream Debian
  packaging; it only has `Breaks: dde-shell (<< 2.0.55)`.  Our spec had a hard
  `Requires: dde-shell`, which closed a cycle because `dde-shell` needs
  `dde-tray-loader-devel` at build time.  The runtime requirement is now
  `dde-daemon`, matching upstream.
- `dde-daemon` does not depend on `dde-session` upstream.  Our spec added that
  reverse dependency, which pulled `dde-polkit-agent` into every buildroot
  that installed `dde-application-manager-devel`.
- `dde-daemon` still uses PolicyKit, but now declares `dde-polkit-agent` as a
  `Recommends`.  `dde-session` and the `dde-desktop` meta package require the
  agent explicitly.  COPR/mock buildroots use `install_weak_deps=0`, so the
  weak dependency does not recreate the cycle during builds.

Other dependency-name fixes found by resolving every spec's BuildRequires in a
clean Fedora 45 root:

- `pkgconfig(libmount)` is `pkgconfig(mount)` on Fedora.
- `pkgconfig(libgudev-1.0)` is `pkgconfig(gudev-1.0)`.
- `pkgconfig(utf8proc)` is `pkgconfig(libutf8proc)`.
- `dtk6log`'s CMake package version is `0.7.54` by upstream design, even
  though the RPM version is `6.7.54`; `dtk6core` no longer requires a
  `cmake(Dtk6Log) >= 6.7.54` version.
- `util-dfm`'s `dfm6-search.pc` listed the CMake names `Boostsystem` and
  `Threads` as pkgconfig modules.  They are removed.
- `dde-file-manager`'s `dfm6-base.pc` listed `libappimage`, which Fedora does
  not ship and the AppImage code is disabled.  It is removed from the pc file.
- `dareader-libs` required a `dareader` base package that the spec never
  produced; the bogus requirement is gone.
