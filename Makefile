RPM_BUILD_ROOT=${HOME}/rpmbuild

.PHONY: all check

all: build check
	
build:
	rm -fR ${RPM_BUILD_ROOT}/RPMS
	rpmbuild -ba allegro5.spec

check:
	rpmlint ${RPM_BUILD_ROOT}/RPMS/*/allegro5-*.rpm

