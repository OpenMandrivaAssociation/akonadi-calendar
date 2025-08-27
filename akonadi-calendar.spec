#define git 20240217
%define gitbranch release/24.02
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")
Summary:	Akonadi Calendar Integration
Name:		akonadi-calendar
Version:	25.08.0
Release:	%{?git:0.%{git}.}1
License:	GPLv2+
Group:		Graphical desktop/KDE
%define is_beta %(if test `echo %{version} |cut -d. -f3` -ge 70; then echo -n 1; else echo -n 0; fi)
%if %{is_beta}
%define ftpdir unstable
%else
%define ftpdir stable
%endif
%if 0%{?git:1}
Source0:	https://invent.kde.org/pim/akonadi-calendar/-/archive/%{gitbranch}/akonadi-calendar-%{gitbranchd}.tar.bz2#/akonadi-calendar-%{git}.tar.bz2
%else
Source0:	http://download.kde.org/%{ftpdir}/release-service/%{version}/src/akonadi-calendar-%{version}.tar.xz
%endif
URL:		https://www.kde.org/
BuildRequires:	cmake(Qt6)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6Gui)
BuildRequires:	cmake(Qt6Test)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	cmake(Qt6Test)
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF6KIO)
BuildRequires:	cmake(KF6Wallet)
BuildRequires:	cmake(KF6Codecs)
BuildRequires:	cmake(KPim6MailTransport)
BuildRequires:	cmake(KPim6MessageCore)
BuildRequires:	cmake(KF6Contacts)
BuildRequires:	cmake(KPim6IdentityManagementCore)
BuildRequires:	cmake(KF6CalendarCore)
BuildRequires:	cmake(KPim6CalendarUtils)
BuildRequires:	cmake(KPim6Akonadi)
BuildRequires:	cmake(KPim6AkonadiContactCore)
BuildRequires:	cmake(KF6Notifications)
BuildRequires:	cmake(KF6TextTemplate)
BuildRequires:	boost-devel
BuildRequires:	sasl-devel
BuildRequires:	libxml2-utils
BuildRequires:	docbook-dtds
BuildRequires:	docbook-style-xsl
# For QCH format docs
BuildRequires: doxygen
BuildRequires: qt6-qttools-assistant
BuildSystem:	cmake
BuildOption:	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON
# Renamed after 6.0 2025-07-10
%rename plasma6-akonadi-calendar

%define major 6
%define libname %mklibname KPim6AkonadiCalendar

Requires:	%{libname} = %{EVRD}

%description
Akonadi Calendar Integration.

%files -f libakonadi-calendar6.lang -f libakonadi-calendar6-serializer.lang -f kalendarac.lang
%{_datadir}/qlogging-categories6/akonadi-calendar.categories
%{_datadir}/qlogging-categories6/akonadi-calendar.renamecategories
%{_libdir}/qt6/plugins/akonadi_serializer_kcalcore.so
%{_datadir}/akonadi/plugins/serializer/akonadi_serializer_kcalcore.desktop
%{_sysconfdir}/xdg/autostart/org.kde.kalendarac.desktop
%{_bindir}/kalendarac
%{_datadir}/dbus-1/services/org.kde.kalendarac.service
%{_datadir}/knotifications6/kalendarac.notifyrc
%{_datadir}/qlogging-categories6/org_kde_kalendarac.categories
%{_datadir}/knotifications6/notification_gui.notifyrc

#--------------------------------------------------------------------

%package -n %{libname}
Summary:      Akonadi Calendar Integration
Group:        System/Libraries
Requires:     %{name} = %{EVRD}

%description -n %{libname}
Akonadi Calendar Integration

%files -n %{libname}
%{_libdir}/libKPim6AkonadiCalendar.so.*
%{_libdir}/libKPim6AkonadiCalendarCore.so.*
%{_libdir}/qt6/plugins/kf6/org.kde.kcalendarcore.calendars/libakonadicalendarplugin.so

#--------------------------------------------------------------------

%define develname %mklibname KPim6AkonadiCalendar -d

%package -n %{develname}
Summary:        Devel stuff for %{name}
Group:          Development/KDE and Qt
Requires:       %{libname} = %{EVRD}
Provides:       %{name}-devel = %{EVRD}

%description -n %{develname}
This package contains header files needed if you wish to build applications
based on %{name}.

%files -n %{develname}
%{_includedir}/KPim6/AkonadiCalendar
%{_includedir}/KPim6/AkonadiCalendarCore
%{_libdir}/*.so
%{_libdir}/cmake/KPim6AkonadiCalendar
%{_libdir}/cmake/KPim6AkonadiCalendarCore

#--------------------------------------------------------------------

%install -a
%find_lang libakonadi-calendar6
%find_lang libakonadi-calendar6-serializer
%find_lang kalendarac
