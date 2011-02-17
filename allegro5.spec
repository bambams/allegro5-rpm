# vim: noexpandtab textwidth=0
Name:		allegro5
Version:	5.0.0
Release:	1%{?dist}
Summary:	A game programming library.

Group:		System Environment/Libraries
License:	zlib
URL:		http://liballeg.org/
Source0:	http://downloads.sourceforge.net/project/alleg/allegro/5.0.0/allegro-5.0.0.tar.gz
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

BuildRequires:	alsa-lib-devel cmake dumb-devel flac-devel freetype-devel gcc gtk2-devel libcurl-devel libjpeg-devel libpng-devel libvorbis-devel make mesa-libGL-devel mesa-libGLU-devel physfs-devel pulseaudio-libs-devel
Requires:	freetype gtk2 libjpeg libpng mesa-libGL mesa-libGLU physfs pulseaudio-libs

%description


%prep
%setup -n allegro-5.0.0 -q


%build
%cmake .
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT


%post
ldconfig


%postun
ldconfig


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%{_includedir}/allegro5/alcompat.h
%{_includedir}/allegro5/alinline.h
%{_includedir}/allegro5/allegro.h
%{_includedir}/allegro5/allegro5.h
%{_includedir}/allegro5/allegro_direct3d.h
%{_includedir}/allegro5/allegro_opengl.h
%{_includedir}/allegro5/altime.h
%{_includedir}/allegro5/base.h
%{_includedir}/allegro5/bitmap.h
%{_includedir}/allegro5/bitmap_io.h
%{_includedir}/allegro5/color.h
%{_includedir}/allegro5/config.h
%{_includedir}/allegro5/debug.h
%{_includedir}/allegro5/display.h
%{_includedir}/allegro5/error.h
%{_includedir}/allegro5/events.h
%{_includedir}/allegro5/file.h
%{_includedir}/allegro5/fixed.h
%{_includedir}/allegro5/fmaths.h
%{_includedir}/allegro5/fshook.h
%{_includedir}/allegro5/inline/fmaths.inl
%{_includedir}/allegro5/internal/aintern.h
%{_includedir}/allegro5/internal/aintern_atomicops.h
%{_includedir}/allegro5/internal/aintern_bitmap.h
%{_includedir}/allegro5/internal/aintern_blend.h
%{_includedir}/allegro5/internal/aintern_convert.h
%{_includedir}/allegro5/internal/aintern_display.h
%{_includedir}/allegro5/internal/aintern_dtor.h
%{_includedir}/allegro5/internal/aintern_events.h
%{_includedir}/allegro5/internal/aintern_float.h
%{_includedir}/allegro5/internal/aintern_fshook.h
%{_includedir}/allegro5/internal/aintern_joystick.h
%{_includedir}/allegro5/internal/aintern_keyboard.h
%{_includedir}/allegro5/internal/aintern_list.h
%{_includedir}/allegro5/internal/aintern_mouse.h
%{_includedir}/allegro5/internal/aintern_opengl.h
%{_includedir}/allegro5/internal/aintern_pixels.h
%{_includedir}/allegro5/internal/aintern_system.h
%{_includedir}/allegro5/internal/aintern_thread.h
%{_includedir}/allegro5/internal/aintern_tls.h
%{_includedir}/allegro5/internal/aintern_vector.h
%{_includedir}/allegro5/internal/alconfig.h
%{_includedir}/allegro5/joystick.h
%{_includedir}/allegro5/keyboard.h
%{_includedir}/allegro5/keycodes.h
%{_includedir}/allegro5/memory.h
%{_includedir}/allegro5/mouse.h
%{_includedir}/allegro5/opengl/GLext/gl_ext_alias.h
%{_includedir}/allegro5/opengl/GLext/gl_ext_api.h
%{_includedir}/allegro5/opengl/GLext/gl_ext_defs.h
%{_includedir}/allegro5/opengl/GLext/gl_ext_list.h
%{_includedir}/allegro5/opengl/GLext/glx_ext_alias.h
%{_includedir}/allegro5/opengl/GLext/glx_ext_api.h
%{_includedir}/allegro5/opengl/GLext/glx_ext_defs.h
%{_includedir}/allegro5/opengl/GLext/glx_ext_list.h
%{_includedir}/allegro5/opengl/GLext/wgl_ext_alias.h
%{_includedir}/allegro5/opengl/GLext/wgl_ext_api.h
%{_includedir}/allegro5/opengl/GLext/wgl_ext_defs.h
%{_includedir}/allegro5/opengl/GLext/wgl_ext_list.h
%{_includedir}/allegro5/opengl/gl_ext.h
%{_includedir}/allegro5/path.h
%{_includedir}/allegro5/platform/aintlnx.h
%{_includedir}/allegro5/platform/aintosx.h
%{_includedir}/allegro5/platform/aintunix.h
%{_includedir}/allegro5/platform/aintuthr.h
%{_includedir}/allegro5/platform/aintwin.h
%{_includedir}/allegro5/platform/aintwthr.h
%{_includedir}/allegro5/platform/al386gcc.h
%{_includedir}/allegro5/platform/al386vc.h
%{_includedir}/allegro5/platform/al386wat.h
%{_includedir}/allegro5/platform/albcc32.h
%{_includedir}/allegro5/platform/almngw32.h
%{_includedir}/allegro5/platform/almsvc.h
%{_includedir}/allegro5/platform/alosx.h
%{_includedir}/allegro5/platform/alosxcfg.h
%{_includedir}/allegro5/platform/alplatf.h
%{_includedir}/allegro5/platform/alucfg.h
%{_includedir}/allegro5/platform/alunix.h
%{_includedir}/allegro5/platform/alwatcom.h
%{_includedir}/allegro5/platform/alwin.h
%{_includedir}/allegro5/platform/astdbool.h
%{_includedir}/allegro5/platform/astdint.h
%{_includedir}/allegro5/system.h
%{_includedir}/allegro5/threads.h
%{_includedir}/allegro5/timer.h
%{_includedir}/allegro5/tls.h
%{_includedir}/allegro5/transformations.h
%{_includedir}/allegro5/utf8.h
%{_libdir}/liballegro.so
%{_libdir}/liballegro.so.5.0
%{_libdir}/liballegro.so.5.0.0
%{_libdir}/pkgconfig/allegro-5.0.pc

%doc



%changelog


%package devel
Summary:	
Group:		
Requires:	allegro5
%description devel

%files devel

%package addon-acodec
Summary:	
Group:		
Requires:	 allegro5 dumb flac libvorbis
%description addon-acodec

%files addon-acodec
%{_libdir}/liballegro_acodec.so
%{_libdir}/liballegro_acodec.so.5.0
%{_libdir}/liballegro_acodec.so.5.0.0

%package addon-acodec-devel
Summary:	
Group:		
Requires:	allegro5-addon-acodec dumb-devel flac-devel libvorbis-devel
%description addon-acodec-devel

%files addon-acodec-devel
%{_includedir}/allegro5/allegro_acodec.h
%{_libdir}/pkgconfig/allegro_acodec-5.0.pc

%package addon-audio
Summary:	
Group:		
Requires:	allegro5 alsa-lib
%description addon-audio

%files addon-audio
%{_libdir}/liballegro_audio.so
%{_libdir}/liballegro_audio.so.5.0
%{_libdir}/liballegro_audio.so.5.0.0

%package addon-audio-devel
Summary:	
Group:		
Requires:	allegro5-addon-audio alsa-lib-devel
%description addon-audio-devel

%files addon-audio-devel
%{_includedir}/allegro5/allegro_audio.h
%{_libdir}/pkgconfig/allegro_audio-5.0.pc

%package addon-color
Summary:	
Group:		
Requires:	allegro5
%description addon-color

%files addon-color
%{_libdir}/liballegro_color.so
%{_libdir}/liballegro_color.so.5.0
%{_libdir}/liballegro_color.so.5.0.0

%package addon-color-devel
Summary:	
Group:		
Requires:	allegro5-addon-color
%description addon-color-devel

%files addon-color-devel
%{_includedir}/allegro5/allegro_color.h
%{_libdir}/pkgconfig/allegro_color-5.0.pc

%package addon-dialog
Summary:	
Group:		
Requires:	allegro5
%description addon-dialog

%files addon-dialog
%{_libdir}/liballegro_dialog.so
%{_libdir}/liballegro_dialog.so.5.0
%{_libdir}/liballegro_dialog.so.5.0.0

%package addon-dialog-devel
Summary:	
Group:		
Requires:	allegro5-addon-dialog
%description addon-dialog-devel

%files addon-dialog-devel
%{_includedir}/allegro5/allegro_native_dialog.h
%{_libdir}/pkgconfig/allegro_dialog-5.0.pc

%package addon-font
Summary:	
Group:		
Requires:	allegro5
%description addon-font

%files addon-font
%{_libdir}/liballegro_font.so
%{_libdir}/liballegro_font.so.5.0
%{_libdir}/liballegro_font.so.5.0.0

%package addon-font-devel
Summary:	
Group:		
Requires:	allegro5-addon-font
%description addon-font-devel

%files addon-font-devel
%{_includedir}/allegro5/allegro_font.h
%{_libdir}/pkgconfig/allegro_font-5.0.pc

%package addon-image
Summary:	
Group:		
Requires:	allegro5
%description addon-image

%files addon-image
%{_libdir}/liballegro_image.so
%{_libdir}/liballegro_image.so.5.0
%{_libdir}/liballegro_image.so.5.0.0

%package addon-image-devel
Summary:	
Group:		
Requires:	allegro5-addon-image
%description addon-image-devel

%files addon-image-devel
%{_includedir}/allegro5/allegro_image.h
%{_libdir}/pkgconfig/allegro_image-5.0.pc

%package addon-main
Summary:	
Group:		
Requires:	allegro5
%description addon-main

%files addon-main
%{_libdir}/liballegro_main.so
%{_libdir}/liballegro_main.so.5.0
%{_libdir}/liballegro_main.so.5.0.0

%package addon-main-devel
Summary:	
Group:		
Requires:	
%description addon-main-devel

%files addon-main-devel
%{_libdir}/pkgconfig/allegro_main-5.0.pc

%package addon-memfile
Summary:	
Group:		
Requires:	allegro5
%description addon-memfile

%files addon-memfile
%{_libdir}/liballegro_memfile.so
%{_libdir}/liballegro_memfile.so.5.0
%{_libdir}/liballegro_memfile.so.5.0.0

%package addon-memfile-devel
Summary:	
Group:		
Requires:	allegro5-addon-memfile
%description addon-memfile-devel

%files addon-memfile-devel
%{_includedir}/allegro5/allegro_memfile.h
%{_libdir}/pkgconfig/allegro_memfile-5.0.pc

%package addon-physfs
Summary:	
Group:		
Requires:	allegro5
%description addon-physfs

%files addon-physfs
%{_libdir}/liballegro_physfs.so
%{_libdir}/liballegro_physfs.so.5.0
%{_libdir}/liballegro_physfs.so.5.0.0

%package addon-physfs-devel
Summary:	
Group:		
Requires:	allegro5-addon-physfs
%description addon-physfs-devel

%files addon-physfs-devel
%{_includedir}/allegro5/allegro_physfs.h
%{_libdir}/pkgconfig/allegro_physfs-5.0.pc

%package addon-primitives
Summary:	
Group:		
Requires:	allegro5
%description addon-primitives

%files addon-primitives
%{_libdir}/liballegro_primitives.so
%{_libdir}/liballegro_primitives.so.5.0
%{_libdir}/liballegro_primitives.so.5.0.0

%package addon-primitives-devel
Summary:	
Group:		
Requires:	allegro5-addon-primitives
%description addon-primitives-devel

%files addon-primitives-devel
%{_includedir}/allegro5/allegro_primitives.h
%{_libdir}/pkgconfig/allegro_primitives-5.0.pc

%package addon-ttf
Summary:	
Group:		
Requires:	allegro5
%description addon-ttf

%files addon-ttf
%{_libdir}/liballegro_ttf.so
%{_libdir}/liballegro_ttf.so.5.0
%{_libdir}/liballegro_ttf.so.5.0.0

%package addon-ttf-devel
Summary:	
Group:		
Requires:	allegro5-addon-ttf
%description addon-ttf-devel

%files addon-ttf-devel
%{_includedir}/allegro5/allegro_ttf.h
%{_libdir}/pkgconfig/allegro_ttf-5.0.pc

