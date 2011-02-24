RPM_BUILD_ROOT=${HOME}/rpm

.PHONY: all check

all: build check
	
build:
	rpmbuild -ba allegro5.spec

check:
	rpmlint ${RPM_BUILD_ROOT}/RPMS/*/allegro5-*.rpm

