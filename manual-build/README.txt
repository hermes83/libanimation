git clone https://github.com/hermes83/libanimation.git

cd libanimation

meson . build
ninja -C build
sudo ninja -C build install
