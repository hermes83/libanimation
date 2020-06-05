zypper install git meson rpm-build gmock gtest gobject-introspection gobject-introspection-devel gcc-c++ glib2-devel-static gobject-introspection-devel rpmdevtools

rpmbuild -bb libanimation.spec

zypper install /usr/src/packages/RPMS/x86_64/libanimation-3.8.6-1.x86_64.rpm  /usr/src/packages/RPMS/x86_64/libanimation-devel-3.8.6-1.x86_64.rpm
