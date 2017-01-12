Summary:	Akonadi Calendar Integration
Name:		akonadi-calendar
Version:	16.12.1
Release:	1
License:	GPLv2+
Group:		Graphical desktop/KDE
Source0:	http://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz
URL:		https://www.kde.org/
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5Gui)
BuildRequires:	pkgconfig(Qt5Test)
BuildRequires:	pkgconfig(Qt5Widgets)
BuildRequires:	cmake(Qt5Test)
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF5KDELibs4Support)
BuildRequires:	cmake(KF5KIO)
BuildRequires:	cmake(KF5Wallet)
BuildRequires:	cmake(KF5Codecs)
BuildRequires:	cmake(KF5MailTransport)
BuildRequires:	cmake(KF5Contacts)
BuildRequires:	cmake(KF5IdentityManagement)
BuildRequires:	cmake(KF5CalendarCore)
BuildRequires:	cmake(KF5CalendarUtils)
BuildRequires:	cmake(KF5Akonadi)
BuildRequires:	cmake(KF5AkonadiContact)
BuildRequires:	boost-devel
BuildRequires:	sasl-devel
BuildRequires:	libxml2-utils
BuildRequires:	docbook-dtds
BuildRequires:	docbook-style-xsl

%description
Akonadi Calendar Integration.

#--------------------------------------------------------------------

%define major 5
%define libname %mklibname KF5AkonadiCalendar %{major}

%package -n %{libname}
Summary:      Akonadi Calendar Integration
Group:        System/Libraries
Obsoletes:    %mklibname kf5akonadicalendar 4
Obsoletes:    %mklibname kf5akonadicalendar 5

%description -n %{libname}
Akonadi Calendar Integration

%files -n %{libname}
%{_libdir}/libKF5AkonadiCalendar.so.%{major}*

#--------------------------------------------------------------------

%define develname %mklibname KF5AkonadiCalendar -d

%package -n %{develname}
Summary:        Devel stuff for %{name}
Group:          Development/KDE and Qt
Requires:       %{libname} = %{EVRD}
Provides:       %{name}-devel = %{EVRD}

%description -n %{develname}
This package contains header files needed if you wish to build applications
based on %{name}.

%files -n %{develname}
%{_includedir}/KF5/Akonadi/Calendar
%{_includedir}/KF5/akonadi/calendar
%{_includedir}/KF5/*_version.h
%{_libdir}/*.so
%{_libdir}/cmake/KF5AkonadiCalendar
%{_libdir}/qt5/mkspecs/modules/*.pri

#--------------------------------------------------------------------

%prep
%setup -q 
%apply_patches
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build
