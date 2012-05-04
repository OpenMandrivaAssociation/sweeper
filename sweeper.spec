Name:    sweeper
Summary: Clean unwanted traces from your system
Version: 4.8.3
Release: 1
Group:   Graphical desktop/KDE
License: LGPLv2
URL:     http://www.kde.org/
Source:  ftp://ftp.kde.org/pub/kde/stable/%version/src/%{name}-%version.tar.xz

BuildRequires: kdelibs4-devel >= 2:%{version}

%description
Sweeper helps to clean unwanted traces the user leaves on the system.

%files
%_kde_appsdir/sweeper
%_kde_bindir/sweeper
%_kde_datadir/applications/kde4/sweeper.desktop
%_kde_datadir/dbus-1/interfaces/org.kde.sweeper.xml
%_kde_docdir/HTML/*/sweeper

#----------------------------------------------------------------------

%prep
%setup -q 

%build
%cmake_kde4
	
%make

%install
%makeinstall_std -C build

