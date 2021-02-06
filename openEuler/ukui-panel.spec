%define debug_package %{nil}

Name:           ukui-panel
Version:        3.0.3
Release:        1
Summary:        ukui desktop panel
License:        LGPL-2.1+ GPL-2+ LGPL-3
URL:            http://www.ukui.org
Source0:        %{name}-%{version}.tar.gz

BuildRequires: cmake
BuildRequires: alsa-lib-devel
BuildRequires: dbusmenu-qt5-devel
BuildRequires: glib2-devel >= 2.36
BuildRequires: libicu-devel
BuildRequires: kf5-solid-devel
BuildRequires: kf5-kwindowsystem-devel
BuildRequires: pulseaudio-devel
BuildRequires: qt5-qtsvg-devel
BuildRequires: qt5-qtx11extras-devel
BuildRequires: lm_sensors-devel
BuildRequires: libstatgrab-devel
BuildRequires: libsysstat-devel >= 0.4.2
BuildRequires: libX11-devel
BuildRequires: xcb-util-devel
BuildRequires: libxcb-devel
BuildRequires: libXcomposite-devel
BuildRequires: libXdamage-devel
BuildRequires: libxkbcommon-devel
BuildRequires: libxkbcommon-x11-devel
BuildRequires: libXrender-devel
BuildRequires: qt5-qtwebkit-devel
BuildRequires: qt5-qttools-devel
BuildRequires: libqtxdg-devel
BuildRequires: gsettings-qt-devel
BuildRequires: poppler-devel
BuildRequires: poppler-qt5-devel
BuildRequires: libpeony-dev
BuildRequires: dconf-devel
BuildRequires: libpeony-dev

Provides: ukui-indicators

Suggests: ukui-window-switch >= 3.0.0-3
Suggests: time-shutdown

%description
 The ukui desktop panel is used on ukui desktop and has some plugins like
 starmenu, quicklaunch and other useful tools.
 This package contains the ukui panel.

%prep
%setup -q

%build
mkdir build && cd build
%{cmake3} ..

%install
rm -rf $RPM_BUILD_ROOT
cd %{_builddir}/%{name}-%{version}/build
make DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc debian/copyright  debian/changelog
%{_sysconfdir}/xdg/autostart/*
%{_bindir}/*
%{_includedir}/ukui/*
%{_libdir}/*
%{_datadir}/*

%changelog
* Thu Jan 28 2021 lvhan <lvhan@kylinos.cn> - 3.0.3-1
- update to upstream version 3.0.3-1

* Fri Dec 4 2020 lvhan <lvhan@kylinos.cn> - 3.0.2-4
- block taskbar right click

* Fri Dec 4 2020 lvhan <lvhan@kylinos.cn> - 3.0.2-3
- fix calendar

* Thu Dec 3 2020 douyan <douyan@kylinos.cn> - 3.0.2-2
- block calendar

* Mon Oct 26 2020 douyan <douyan@kylinos.cn> - 3.0.2-1
- update to upstream version 3.0.1-1+1028

* Thu Jul 9 2020 douyan <douyan@kylinos.cn> - 2.0.8-1
- Init package for openEuler
