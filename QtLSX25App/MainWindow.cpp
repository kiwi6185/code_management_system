#include "MainWindow.h"
#include "ui_MainWindow.h"

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{
    ui->setupUi(this);
}

MainWindow::~MainWindow()
{
    delete ui;
}


void MainWindow::on_toolBtn_GenData_clicked()
{

}

void MainWindow::on_toolBtn_Counting_clicked()
{

}

void MainWindow::on_PR_view_clicked(const QModelIndex &index)
{
    
}

void MainWindow::on_PR_view_doubleClicked(const QModelIndex &index)
{

}

void MainWindow::on_actRecEdit_triggered()
{

}
