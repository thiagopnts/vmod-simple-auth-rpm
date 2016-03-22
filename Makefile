rpm:
	mkdir -p dist/{BUILD,RPMS,SPECS,SOURCES,SRPMS,install}
	cp nytd-libvmod-simple-auth-1.1.spec dist/SPECS
	wget https://github.com/thiagopnts/vmod-simple-auth/archive/0.0.2.tar.gz -O libvmod-simple-auth.tar.gz
	cp varnish-3.0.3.tar.gz dist/BUILD

	mv libvmod-simple-auth.tar.gz dist/SOURCES
	tar -zxf dist/BUILD/varnish-3.0.3.tar.gz -C dist/BUILD
	cd dist/BUILD/varnish-3.0.3 ; ./autogen.sh ; ./configure ; make
	QA_SKIP_BUILD_ROOT=1 rpmbuild -ba \
                    --define "_topdir $(PWD)/dist" \
                    --define "buildroot $(PWD)/dist/install" \
                    --clean \
                    dist/SPECS/nytd-libvmod-simple-auth-1.1.spec
