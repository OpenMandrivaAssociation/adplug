%define api 2.2
%define major 0
%define libname %mklibname %name %api %major
%define develname %mklibname -d %name
%define staticname %mklibname -s -d %name

Summary: AdLib sound player library
Name:    adplug
Version: 2.2
Release: 6
Source0: http://prdownloads.sourceforge.net/%name/%{name}-%{version}.tar.bz2
Source1: http://prdownloads.sourceforge.net/adplug/adplug.db.bz2
URL: http://adplug.sourceforge.net/
License: LGPLv2+
Group: Sound

BuildRequires: pkgconfig(libbinio)
BuildRequires: chrpath

%description
AdPlug is a free, multi-platform, hardware independent AdLib sound player
library, mainly written in C++. AdPlug plays sound data, originally created
for the AdLib (OPL2) audio board, on top of an OPL2 emulator or by using the
real hardware. No OPL2 chip is required for playback.

It supports various audio formats from MS-DOS AdLib trackers.

%package -n %libname
Group: System/Libraries
Summary: Shared library of the AdPlug audio emulator

%description -n %libname
AdPlug is a free, multi-platform, hardware independent AdLib sound player
library, mainly written in C++. AdPlug plays sound data, originally created
for the AdLib (OPL2) audio board, on top of an OPL2 emulator or by using the
real hardware. No OPL2 chip is required for playback.

It supports various audio formats from MS-DOS AdLib trackers.

This package contains the shared library required to run applications
based on AdPlug.

%package -n %develname
Group: Development/C++
Summary: Development files of AdPlug
Requires: %libname = %version
Provides: libadplug-devel = %version-%release
Requires: libbinio-devel
Obsoletes: %mklibname -d %name 2.1

%description -n %develname
AdPlug is a free, multi-platform, hardware independent AdLib sound player
library, mainly written in C++. AdPlug plays sound data, originally created
for the AdLib (OPL2) audio board, on top of an OPL2 emulator or by using the
real hardware. No OPL2 chip is required for playback.

It supports various audio formats from MS-DOS AdLib trackers.

This package contains the C++ headers and documentation required for
building programs based on AdPlug.

%package -n %staticname
Group: Development/C++
Summary: Static library of AdPlug
Requires: %develname = %version
Provides: libadplug-static-devel = %version-%release
Obsoletes: %mklibname -s -d %name 2.1

%description -n %staticname
AdPlug is a free, multi-platform, hardware independent AdLib sound player
library, mainly written in C++. AdPlug plays sound data, originally created
for the AdLib (OPL2) audio board, on top of an OPL2 emulator or by using the
real hardware. No OPL2 chip is required for playback.

It supports various audio formats from MS-DOS AdLib trackers.

This package contains the static library required for statically
linking applications based on AdPlug.

%prep
%setup -q
perl -pi -e "s!/usr/local/share/adplug!%_datadir/%name!" doc/adplugdb.1

%build
export CPPFLAGS="-I%_includedir/libbinio"
%configure2_5x
%make

%install
%makeinstall_std
mkdir -p %buildroot%_datadir/%name
bzcat %SOURCE1 > %buildroot%_datadir/%name/adplug.db
chrpath -d %buildroot%_bindir/adplugdb


%files
%doc README
%_bindir/adplugdb
%_mandir/man1/adplugdb.1*
%dir %_datadir/%name/
%_datadir/%name/adplug.db

%files -n %libname
%doc AUTHORS NEWS TODO COPYING
%_libdir/libadplug-%{api}.so.%{major}*

%files -n %develname
%_includedir/adplug/
%_libdir/*.so
%_infodir/libadplug.info*
%_libdir/pkgconfig/*.pc

%files -n %staticname
%_libdir/*.a


%changelog
* Tue Dec 06 2011 GÃ¶tz Waschk <waschk@mandriva.org> 2.2-3mdv2012.0
+ Revision: 738093
- yearly rebuild

* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 2.2-2mdv2011.0
+ Revision: 609907
- rebuild

* Wed Feb 10 2010 GÃ¶tz Waschk <waschk@mandriva.org> 2.2-1mdv2010.1
+ Revision: 503778
- new version
- drop patch
- new libname

* Fri May 22 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.1-3mdv2010.0
+ Revision: 378725
- rebuild

* Wed Apr 22 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.1-2mdv2010.0
+ Revision: 368667
- fix build
- update license

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild early 2009.0 package (before pixel changes)

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Thu Dec 20 2007 Olivier Blin <blino@mandriva.org> 2.1-1mdv2009.0
+ Revision: 135817
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Tue Apr 17 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.1-1mdv2008.0
+ Revision: 14053
- new version
- new major


* Fri Aug 25 2006 Götz Waschk <waschk@mandriva.org> 2.0.1-2mdv2007.0
- remove rpath

* Mon Jul 17 2006 Götz Waschk <waschk@mandriva.org> 2.0.1-1mdv2007.0
- new major
- New release 2.0.1

* Wed Jun 28 2006 Lenny Cartier <lenny@mandriva.com> 2.0-2mdv2007.0
- rebuild

* Fri May 05 2006 Götz Waschk <waschk@mandriva.org> 2.0-1mdk
- new major
- New release 2.0
- use mkrel

* Mon Sep 19 2005 Götz Waschk <waschk@mandriva.org> 1.5.1-2mdk
- adapt for new libbinio header location

* Sun May 15 2005 Götz Waschk <waschk@mandriva.org> 1.5.1-1mdk
- new major
- New release 1.5.1

* Sat Oct 02 2004 Götz Waschk <waschk@linux-mandrake.com> 1.5-1mdk
- new major 1.5
- New release 1.5

* Sat Jun 05 2004 Götz Waschk <waschk@linux-mandrake.com> 1.4.1-4mdk
- new g++
- drop prefix

