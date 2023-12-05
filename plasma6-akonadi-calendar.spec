Summary:	Akonadi Calendar Integration
Name:		plasma6-akonadi-calendar
Version:	24.01.80
Release:	1
License:	GPLv2+
Group:		Graphical desktop/KDE
%define is_beta %(if test `echo %{version} |cut -d. -f3` -ge 70; then echo -n 1; else echo -n 0; fi)
%if %{is_beta}
%define ftpdir unstable
%else
%define ftpdir stable
%endif
Source0:	http://download.kde.org/%{ftpdir}/release-service/%{version}/src/akonadi-calendar-%{version}.tar.xz
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

%define major 6
%define libname %mklibname KPim6AkonadiCalendar

Requires:	%{libname} = %{EVRD}

%description
Akonadi Calendar Integration.

%files -f libakonadi-calendar5.lang -f libakonadi-calendar5-serializer.lang -f kalendarac.lang
%{_datadir}/qlogging-categories6/akonadi-calendar.categories
%{_datadir}/qlogging-categories6/akonadi-calendar.renamecategories
%{_libdir}/qt6/plugins/akonadi_serializer_kcalcore.so
%{_datadir}/akonadi/plugins/serializer/akonadi_serializer_kcalcore.desktop
%{_sysconfdir}/xdg/autostart/org.kde.kalendarac.desktop
%{_bindir}/kalendarac
%{_datadir}/dbus-1/services/org.kde.kalendarac.service
%{_datadir}/knotifications6/kalendarac.notifyrc
%{_datadir}/qlogging-categories6/org_kde_kalendarac.categories


#--------------------------------------------------------------------

%package -n %{libname}
Summary:      Akonadi Calendar Integration
Group:        System/Libraries
Requires:     %{name} = %{EVRD}

%description -n %{libname}
Akonadi Calendar Integration

%files -n %{libname}
%{_libdir}/libKPim6AkonadiCalendar.so.*
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
%{_libdir}/*.so
%{_libdir}/cmake/KPim6AkonadiCalendar

#--------------------------------------------------------------------

%prep
%autosetup -p1 -n akonadi-calendar-%{version}
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang libakonadi-calendar5
%find_lang libakonadi-calendar5-serializer
%find_lang kalendarac
