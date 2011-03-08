# vim: noexpandtab textwidth=74
Name:		allegro5
Version:	5.0.0
Release:	2%{?dist}
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
%{_includedir}/allegro5/alcompat.h
%{_includedir}/allegro5/alinline.h
%{_includedir}/allegro5/allegro.h
%{_includedir}/allegro5/allegro5.h
%{_includedir}/allegro5/allegro_color.h
%{_includedir}/allegro5/allegro_direct3d.h
%{_includedir}/allegro5/allegro_font.h
%{_includedir}/allegro5/allegro_memfile.h
%{_includedir}/allegro5/allegro_opengl.h
%{_includedir}/allegro5/allegro_primitives.h
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
%doc
%{_mandir}/man3/ALLEGRO_AUDIO_DEPTH.3.gz
%{_mandir}/man3/ALLEGRO_AUDIO_PAN_NONE.3.gz
%{_mandir}/man3/ALLEGRO_AUDIO_STREAM.3.gz
%{_mandir}/man3/ALLEGRO_BITMAP.3.gz
%{_mandir}/man3/ALLEGRO_BPM_TO_SECS.3.gz
%{_mandir}/man3/ALLEGRO_BPS_TO_SECS.3.gz
%{_mandir}/man3/ALLEGRO_CHANNEL_CONF.3.gz
%{_mandir}/man3/ALLEGRO_COLOR.3.gz
%{_mandir}/man3/ALLEGRO_COND.3.gz
%{_mandir}/man3/ALLEGRO_CONFIG.3.gz
%{_mandir}/man3/ALLEGRO_DISPLAY.3.gz
%{_mandir}/man3/ALLEGRO_DISPLAY_MODE.3.gz
%{_mandir}/man3/ALLEGRO_EVENT.3.gz
%{_mandir}/man3/ALLEGRO_EVENT_QUEUE.3.gz
%{_mandir}/man3/ALLEGRO_EVENT_SOURCE.3.gz
%{_mandir}/man3/ALLEGRO_EVENT_TYPE.3.gz
%{_mandir}/man3/ALLEGRO_EVENT_TYPE_IS_USER.3.gz
%{_mandir}/man3/ALLEGRO_FILE.3.gz
%{_mandir}/man3/ALLEGRO_FILECHOOSER.3.gz
%{_mandir}/man3/ALLEGRO_FILE_INTERFACE.3.gz
%{_mandir}/man3/ALLEGRO_FILE_MODE.3.gz
%{_mandir}/man3/ALLEGRO_FONT.3.gz
%{_mandir}/man3/ALLEGRO_FS_ENTRY.3.gz
%{_mandir}/man3/ALLEGRO_FS_INTERFACE.3.gz
%{_mandir}/man3/ALLEGRO_GET_EVENT_TYPE.3.gz
%{_mandir}/man3/ALLEGRO_JOYFLAGS.3.gz
%{_mandir}/man3/ALLEGRO_JOYSTICK.3.gz
%{_mandir}/man3/ALLEGRO_JOYSTICK_STATE.3.gz
%{_mandir}/man3/ALLEGRO_KEYBOARD_STATE.3.gz
%{_mandir}/man3/ALLEGRO_LOCKED_REGION.3.gz
%{_mandir}/man3/ALLEGRO_MEMORY_INTERFACE.3.gz
%{_mandir}/man3/ALLEGRO_MIXER.3.gz
%{_mandir}/man3/ALLEGRO_MIXER_QUALITY.3.gz
%{_mandir}/man3/ALLEGRO_MONITOR_INFO.3.gz
%{_mandir}/man3/ALLEGRO_MOUSE_STATE.3.gz
%{_mandir}/man3/ALLEGRO_MSECS_TO_SECS.3.gz
%{_mandir}/man3/ALLEGRO_MUTEX.3.gz
%{_mandir}/man3/ALLEGRO_PI.3.gz
%{_mandir}/man3/ALLEGRO_PIXEL_FORMAT.3.gz
%{_mandir}/man3/ALLEGRO_PLAYMODE.3.gz
%{_mandir}/man3/ALLEGRO_PRIM_ATTR.3.gz
%{_mandir}/man3/ALLEGRO_PRIM_QUALITY.3.gz
%{_mandir}/man3/ALLEGRO_PRIM_STORAGE.3.gz
%{_mandir}/man3/ALLEGRO_PRIM_TYPE.3.gz
%{_mandir}/man3/ALLEGRO_SAMPLE.3.gz
%{_mandir}/man3/ALLEGRO_SAMPLE_ID.3.gz
%{_mandir}/man3/ALLEGRO_SAMPLE_INSTANCE.3.gz
%{_mandir}/man3/ALLEGRO_SEEK.3.gz
%{_mandir}/man3/ALLEGRO_STATE.3.gz
%{_mandir}/man3/ALLEGRO_STATE_FLAGS.3.gz
%{_mandir}/man3/ALLEGRO_TEXTLOG.3.gz
%{_mandir}/man3/ALLEGRO_THREAD.3.gz
%{_mandir}/man3/ALLEGRO_TIMEOUT.3.gz
%{_mandir}/man3/ALLEGRO_TIMER.3.gz
%{_mandir}/man3/ALLEGRO_TRANSFORM.3.gz
%{_mandir}/man3/ALLEGRO_USECS_TO_SECS.3.gz
%{_mandir}/man3/ALLEGRO_USER_EVENT.3.gz
%{_mandir}/man3/ALLEGRO_USTR.3.gz
%{_mandir}/man3/ALLEGRO_USTR_INFO.3.gz
%{_mandir}/man3/ALLEGRO_VERTEX.3.gz
%{_mandir}/man3/ALLEGRO_VERTEX_CACHE_SIZE.3.gz
%{_mandir}/man3/ALLEGRO_VERTEX_DECL.3.gz
%{_mandir}/man3/ALLEGRO_VERTEX_ELEMENT.3.gz
%{_mandir}/man3/ALLEGRO_VOICE.3.gz
%{_mandir}/man3/al_acknowledge_resize.3.gz
%{_mandir}/man3/al_add_config_comment.3.gz
%{_mandir}/man3/al_add_config_section.3.gz
%{_mandir}/man3/al_add_new_bitmap_flag.3.gz
%{_mandir}/man3/al_add_timer_count.3.gz
%{_mandir}/man3/al_append_native_text_log.3.gz
%{_mandir}/man3/al_append_path_component.3.gz
%{_mandir}/man3/al_attach_audio_stream_to_mixer.3.gz
%{_mandir}/man3/al_attach_audio_stream_to_voice.3.gz
%{_mandir}/man3/al_attach_mixer_to_mixer.3.gz
%{_mandir}/man3/al_attach_mixer_to_voice.3.gz
%{_mandir}/man3/al_attach_sample_instance_to_mixer.3.gz
%{_mandir}/man3/al_attach_sample_instance_to_voice.3.gz
%{_mandir}/man3/al_broadcast_cond.3.gz
%{_mandir}/man3/al_build_transform.3.gz
%{_mandir}/man3/al_calculate_arc.3.gz
%{_mandir}/man3/al_calculate_ribbon.3.gz
%{_mandir}/man3/al_calculate_spline.3.gz
%{_mandir}/man3/al_calloc.3.gz
%{_mandir}/man3/al_calloc_with_context.3.gz
%{_mandir}/man3/al_change_directory.3.gz
%{_mandir}/man3/al_check_inverse.3.gz
%{_mandir}/man3/al_clear_to_color.3.gz
%{_mandir}/man3/al_clone_bitmap.3.gz
%{_mandir}/man3/al_clone_path.3.gz
%{_mandir}/man3/al_close_directory.3.gz
%{_mandir}/man3/al_close_native_text_log.3.gz
%{_mandir}/man3/al_color_cmyk.3.gz
%{_mandir}/man3/al_color_cmyk_to_rgb.3.gz
%{_mandir}/man3/al_color_hsl.3.gz
%{_mandir}/man3/al_color_hsl_to_rgb.3.gz
%{_mandir}/man3/al_color_hsv.3.gz
%{_mandir}/man3/al_color_hsv_to_rgb.3.gz
%{_mandir}/man3/al_color_html.3.gz
%{_mandir}/man3/al_color_html_to_rgb.3.gz
%{_mandir}/man3/al_color_name.3.gz
%{_mandir}/man3/al_color_name_to_rgb.3.gz
%{_mandir}/man3/al_color_rgb_to_cmyk.3.gz
%{_mandir}/man3/al_color_rgb_to_hsl.3.gz
%{_mandir}/man3/al_color_rgb_to_hsv.3.gz
%{_mandir}/man3/al_color_rgb_to_html.3.gz
%{_mandir}/man3/al_color_rgb_to_name.3.gz
%{_mandir}/man3/al_color_rgb_to_yuv.3.gz
%{_mandir}/man3/al_color_yuv.3.gz
%{_mandir}/man3/al_color_yuv_to_rgb.3.gz
%{_mandir}/man3/al_compose_transform.3.gz
%{_mandir}/man3/al_convert_mask_to_alpha.3.gz
%{_mandir}/man3/al_copy_transform.3.gz
%{_mandir}/man3/al_create_audio_stream.3.gz
%{_mandir}/man3/al_create_bitmap.3.gz
%{_mandir}/man3/al_create_cond.3.gz
%{_mandir}/man3/al_create_config.3.gz
%{_mandir}/man3/al_create_display.3.gz
%{_mandir}/man3/al_create_event_queue.3.gz
%{_mandir}/man3/al_create_file_handle.3.gz
%{_mandir}/man3/al_create_fs_entry.3.gz
%{_mandir}/man3/al_create_mixer.3.gz
%{_mandir}/man3/al_create_mouse_cursor.3.gz
%{_mandir}/man3/al_create_mutex.3.gz
%{_mandir}/man3/al_create_mutex_recursive.3.gz
%{_mandir}/man3/al_create_native_file_dialog.3.gz
%{_mandir}/man3/al_create_path.3.gz
%{_mandir}/man3/al_create_path_for_directory.3.gz
%{_mandir}/man3/al_create_sample.3.gz
%{_mandir}/man3/al_create_sample_instance.3.gz
%{_mandir}/man3/al_create_sub_bitmap.3.gz
%{_mandir}/man3/al_create_thread.3.gz
%{_mandir}/man3/al_create_timer.3.gz
%{_mandir}/man3/al_create_vertex_decl.3.gz
%{_mandir}/man3/al_create_voice.3.gz
%{_mandir}/man3/al_cstr.3.gz
%{_mandir}/man3/al_cstr_dup.3.gz
%{_mandir}/man3/al_current_time.3.gz
%{_mandir}/man3/al_destroy_audio_stream.3.gz
%{_mandir}/man3/al_destroy_bitmap.3.gz
%{_mandir}/man3/al_destroy_cond.3.gz
%{_mandir}/man3/al_destroy_config.3.gz
%{_mandir}/man3/al_destroy_display.3.gz
%{_mandir}/man3/al_destroy_event_queue.3.gz
%{_mandir}/man3/al_destroy_font.3.gz
%{_mandir}/man3/al_destroy_fs_entry.3.gz
%{_mandir}/man3/al_destroy_mixer.3.gz
%{_mandir}/man3/al_destroy_mouse_cursor.3.gz
%{_mandir}/man3/al_destroy_mutex.3.gz
%{_mandir}/man3/al_destroy_native_file_dialog.3.gz
%{_mandir}/man3/al_destroy_path.3.gz
%{_mandir}/man3/al_destroy_sample.3.gz
%{_mandir}/man3/al_destroy_sample_instance.3.gz
%{_mandir}/man3/al_destroy_thread.3.gz
%{_mandir}/man3/al_destroy_timer.3.gz
%{_mandir}/man3/al_destroy_user_event_source.3.gz
%{_mandir}/man3/al_destroy_vertex_decl.3.gz
%{_mandir}/man3/al_destroy_voice.3.gz
%{_mandir}/man3/al_detach_audio_stream.3.gz
%{_mandir}/man3/al_detach_mixer.3.gz
%{_mandir}/man3/al_detach_sample_instance.3.gz
%{_mandir}/man3/al_detach_voice.3.gz
%{_mandir}/man3/al_drain_audio_stream.3.gz
%{_mandir}/man3/al_draw_arc.3.gz
%{_mandir}/man3/al_draw_bitmap.3.gz
%{_mandir}/man3/al_draw_bitmap_region.3.gz
%{_mandir}/man3/al_draw_circle.3.gz
%{_mandir}/man3/al_draw_ellipse.3.gz
%{_mandir}/man3/al_draw_filled_circle.3.gz
%{_mandir}/man3/al_draw_filled_ellipse.3.gz
%{_mandir}/man3/al_draw_filled_rectangle.3.gz
%{_mandir}/man3/al_draw_filled_rounded_rectangle.3.gz
%{_mandir}/man3/al_draw_filled_triangle.3.gz
%{_mandir}/man3/al_draw_indexed_prim.3.gz
%{_mandir}/man3/al_draw_justified_text.3.gz
%{_mandir}/man3/al_draw_justified_textf.3.gz
%{_mandir}/man3/al_draw_justified_ustr.3.gz
%{_mandir}/man3/al_draw_line.3.gz
%{_mandir}/man3/al_draw_pixel.3.gz
%{_mandir}/man3/al_draw_prim.3.gz
%{_mandir}/man3/al_draw_rectangle.3.gz
%{_mandir}/man3/al_draw_ribbon.3.gz
%{_mandir}/man3/al_draw_rotated_bitmap.3.gz
%{_mandir}/man3/al_draw_rounded_rectangle.3.gz
%{_mandir}/man3/al_draw_scaled_bitmap.3.gz
%{_mandir}/man3/al_draw_scaled_rotated_bitmap.3.gz
%{_mandir}/man3/al_draw_soft_line.3.gz
%{_mandir}/man3/al_draw_soft_triangle.3.gz
%{_mandir}/man3/al_draw_spline.3.gz
%{_mandir}/man3/al_draw_text.3.gz
%{_mandir}/man3/al_draw_textf.3.gz
%{_mandir}/man3/al_draw_tinted_bitmap.3.gz
%{_mandir}/man3/al_draw_tinted_bitmap_region.3.gz
%{_mandir}/man3/al_draw_tinted_rotated_bitmap.3.gz
%{_mandir}/man3/al_draw_tinted_scaled_bitmap.3.gz
%{_mandir}/man3/al_draw_tinted_scaled_rotated_bitmap.3.gz
%{_mandir}/man3/al_draw_triangle.3.gz
%{_mandir}/man3/al_draw_ustr.3.gz
%{_mandir}/man3/al_drop_next_event.3.gz
%{_mandir}/man3/al_drop_path_tail.3.gz
%{_mandir}/man3/al_emit_user_event.3.gz
%{_mandir}/man3/al_fclearerr.3.gz
%{_mandir}/man3/al_fclose.3.gz
%{_mandir}/man3/al_feof.3.gz
%{_mandir}/man3/al_ferror.3.gz
%{_mandir}/man3/al_fflush.3.gz
%{_mandir}/man3/al_fget_ustr.3.gz
%{_mandir}/man3/al_fgetc.3.gz
%{_mandir}/man3/al_fgets.3.gz
%{_mandir}/man3/al_filename_exists.3.gz
%{_mandir}/man3/al_fixacos.3.gz
%{_mandir}/man3/al_fixadd.3.gz
%{_mandir}/man3/al_fixasin.3.gz
%{_mandir}/man3/al_fixatan.3.gz
%{_mandir}/man3/al_fixatan2.3.gz
%{_mandir}/man3/al_fixceil.3.gz
%{_mandir}/man3/al_fixcos.3.gz
%{_mandir}/man3/al_fixdiv.3.gz
%{_mandir}/man3/al_fixed.3.gz
%{_mandir}/man3/al_fixfloor.3.gz
%{_mandir}/man3/al_fixhypot.3.gz
%{_mandir}/man3/al_fixmul.3.gz
%{_mandir}/man3/al_fixsin.3.gz
%{_mandir}/man3/al_fixsqrt.3.gz
%{_mandir}/man3/al_fixsub.3.gz
%{_mandir}/man3/al_fixtan.3.gz
%{_mandir}/man3/al_fixtof.3.gz
%{_mandir}/man3/al_fixtoi.3.gz
%{_mandir}/man3/al_fixtorad_r.3.gz
%{_mandir}/man3/al_flip_display.3.gz
%{_mandir}/man3/al_flush_event_queue.3.gz
%{_mandir}/man3/al_fopen.3.gz
%{_mandir}/man3/al_fopen_fd.3.gz
%{_mandir}/man3/al_fopen_interface.3.gz
%{_mandir}/man3/al_fputc.3.gz
%{_mandir}/man3/al_fputs.3.gz
%{_mandir}/man3/al_fread.3.gz
%{_mandir}/man3/al_fread16be.3.gz
%{_mandir}/man3/al_fread16le.3.gz
%{_mandir}/man3/al_fread32be.3.gz
%{_mandir}/man3/al_fread32le.3.gz
%{_mandir}/man3/al_free.3.gz
%{_mandir}/man3/al_free_with_context.3.gz
%{_mandir}/man3/al_fs_entry_exists.3.gz
%{_mandir}/man3/al_fseek.3.gz
%{_mandir}/man3/al_fsize.3.gz
%{_mandir}/man3/al_ftell.3.gz
%{_mandir}/man3/al_ftofix.3.gz
%{_mandir}/man3/al_fungetc.3.gz
%{_mandir}/man3/al_fwrite.3.gz
%{_mandir}/man3/al_fwrite16be.3.gz
%{_mandir}/man3/al_fwrite16le.3.gz
%{_mandir}/man3/al_fwrite32be.3.gz
%{_mandir}/man3/al_fwrite32le.3.gz
%{_mandir}/man3/al_get_allegro_acodec_version.3.gz
%{_mandir}/man3/al_get_allegro_audio_version.3.gz
%{_mandir}/man3/al_get_allegro_color_version.3.gz
%{_mandir}/man3/al_get_allegro_font_version.3.gz
%{_mandir}/man3/al_get_allegro_image_version.3.gz
%{_mandir}/man3/al_get_allegro_memfile_version.3.gz
%{_mandir}/man3/al_get_allegro_native_dialog_version.3.gz
%{_mandir}/man3/al_get_allegro_physfs_version.3.gz
%{_mandir}/man3/al_get_allegro_primitives_version.3.gz
%{_mandir}/man3/al_get_allegro_ttf_version.3.gz
%{_mandir}/man3/al_get_allegro_version.3.gz
%{_mandir}/man3/al_get_app_name.3.gz
%{_mandir}/man3/al_get_audio_depth_size.3.gz
%{_mandir}/man3/al_get_audio_stream_attached.3.gz
%{_mandir}/man3/al_get_audio_stream_channels.3.gz
%{_mandir}/man3/al_get_audio_stream_depth.3.gz
%{_mandir}/man3/al_get_audio_stream_event_source.3.gz
%{_mandir}/man3/al_get_audio_stream_fragment.3.gz
%{_mandir}/man3/al_get_audio_stream_fragments.3.gz
%{_mandir}/man3/al_get_audio_stream_frequency.3.gz
%{_mandir}/man3/al_get_audio_stream_gain.3.gz
%{_mandir}/man3/al_get_audio_stream_length.3.gz
%{_mandir}/man3/al_get_audio_stream_length_secs.3.gz
%{_mandir}/man3/al_get_audio_stream_pan.3.gz
%{_mandir}/man3/al_get_audio_stream_playing.3.gz
%{_mandir}/man3/al_get_audio_stream_playmode.3.gz
%{_mandir}/man3/al_get_audio_stream_position_secs.3.gz
%{_mandir}/man3/al_get_audio_stream_speed.3.gz
%{_mandir}/man3/al_get_available_audio_stream_fragments.3.gz
%{_mandir}/man3/al_get_backbuffer.3.gz
%{_mandir}/man3/al_get_bitmap_flags.3.gz
%{_mandir}/man3/al_get_bitmap_format.3.gz
%{_mandir}/man3/al_get_bitmap_height.3.gz
%{_mandir}/man3/al_get_bitmap_width.3.gz
%{_mandir}/man3/al_get_blender.3.gz
%{_mandir}/man3/al_get_channel_count.3.gz
%{_mandir}/man3/al_get_clipping_rectangle.3.gz
%{_mandir}/man3/al_get_config_value.3.gz
%{_mandir}/man3/al_get_current_directory.3.gz
%{_mandir}/man3/al_get_current_display.3.gz
%{_mandir}/man3/al_get_current_transform.3.gz
%{_mandir}/man3/al_get_d3d_device.3.gz
%{_mandir}/man3/al_get_d3d_system_texture.3.gz
%{_mandir}/man3/al_get_d3d_texture_position.3.gz
%{_mandir}/man3/al_get_d3d_video_texture.3.gz
%{_mandir}/man3/al_get_default_mixer.3.gz
%{_mandir}/man3/al_get_display_event_source.3.gz
%{_mandir}/man3/al_get_display_flags.3.gz
%{_mandir}/man3/al_get_display_format.3.gz
%{_mandir}/man3/al_get_display_height.3.gz
%{_mandir}/man3/al_get_display_mode.3.gz
%{_mandir}/man3/al_get_display_option.3.gz
%{_mandir}/man3/al_get_display_refresh_rate.3.gz
%{_mandir}/man3/al_get_display_width.3.gz
%{_mandir}/man3/al_get_errno.3.gz
%{_mandir}/man3/al_get_event_source_data.3.gz
%{_mandir}/man3/al_get_file_userdata.3.gz
%{_mandir}/man3/al_get_first_config_entry.3.gz
%{_mandir}/man3/al_get_first_config_section.3.gz
%{_mandir}/man3/al_get_font_ascent.3.gz
%{_mandir}/man3/al_get_font_descent.3.gz
%{_mandir}/man3/al_get_font_line_height.3.gz
%{_mandir}/man3/al_get_fs_entry_atime.3.gz
%{_mandir}/man3/al_get_fs_entry_ctime.3.gz
%{_mandir}/man3/al_get_fs_entry_mode.3.gz
%{_mandir}/man3/al_get_fs_entry_mtime.3.gz
%{_mandir}/man3/al_get_fs_entry_name.3.gz
%{_mandir}/man3/al_get_fs_entry_size.3.gz
%{_mandir}/man3/al_get_fs_interface.3.gz
%{_mandir}/man3/al_get_joystick.3.gz
%{_mandir}/man3/al_get_joystick_active.3.gz
%{_mandir}/man3/al_get_joystick_axis_name.3.gz
%{_mandir}/man3/al_get_joystick_button_name.3.gz
%{_mandir}/man3/al_get_joystick_event_source.3.gz
%{_mandir}/man3/al_get_joystick_name.3.gz
%{_mandir}/man3/al_get_joystick_num_axes.3.gz
%{_mandir}/man3/al_get_joystick_num_buttons.3.gz
%{_mandir}/man3/al_get_joystick_num_sticks.3.gz
%{_mandir}/man3/al_get_joystick_state.3.gz
%{_mandir}/man3/al_get_joystick_stick_flags.3.gz
%{_mandir}/man3/al_get_joystick_stick_name.3.gz
%{_mandir}/man3/al_get_keyboard_event_source.3.gz
%{_mandir}/man3/al_get_keyboard_state.3.gz
%{_mandir}/man3/al_get_mixer_attached.3.gz
%{_mandir}/man3/al_get_mixer_channels.3.gz
%{_mandir}/man3/al_get_mixer_depth.3.gz
%{_mandir}/man3/al_get_mixer_frequency.3.gz
%{_mandir}/man3/al_get_mixer_playing.3.gz
%{_mandir}/man3/al_get_mixer_quality.3.gz
%{_mandir}/man3/al_get_monitor_info.3.gz
%{_mandir}/man3/al_get_mouse_cursor_position.3.gz
%{_mandir}/man3/al_get_mouse_event_source.3.gz
%{_mandir}/man3/al_get_mouse_num_axes.3.gz
%{_mandir}/man3/al_get_mouse_num_buttons.3.gz
%{_mandir}/man3/al_get_mouse_state.3.gz
%{_mandir}/man3/al_get_mouse_state_axis.3.gz
%{_mandir}/man3/al_get_native_file_dialog_count.3.gz
%{_mandir}/man3/al_get_native_file_dialog_path.3.gz
%{_mandir}/man3/al_get_native_text_log_event_source.3.gz
%{_mandir}/man3/al_get_new_bitmap_flags.3.gz
%{_mandir}/man3/al_get_new_bitmap_format.3.gz
%{_mandir}/man3/al_get_new_display_adapter.3.gz
%{_mandir}/man3/al_get_new_display_flags.3.gz
%{_mandir}/man3/al_get_new_display_option.3.gz
%{_mandir}/man3/al_get_new_display_refresh_rate.3.gz
%{_mandir}/man3/al_get_new_file_interface.3.gz
%{_mandir}/man3/al_get_new_window_position.3.gz
%{_mandir}/man3/al_get_next_config_entry.3.gz
%{_mandir}/man3/al_get_next_config_section.3.gz
%{_mandir}/man3/al_get_next_event.3.gz
%{_mandir}/man3/al_get_num_display_modes.3.gz
%{_mandir}/man3/al_get_num_joysticks.3.gz
%{_mandir}/man3/al_get_num_video_adapters.3.gz
%{_mandir}/man3/al_get_opengl_extension_list.3.gz
%{_mandir}/man3/al_get_opengl_fbo.3.gz
%{_mandir}/man3/al_get_opengl_proc_address.3.gz
%{_mandir}/man3/al_get_opengl_texture.3.gz
%{_mandir}/man3/al_get_opengl_texture_position.3.gz
%{_mandir}/man3/al_get_opengl_texture_size.3.gz
%{_mandir}/man3/al_get_opengl_variant.3.gz
%{_mandir}/man3/al_get_opengl_version.3.gz
%{_mandir}/man3/al_get_org_name.3.gz
%{_mandir}/man3/al_get_path_basename.3.gz
%{_mandir}/man3/al_get_path_component.3.gz
%{_mandir}/man3/al_get_path_drive.3.gz
%{_mandir}/man3/al_get_path_extension.3.gz
%{_mandir}/man3/al_get_path_filename.3.gz
%{_mandir}/man3/al_get_path_num_components.3.gz
%{_mandir}/man3/al_get_path_tail.3.gz
%{_mandir}/man3/al_get_pixel.3.gz
%{_mandir}/man3/al_get_pixel_format_bits.3.gz
%{_mandir}/man3/al_get_pixel_size.3.gz
%{_mandir}/man3/al_get_sample.3.gz
%{_mandir}/man3/al_get_sample_channels.3.gz
%{_mandir}/man3/al_get_sample_data.3.gz
%{_mandir}/man3/al_get_sample_depth.3.gz
%{_mandir}/man3/al_get_sample_frequency.3.gz
%{_mandir}/man3/al_get_sample_instance_attached.3.gz
%{_mandir}/man3/al_get_sample_instance_channels.3.gz
%{_mandir}/man3/al_get_sample_instance_depth.3.gz
%{_mandir}/man3/al_get_sample_instance_frequency.3.gz
%{_mandir}/man3/al_get_sample_instance_gain.3.gz
%{_mandir}/man3/al_get_sample_instance_length.3.gz
%{_mandir}/man3/al_get_sample_instance_pan.3.gz
%{_mandir}/man3/al_get_sample_instance_playing.3.gz
%{_mandir}/man3/al_get_sample_instance_playmode.3.gz
%{_mandir}/man3/al_get_sample_instance_position.3.gz
%{_mandir}/man3/al_get_sample_instance_speed.3.gz
%{_mandir}/man3/al_get_sample_instance_time.3.gz
%{_mandir}/man3/al_get_sample_length.3.gz
%{_mandir}/man3/al_get_separate_blender.3.gz
%{_mandir}/man3/al_get_standard_path.3.gz
%{_mandir}/man3/al_get_system_config.3.gz
%{_mandir}/man3/al_get_target_bitmap.3.gz
%{_mandir}/man3/al_get_text_dimensions.3.gz
%{_mandir}/man3/al_get_text_width.3.gz
%{_mandir}/man3/al_get_thread_should_stop.3.gz
%{_mandir}/man3/al_get_time.3.gz
%{_mandir}/man3/al_get_timer_count.3.gz
%{_mandir}/man3/al_get_timer_event_source.3.gz
%{_mandir}/man3/al_get_timer_speed.3.gz
%{_mandir}/man3/al_get_timer_started.3.gz
%{_mandir}/man3/al_get_ustr_dimensions.3.gz
%{_mandir}/man3/al_get_ustr_width.3.gz
%{_mandir}/man3/al_get_voice_channels.3.gz
%{_mandir}/man3/al_get_voice_depth.3.gz
%{_mandir}/man3/al_get_voice_frequency.3.gz
%{_mandir}/man3/al_get_voice_playing.3.gz
%{_mandir}/man3/al_get_voice_position.3.gz
%{_mandir}/man3/al_get_win_window_handle.3.gz
%{_mandir}/man3/al_get_window_position.3.gz
%{_mandir}/man3/al_grab_font_from_bitmap.3.gz
%{_mandir}/man3/al_grab_mouse.3.gz
%{_mandir}/man3/al_have_d3d_non_pow2_texture_support.3.gz
%{_mandir}/man3/al_have_d3d_non_square_texture_support.3.gz
%{_mandir}/man3/al_have_opengl_extension.3.gz
%{_mandir}/man3/al_hide_mouse_cursor.3.gz
%{_mandir}/man3/al_hold_bitmap_drawing.3.gz
%{_mandir}/man3/al_identity_transform.3.gz
%{_mandir}/man3/al_inhibit_screensaver.3.gz
%{_mandir}/man3/al_init.3.gz
%{_mandir}/man3/al_init_acodec_addon.3.gz
%{_mandir}/man3/al_init_font_addon.3.gz
%{_mandir}/man3/al_init_image_addon.3.gz
%{_mandir}/man3/al_init_primitives_addon.3.gz
%{_mandir}/man3/al_init_timeout.3.gz
%{_mandir}/man3/al_init_ttf_addon.3.gz
%{_mandir}/man3/al_init_user_event_source.3.gz
%{_mandir}/man3/al_insert_path_component.3.gz
%{_mandir}/man3/al_install_audio.3.gz
%{_mandir}/man3/al_install_joystick.3.gz
%{_mandir}/man3/al_install_keyboard.3.gz
%{_mandir}/man3/al_install_mouse.3.gz
%{_mandir}/man3/al_install_system.3.gz
%{_mandir}/man3/al_invert_transform.3.gz
%{_mandir}/man3/al_iphone_override_screen_scale.3.gz
%{_mandir}/man3/al_iphone_program_has_halted.3.gz
%{_mandir}/man3/al_is_audio_installed.3.gz
%{_mandir}/man3/al_is_bitmap_drawing_held.3.gz
%{_mandir}/man3/al_is_bitmap_locked.3.gz
%{_mandir}/man3/al_is_compatible_bitmap.3.gz
%{_mandir}/man3/al_is_d3d_device_lost.3.gz
%{_mandir}/man3/al_is_event_queue_empty.3.gz
%{_mandir}/man3/al_is_joystick_installed.3.gz
%{_mandir}/man3/al_is_keyboard_installed.3.gz
%{_mandir}/man3/al_is_mouse_installed.3.gz
%{_mandir}/man3/al_is_sub_bitmap.3.gz
%{_mandir}/man3/al_is_system_installed.3.gz
%{_mandir}/man3/al_itofix.3.gz
%{_mandir}/man3/al_join_paths.3.gz
%{_mandir}/man3/al_join_thread.3.gz
%{_mandir}/man3/al_key_down.3.gz
%{_mandir}/man3/al_keycode_to_name.3.gz
%{_mandir}/man3/al_load_audio_stream.3.gz
%{_mandir}/man3/al_load_audio_stream_f.3.gz
%{_mandir}/man3/al_load_bitmap.3.gz
%{_mandir}/man3/al_load_bitmap_f.3.gz
%{_mandir}/man3/al_load_bitmap_font.3.gz
%{_mandir}/man3/al_load_config_file.3.gz
%{_mandir}/man3/al_load_config_file_f.3.gz
%{_mandir}/man3/al_load_font.3.gz
%{_mandir}/man3/al_load_sample.3.gz
%{_mandir}/man3/al_load_sample_f.3.gz
%{_mandir}/man3/al_load_ttf_font.3.gz
%{_mandir}/man3/al_load_ttf_font_f.3.gz
%{_mandir}/man3/al_lock_bitmap.3.gz
%{_mandir}/man3/al_lock_bitmap_region.3.gz
%{_mandir}/man3/al_lock_mutex.3.gz
%{_mandir}/man3/al_make_directory.3.gz
%{_mandir}/man3/al_make_path_canonical.3.gz
%{_mandir}/man3/al_make_temp_file.3.gz
%{_mandir}/man3/al_malloc.3.gz
%{_mandir}/man3/al_malloc_with_context.3.gz
%{_mandir}/man3/al_map_rgb.3.gz
%{_mandir}/man3/al_map_rgb_f.3.gz
%{_mandir}/man3/al_map_rgba.3.gz
%{_mandir}/man3/al_map_rgba_f.3.gz
%{_mandir}/man3/al_merge_config.3.gz
%{_mandir}/man3/al_merge_config_into.3.gz
%{_mandir}/man3/al_mouse_button_down.3.gz
%{_mandir}/man3/al_open_directory.3.gz
%{_mandir}/man3/al_open_fs_entry.3.gz
%{_mandir}/man3/al_open_memfile.3.gz
%{_mandir}/man3/al_open_native_text_log.3.gz
%{_mandir}/man3/al_path_cstr.3.gz
%{_mandir}/man3/al_peek_next_event.3.gz
%{_mandir}/man3/al_play_sample.3.gz
%{_mandir}/man3/al_play_sample_instance.3.gz
%{_mandir}/man3/al_put_blended_pixel.3.gz
%{_mandir}/man3/al_put_pixel.3.gz
%{_mandir}/man3/al_radtofix_r.3.gz
%{_mandir}/man3/al_read_directory.3.gz
%{_mandir}/man3/al_realloc.3.gz
%{_mandir}/man3/al_realloc_with_context.3.gz
%{_mandir}/man3/al_rebase_path.3.gz
%{_mandir}/man3/al_reconfigure_joysticks.3.gz
%{_mandir}/man3/al_ref_buffer.3.gz
%{_mandir}/man3/al_ref_cstr.3.gz
%{_mandir}/man3/al_ref_ustr.3.gz
%{_mandir}/man3/al_register_audio_stream_loader.3.gz
%{_mandir}/man3/al_register_audio_stream_loader_f.3.gz
%{_mandir}/man3/al_register_bitmap_loader.3.gz
%{_mandir}/man3/al_register_bitmap_loader_f.3.gz
%{_mandir}/man3/al_register_bitmap_saver.3.gz
%{_mandir}/man3/al_register_bitmap_saver_f.3.gz
%{_mandir}/man3/al_register_event_source.3.gz
%{_mandir}/man3/al_register_font_loader.3.gz
%{_mandir}/man3/al_register_sample_loader.3.gz
%{_mandir}/man3/al_register_sample_loader_f.3.gz
%{_mandir}/man3/al_register_sample_saver.3.gz
%{_mandir}/man3/al_register_sample_saver_f.3.gz
%{_mandir}/man3/al_release_joystick.3.gz
%{_mandir}/man3/al_remove_filename.3.gz
%{_mandir}/man3/al_remove_fs_entry.3.gz
%{_mandir}/man3/al_remove_opengl_fbo.3.gz
%{_mandir}/man3/al_remove_path_component.3.gz
%{_mandir}/man3/al_replace_path_component.3.gz
%{_mandir}/man3/al_reserve_samples.3.gz
%{_mandir}/man3/al_reset_new_display_options.3.gz
%{_mandir}/man3/al_resize_display.3.gz
%{_mandir}/man3/al_rest.3.gz
%{_mandir}/man3/al_restore_default_mixer.3.gz
%{_mandir}/man3/al_restore_state.3.gz
%{_mandir}/man3/al_rewind_audio_stream.3.gz
%{_mandir}/man3/al_rotate_transform.3.gz
%{_mandir}/man3/al_run_detached_thread.3.gz
%{_mandir}/man3/al_run_main.3.gz
%{_mandir}/man3/al_save_bitmap.3.gz
%{_mandir}/man3/al_save_bitmap_f.3.gz
%{_mandir}/man3/al_save_config_file.3.gz
%{_mandir}/man3/al_save_config_file_f.3.gz
%{_mandir}/man3/al_save_sample.3.gz
%{_mandir}/man3/al_save_sample_f.3.gz
%{_mandir}/man3/al_scale_transform.3.gz
%{_mandir}/man3/al_seek_audio_stream_secs.3.gz
%{_mandir}/man3/al_set_app_name.3.gz
%{_mandir}/man3/al_set_audio_stream_fragment.3.gz
%{_mandir}/man3/al_set_audio_stream_gain.3.gz
%{_mandir}/man3/al_set_audio_stream_loop_secs.3.gz
%{_mandir}/man3/al_set_audio_stream_pan.3.gz
%{_mandir}/man3/al_set_audio_stream_playing.3.gz
%{_mandir}/man3/al_set_audio_stream_playmode.3.gz
%{_mandir}/man3/al_set_audio_stream_speed.3.gz
%{_mandir}/man3/al_set_blender.3.gz
%{_mandir}/man3/al_set_clipping_rectangle.3.gz
%{_mandir}/man3/al_set_config_value.3.gz
%{_mandir}/man3/al_set_current_opengl_context.3.gz
%{_mandir}/man3/al_set_default_mixer.3.gz
%{_mandir}/man3/al_set_display_icon.3.gz
%{_mandir}/man3/al_set_errno.3.gz
%{_mandir}/man3/al_set_event_source_data.3.gz
%{_mandir}/man3/al_set_fs_interface.3.gz
%{_mandir}/man3/al_set_keyboard_leds.3.gz
%{_mandir}/man3/al_set_memory_interface.3.gz
%{_mandir}/man3/al_set_mixer_frequency.3.gz
%{_mandir}/man3/al_set_mixer_playing.3.gz
%{_mandir}/man3/al_set_mixer_postprocess_callback.3.gz
%{_mandir}/man3/al_set_mixer_quality.3.gz
%{_mandir}/man3/al_set_mouse_axis.3.gz
%{_mandir}/man3/al_set_mouse_cursor.3.gz
%{_mandir}/man3/al_set_mouse_w.3.gz
%{_mandir}/man3/al_set_mouse_xy.3.gz
%{_mandir}/man3/al_set_mouse_z.3.gz
%{_mandir}/man3/al_set_new_bitmap_flags.3.gz
%{_mandir}/man3/al_set_new_bitmap_format.3.gz
%{_mandir}/man3/al_set_new_display_adapter.3.gz
%{_mandir}/man3/al_set_new_display_flags.3.gz
%{_mandir}/man3/al_set_new_display_option.3.gz
%{_mandir}/man3/al_set_new_display_refresh_rate.3.gz
%{_mandir}/man3/al_set_new_file_interface.3.gz
%{_mandir}/man3/al_set_new_window_position.3.gz
%{_mandir}/man3/al_set_org_name.3.gz
%{_mandir}/man3/al_set_path_drive.3.gz
%{_mandir}/man3/al_set_path_extension.3.gz
%{_mandir}/man3/al_set_path_filename.3.gz
%{_mandir}/man3/al_set_physfs_file_interface.3.gz
%{_mandir}/man3/al_set_sample.3.gz
%{_mandir}/man3/al_set_sample_instance_gain.3.gz
%{_mandir}/man3/al_set_sample_instance_length.3.gz
%{_mandir}/man3/al_set_sample_instance_pan.3.gz
%{_mandir}/man3/al_set_sample_instance_playing.3.gz
%{_mandir}/man3/al_set_sample_instance_playmode.3.gz
%{_mandir}/man3/al_set_sample_instance_position.3.gz
%{_mandir}/man3/al_set_sample_instance_speed.3.gz
%{_mandir}/man3/al_set_separate_blender.3.gz
%{_mandir}/man3/al_set_standard_file_interface.3.gz
%{_mandir}/man3/al_set_standard_fs_interface.3.gz
%{_mandir}/man3/al_set_system_mouse_cursor.3.gz
%{_mandir}/man3/al_set_target_backbuffer.3.gz
%{_mandir}/man3/al_set_target_bitmap.3.gz
%{_mandir}/man3/al_set_thread_should_stop.3.gz
%{_mandir}/man3/al_set_timer_count.3.gz
%{_mandir}/man3/al_set_timer_speed.3.gz
%{_mandir}/man3/al_set_voice_playing.3.gz
%{_mandir}/man3/al_set_voice_position.3.gz
%{_mandir}/man3/al_set_window_position.3.gz
%{_mandir}/man3/al_set_window_title.3.gz
%{_mandir}/man3/al_show_mouse_cursor.3.gz
%{_mandir}/man3/al_show_native_file_dialog.3.gz
%{_mandir}/man3/al_show_native_message_box.3.gz
%{_mandir}/man3/al_shutdown_font_addon.3.gz
%{_mandir}/man3/al_shutdown_image_addon.3.gz
%{_mandir}/man3/al_shutdown_primitives_addon.3.gz
%{_mandir}/man3/al_shutdown_ttf_addon.3.gz
%{_mandir}/man3/al_signal_cond.3.gz
%{_mandir}/man3/al_start_thread.3.gz
%{_mandir}/man3/al_start_timer.3.gz
%{_mandir}/man3/al_stop_sample.3.gz
%{_mandir}/man3/al_stop_sample_instance.3.gz
%{_mandir}/man3/al_stop_samples.3.gz
%{_mandir}/man3/al_stop_timer.3.gz
%{_mandir}/man3/al_store_state.3.gz
%{_mandir}/man3/al_toggle_display_flag.3.gz
%{_mandir}/man3/al_transform_coordinates.3.gz
%{_mandir}/man3/al_translate_transform.3.gz
%{_mandir}/man3/al_ungrab_mouse.3.gz
%{_mandir}/man3/al_uninstall_audio.3.gz
%{_mandir}/man3/al_uninstall_joystick.3.gz
%{_mandir}/man3/al_uninstall_keyboard.3.gz
%{_mandir}/man3/al_uninstall_mouse.3.gz
%{_mandir}/man3/al_uninstall_system.3.gz
%{_mandir}/man3/al_unlock_bitmap.3.gz
%{_mandir}/man3/al_unlock_mutex.3.gz
%{_mandir}/man3/al_unmap_rgb.3.gz
%{_mandir}/man3/al_unmap_rgb_f.3.gz
%{_mandir}/man3/al_unmap_rgba.3.gz
%{_mandir}/man3/al_unmap_rgba_f.3.gz
%{_mandir}/man3/al_unref_user_event.3.gz
%{_mandir}/man3/al_unregister_event_source.3.gz
%{_mandir}/man3/al_update_display_region.3.gz
%{_mandir}/man3/al_update_fs_entry.3.gz
%{_mandir}/man3/al_use_transform.3.gz
%{_mandir}/man3/al_ustr_append.3.gz
%{_mandir}/man3/al_ustr_append_chr.3.gz
%{_mandir}/man3/al_ustr_append_cstr.3.gz
%{_mandir}/man3/al_ustr_appendf.3.gz
%{_mandir}/man3/al_ustr_assign.3.gz
%{_mandir}/man3/al_ustr_assign_cstr.3.gz
%{_mandir}/man3/al_ustr_assign_substr.3.gz
%{_mandir}/man3/al_ustr_compare.3.gz
%{_mandir}/man3/al_ustr_dup.3.gz
%{_mandir}/man3/al_ustr_dup_substr.3.gz
%{_mandir}/man3/al_ustr_empty_string.3.gz
%{_mandir}/man3/al_ustr_encode_utf16.3.gz
%{_mandir}/man3/al_ustr_equal.3.gz
%{_mandir}/man3/al_ustr_find_chr.3.gz
%{_mandir}/man3/al_ustr_find_cset.3.gz
%{_mandir}/man3/al_ustr_find_cset_cstr.3.gz
%{_mandir}/man3/al_ustr_find_cstr.3.gz
%{_mandir}/man3/al_ustr_find_replace.3.gz
%{_mandir}/man3/al_ustr_find_replace_cstr.3.gz
%{_mandir}/man3/al_ustr_find_set.3.gz
%{_mandir}/man3/al_ustr_find_set_cstr.3.gz
%{_mandir}/man3/al_ustr_find_str.3.gz
%{_mandir}/man3/al_ustr_free.3.gz
%{_mandir}/man3/al_ustr_get.3.gz
%{_mandir}/man3/al_ustr_get_next.3.gz
%{_mandir}/man3/al_ustr_has_prefix.3.gz
%{_mandir}/man3/al_ustr_has_prefix_cstr.3.gz
%{_mandir}/man3/al_ustr_has_suffix.3.gz
%{_mandir}/man3/al_ustr_has_suffix_cstr.3.gz
%{_mandir}/man3/al_ustr_insert.3.gz
%{_mandir}/man3/al_ustr_insert_chr.3.gz
%{_mandir}/man3/al_ustr_insert_cstr.3.gz
%{_mandir}/man3/al_ustr_length.3.gz
%{_mandir}/man3/al_ustr_ltrim_ws.3.gz
%{_mandir}/man3/al_ustr_ncompare.3.gz
%{_mandir}/man3/al_ustr_new.3.gz
%{_mandir}/man3/al_ustr_new_from_buffer.3.gz
%{_mandir}/man3/al_ustr_new_from_utf16.3.gz
%{_mandir}/man3/al_ustr_newf.3.gz
%{_mandir}/man3/al_ustr_next.3.gz
%{_mandir}/man3/al_ustr_offset.3.gz
%{_mandir}/man3/al_ustr_prev.3.gz
%{_mandir}/man3/al_ustr_prev_get.3.gz
%{_mandir}/man3/al_ustr_remove_chr.3.gz
%{_mandir}/man3/al_ustr_remove_range.3.gz
%{_mandir}/man3/al_ustr_replace_range.3.gz
%{_mandir}/man3/al_ustr_rfind_chr.3.gz
%{_mandir}/man3/al_ustr_rfind_cstr.3.gz
%{_mandir}/man3/al_ustr_rfind_str.3.gz
%{_mandir}/man3/al_ustr_rtrim_ws.3.gz
%{_mandir}/man3/al_ustr_set_chr.3.gz
%{_mandir}/man3/al_ustr_size.3.gz
%{_mandir}/man3/al_ustr_size_utf16.3.gz
%{_mandir}/man3/al_ustr_to_buffer.3.gz
%{_mandir}/man3/al_ustr_trim_ws.3.gz
%{_mandir}/man3/al_ustr_truncate.3.gz
%{_mandir}/man3/al_ustr_vappendf.3.gz
%{_mandir}/man3/al_utf16_encode.3.gz
%{_mandir}/man3/al_utf16_width.3.gz
%{_mandir}/man3/al_utf8_encode.3.gz
%{_mandir}/man3/al_utf8_width.3.gz
%{_mandir}/man3/al_wait_cond.3.gz
%{_mandir}/man3/al_wait_cond_until.3.gz
%{_mandir}/man3/al_wait_for_event.3.gz
%{_mandir}/man3/al_wait_for_event_timed.3.gz
%{_mandir}/man3/al_wait_for_event_until.3.gz
%{_mandir}/man3/al_wait_for_vsync.3.gz

%files addon-acodec
%{_libdir}/liballegro_acodec.so.5.0
%{_libdir}/liballegro_acodec.so.5.0.0

%files addon-acodec-devel
%{_includedir}/allegro5/allegro_acodec.h
%{_libdir}/liballegro_acodec.so
%{_libdir}/pkgconfig/allegro_acodec-5.0.pc

%files addon-audio
%{_libdir}/liballegro_audio.so.5.0
%{_libdir}/liballegro_audio.so.5.0.0

%files addon-audio-devel
%{_includedir}/allegro5/allegro_audio.h
%{_libdir}/liballegro_audio.so
%{_libdir}/pkgconfig/allegro_audio-5.0.pc

%files addon-dialog
%{_libdir}/liballegro_dialog.so.5.0
%{_libdir}/liballegro_dialog.so.5.0.0

%files addon-dialog-devel
%{_includedir}/allegro5/allegro_native_dialog.h
%{_libdir}/liballegro_dialog.so
%{_libdir}/pkgconfig/allegro_dialog-5.0.pc

%files addon-image
%{_libdir}/liballegro_image.so.5.0
%{_libdir}/liballegro_image.so.5.0.0

%files addon-image-devel
%{_includedir}/allegro5/allegro_image.h
%{_libdir}/liballegro_image.so
%{_libdir}/pkgconfig/allegro_image-5.0.pc

%files addon-physfs
%{_libdir}/liballegro_physfs.so.5.0
%{_libdir}/liballegro_physfs.so.5.0.0

%files addon-physfs-devel
%{_includedir}/allegro5/allegro_physfs.h
%{_libdir}/liballegro_physfs.so
%{_libdir}/pkgconfig/allegro_physfs-5.0.pc

%files addon-ttf
%{_libdir}/liballegro_ttf.so.5.0
%{_libdir}/liballegro_ttf.so.5.0.0

%files addon-ttf-devel
%{_includedir}/allegro5/allegro_ttf.h
%{_libdir}/liballegro_ttf.so
%{_libdir}/pkgconfig/allegro_ttf-5.0.pc

%changelog
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

