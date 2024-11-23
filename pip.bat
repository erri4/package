rmdir /s /q build
rmdir /s /q %1.egg-info
del "filesforpip\%1-%3-py3-none-any.whl"
move "dist\%1-%2-py3-none-any.whl" "filesforpip\%1-%2-py3-none-any.whl"
rmdir /s /q dist