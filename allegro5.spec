# vim: noexpandtab textwidth=74
Name:		allegro5
Version:	5.0.0
Release:	3%{?dist}
Summary:	A game programming library

Group:		System Environment/Libraries
License:	zlib
URL:		http://liballeg.org/
Source0:	http://downloads.sourceforge.net/alleg/allegro-5.0.0.tar.gz
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

BuildRequires:	alsa-lib-devel cmake dumb-devel flac-devel freetype-devel
BuildRequires:	gtk2-devel libjpeg-devel libpng-devel libvorbis-devel
BuildRequires:	libXext-devel libXxf86vm-devel libXrandr-devel
BuildRequires:	libXinerama-devel libXpm-devel mesa-libGL-devel
BuildRequires:	mesa-libGLU-devel openal-soft-devel pandoc physfs-devel
BuildRequires:	pulseaudio-libs-devel

%description
Allegro is a cross-platform library intended for use in computer games
and other types of multimedia programming. Allegro 5 is the latest major
revision of the library, designed to take advantage of modern hardware
(e.g. hardware acceleration using 3D cards) and operating systems.
Although it is not backwards compatible with earlier versions, it still
occupies the same niche and retains a familiar style.

%package devel
Summary:	Development files for the Allegro 5 library
Group:		System Environment/Libraries
Requires:	%{name} = %{version}-%{release}
%description devel
This package is needed to build programs using the Allegro 5 library.
Contains header files and man-page documentation.

%package addon-acodec
Summary:	Audio codec addon for the Allegro 5 library
Group:		System Environment/Libraries
Requires:	%{name} = %{version}-%{release}
%description addon-acodec
This package provides the audio codec addon for the Allegro 5 library.
This addon allows you to load audio sample formats.

%package addon-acodec-devel
Summary:	Header files for the Allegro 5 audio codec addon
Group:		System Environment/Libraries
Requires:	%{name}-addon-acodec = %{version}-%{release}
Requires:	%{name}-devel = %{version}-%{release}
%description addon-acodec-devel
This package is required to build programs that use the Allegro 5 audio
codec addon.

%package addon-audio
Summary:	Audio addon for the Allegro 5 library
Group:		System Environment/Libraries
Requires:	%{name} = %{version}-%{release}
%description addon-audio
This package provides the audio addon for the Allegro 5 library. This
addon allows you to play sounds in your Allegro 5 programs.

%package addon-audio-devel
Summary:	Header files for the Allegro 5 audio addon
Group:		System Environment/Libraries
Requires:	%{name}-addon-audio = %{version}-%{release}
Requires:	%{name}-devel = %{version}-%{release}
%description addon-audio-devel
This package is required to build programs that use the Allegro 5 audio
addon.

%package addon-dialog
Summary:	Dialog addon for the Allegro 5 library
Group:		System Environment/Libraries
Requires:	%{name} = %{version}-%{release}
%description addon-dialog
This package provides the dialog addon for the Allegro 5 library. This
addon allows you to show dialog boxes.

%package addon-dialog-devel
Summary:	Header files for the Allegro 5 dialog addon
Group:		System Environment/Libraries
Requires:	%{name}-addon-dialog = %{version}-%{release}
Requires:	%{name}-devel = %{version}-%{release}
%description addon-dialog-devel
This package is required to build programs that use the Allegro 5 dialog
addon.

%package addon-image
Summary:	Image addon for the Allegro 5 library
Group:		System Environment/Libraries
Requires:	%{name} = %{version}-%{release}
%description addon-image
This package provides the image addon for the Allegro 5 library. Provides
support for loading image file formats.

%package addon-image-devel
Summary:	Header files for the Allegro 5 image addon
Group:		System Environment/Libraries
Requires:	%{name}-addon-image = %{version}-%{release}
Requires:	%{name}-devel = %{version}-%{release}
%description addon-image-devel
This package is required to build programs that use the Allegro 5 image
addon.

%package addon-physfs
Summary:	Physfs addon for the Allegro 5 library
Group:		System Environment/Libraries
Requires:	%{name} = %{version}-%{release}
%description addon-physfs
This package provides the physfs addon for the Allegro 5 library. This
addon provides an interface to the PhysicsFS library, allowing you to
mount virtual file-systems (e.g., archives) and access files as if they
were physically on the file-system.

%package addon-physfs-devel
Summary:	Header files for the Allegro 5 physfs addon
Group:		System Environment/Libraries
Requires:	%{name}-addon-physfs = %{version}-%{release}
%description addon-physfs-devel
This package is required to build programs that use the Allegro 5 physfs
addon.

%package addon-ttf
Summary:	TTF addon for the Allegro 5 library
Group:		System Environment/Libraries
Requires:	%{name} = %{version}-%{release}
%description addon-ttf
This package provides the ttf addon for the Allegro 5 library. This addon
allows you to load and use TTF fonts in your Allegro 5 programs.

%package addon-ttf-devel
Summary:	Header files for the Allegro 5 TTF addon
Group:		System Environment/Libraries
Requires:	%{name}-addon-ttf = %{version}-%{release}
Requires:	%{name}-devel = %{version}-%{release}
%description addon-ttf-devel
This package is required to build programs that use the Allegro 5 ttf
addon.

%prep
%setup -n allegro-5.0.0 -q

%build
%cmake -DMANDIR=%{_mandir} .
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
mkdir %buildroot/%{_sysconfdir}
mv allegro5.cfg %buildroot/%{_sysconfdir}/allegro5rc

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%post addon-acodec -p /sbin/ldconfig

%postun addon-acodec -p /sbin/ldconfig

%post addon-audio -p /sbin/ldconfig

%postun addon-audio -p /sbin/ldconfig

%post addon-dialog -p /sbin/ldconfig

%postun addon-dialog -p /sbin/ldconfig

%post addon-image -p /sbin/ldconfig

%postun addon-image -p /sbin/ldconfig

%post addon-physfs -p /sbin/ldconfig

%postun addon-physfs -p /sbin/ldconfig

%post addon-ttf -p /sbin/ldconfig

%postun addon-ttf -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%config(noreplace) %{_sysconfdir}/allegro5rc
%doc CHANGES-5.0.txt CONTRIBUTORS.txt LICENSE.txt README.txt
%{_libdir}/liballegro.so.5.0
%{_libdir}/liballegro.so.5.0.0
%{_libdir}/liballegro_color.so.5.0
%{_libdir}/liballegro_color.so.5.0.0
%{_libdir}/liballegro_font.so.5.0
%{_libdir}/liballegro_font.so.5.0.0
%{_libdir}/liballegro_main.so.5.0
%{_libdir}/liballegro_main.so.5.0.0
%{_libdir}/liballegro_memfile.so.5.0
%{_libdir}/liballegro_memfile.so.5.0.0
%{_libdir}/liballegro_primitives.so.5.0
%{_libdir}/liballegro_primitives.so.5.0.0

%files devel
%defattr(-,root,root,-)
%{_includedir}/allegro5
%exclude %{_includedir}/allegro5/allegro_acodec.h
%exclude %{_includedir}/allegro5/allegro_audio.h
%exclude %{_includedir}/allegro5/allegro_native_dialog.h
%exclude %{_includedir}/allegro5/allegro_image.h
%exclude %{_includedir}/allegro5/allegro_physfs.h
%exclude %{_includedir}/allegro5/allegro_ttf.h
%{_libdir}/liballegro.so
%{_libdir}/liballegro_color.so
%{_libdir}/liballegro_font.so
%{_libdir}/liballegro_main.so
%{_libdir}/liballegro_memfile.so
%{_libdir}/liballegro_primitives.so
%{_libdir}/pkgconfig/allegro-5.0.pc
%{_libdir}/pkgconfig/allegro_color-5.0.pc
%{_libdir}/pkgconfig/allegro_font-5.0.pc
%{_libdir}/pkgconfig/allegro_main-5.0.pc
%{_libdir}/pkgconfig/allegro_memfile-5.0.pc
%{_libdir}/pkgconfig/allegro_primitives-5.0.pc
%{_mandir}/man3/ALLEGRO_*.3*
%{_mandir}/man3/al_*.3*

%files addon-acodec
%defattr(-,root,root,-)
%{_libdir}/liballegro_acodec.so.5.0
%{_libdir}/liballegro_acodec.so.5.0.0

%files addon-acodec-devel
%defattr(-,root,root,-)
%{_includedir}/allegro5/allegro_acodec.h
%{_libdir}/liballegro_acodec.so
%{_libdir}/pkgconfig/allegro_acodec-5.0.pc

%files addon-audio
%defattr(-,root,root,-)
%{_libdir}/liballegro_audio.so.5.0
%{_libdir}/liballegro_audio.so.5.0.0

%files addon-audio-devel
%defattr(-,root,root,-)
%{_includedir}/allegro5/allegro_audio.h
%{_libdir}/liballegro_audio.so
%{_libdir}/pkgconfig/allegro_audio-5.0.pc

%files addon-dialog
%defattr(-,root,root,-)
%{_libdir}/liballegro_dialog.so.5.0
%{_libdir}/liballegro_dialog.so.5.0.0

%files addon-dialog-devel
%defattr(-,root,root,-)
%{_includedir}/allegro5/allegro_native_dialog.h
%{_libdir}/liballegro_dialog.so
%{_libdir}/pkgconfig/allegro_dialog-5.0.pc

%files addon-image
%defattr(-,root,root,-)
%{_libdir}/liballegro_image.so.5.0
%{_libdir}/liballegro_image.so.5.0.0

%files addon-image-devel
%defattr(-,root,root,-)
%{_includedir}/allegro5/allegro_image.h
%{_libdir}/liballegro_image.so
%{_libdir}/pkgconfig/allegro_image-5.0.pc

%files addon-physfs
%defattr(-,root,root,-)
%{_libdir}/liballegro_physfs.so.5.0
%{_libdir}/liballegro_physfs.so.5.0.0

%files addon-physfs-devel
%defattr(-,root,root,-)
%{_includedir}/allegro5/allegro_physfs.h
%{_libdir}/liballegro_physfs.so
%{_libdir}/pkgconfig/allegro_physfs-5.0.pc

%files addon-ttf
%defattr(-,root,root,-)
%{_libdir}/liballegro_ttf.so.5.0
%{_libdir}/liballegro_ttf.so.5.0.0

%files addon-ttf-devel
%defattr(-,root,root,-)
%{_includedir}/allegro5/allegro_ttf.h
%{_libdir}/liballegro_ttf.so
%{_libdir}/pkgconfig/allegro_ttf-5.0.pc

%changelog
* Wed Mar 09 2011 Brandon McCaig <bamccaig@gmail.com> 5.0.0-3
- Adding file permissions to subpackages.
- Moving devel files (namely .so symlinks) to devel packages.
- Added %%doc section proper; readmes, changes, license, etc.
- Fixed SF.net URI.
- Modified BuildRequires.
- Added main devel dependency to subpackage devels.
- Replaced many al_*.3* manpage files with a glob.
- Replaced many header files with directory and %%exclude macros.
- Added allegro5.cfg file under /etc/allegro5rc.

* Fri Mar 04 2011 Brandon McCaig <bamccaig@gmail.com> 5.0.0-2
- Merged primitives addon packages into core packages.
- Merged memfile addon packages into core packages.
- Merged "main" addon packages into core packages.
- Merged font packages into core packages.
- Merged color packages into core packages.
- Merged doc package into the devel package.
- Fixed spelling mistakes.
- Removed explicit library dependencies.

* Fri Feb 25 2011 Brandon McCaig <bamccaig@gmail.com> 5.0.0-1
- Initial version.

