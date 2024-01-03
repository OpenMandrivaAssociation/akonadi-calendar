Summary:	Akonadi Calendar Integration
Name:		akonadi-calendar
Version:	23.08.4
Release:	2
License:	GPLv2+
Group:		Graphical desktop/KDE
%define is_beta %(if test `echo %{version} |cut -d. -f3` -ge 70; then echo -n 1; else echo -n 0; fi)
%if %{is_beta}
%define ftpdir unstable
%else
%define ftpdir stable
%endif
Source0:	http://download.kde.org/%{ftpdir}/release-service/%{version}/src/%{name}-%{version}.tar.xz
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
BuildRequires:	cmake(KPim5MailTransport)
BuildRequires:	cmake(KPim5MessageCore)
BuildRequires:	cmake(KF5Contacts)
BuildRequires:	cmake(KPim5IdentityManagement)
BuildRequires:	cmake(KF5CalendarCore)
BuildRequires:	cmake(KPim5CalendarUtils)
BuildRequires:	cmake(KPim5Akonadi)
BuildRequires:	cmake(KPim5AkonadiContact)
BuildRequires:	boost-devel
BuildRequires:	sasl-devel
BuildRequires:	libxml2-utils
BuildRequires:	docbook-dtds
BuildRequires:	docbook-style-xsl
# For QCH format docs
BuildRequires: doxygen
BuildRequires: qt5-assistant

%define major 5
%define oldlibname %mklibname KF5AkonadiCalendar 5
%define libname %mklibname KPim5AkonadiCalendar

Requires:	%{libname} = %{EVRD}

%description
Akonadi Calendar Integration.

%files -f libakonadi-calendar5.lang -f libakonadi-calendar5-serializer.lang -f kalendarac.lang
%{_datadir}/qlogging-categories5/akonadi-calendar.categories
%{_datadir}/qlogging-categories5/akonadi-calendar.renamecategories
%{_libdir}/qt5/plugins/akonadi_serializer_kcalcore.so
%{_datadir}/akonadi/plugins/serializer/akonadi_serializer_kcalcore.desktop
%{_sysconfdir}/xdg/autostart/org.kde.kalendarac.desktop
%{_bindir}/kalendarac
%{_datadir}/dbus-1/services/org.kde.kalendarac.service
%{_datadir}/knotifications5/kalendarac.notifyrc
%{_datadir}/qlogging-categories5/org_kde_kalendarac.categories


#--------------------------------------------------------------------

%package -n %{libname}
Summary:      Akonadi Calendar Integration
Group:        System/Libraries
Obsoletes:    %mklibname kf5akonadicalendar 4
Obsoletes:    %mklibname kf5akonadicalendar 5
Requires:     %{name} = %{EVRD}
%rename %{oldlibname}

%description -n %{libname}
Akonadi Calendar Integration

%files -n %{libname}
%{_libdir}/libKPim5AkonadiCalendar.so.%{major}*
%{_libdir}/qt5/plugins/kf5/org.kde.kcalendarcore.calendars/libakonadicalendarplugin.so

#--------------------------------------------------------------------

%define olddevelname %mklibname KF5AkonadiCalendar -d
%define develname %mklibname KPim5AkonadiCalendar -d

%package -n %{develname}
Summary:        Devel stuff for %{name}
Group:          Development/KDE and Qt
Requires:       %{libname} = %{EVRD}
Provides:       %{name}-devel = %{EVRD}
%rename %{olddevelname}

%description -n %{develname}
This package contains header files needed if you wish to build applications
based on %{name}.

%files -n %{develname}
%{_includedir}/KPim5/AkonadiCalendar
%{_libdir}/*.so
%{_libdir}/cmake/KPim5AkonadiCalendar
%{_libdir}/cmake/KF5AkonadiCalendar
%{_libdir}/qt5/mkspecs/modules/*.pri
%optional %doc %{_docdir}/qt5/*.{qch,tags}

#--------------------------------------------------------------------

%prep
%autosetup -p1
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang libakonadi-calendar5
%find_lang libakonadi-calendar5-serializer
%find_lang kalendarac
