#
# Please do not update/rebuild/touch this package before asking first to mikala and/or neoclust
# This package is part of the KDE Stack.
#
#define debug_package %{nil}

Summary:        Akonadi Calendar Integration
Name:           akonadi-calendar
Version: 15.08.0
Release:        1
License:        GPLv2+
Group:          System/Base
Source0:        http://fr2.rpmfind.net/linux/KDE/stable/plasma/%{name}-%{version}.tar.xz

URL:            https://www.kde.org/

BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Test)
BuildRequires:  pkgconfig(Qt5Widgets)

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

BuildRequires:  boost-devel
BuildRequires:  sasl-devel


BuildRequires:	libxml2-utils
BuildRequires:	docbook-dtds
BuildRequires:	docbook-style-xsl

%description
Akonadi Calendar Integration

#--------------------------------------------------------------------

%define kf5akonadicalendar_major 4
%define libkf5akonadicalendar %mklibname kf5akonadicalendar %{kf5akonadicalendar_major}

%package -n %libkf5akonadicalendar
Summary:      Akonadi Calendar Integration
Group:        System/Libraries


%description -n %libkf5akonadicalendar
Akonadi Calendar Integration

%files -n %libkf5akonadicalendar
%_kf5_libdir/libKF5AkonadiCalendar.so.%{kf5akonadicalendar_major}*
%_kf5_libdir/libKF5AkonadiCalendar.so.5

#--------------------------------------------------------------------

%define kf5akonadicalendar_devel %mklibname kf5akonadicalendar -d

%package -n %kf5akonadicalendar_devel

Summary:        Devel stuff for %name
Group:          Development/KDE and Qt
Requires:       %libkf5akonadicalendar = %version-%release
Provides:       %name-devel = %{version}-%{release}

%description -n %kf5akonadicalendar_devel
This package contains header files needed if you wish to build applications
based on %name.

%files -n %kf5akonadicalendar_devel
%_kf5_includedir/Akonadi/Calendar
%_kf5_includedir/akonadi/calendar
%_kf5_includedir/*_version.h
%_kf5_libdir/*.so
%_kf5_libdir/cmake/KF5AkonadiCalendar
%_qt5_prefix/mkspecs/modules/*.pri

#--------------------------------------------------------------------

%prep
%setup -q 
%apply_patches

%build
%cmake_kde5
%ninja

%install
%ninja_install -C build


