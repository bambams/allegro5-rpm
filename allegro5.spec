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
Requires:	alsa-lib dumb flac freetype gtk2 libjpeg libpng libvorbis mesa-libGL mesa-libGLU physfs pulseaudio-libs

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
%{_includedir}/allegro5/allegro_acodec.h
%{_includedir}/allegro5/allegro_audio.h
%{_includedir}/allegro5/allegro_color.h
%{_includedir}/allegro5/allegro_direct3d.h
%{_includedir}/allegro5/allegro_font.h
%{_includedir}/allegro5/allegro_image.h
%{_includedir}/allegro5/allegro_memfile.h
%{_includedir}/allegro5/allegro_native_dialog.h
%{_includedir}/allegro5/allegro_opengl.h
%{_includedir}/allegro5/allegro_physfs.h
%{_includedir}/allegro5/allegro_primitives.h
%{_includedir}/allegro5/allegro_ttf.h
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
%{_libdir}/liballegro_acodec.so
%{_libdir}/liballegro_acodec.so.5.0
%{_libdir}/liballegro_acodec.so.5.0.0
%{_libdir}/liballegro_audio.so
%{_libdir}/liballegro_audio.so.5.0
%{_libdir}/liballegro_audio.so.5.0.0
%{_libdir}/liballegro_color.so
%{_libdir}/liballegro_color.so.5.0
%{_libdir}/liballegro_color.so.5.0.0
%{_libdir}/liballegro_dialog.so
%{_libdir}/liballegro_dialog.so.5.0
%{_libdir}/liballegro_dialog.so.5.0.0
%{_libdir}/liballegro_font.so
%{_libdir}/liballegro_font.so.5.0
%{_libdir}/liballegro_font.so.5.0.0
%{_libdir}/liballegro_image.so
%{_libdir}/liballegro_image.so.5.0
%{_libdir}/liballegro_image.so.5.0.0
%{_libdir}/liballegro_main.so
%{_libdir}/liballegro_main.so.5.0
%{_libdir}/liballegro_main.so.5.0.0
%{_libdir}/liballegro_memfile.so
%{_libdir}/liballegro_memfile.so.5.0
%{_libdir}/liballegro_memfile.so.5.0.0
%{_libdir}/liballegro_physfs.so
%{_libdir}/liballegro_physfs.so.5.0
%{_libdir}/liballegro_physfs.so.5.0.0
%{_libdir}/liballegro_primitives.so
%{_libdir}/liballegro_primitives.so.5.0
%{_libdir}/liballegro_primitives.so.5.0.0
%{_libdir}/liballegro_ttf.so
%{_libdir}/liballegro_ttf.so.5.0
%{_libdir}/liballegro_ttf.so.5.0.0
%{_libdir}/pkgconfig/allegro-5.0.pc
%{_libdir}/pkgconfig/allegro_acodec-5.0.pc
%{_libdir}/pkgconfig/allegro_audio-5.0.pc
%{_libdir}/pkgconfig/allegro_color-5.0.pc
%{_libdir}/pkgconfig/allegro_dialog-5.0.pc
%{_libdir}/pkgconfig/allegro_font-5.0.pc
%{_libdir}/pkgconfig/allegro_image-5.0.pc
%{_libdir}/pkgconfig/allegro_main-5.0.pc
%{_libdir}/pkgconfig/allegro_memfile-5.0.pc
%{_libdir}/pkgconfig/allegro_physfs-5.0.pc
%{_libdir}/pkgconfig/allegro_primitives-5.0.pc
%{_libdir}/pkgconfig/allegro_ttf-5.0.pc

%doc



%changelog


%package devel
Summary:	
Group:		
%description devel

%files devel

%package addon-acodec
Summary:	
Group:		
%description addon-acodec

%files addon-acodec

%package addon-acodec-devel
Summary:	
Group:		
%description addon-acodec-devel

%files addon-acodec-devel

%package addon-audio
Summary:	
Group:		
%description addon-audio

%files addon-audio

%package addon-audio-devel
Summary:	
Group:		
%description addon-audio-devel

%files addon-audio-devel

%package addon-color
Summary:	
Group:		
%description addon-color

%files addon-color

%package addon-color-devel
Summary:	
Group:		
%description addon-color-devel

%files addon-color-devel

%package addon-dialog
Summary:	
Group:		
%description addon-dialog

%files addon-dialog

%package addon-dialog-devel
Summary:	
Group:		
%description addon-dialog-devel

%files addon-dialog-devel

%package addon-font
Summary:	
Group:		
%description addon-font

%files addon-font

%package addon-font-devel
Summary:	
Group:		
%description addon-font-devel

%files addon-font-devel

%package addon-image
Summary:	
Group:		
%description addon-image

%files addon-image

%package addon-image-devel
Summary:	
Group:		
%description addon-image-devel

%files addon-image-devel

%package addon-main
Summary:	
Group:		
%description addon-main

%files addon-main

%package addon-main-devel
Summary:	
Group:		
%description addon-main-devel

%files addon-main-devel

%package addon-memfile
Summary:	
Group:		
%description addon-memfile

%files addon-memfile

%package addon-memfile-devel
Summary:	
Group:		
%description addon-memfile-devel

%files addon-memfile-devel

%package addon-physfs
Summary:	
Group:		
%description addon-physfs

%files addon-physfs

%package addon-physfs-devel
Summary:	
Group:		
%description addon-physfs-devel

%files addon-physfs-devel

%package addon-primitives
Summary:	
Group:		
%description addon-primitives

%files addon-primitives

%package addon-primitives-devel
Summary:	
Group:		
%description addon-primitives-devel

%files addon-primitives-devel

%package addon-ttf
Summary:	
Group:		
%description addon-ttf

%files addon-ttf

%package addon-ttf-devel
Summary:	
Group:		
%description addon-ttf-devel

%files addon-ttf-devel

