# TODO:
# - brcm_egl, libhybris_egl_server
# - enable docs & examples when ready upstream
#
# Conditional build:
%bcond_with	qch		# documentation in QCH format [TODO: enable when docs exist]
%bcond_without	qtcompositor	# QtCompositor API

%define		orgname		qtwayland
%define		qtbase_ver		%{version}
%define		qtdeclarative_ver	%{version}
%define		qttools_ver		%{version}
Summary:	The Qt5 Wayland libraries
Summary(pl.UTF-8):	Biblioteki Qt5 Wayland
Name:		qt5-%{orgname}
Version:	5.4.2
Release:	1
License:	LGPL v2.1 with Digia Qt LGPL Exception v1.1 or GPL v3.0
Group:		Libraries
Source0:	http://download.qt.io/official_releases/qt/5.4/%{version}/submodules/%{orgname}-opensource-src-%{version}.tar.xz
# Source0-md5:	68de7d22a4275e55e787fb8b0f0e2896
URL:		http://qt-project.org/
BuildRequires:	EGL-devel
BuildRequires:	Mesa-libwayland-egl-devel
BuildRequires:	OpenGL-GLX-devel
BuildRequires:	Qt5Core-devel >= %{qtbase_ver}
BuildRequires:	Qt5Gui-devel >= %{qtbase_ver}
BuildRequires:	Qt5PlatformSupport-devel >= %{qtbase_ver}
BuildRequires:	pkgconfig
%if %{with qch}
BuildRequires:	qt5-assistant >= %{qttools_ver}
%endif
BuildRequires:	qt5-build >= %{qtbase_ver}
BuildRequires:	qt5-qmake >= %{qtbase_ver}
BuildRequires:	rpmbuild(macros) >= 1.654
BuildRequires:	tar >= 1:1.22
BuildRequires:	wayland-devel >= 1.2.0
BuildRequires:	xorg-lib-libXcomposite-devel
BuildRequires:	xorg-lib-libxkbcommon-devel >= 0.2.0
BuildRequires:	xz
%if %{with qtcompositor}
BuildRequires:	Qt5Qml-devel >= %{qtdeclarative_ver}
BuildRequires:	Qt5Quick-devel >= %{qtdeclarative_ver}
BuildRequires:	xorg-lib-libX11-devel
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

%package -n Qt5Compositor
Summary:	The Qt5 Compositor library
Summary(pl.UTF-8):	Biblioteka Qt5 Compositor
Group:		Libraries
Requires:	Qt5Core >= %{qtbase_ver}
Requires:	Qt5Gui >= %{qtbase_ver}
Requires:	Qt5Network >= %{qtbase_ver}
Requires:	Qt5Qml >= %{qtdeclarative_ver}
Requires:	Qt5Quick >= %{qtdeclarative_ver}
Requires:	wayland >= 1.2.0
Requires:	xorg-lib-libxkbcommon >= 0.2.0

%description -n Qt5Compositor
Qt5 Compositor library enables the creation of Wayland compositors
using Qt and QtQuick.

%description -n Qt5Compositor -l pl.UTF-8
Biblioteka Qt5 Compositor pozwala na tworzenie kompozytorów Wayland
przy użyciu bibliotek Qt i QtQuick.

%package -n Qt5Compositor-devel
Summary:	Qt5 Compositor library - development files
Summary(pl.UTF-8):	Biblioteka Qt5 Compositor - pliki programistyczne
Group:		Development/Libraries
Requires:	OpenGL-devel
Requires:	Qt5Compositor = %{version}-%{release}
Requires:	Qt5Core-devel >= %{qtbase_ver}
Requires:	Qt5Gui-devel >= %{qtbase_ver}
Requires:	Qt5Network-devel >= %{qtbase_ver}
Requires:	Qt5Qml-devel >= %{qtdeclarative_ver}
Requires:	Qt5Quick-devel >= %{qtdeclarative_ver}
Requires:	wayland-devel >= 1.2.0
Requires:	xorg-lib-libxkbcommon-devel >= 0.2.0

%description -n Qt5Compositor-devel
Qt5 Compositor library - development files.

%description -n Qt5Compositor-devel -l pl.UTF-8
Biblioteka Qt5 Compositor - pliki programistyczne.

%package -n Qt5WaylandClient
Summary:	The Qt5 WaylandClient library
Summary(pl.UTF-8):	Biblioteka Qt5 WaylandClient
Group:		Libraries
Requires:	Qt5Core >= %{qtbase_ver}
Requires:	Qt5Gui >= %{qtbase_ver}
Requires:	wayland >= 1.2.0
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
Requires:	Qt5PlatformSupport-devel >= %{qtbase_ver}
Requires:	Qt5WaylandClient = %{version}-%{release}
Requires:	wayland-devel >= 1.2.0
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
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description doc
Qt5 Wayland documentation in HTML format.

%description doc -l pl.UTF-8
Dokumentacja do bibliotek Qt5 Wayland w formacie HTML.

%package doc-qch
Summary:	Qt5 Wayland documentation in QCH format
Summary(pl.UTF-8):	Dokumentacja do bibliotek Qt5 Wayland w formacie QCH
Group:		Documentation
Requires:	qt5-doc-common >= %{qtbase_ver}
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description doc-qch
Qt5 Wayland documentation in QCH format.

%description doc-qch -l pl.UTF-8
Dokumentacja do bibliotek Qt5 Wayland w formacie QCH.

%package examples
Summary:	Qt5 Wayland examples
Summary(pl.UTF-8):	Przykłady do bibliotek Qt5 Wayland
Group:		X11/Development/Libraries
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description examples
Qt5 Wayland examples.

%description examples -l pl.UTF-8
Przykłady do bibliotek Qt5 Wayland.

%prep
%setup -q -n %{orgname}-opensource-src-%{version}

%build
qmake-qt5 \
	%{?with_qtcompositor:CONFIG+=wayland-compositor}
%{__make}
%{__make} %{!?with_qch:html_}docs

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	INSTALL_ROOT=$RPM_BUILD_ROOT

%{__make} install_%{!?with_qch:html_}docs \
	INSTALL_ROOT=$RPM_BUILD_ROOT

# useless symlinks
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libQt5*.so.5.?
# actually drop *.la, follow policy of not packaging them when *.pc exist
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libQt5*.la

# no proper cmake support as of 5.4.1
%{__rm} $RPM_BUILD_ROOT%{_libdir}/cmake/{Qt5Gui/Qt5Gui_,Qt5WaylandClient/Qt5WaylandClient_}.cmake
%if %{with qtcompositor}
%{__rm} $RPM_BUILD_ROOT%{_libdir}/cmake/Qt5Compositor/Qt5Compositor_.cmake
%endif

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

# examples present only for QtCompositor (as of 5.4.1)
%if %{with qtcompositor}
echo "%defattr(644,root,root,755)" > examples.files
ifecho_tree examples %{_examplesdir}/qt5/wayland
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%post	-n Qt5Compositor -p /sbin/ldconfig
%postun	-n Qt5Compositor -p /sbin/ldconfig

%post	-n Qt5WaylandClient -p /sbin/ldconfig
%postun	-n Qt5WaylandClient -p /sbin/ldconfig

%if %{with qtcompositor}
%files -n Qt5Compositor
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libQt5Compositor.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libQt5Compositor.so.5
%attr(755,root,root) %{qt5dir}/plugins/platforms/libqwayland-xcomposite-egl.so
%attr(755,root,root) %{qt5dir}/plugins/platforms/libqwayland-xcomposite-glx.so
%dir %{qt5dir}/plugins/wayland-graphics-integration-server
%attr(755,root,root) %{qt5dir}/plugins/wayland-graphics-integration-server/libdrm-egl-server.so
%attr(755,root,root) %{qt5dir}/plugins/wayland-graphics-integration-server/libwayland-egl.so
%attr(755,root,root) %{qt5dir}/plugins/wayland-graphics-integration-server/libxcomposite-egl.so
%attr(755,root,root) %{qt5dir}/plugins/wayland-graphics-integration-server/libxcomposite-glx.so

%files -n Qt5Compositor-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libQt5Compositor.so
%{_libdir}/libQt5Compositor.prl
%{_includedir}/qt5/QtCompositor
%{_pkgconfigdir}/Qt5Compositor.pc
%{_libdir}/cmake/Qt5Compositor
%{qt5dir}/mkspecs/modules/qt_lib_compositor.pri
%{qt5dir}/mkspecs/modules/qt_lib_compositor_private.pri
%endif

%files -n Qt5WaylandClient
%defattr(644,root,root,755)
%doc LGPL_EXCEPTION.txt README
# dist/changes-*
%attr(755,root,root) %{_libdir}/libQt5WaylandClient.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libQt5WaylandClient.so.5
%attr(755,root,root) %{qt5dir}/bin/qtwaylandscanner
%attr(755,root,root) %{qt5dir}/plugins/platforms/libqwayland-egl.so
%attr(755,root,root) %{qt5dir}/plugins/platforms/libqwayland-generic.so
%dir %{qt5dir}/plugins/wayland-decoration-client
%attr(755,root,root) %{qt5dir}/plugins/wayland-decoration-client/libbradient.so
%dir %{qt5dir}/plugins/wayland-graphics-integration-client
%attr(755,root,root) %{qt5dir}/plugins/wayland-graphics-integration-client/libdrm-egl-server.so
%attr(755,root,root) %{qt5dir}/plugins/wayland-graphics-integration-client/libwayland-egl.so
%attr(755,root,root) %{qt5dir}/plugins/wayland-graphics-integration-client/libxcomposite-egl.so
%attr(755,root,root) %{qt5dir}/plugins/wayland-graphics-integration-client/libxcomposite-glx.so

%files -n Qt5WaylandClient-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libQt5WaylandClient.so
%{_libdir}/libQt5WaylandClient.prl
%{_includedir}/qt5/QtWaylandClient
%{_pkgconfigdir}/Qt5WaylandClient.pc
# FIXME (see above)
#%{_libdir}/cmake/Qt5Gui/Qt5Gui_???.cmake
#%{_libdir}/cmake/Qt5WaylandClient
%{qt5dir}/mkspecs/modules/qt_lib_waylandclient.pri
%{qt5dir}/mkspecs/modules/qt_lib_waylandclient_private.pri

# not finished
%if 0
%files doc
%defattr(644,root,root,755)
%{_docdir}/qt5-doc/qtenginio
%{_docdir}/qt5-doc/qtenginiooverview
%{_docdir}/qt5-doc/qtenginioqml

%if %{with qch}
%files doc-qch
%defattr(644,root,root,755)
%{_docdir}/qt5-doc/qtenginio.qch
%{_docdir}/qt5-doc/qtenginiooverview.qch
%{_docdir}/qt5-doc/qtenginioqml.qch
%endif
%endif

%if %{with qtcompositor}
%files examples -f examples.files
%defattr(644,root,root,755)
# XXX: dir shared with qt5-qtbase-examples
%dir %{_examplesdir}/qt5
%endif
