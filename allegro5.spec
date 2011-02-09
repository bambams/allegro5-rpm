# vim: noexpandtab textwidth=0
Name:		allegro5
Version:	5.0.0
Release:	1%{?dist}
Summary:	A game programming library.

Group:		System Environment/Libraries
License:	zlib
URL:		http://liballeg.org/
Source:		allegro-5.0.0.tar.gz
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

BuildRequires:	cmake freetype-devel gcc libcurl-devel libjpeg-devel libpng-devel libvorbis-devel make mesa-libGL-devel mesa-libGLU-devel physfs-devel
Requires:	

%description


%prep
%setup -q


%build
%configure
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc



%changelog


