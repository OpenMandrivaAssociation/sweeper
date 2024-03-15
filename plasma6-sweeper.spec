#define git 20240218
%define gitbranch release/24.02
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Name:		plasma6-sweeper
Summary:	Clean unwanted traces from your system
Version:	24.02.0
Release:	%{?git:0.%{git}.}2
Group:		Graphical desktop/KDE
License:	LGPLv2
URL:		http://www.kde.org/
%if 0%{?git:1}
Source0:	https://invent.kde.org/utilities/sweeper/-/archive/%{gitbranch}/sweeper-%{gitbranchd}.tar.bz2#/sweeper-%{git}.tar.bz2
%else
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/sweeper-%{version}.tar.xz
%endif
BuildRequires:	cmake cmake(ECM) ninja
BuildRequires:	cmake(PlasmaActivitiesStats) cmake(KF6Bookmarks) cmake(KF6Config) cmake(KF6CoreAddons)
BuildRequires:	cmake(KF6Crash) cmake(KF6I18n) cmake(KF6KIO) cmake(KF6TextWidgets)
BuildRequires:	cmake(KF6WidgetsAddons) cmake(KF6XmlGui) cmake(Qt6Core) cmake(Qt6DBus)
BuildRequires:	cmake(Qt6Gui) cmake(Qt6Widgets) cmake(Qt6Xml)
BuildRequires:	cmake(KF6DocTools)
%description
Sweeper helps to clean unwanted traces the user leaves on the system.

%files -f %{name}.lang
%{_bindir}/sweeper                                                                                     
%{_datadir}/qlogging-categories6/sweeper.categories
%{_datadir}/metainfo/org.kde.sweeper.appdata.xml
%{_datadir}/applications/org.kde.sweeper.desktop                                                          
%{_datadir}/dbus-1/interfaces/org.kde.sweeper.xml                                                      

#----------------------------------------------------------------------

%prep
%autosetup -p1 -n sweeper-%{?git:%{gitbranchd}}%{!?git:%{version}}

%build
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja
%ninja

%install
%ninja_install -C build
%find_lang %{name} --with-html --all-name
