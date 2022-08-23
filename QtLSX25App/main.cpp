#include "MainWindow.h"

#include <QApplication>

#include <QFile>

#include <QTextStream>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    MainWindow w;

//    QFile file(":/qss/css/qss.css");
//    if (!file.open(QIODevice::ReadOnly))
//        exit(0);

//    QTextStream in(&file);
//    QString css = in.readAll();
//    qApp->setStyleSheet(css);

    w.show();
    return a.exec();
}
