# TODO:
# - brcm_egl, libhybris_egl_server
#
# Conditional build:
%bcond_without	doc		# Build documentation
%bcond_without	qtcompositor	# QtCompositor API

%define		orgname		qtwayland
%define		qtbase_ver		%{version}
%define		qtdeclarative_ver	%{version}
%define		qttools_ver		%{version}
Summary:	The Qt5 Wayland libraries
Summary(pl.UTF-8):	Biblioteki Qt5 Wayland
Name:		qt5-%{orgname}
Version:	5.15.10
Release:	1
License:	LGPL v3 or GPL v2 or GPL v3 or commercial
Group:		Libraries
Source0:	https://download.qt.io/official_releases/qt/5.15/%{version}/submodules/%{orgname}-everywhere-opensource-src-%{version}.tar.xz
# Source0-md5:	de32005eba5f53d3bd2886ee14a39809
Patch0:		%{name}-revert-QTBUG-83303.patch
URL:		https://www.qt.io/
BuildRequires:	EGL-devel
BuildRequires:	OpenGL-GLX-devel
BuildRequires:	Qt5AccessibilitySupport-devel >= %{qtbase_ver}
BuildRequires:	Qt5Core-devel >= %{qtbase_ver}
BuildRequires:	Qt5EglSupport-devel >= %{qtbase_ver}
BuildRequires:	Qt5EventDispatcherSupport-devel >= %{qtbase_ver}
BuildRequires:	Qt5FontDatabaseSupport-devel >= %{qtbase_ver}
BuildRequires:	Qt5GlxSupport-devel >= %{qtbase_ver}
BuildRequires:	Qt5Gui-devel >= %{qtbase_ver}
BuildRequires:	Qt5PlatformCompositorSupport-devel >= %{qtbase_ver}
BuildRequires:	Qt5ServiceSupport-devel >= %{qtbase_ver}
BuildRequires:	Qt5ThemeSupport-devel >= %{qtbase_ver}
BuildRequires:	Qt5VulkanSupport-devel >= %{qtbase_ver}
BuildRequires:	Qt5XkbCommonSupport-devel >= %{qtbase_ver}
BuildRequires:	libdrm-devel
BuildRequires:	pkgconfig
%if %{with doc}
BuildRequires:	qt5-assistant >= %{qttools_ver}
%endif
BuildRequires:	qt5-build >= %{qtbase_ver}
BuildRequires:	qt5-qmake >= %{qtbase_ver}
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpmbuild(macros) >= 2.016
BuildRequires:	tar >= 1:1.22
BuildRequires:	wayland-devel >= 1.4.0
BuildRequires:	wayland-egl-devel
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXcomposite-devel
BuildRequires:	xorg-lib-libxkbcommon-devel >= 0.2.0
BuildRequires:	xz
%if %{with qtcompositor}
BuildRequires:	Qt5Qml-devel >= %{qtdeclarative_ver}
BuildRequires:	Qt5Quick-devel >= %{qtdeclarative_ver}
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		specflags	-fno-strict-aliasing
%define		qt5dir		%{_libdir}/qt5

%description
Qt is a cross-platform application and UI framework. Using Qt, you can
write web-enabled applications once and deploy them across desktop,
mobile and embedded systems without rewriting the source code.

This package contains Qt5 Wayland libraries.

%description -l pl.UTF-8
Qt to wieloplatformowy szkielet aplikacji i interfejsów użytkownika.
Przy użyciu Qt można pisać aplikacje powiązane z WWW i wdrażać je w
systemach biurkowych, przenośnych i wbudowanych bez przepisywania kodu
źródłowego.

Ten pakiet zawiera biblioteki Qt5 Wayland.

%package -n Qt5WaylandCompositor
Summary:	The Qt5 WaylandCompositor library
Summary(pl.UTF-8):	Biblioteka Qt5 WaylandCompositor
Group:		Libraries
%requires_eq_to	Qt5Core Qt5Core-devel
Requires:	Qt5Gui >= %{qtbase_ver}
Requires:	Qt5Qml >= %{qtdeclarative_ver}
Requires:	Qt5Quick >= %{qtdeclarative_ver}
Requires:	wayland >= 1.4.0
Requires:	xorg-lib-libxkbcommon >= 0.2.0
Obsoletes:	Qt5Compositor < 5.8.0

%description -n Qt5WaylandCompositor
Qt5 WaylandCompositor library enables the creation of Wayland
compositors using Qt and QtQuick.

%description -n Qt5WaylandCompositor -l pl.UTF-8
Biblioteka Qt5 WaylandCompositor pozwala na tworzenie kompozytorów
Wayland przy użyciu bibliotek Qt i QtQuick.

%package -n Qt5WaylandCompositor-devel
Summary:	Qt5 WaylandCompositor library - development files
Summary(pl.UTF-8):	Biblioteka Qt5 WaylandCompositor - pliki programistyczne
Group:		Development/Libraries
Requires:	OpenGL-devel
Requires:	Qt5WaylandCompositor = %{version}-%{release}
Requires:	Qt5Core-devel >= %{qtbase_ver}
Requires:	Qt5Gui-devel >= %{qtbase_ver}
Requires:	Qt5Network-devel >= %{qtbase_ver}
Requires:	Qt5Qml-devel >= %{qtdeclarative_ver}
Requires:	Qt5Quick-devel >= %{qtdeclarative_ver}
Requires:	wayland-devel >= 1.4.0
Requires:	xorg-lib-libxkbcommon-devel >= 0.2.0
Obsoletes:	Qt5Compositor-devel < 5.8.0

%description -n Qt5WaylandCompositor-devel
Qt5 WaylandCompositor library - development files.

%description -n Qt5WaylandCompositor-devel -l pl.UTF-8
Biblioteka Qt5 WaylandCompositor - pliki programistyczne.

%package -n Qt5WaylandClient
Summary:	The Qt5 WaylandClient library
Summary(pl.UTF-8):	Biblioteka Qt5 WaylandClient
Group:		Libraries
%requires_eq_to	Qt5Core Qt5Core-devel
Requires:	Qt5DBus >= %{qtbase_ver}
Requires:	Qt5Gui >= %{qtbase_ver}
Requires:	wayland >= 1.4.0
Requires:	xorg-lib-libxkbcommon >= 0.2.0

%description -n Qt5WaylandClient
Qt5 WaylandClient library enables Qt applications to be run as Wayland
clients.

%description -n Qt5WaylandClient -l pl.UTF-8
Biblioteka Qt5 WaylandClient pozwala na uruchamianie aplikacji Qt jako
klientów Wayland.

%package -n Qt5WaylandClient-devel
Summary:	Qt5 WaylandClient library - development files
Summary(pl.UTF-8):	Biblioteka Qt5 WaylandClient - pliki programistyczne
Group:		Development/Libraries
Requires:	Qt5Core-devel >= %{qtbase_ver}
Requires:	Qt5DBus-devel >= %{qtbase_ver}
Requires:	Qt5Gui-devel >= %{qtbase_ver}
Requires:	Qt5PlatformCompositorSupport-devel >= %{qtbase_ver}
Requires:	Qt5WaylandClient = %{version}-%{release}
Requires:	wayland-devel >= 1.4.0
Requires:	xorg-lib-libxkbcommon-devel >= 0.2.0

%description -n Qt5WaylandClient-devel
Qt5 WaylandClient library - development files.

%description -n Qt5WaylandClient-devel -l pl.UTF-8
Biblioteka Qt5 WaylandClient - pliki programistyczne.

%package doc
Summary:	Qt5 Wayland documentation in HTML format
Summary(pl.UTF-8):	Dokumentacja do bibliotek Qt5 Wayland w formacie HTML
Group:		Documentation
Requires:	qt5-doc-common >= %{qtbase_ver}
BuildArch:	noarch

%description doc
Qt5 Wayland documentation in HTML format.

%description doc -l pl.UTF-8
Dokumentacja do bibliotek Qt5 Wayland w formacie HTML.

%package doc-qch
Summary:	Qt5 Wayland documentation in QCH format
Summary(pl.UTF-8):	Dokumentacja do bibliotek Qt5 Wayland w formacie QCH
Group:		Documentation
Requires:	qt5-doc-common >= %{qtbase_ver}
BuildArch:	noarch

%description doc-qch
Qt5 Wayland documentation in QCH format.

%description doc-qch -l pl.UTF-8
Dokumentacja do bibliotek Qt5 Wayland w formacie QCH.

%package examples
Summary:	Qt5 Wayland examples
Summary(pl.UTF-8):	Przykłady do bibliotek Qt5 Wayland
Group:		X11/Development/Libraries
BuildArch:	noarch

%description examples
Qt5 Wayland examples.

%description examples -l pl.UTF-8
Przykłady do bibliotek Qt5 Wayland.

%prep
%setup -q -n %{orgname}-everywhere-src-%{version}
%patch0 -p1

%build
%{qmake_qt5} \
	%{?with_qtcompositor:CONFIG+=wayland-compositor}
%{__make}
%{?with_doc:%{__make} docs}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	INSTALL_ROOT=$RPM_BUILD_ROOT

%if %{with doc}
%{__make} install_docs \
	INSTALL_ROOT=$RPM_BUILD_ROOT
%endif

# useless symlinks
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libQt5*.so.5.??
# actually drop *.la, follow policy of not packaging them when *.pc exist
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libQt5*.la

# Prepare some files list
ifecho() {
	r="$RPM_BUILD_ROOT$2"
	if [ -d "$r" ]; then
		echo "%%dir $2" >> $1.files
	elif [ -x "$r" ] ; then
		echo "%%attr(755,root,root) $2" >> $1.files
	elif [ -f "$r" ]; then
		echo "$2" >> $1.files
	else
		echo "Error generation $1 files list!"
		echo "$r: no such file or directory!"
		return 1
	fi
}
ifecho_tree() {
	ifecho $1 $2
	for f in `find $RPM_BUILD_ROOT$2 -printf "%%P "`; do
		ifecho $1 $2/$f
	done
}

# examples present only for QtCompositor (as of 5.5.1)
%if %{with qtcompositor}
echo "%defattr(644,root,root,755)" > examples.files
ifecho_tree examples %{_examplesdir}/qt5/wayland
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%post	-n Qt5WaylandCompositor -p /sbin/ldconfig
%postun	-n Qt5WaylandCompositor -p /sbin/ldconfig

%post	-n Qt5WaylandClient -p /sbin/ldconfig
%postun	-n Qt5WaylandClient -p /sbin/ldconfig

%if %{with qtcompositor}
%files -n Qt5WaylandCompositor
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libQt5WaylandCompositor.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libQt5WaylandCompositor.so.5
%dir %{qt5dir}/plugins/wayland-graphics-integration-server
%attr(755,root,root) %{qt5dir}/plugins/wayland-graphics-integration-server/libqt-wayland-compositor-dmabuf-server-buffer.so
%attr(755,root,root) %{qt5dir}/plugins/wayland-graphics-integration-server/libqt-wayland-compositor-drm-egl-server-buffer.so
%attr(755,root,root) %{qt5dir}/plugins/wayland-graphics-integration-server/libqt-wayland-compositor-linux-dmabuf-unstable-v1.so
%attr(755,root,root) %{qt5dir}/plugins/wayland-graphics-integration-server/libqt-wayland-compositor-shm-emulation-server.so
%attr(755,root,root) %{qt5dir}/plugins/wayland-graphics-integration-server/libqt-wayland-compositor-vulkan-server.so
%attr(755,root,root) %{qt5dir}/plugins/wayland-graphics-integration-server/libqt-wayland-compositor-wayland-egl.so
%attr(755,root,root) %{qt5dir}/plugins/wayland-graphics-integration-server/libqt-wayland-compositor-wayland-eglstream-controller.so
%attr(755,root,root) %{qt5dir}/plugins/wayland-graphics-integration-server/libqt-wayland-compositor-xcomposite-egl.so
%attr(755,root,root) %{qt5dir}/plugins/wayland-graphics-integration-server/libqt-wayland-compositor-xcomposite-glx.so
# dir shared Qt5WaylandClient
%dir %{qt5dir}/qml/QtWayland
%dir %{qt5dir}/qml/QtWayland/Compositor
%attr(755,root,root) %{qt5dir}/qml/QtWayland/Compositor/libqwaylandcompositorplugin.so
%{qt5dir}/qml/QtWayland/Compositor/plugins.qmltypes
%{qt5dir}/qml/QtWayland/Compositor/qmldir
%dir %{qt5dir}/qml/QtWayland/Compositor/TextureSharingExtension
%attr(755,root,root) %{qt5dir}/qml/QtWayland/Compositor/TextureSharingExtension/libqwaylandtexturesharingextension.so
%{qt5dir}/qml/QtWayland/Compositor/TextureSharingExtension/qmldir

%files -n Qt5WaylandCompositor-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libQt5WaylandCompositor.so
%{_libdir}/libQt5WaylandCompositor.prl
%{_includedir}/qt5/QtWaylandCompositor
%{_pkgconfigdir}/Qt5WaylandCompositor.pc
%{_libdir}/cmake/Qt5Gui/Qt5Gui_QWaylandXCompositeEglPlatformIntegrationPlugin.cmake
%{_libdir}/cmake/Qt5Gui/Qt5Gui_QWaylandXCompositeGlxPlatformIntegrationPlugin.cmake
%{_libdir}/cmake/Qt5WaylandCompositor
%{qt5dir}/mkspecs/modules/qt_lib_waylandcompositor.pri
%{qt5dir}/mkspecs/modules/qt_lib_waylandcompositor_private.pri
%endif

%files -n Qt5WaylandClient
%defattr(644,root,root,755)
%doc LICENSE.GPL3-EXCEPT README dist/changes-*
%attr(755,root,root) %{_libdir}/libQt5WaylandClient.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libQt5WaylandClient.so.5
%attr(755,root,root) %{qt5dir}/bin/qtwaylandscanner
%attr(755,root,root) %{qt5dir}/plugins/platforms/libqwayland-egl.so
%attr(755,root,root) %{qt5dir}/plugins/platforms/libqwayland-generic.so
%attr(755,root,root) %{qt5dir}/plugins/platforms/libqwayland-xcomposite-egl.so
%attr(755,root,root) %{qt5dir}/plugins/platforms/libqwayland-xcomposite-glx.so
%dir %{qt5dir}/plugins/wayland-decoration-client
%attr(755,root,root) %{qt5dir}/plugins/wayland-decoration-client/libbradient.so
%dir %{qt5dir}/plugins/wayland-graphics-integration-client
%attr(755,root,root) %{qt5dir}/plugins/wayland-graphics-integration-client/libdmabuf-server.so
%attr(755,root,root) %{qt5dir}/plugins/wayland-graphics-integration-client/libdrm-egl-server.so
%attr(755,root,root) %{qt5dir}/plugins/wayland-graphics-integration-client/libqt-plugin-wayland-egl.so
%attr(755,root,root) %{qt5dir}/plugins/wayland-graphics-integration-client/libshm-emulation-server.so
%attr(755,root,root) %{qt5dir}/plugins/wayland-graphics-integration-client/libvulkan-server.so
%attr(755,root,root) %{qt5dir}/plugins/wayland-graphics-integration-client/libxcomposite-egl.so
%attr(755,root,root) %{qt5dir}/plugins/wayland-graphics-integration-client/libxcomposite-glx.so
%dir %{qt5dir}/plugins/wayland-shell-integration
%attr(755,root,root) %{qt5dir}/plugins/wayland-shell-integration/libfullscreen-shell-v1.so
%attr(755,root,root) %{qt5dir}/plugins/wayland-shell-integration/libivi-shell.so
%attr(755,root,root) %{qt5dir}/plugins/wayland-shell-integration/libwl-shell.so
%attr(755,root,root) %{qt5dir}/plugins/wayland-shell-integration/libxdg-shell.so
%attr(755,root,root) %{qt5dir}/plugins/wayland-shell-integration/libxdg-shell-v5.so
%attr(755,root,root) %{qt5dir}/plugins/wayland-shell-integration/libxdg-shell-v6.so
# dir shared Qt5WaylandCompositor
%dir %{qt5dir}/qml/QtWayland
%dir %{qt5dir}/qml/QtWayland/Client
%dir %{qt5dir}/qml/QtWayland/Client/TextureSharing
%attr(755,root,root) %{qt5dir}/qml/QtWayland/Client/TextureSharing/libqwaylandtexturesharing.so
%{qt5dir}/qml/QtWayland/Client/TextureSharing/qmldir

%files -n Qt5WaylandClient-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libQt5WaylandClient.so
%{_libdir}/libQt5WaylandClient.prl
%{_includedir}/qt5/QtWaylandClient
%{_pkgconfigdir}/Qt5WaylandClient.pc
%{_libdir}/cmake/Qt5Gui/Qt5Gui_QWaylandEglPlatformIntegrationPlugin.cmake
%{_libdir}/cmake/Qt5Gui/Qt5Gui_QWaylandIntegrationPlugin.cmake
%{_libdir}/cmake/Qt5WaylandClient
%{qt5dir}/mkspecs/modules/qt_lib_waylandclient.pri
%{qt5dir}/mkspecs/modules/qt_lib_waylandclient_private.pri

%if %{with doc}
%files doc
%defattr(644,root,root,755)
%{_docdir}/qt5-doc/qtwaylandcompositor

%files doc-qch
%defattr(644,root,root,755)
%{_docdir}/qt5-doc/qtwaylandcompositor.qch
%endif

%if %{with qtcompositor}
%files examples -f examples.files
%defattr(644,root,root,755)
# XXX: dir shared with qt5-qtbase-examples
%dir %{_examplesdir}/qt5
%endif
