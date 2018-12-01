%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Name:		sweeper
Summary:	Clean unwanted traces from your system
Version:	18.11.90
Release:	1
Group:		Graphical desktop/KDE
License:	LGPLv2
URL:		http://www.kde.org/
Source0:	http://download.kde.org/%{stable}/applications/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	cmake cmake(ECM) ninja
BuildRequires:	cmake(KF5ActivitiesStats) cmake(KF5Bookmarks) cmake(KF5Config) cmake(KF5CoreAddons)
BuildRequires:	cmake(KF5Crash) cmake(KF5I18n) cmake(KF5KIO) cmake(KF5TextWidgets)
BuildRequires:	cmake(KF5WidgetsAddons) cmake(KF5XmlGui) cmake(Qt5Core) cmake(Qt5DBus)
BuildRequires:	cmake(Qt5Gui) cmake(Qt5Widgets) cmake(Qt5Xml)
BuildRequires:	cmake(KF5DocTools)
%description
Sweeper helps to clean unwanted traces the user leaves on the system.

%files -f %{name}.lang
%{_bindir}/sweeper                                                                                     
%{_datadir}/kxmlgui5/sweeper/sweeperui.rc
%{_datadir}/metainfo/org.kde.sweeper.appdata.xml
%{_datadir}/applications/org.kde.sweeper.desktop                                                          
%{_datadir}/dbus-1/interfaces/org.kde.sweeper.xml                                                      

#----------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde5
%ninja

%install
%ninja_install -C build
%find_lang %{name} --with-html --all-name
