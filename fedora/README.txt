yum install git meson rpm-build gmock gtest gmock-devel gtest-devel gobject-introspection gobject-introspection-devel gcc-c++ glib2-devel gobject-introspection-devel rpmdevtools

rpmbuild -bb libanimation.spec

yum install /root/rpmbuild/RPMS/x86_64/libanimation-devel-3.8.6-1.fc32.x86_64.rpm /root/rpmbuild/RPMS/x86_64/libanimation-3.8.6-1.fc32.x86_64.rpm
