g++ -shared -o attach_linux_aarch64.so -fPIC -nostartfiles attach.cpp
mv attach_linux_aarch64.so ../attach_linux_aarch64.so
echo Compiled aarch64
