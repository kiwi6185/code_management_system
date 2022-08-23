echo off

copy .\QtLSX25App\MainWindow.ui MainWindow.ui
pyuic5 -o Ui_MainWindow.py MainWindow.ui

copy .\QtLSX25App\QWDialogData.ui QWDialogData.ui
pyuic5 -o Ui_QWDialogData.py QWDialogData.ui

pyrcc5 .\QtLSX25App\res.qrc -o res_rc.py
