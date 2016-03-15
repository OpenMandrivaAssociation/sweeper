Name:		sweeper
Summary:	Clean unwanted traces from your system
Version:	15.12.3
Release:	1
Group:		Graphical desktop/KDE
License:	LGPLv2
URL:		http://www.kde.org/
Source:		http://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	kdelibs-devel

%description
Sweeper helps to clean unwanted traces the user leaves on the system.

%files
%{_datadir}/apps/sweeper                                                                               
%{_bindir}/sweeper                                                                                     
%{_datadir}/applications/kde4/sweeper.desktop                                                          
%{_datadir}/dbus-1/interfaces/org.kde.sweeper.xml                                                      
%doc %{_docdir}/HTML/*/sweeper

#----------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde4 \
	-DCMAKE_MINIMUM_REQUIRED_VERSION=3.1
%make

%install
%makeinstall_std -C build

