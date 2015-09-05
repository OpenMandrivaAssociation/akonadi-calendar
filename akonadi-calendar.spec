#
# Please do not update/rebuild/touch this package before asking first to mikala and/or neoclust
# This package is part of the KDE Stack.
#
#define debug_package %{nil}

%define rel 1

Summary:        Akonadi Calendar Integration
Name:           akonadi-calendar
Version: 15.08.0
Release:        %mkrel %rel
License:        GPLv2+
Group:          System/Base
Source0:        http://fr2.rpmfind.net/linux/KDE/stable/plasma/%{name}-%{version}.tar.xz

URL:            https://www.kde.org/

BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Test)
BuildRequires:  pkgconfig(Qt5Widgets)

BuildRequires:  kf5-macros
BuildRequires:  kdelibs4support-devel >= 5.12.0
BuildRequires:  kio-devel >= 5.12.0
BuildRequires:  kwallet-devel >= 5.12.0
BuildRequires:  kcodecs-devel >= 5.12.0
BuildRequires:  kmailtransport-devel 
BuildRequires:  kcontacts-devel
BuildRequires:  kidentitymanagement-devel
BuildRequires:  kcalcore-devel
BuildRequires:  kcalutils-devel
BuildRequires:  akonadi-devel
BuildRequires:  kdepimlibs-devel

BuildRequires:  boost-devel
BuildRequires:  pkgconfig(libsasl2)


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
%cmake_kf5
%make

%install
%makeinstall_std -C build

%find_lang --all %{name}5



%changelog
* Wed Aug 19 2015 neoclust <neoclust> 15.08.0-1.mga6
+ Revision: 865896
- New version 15.08.0
- New version 15.07.90

* Wed Aug 12 2015 neoclust <neoclust> 15.07.90-2.mga6
+ Revision: 863755
- Plasma Mass Rebuild - Rebuild for new Plasma

* Sun Aug 09 2015 neoclust <neoclust> 15.07.90-1.mga6
+ Revision: 861709
- New version 15.07.90

* Tue Jul 28 2015 neoclust <neoclust> 15.07.80-1.mga6
+ Revision: 858656
- imported package akonadi-calendar

