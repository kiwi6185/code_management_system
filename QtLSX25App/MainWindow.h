#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>

QT_BEGIN_NAMESPACE
namespace Ui { class MainWindow; }
QT_END_NAMESPACE

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    MainWindow(QWidget *parent = nullptr);
    ~MainWindow();

private slots:
    void on_toolBtn_GenData_clicked();

    void on_toolBtn_Counting_clicked();

    void on_PR_view_clicked(const QModelIndex &index);

    void on_PR_view_doubleClicked(const QModelIndex &index);

    void on_actRecEdit_triggered();

private:
    Ui::MainWindow *ui;
};
#endif // MAINWINDOW_H
