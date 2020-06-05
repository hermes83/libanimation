# Ubuntu 20.04 / Ubuntu 18.04 / Debian 10.4

apt install git build-essential fakeroot dpkg dpkg-dev debhelper cdbs gobject-introspection googletest google-mock libgirepository1.0-dev libglib2.0-dev libgtest-dev meson

git clone https://github.com/hermes83/libanimation.git

cd libanimation && dpkg-buildpackage -rfakeroot -b -uc -us

sudo dpkg --install ../libanimation0_0.0.0_amd64.deb \
../libanimation-glib0_0.0.0_amd64.deb \
../gir1.2-animation-glib-0_0.0.0_amd64.deb
