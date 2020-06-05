libanimation for gnome-shell
=========

Wobbly windows logic split out from Compiz (Gnome Shell patched version).

Following the instructions to build the source code:
- [Manual build with meson and ninja](#manual)
- [Ubuntu (18.04 and 20.04) or Debian (10.4)](#ubuntu-or-debian-based) 
- [Arch or Manjaro](#arch-or-manjaro)
- [Fedora (22)](#fedora)
- [Opensuse (LEAP 15.2)](#opensuse)

# Installation from sources

In order to build the source code, you need Meson and Ninja build tools.

## Manual

1. Create a working directory

```bash
mkdir libanimation-patched && cd libanimation-patched
```

2. Install dependencies

3. clone this repo 

```bash
git clone https://github.com/hermes83/libanimation.git
```

4. Build packages from sources

```bash
cd libanimation
meson . build
ninja -C build
```

5. Install

```bash
sudo ninja -C build install
```

## Ubuntu or Debian based

1. Create a working directory

```bash
mkdir libanimation-patched && cd libanimation-patched
```

2. Install dependencies

```bash
sudo apt install git build-essential fakeroot dpkg dpkg-dev debhelper cdbs \
gobject-introspection googletest google-mock libgirepository1.0-dev \
libglib2.0-dev libgtest-dev meson
```

3. Download sources

```bash
git clone https://github.com/hermes83/libanimation.git
```

4. Build packages from sources

```bash
cd libanimation && dpkg-buildpackage -rfakeroot -b -uc -us
```

5. Install builded packages

```bash
sudo dpkg --install ../libanimation0_0.0.0_amd64.deb \
../libanimation-glib0_0.0.0_amd64.deb \
../gir1.2-animation-glib-0_0.0.0_amd64.deb
```

## Arch or Manjaro

The easy way to compile from source is to use tool such as pacaur from the [AUR repo](https://aur.archlinux.org/packages/libanimation-gnome-shell-git):

```bash
pacaur -S libanimation-gnome-shell-git
```

Alternatively you can follow the instructions:

1. Create a working directory

```bash
mkdir libanimation-patched && cd libanimation-patched
```

2. Download PKGBUILD file

```bash
wget https://aur.archlinux.org/cgit/aur.git/snapshot/libanimation-gnome-shell-git.tar.gz
tar -zxvf libanimation-gnome-shell-git.tar.gz
cd libanimation-gnome-shell-git
```

3. Install dependencies

```bash
sudo pacman -S fakeroot strip binutils meson gobject-introspection gmock gtest gcc cmake glib2 pkgconf 
```

4. Build package from sources

```bash
makepkg
```

5. Install builded packages

```bash
sudo pacman -U libanimation-gnome-shell-*.pkg.tar.xz
```

## Fedora

1. Create a working directory

```bash
mkdir libanimation-patched && cd libanimation-patched
```

2. Download RPM spec file

```bash
wget https://raw.githubusercontent.com/hermes83/libanimation/master/fedora/libanimation.spec
```

3. Install dependecies

```bash
sudo yum install git meson rpm-build gmock gtest gmock-devel gtest-devel \ 
gobject-introspection gobject-introspection-devel gcc-c++ glib2-devel \
gobject-introspection-devel rpmdevtools
```

4. Build package from sources

```bash
rpmbuild -bb libanimation.spec
```

5. Install builded packages

```bash
sudo yum install /root/rpmbuild/RPMS/x86_64/libanimation-devel-3.8.6-1.fc32.x86_64.rpm \
/root/rpmbuild/RPMS/x86_64/libanimation-3.8.6-1.fc32.x86_64.rpm
```

## Opensuse

1. Create a working directory

```bash
mkdir libanimation-patched && cd libanimation-patched
```

2. Download RPM spec file

```bash
wget https://raw.githubusercontent.com/hermes83/libanimation/master/opensuse/libanimation.spec
```

3. Install dependecies

```bash
sudo zypper install git meson rpm-build gmock gtest gobject-introspection \
gobject-introspection-devel gcc-c++ glib2-devel-static gobject-introspection-devel rpmdevtools
```

4. Build package from sources

```bash
rpmbuild -bb libanimation.spec
```

5. Install builded packages

```bash
sudo zypper install /usr/src/packages/RPMS/x86_64/libanimation-3.8.6-1.x86_64.rpm  \
/usr/src/packages/RPMS/x86_64/libanimation-devel-3.8.6-1.x86_64.rpm
```
